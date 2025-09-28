"""
Funciones auxiliares para la aplicación MathEngine
"""

import streamlit as st
import sympy as sp
from sympy import latex, parse_expr, simplify
from fractions import Fraction
import re
import random

def format_latex(expression):
    """Formatea una expresión para mostrar en LaTeX"""
    try:
        if isinstance(expression, str):
            # Intentar parsear como expresión SymPy
            try:
                expr = parse_expr(expression)
                return latex(expr)
            except:
                return expression
        else:
            return latex(expression)
    except:
        return str(expression)

def normalize_answer(answer):
    """Normaliza una respuesta para comparación"""
    if not answer:
        return ""
    
    # Convertir a string y limpiar
    answer_str = str(answer).strip().replace(' ', '').lower()
    
    # Reemplazar símbolos comunes
    replacements = {
        '×': '*',
        '÷': '/',
        '−': '-',
        '√': 'sqrt'
    }
    
    for old, new in replacements.items():
        answer_str = answer_str.replace(old, new)
    
    return answer_str

def check_mathematical_equivalence(user_answer, correct_answer):
    """Verifica si dos expresiones matemáticas son equivalentes"""
    try:
        # Normalizar respuestas
        user_clean = normalize_answer(user_answer)
        correct_clean = normalize_answer(correct_answer)
        
        # Comparación directa
        if user_clean == correct_clean:
            return True
        
        # Intentar evaluación matemática con SymPy
        try:
            user_expr = parse_expr(user_answer)
            correct_expr = parse_expr(correct_answer)
            
            # Verificar si son equivalentes
            diff = simplify(user_expr - correct_expr)
            return diff == 0
        except:
            pass
        
        # Comparación de fracciones
        try:
            user_frac = Fraction(user_answer)
            correct_frac = Fraction(correct_answer)
            return user_frac == correct_frac
        except:
            pass
        
        # Comparación numérica con tolerancia
        try:
            user_val = float(user_answer)
            correct_val = float(correct_answer)
            return abs(user_val - correct_val) < 1e-10
        except:
            pass
        
        return False
        
    except:
        return False

def generate_hint(exercise_type, error_type=None):
    """Genera una pista basada en el tipo de ejercicio"""
    hints = {
        'fraction_operations': [
            "Para sumar fracciones, necesitas un denominador común",
            "Para multiplicar fracciones, multiplica numeradores y denominadores",
            "Para dividir fracciones, multiplica por el recíproco"
        ],
        'combined_operations': [
            "Recuerda el orden de operaciones: PEMDAS",
            "Resuelve primero los paréntesis",
            "Los exponentes van antes que la multiplicación"
        ],
        'mcm_mcd': [
            "Factoriza ambos números en primos",
            "MCD: factores comunes con menor exponente",
            "MCM: todos los factores con mayor exponente"
        ],
        'monomios': [
            "Para multiplicar monomios, multiplica coeficientes y suma exponentes",
            "Solo puedes sumar monomios semejantes",
            "Para dividir, divide coeficientes y resta exponentes"
        ],
        'productos_notables': [
            "Identifica el patrón: (a+b)², (a-b)², (a+b)(a-b)",
            "Cuadrado de suma: a² + 2ab + b²",
            "Diferencia de cuadrados: a² - b²"
        ]
    }
    
    exercise_hints = hints.get(exercise_type, ["Revisa la teoría del tema"])
    return random.choice(exercise_hints)

def format_time(seconds):
    """Formatea tiempo en segundos a formato MM:SS"""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def calculate_grade(score):
    """Calcula la calificación basada en el puntaje"""
    if score >= 90:
        return "A", "Excelente"
    elif score >= 80:
        return "B", "Muy Bueno"
    elif score >= 70:
        return "C", "Bueno"
    elif score >= 60:
        return "D", "Suficiente"
    else:
        return "F", "Insuficiente"

def get_difficulty_color(difficulty):
    """Retorna el color asociado a cada dificultad"""
    colors = {
        'easy': '#4caf50',    # Verde
        'medium': '#ff9800',  # Naranja
        'hard': '#f44336'     # Rojo
    }
    return colors.get(difficulty, '#2196f3')

def create_progress_bar(current, total, color="#667eea"):
    """Crea una barra de progreso HTML personalizada"""
    percentage = (current / total * 100) if total > 0 else 0
    
    return f"""
    <div style="background: #e0e0e0; border-radius: 10px; overflow: hidden; height: 20px; margin: 10px 0;">
        <div style="background: {color}; height: 100%; width: {percentage}%; transition: width 0.3s ease;"></div>
    </div>
    <div style="text-align: center; font-size: 14px; color: #666;">
        {current}/{total} ({percentage:.1f}%)
    </div>
    """

def display_math_steps(steps):
    """Muestra pasos matemáticos con formato mejorado"""
    for i, step in enumerate(steps, 1):
        st.markdown(f"""
        <div class="step-box">
            <strong>Paso {i}:</strong> {step}
        </div>
        """, unsafe_allow_html=True)

def create_metric_card(title, value, delta=None, color="#667eea"):
    """Crea una tarjeta de métrica personalizada"""
    delta_html = ""
    if delta is not None:
        delta_color = "#4caf50" if delta >= 0 else "#f44336"
        delta_symbol = "+" if delta >= 0 else ""
        delta_html = f'<div style="color: {delta_color}; font-size: 14px;">{delta_symbol}{delta}</div>'
    
    return f"""
    <div class="metric-card" style="border-left: 4px solid {color};">
        <div style="font-size: 14px; color: #666; margin-bottom: 5px;">{title}</div>
        <div style="font-size: 24px; font-weight: bold; color: {color};">{value}</div>
        {delta_html}
    </div>
    """

def safe_latex_render(expression):
    """Renderiza LaTeX de forma segura, manejando errores"""
    try:
        if isinstance(expression, str):
            # Limpiar la expresión
            clean_expr = expression.replace('\\\\', '\\')
            st.latex(clean_expr)
        else:
            st.latex(latex(expression))
    except Exception as e:
        st.error(f"Error renderizando LaTeX: {str(e)}")
        st.code(str(expression))

def create_topic_navigation(current_topic, topics_list):
    """Crea navegación entre temas"""
    current_index = topics_list.index(current_topic) if current_topic in topics_list else 0
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if current_index > 0:
            if st.button("⬅️ Anterior"):
                return topics_list[current_index - 1]
    
    with col2:
        st.markdown(f"<div style='text-align: center; padding: 10px;'><strong>{current_topic}</strong></div>", 
                   unsafe_allow_html=True)
    
    with col3:
        if current_index < len(topics_list) - 1:
            if st.button("Siguiente ➡️"):
                return topics_list[current_index + 1]
    
    return current_topic

def export_results_to_text(results_data):
    """Exporta resultados a formato de texto"""
    text_content = "=== RESULTADOS DEL EXAMEN ===\n\n"
    
    # Información general
    text_content += f"Puntuación: {results_data.get('score', 0):.1f}%\n"
    text_content += f"Correctas: {results_data.get('correct', 0)}/{results_data.get('total', 0)}\n"
    text_content += f"Tiempo: {results_data.get('time_taken', 'N/A')}\n\n"
    
    # Detalles por pregunta
    text_content += "=== DETALLES POR PREGUNTA ===\n\n"
    
    for i, result in enumerate(results_data.get('question_results', []), 1):
        text_content += f"Pregunta {i}: {'✓' if result.get('is_correct') else '✗'}\n"
        text_content += f"Pregunta: {result.get('question', 'N/A')}\n"
        text_content += f"Tu respuesta: {result.get('user_answer', 'Sin respuesta')}\n"
        text_content += f"Respuesta correcta: {result.get('correct_answer', 'N/A')}\n\n"
    
    return text_content
