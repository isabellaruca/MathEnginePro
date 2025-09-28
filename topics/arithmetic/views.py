from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .content import get_theory_content, get_explanation_for_error
from .exercise_generator import get_random_exercise


def theory(request):
    """Vista para mostrar el contenido teórico de aritmética"""
    content = get_theory_content()
    return render(request, 'arithmetic/theory.html', {'content': content})


def practice(request):
    """Vista para el módulo de práctica"""
    return render(request, 'arithmetic/practice.html')


@csrf_exempt
def get_exercise(request):
    """
    API endpoint para obtener un nuevo ejercicio
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            topic = data.get('topic', None)
            difficulty = data.get('difficulty', 'medium')
            
            # Generar ejercicio usando el generador
            exercise = get_random_exercise(topic, difficulty)
            
            return JsonResponse({
                'success': True,
                'exercise': exercise
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Error generando ejercicio: {str(e)}'
            })
    
    # GET request - generar ejercicio por defecto
    exercise = get_random_exercise()
    return JsonResponse({
        'success': True,
        'exercise': exercise
    })


@csrf_exempt
def check_answer(request):
    """
    API endpoint para verificar respuestas y dar feedback
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_answer = data.get('answer', '').strip()
            correct_answer = data.get('correct_answer', '')
            error_type = data.get('error_type', 'general')
            
            # Normalizar respuestas para comparación
            user_answer_normalized = user_answer.replace(' ', '').lower()
            correct_answer_normalized = correct_answer.replace(' ', '').lower()
            
            is_correct = user_answer_normalized == correct_answer_normalized
            
            response_data = {
                'success': True,
                'is_correct': is_correct,
                'correct_answer': correct_answer
            }
            
            if is_correct:
                response_data['message'] = '¡Correcto! Excelente trabajo.'
                response_data['feedback_type'] = 'success'
            else:
                response_data['message'] = 'Respuesta incorrecta. Revisa la explicación.'
                response_data['feedback_type'] = 'error'
                response_data['explanation'] = get_explanation_for_error(error_type)
            
            return JsonResponse(response_data)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Error verificando respuesta: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})


def exam_question(request):
    """Vista para generar preguntas de examen"""
    exercise = get_random_exercise()
    return render(request, 'arithmetic/exam_question.html', {'exercise': exercise})
