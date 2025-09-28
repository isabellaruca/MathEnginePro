from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from sympy import latex


def index(request):
    """Vista principal de la aplicación"""
    return render(request, 'core/index.html')


def solver(request):
    """Vista del módulo solucionador"""
    return render(request, 'core/solver.html')


@csrf_exempt
def solve_expression(request):
    """
    Procesa expresiones matemáticas y devuelve solución paso a paso
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            expression = data.get('expression', '')
            
            if not expression:
                return JsonResponse({'error': 'No se proporcionó expresión'})
            
            # Parsear la expresión usando SymPy
            try:
                expr = parse_expr(expression)
            except:
                return JsonResponse({'error': 'Expresión matemática inválida'})
            
            # Generar pasos de solución
            steps = []
            result = None
            
            # Determinar el tipo de operación y generar pasos apropiados
            if expr.is_polynomial():
                # Para polinomios, mostrar factorización si es posible
                factored = sp.factor(expr)
                if factored != expr:
                    steps.append({
                        'description': 'Factorizar la expresión',
                        'expression': latex(factored),
                        'explanation': 'Aplicamos factorización para simplificar'
                    })
                result = factored
            elif expr.has(sp.Symbol):
                # Para ecuaciones con variables, intentar resolver
                variables = list(expr.free_symbols)
                if len(variables) == 1:
                    var = variables[0]
                    try:
                        solutions = sp.solve(expr, var)
                        if solutions:
                            steps.append({
                                'description': f'Resolver para {var}',
                                'expression': f'{var} = {latex(solutions[0])}' if len(solutions) == 1 else f'{var} ∈ {latex(solutions)}',
                                'explanation': 'Aplicamos métodos algebraicos para encontrar la solución'
                            })
                            result = solutions[0] if len(solutions) == 1 else solutions
                    except:
                        pass
            
            # Simplificar la expresión
            simplified = sp.simplify(expr)
            if simplified != expr:
                steps.append({
                    'description': 'Simplificar la expresión',
                    'expression': latex(simplified),
                    'explanation': 'Aplicamos reglas de simplificación algebraica'
                })
                result = simplified
            
            # Si no hay pasos específicos, mostrar evaluación numérica si es posible
            if not steps:
                try:
                    evaluated = expr.evalf()
                    steps.append({
                        'description': 'Evaluar numéricamente',
                        'expression': latex(evaluated),
                        'explanation': 'Calculamos el valor numérico de la expresión'
                    })
                    result = evaluated
                except:
                    result = expr
            
            return JsonResponse({
                'success': True,
                'original': latex(expr),
                'steps': steps,
                'result': latex(result) if result is not None else latex(expr)
            })
            
        except Exception as e:
            return JsonResponse({'error': f'Error procesando la expresión: {str(e)}'})
    
    return JsonResponse({'error': 'Método no permitido'})


def exam_setup(request):
    """Vista para configurar exámenes"""
    topics = [
        {'slug': 'arithmetic', 'name': 'Aritmética'},
        {'slug': 'algebra', 'name': 'Álgebra'},
        # Aquí se pueden agregar más temas en el futuro
    ]
    return render(request, 'core/exam_setup.html', {'topics': topics})


def exam_start(request):
    """Vista para iniciar un examen"""
    if request.method == 'POST':
        selected_topics = request.POST.getlist('topics')
        num_questions = int(request.POST.get('num_questions', 10))
        time_limit = int(request.POST.get('time_limit', 30))
        
        # Guardar configuración en sesión
        request.session['exam_config'] = {
            'topics': selected_topics,
            'num_questions': num_questions,
            'time_limit': time_limit,
            'current_question': 0,
            'answers': [],
            'start_time': None
        }
        
        return render(request, 'core/exam.html', {
            'config': request.session['exam_config']
        })
    
    return render(request, 'core/exam_setup.html')
