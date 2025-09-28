"""
Motor de resolución matemática
Migrado y adaptado desde el proyecto Django original
"""

import sympy as sp
from sympy import latex, parse_expr, simplify, factor, solve, expand, collect
from sympy.parsing.sympy_parser import parse_expr
import re

class MathSolver:
    """Clase principal para resolver expresiones matemáticas"""
    
    def __init__(self):
        self.x = sp.Symbol('x')
        self.y = sp.Symbol('y')
        self.z = sp.Symbol('z')
    
    def solve_expression(self, expression_str):
        """
        Procesa expresiones matemáticas y devuelve solución paso a paso
        """
        try:
            if not expression_str:
                return {'success': False, 'error': 'No se proporcionó expresión'}
            
            # Limpiar y preparar la expresión
            cleaned_expr = self._clean_expression(expression_str)
            
            # Intentar parsear la expresión
            try:
                if '=' in cleaned_expr:
                    # Es una ecuación
                    return self._solve_equation(cleaned_expr)
                else:
                    # Es una expresión
                    return self._solve_expression(cleaned_expr)
            except Exception as parse_error:
                return {'success': False, 'error': f'Expresión matemática inválida: {str(parse_error)}'}
                
        except Exception as e:
            return {'success': False, 'error': f'Error procesando la expresión: {str(e)}'}
    
    def _clean_expression(self, expr_str):
        """Limpia y normaliza la expresión de entrada"""
        # Reemplazar símbolos comunes
        expr_str = expr_str.replace('^', '**')
        expr_str = expr_str.replace('÷', '/')
        expr_str = expr_str.replace('×', '*')
        
        # Agregar multiplicación implícita
        expr_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr_str)
        expr_str = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expr_str)
        expr_str = re.sub(r'\)(\d)', r')*\1', expr_str)
        expr_str = re.sub(r'(\d)\(', r'\1*(', expr_str)
        
        return expr_str
    
    def _solve_equation(self, equation_str):
        """Resuelve ecuaciones"""
        try:
            left, right = equation_str.split('=')
            left_expr = parse_expr(left.strip())
            right_expr = parse_expr(right.strip())
            
            # Crear ecuación
            equation = sp.Eq(left_expr, right_expr)
            
            # Encontrar variables
            variables = list(equation.free_symbols)
            
            if not variables:
                # No hay variables, verificar si es verdadera
                is_true = left_expr.equals(right_expr)
                return {
                    'success': True,
                    'original': latex(equation),
                    'steps': [
                        {
                            'description': 'Verificar igualdad',
                            'expression': f'{latex(left_expr)} = {latex(right_expr)}',
                            'explanation': f'La ecuación es {"verdadera" if is_true else "falsa"}'
                        }
                    ],
                    'result': 'Verdadero' if is_true else 'Falso'
                }
            
            # Resolver para la primera variable encontrada
            var = variables[0]
            solutions = solve(equation, var)
            
            steps = []
            
            # Paso 1: Mostrar ecuación original
            steps.append({
                'description': 'Ecuación original',
                'expression': latex(equation),
                'explanation': f'Resolver para {var}'
            })
            
            # Paso 2: Reorganizar términos si es necesario
            if left_expr != var and right_expr != 0:
                rearranged = sp.Eq(left_expr - right_expr, 0)
                steps.append({
                    'description': 'Reorganizar términos',
                    'expression': latex(rearranged),
                    'explanation': 'Mover todos los términos a un lado'
                })
            
            # Paso 3: Mostrar solución
            if solutions:
                if len(solutions) == 1:
                    solution = solutions[0]
                    steps.append({
                        'description': 'Solución',
                        'expression': f'{var} = {latex(solution)}',
                        'explanation': 'Despejar la variable'
                    })
                    result = f'{var} = {latex(solution)}'
                else:
                    steps.append({
                        'description': 'Soluciones múltiples',
                        'expression': f'{var} \\in \\{' + ', '.join([latex(sol) for sol in solutions]) + '\\}',
                        'explanation': 'La ecuación tiene múltiples soluciones'
                    })
                    result = f'{var} ∈ {{{", ".join([latex(sol) for sol in solutions])}}}'
            else:
                steps.append({
                    'description': 'Sin solución',
                    'expression': '\\emptyset',
                    'explanation': 'La ecuación no tiene solución en los números reales'
                })
                result = 'Sin solución'
            
            return {
                'success': True,
                'original': latex(equation),
                'steps': steps,
                'result': result
            }
            
        except Exception as e:
            return {'success': False, 'error': f'Error resolviendo ecuación: {str(e)}'}
    
    def _solve_expression(self, expr_str):
        """Resuelve y simplifica expresiones"""
        try:
            expr = parse_expr(expr_str)
            steps = []
            result = expr
            
            # Mostrar expresión original
            original_latex = latex(expr)
            
            # Determinar el tipo de operación y generar pasos apropiados
            if expr.is_polynomial():
                # Para polinomios, mostrar factorización si es posible
                factored = factor(expr)
                if factored != expr:
                    steps.append({
                        'description': 'Factorizar la expresión',
                        'expression': latex(factored),
                        'explanation': 'Aplicamos factorización para simplificar'
                    })
                    result = factored
                
                # También mostrar expansión si está factorizada
                expanded = expand(expr)
                if expanded != expr and not steps:
                    steps.append({
                        'description': 'Expandir la expresión',
                        'expression': latex(expanded),
                        'explanation': 'Aplicamos la propiedad distributiva'
                    })
                    result = expanded
            
            # Simplificar la expresión
            simplified = simplify(expr)
            if simplified != expr and simplified != result:
                steps.append({
                    'description': 'Simplificar la expresión',
                    'expression': latex(simplified),
                    'explanation': 'Aplicamos reglas de simplificación algebraica'
                })
                result = simplified
            
            # Coleccionar términos semejantes
            if expr.has(sp.Symbol):
                variables = list(expr.free_symbols)
                if variables:
                    collected = collect(expr, variables[0])
                    if collected != expr and collected != result:
                        steps.append({
                            'description': 'Agrupar términos semejantes',
                            'expression': latex(collected),
                            'explanation': f'Agrupar términos con {variables[0]}'
                        })
                        result = collected
            
            # Si no hay pasos específicos, mostrar evaluación numérica si es posible
            if not steps:
                try:
                    if not expr.has(sp.Symbol):
                        # Solo números, evaluar
                        evaluated = expr.evalf()
                        steps.append({
                            'description': 'Evaluar numéricamente',
                            'expression': latex(evaluated),
                            'explanation': 'Calculamos el valor numérico de la expresión'
                        })
                        result = evaluated
                    else:
                        # Tiene variables, mostrar forma simplificada
                        steps.append({
                            'description': 'Expresión simplificada',
                            'expression': latex(simplified),
                            'explanation': 'La expresión ya está en su forma más simple'
                        })
                        result = simplified
                except:
                    result = expr
            
            return {
                'success': True,
                'original': original_latex,
                'steps': steps,
                'result': latex(result)
            }
            
        except Exception as e:
            return {'success': False, 'error': f'Error procesando expresión: {str(e)}'}
    
    def _generate_step_by_step_solution(self, expr, operation_type):
        """Genera solución paso a paso según el tipo de operación"""
        steps = []
        
        if operation_type == 'factorization':
            # Pasos para factorización
            factored = factor(expr)
            if factored != expr:
                steps.append({
                    'description': 'Buscar factores comunes',
                    'expression': latex(factored),
                    'explanation': 'Extraer el máximo factor común'
                })
        
        elif operation_type == 'expansion':
            # Pasos para expansión
            expanded = expand(expr)
            if expanded != expr:
                steps.append({
                    'description': 'Aplicar propiedad distributiva',
                    'expression': latex(expanded),
                    'explanation': 'Multiplicar cada término'
                })
        
        elif operation_type == 'simplification':
            # Pasos para simplificación
            simplified = simplify(expr)
            if simplified != expr:
                steps.append({
                    'description': 'Simplificar la expresión',
                    'expression': latex(simplified),
                    'explanation': 'Aplicar reglas de simplificación'
                })
        
        return steps
