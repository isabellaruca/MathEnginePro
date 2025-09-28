"""
MathEngine - Aplicación Streamlit para aprendizaje de matemáticas
Migración completa del proyecto Django original
"""

import streamlit as st
import sympy as sp
from sympy import latex, parse_expr, simplify, factor, solve, factorint, gcd, lcm
import random
import json
from fractions import Fraction
import time
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(
    page_title="MathEngine - Plataforma de Matemáticas",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la apariencia
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .math-display {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #dee2e6;
        margin: 1rem 0;
        text-align: center;
    }
    
    .step-box {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        border-left: 3px solid #2196f3;
    }
    
    .success-box {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 5px;
        border-left: 3px solid #4caf50;
        color: #2e7d32;
    }
    
    .error-box {
        background: #ffebee;
        padding: 1rem;
        border-radius: 5px;
        border-left: 3px solid #f44336;
        color: #c62828;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

# Importar módulos de contenido y generadores
from utils.arithmetic_content import get_arithmetic_content, get_arithmetic_section
from utils.algebra_content import get_algebra_content, get_algebra_section
from utils.exercise_generators import ArithmeticExerciseGenerator, AlgebraExerciseGenerator
from utils.solver_engine import MathSolver

def main():
    """Función principal de la aplicación"""
    
    # Inicializar generadores y solver
    if 'arithmetic_generator' not in st.session_state:
        st.session_state.arithmetic_generator = ArithmeticExerciseGenerator()
    if 'algebra_generator' not in st.session_state:
        st.session_state.algebra_generator = AlgebraExerciseGenerator()
    if 'solver' not in st.session_state:
        st.session_state.solver = MathSolver()
    
    # Sidebar para navegación
    st.sidebar.markdown("# 🧮 MathEngine")
    st.sidebar.markdown("---")
    
    page = st.sidebar.selectbox(
        "Selecciona una sección:",
        [
            "🏠 Inicio",
            "🔧 Solver Matemático", 
            "📚 Teoría - Aritmética",
            "📚 Teoría - Álgebra",
            "💪 Práctica - Aritmética",
            "💪 Práctica - Álgebra",
            "📝 Exámenes"
        ]
    )
    
    # Enrutamiento de páginas
    if page == "🏠 Inicio":
        show_home_page()
    elif page == "🔧 Solver Matemático":
        show_solver_page()
    elif page == "📚 Teoría - Aritmética":
        show_arithmetic_theory()
    elif page == "📚 Teoría - Álgebra":
        show_algebra_theory()
    elif page == "💪 Práctica - Aritmética":
        show_arithmetic_practice()
    elif page == "💪 Práctica - Álgebra":
        show_algebra_practice()
    elif page == "📝 Exámenes":
        show_exam_page()

def show_home_page():
    """Página principal de la aplicación"""
    
    # Header principal
    st.markdown("""
    <div class="main-header">
        <h1>🧮 MathEngine</h1>
        <h3>Tu plataforma completa para aprender matemáticas</h3>
        <p>Resuelve, aprende y practica matemáticas con explicaciones paso a paso</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Características principales
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🔧 Solver Inteligente</h4>
            <p>Resuelve expresiones matemáticas con explicaciones detalladas paso a paso</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Ir al Solver", key="solver_btn"):
            st.session_state.page = "🔧 Solver Matemático"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📚 Teoría Completa</h4>
            <p>Aprende conceptos fundamentales de aritmética y álgebra con ejemplos</p>
        </div>
        """, unsafe_allow_html=True)
        
        theory_topic = st.selectbox("Selecciona tema:", ["Aritmética", "Álgebra"], key="theory_select")
        if st.button("Ver Teoría", key="theory_btn"):
            if theory_topic == "Aritmética":
                st.session_state.page = "📚 Teoría - Aritmética"
            else:
                st.session_state.page = "📚 Teoría - Álgebra"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>💪 Práctica Interactiva</h4>
            <p>Ejercicios generados automáticamente con diferentes niveles de dificultad</p>
        </div>
        """, unsafe_allow_html=True)
        
        practice_topic = st.selectbox("Selecciona tema:", ["Aritmética", "Álgebra"], key="practice_select")
        if st.button("Practicar", key="practice_btn"):
            if practice_topic == "Aritmética":
                st.session_state.page = "💪 Práctica - Aritmética"
            else:
                st.session_state.page = "💪 Práctica - Álgebra"
            st.rerun()
    
    # Sección de temas rápidos
    st.markdown("## 🎯 Acceso Rápido a Temas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Aritmética")
        topics = [
            ("Conjuntos Numéricos", "conjuntos_numericos"),
            ("Operaciones Combinadas", "operaciones_combinadas"),
            ("Fracciones", "fracciones"),
            ("MCM y MCD", "mcm_mcd")
        ]
        
        for topic_name, topic_id in topics:
            if st.button(f"📖 {topic_name}", key=f"arith_{topic_id}"):
                st.session_state.selected_arithmetic_section = topic_id
                st.session_state.page = "📚 Teoría - Aritmética"
                st.rerun()
    
    with col2:
        st.markdown("### Álgebra")
        topics = [
            ("Monomios", "monomios"),
            ("Operaciones con Monomios", "operaciones_monomios"),
            ("Polinomios", "polinomios"),
            ("Productos Notables", "productos_notables"),
            ("Factorización", "factorizacion")
        ]
        
        for topic_name, topic_id in topics:
            if st.button(f"📖 {topic_name}", key=f"alg_{topic_id}"):
                st.session_state.selected_algebra_section = topic_id
                st.session_state.page = "📚 Teoría - Álgebra"
                st.rerun()
    
    # Estadísticas de uso (simuladas)
    st.markdown("## 📊 Tu Progreso")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Ejercicios Resueltos", "47", "5")
    with col2:
        st.metric("Precisión", "85%", "3%")
    with col3:
        st.metric("Tiempo de Estudio", "2.5h", "0.5h")
    with col4:
        st.metric("Temas Completados", "6/10", "1")

def show_solver_page():
    """Página del solver matemático"""
    
    st.markdown("# 🔧 Solver Matemático")
    st.markdown("Ingresa cualquier expresión matemática y obtén la solución paso a paso")
    
    # Input para la expresión
    col1, col2 = st.columns([3, 1])
    
    with col1:
        expression = st.text_input(
            "Expresión matemática:",
            placeholder="Ej: 2*x + 3 = 7, x^2 - 4, (2/3) + (1/4), etc.",
            help="Puedes usar +, -, *, /, ^, sqrt(), sin(), cos(), etc."
        )
    
    with col2:
        solve_button = st.button("🔍 Resolver", type="primary")
    
    # Ejemplos rápidos
    st.markdown("**Ejemplos rápidos:**")
    examples = [
        "2*x + 3 = 7",
        "x^2 - 5*x + 6",
        "(2/3) + (1/4)",
        "sqrt(16) + 3^2",
        "2*x^2 - 8"
    ]
    
    cols = st.columns(len(examples))
    for i, example in enumerate(examples):
        with cols[i]:
            if st.button(example, key=f"example_{i}"):
                st.session_state.solver_expression = example
                st.rerun()
    
    # Procesar expresión
    if solve_button and expression:
        try:
            result = st.session_state.solver.solve_expression(expression)
            
            if result['success']:
                st.markdown("## ✅ Solución")
                
                # Mostrar expresión original
                st.markdown("**Expresión original:**")
                st.latex(result['original'])
                
                # Mostrar pasos
                if result['steps']:
                    st.markdown("**Pasos de solución:**")
                    for i, step in enumerate(result['steps'], 1):
                        st.markdown(f"""
                        <div class="step-box">
                            <strong>Paso {i}:</strong> {step['description']}<br>
                            <div style="text-align: center; margin: 0.5rem 0;">
                        """, unsafe_allow_html=True)
                        st.latex(step['expression'])
                        st.markdown(f"""
                            </div>
                            <em>{step['explanation']}</em>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Mostrar resultado final
                st.markdown("**Resultado final:**")
                st.markdown('<div class="math-display">', unsafe_allow_html=True)
                st.latex(result['result'])
                st.markdown('</div>', unsafe_allow_html=True)
                
            else:
                st.markdown(f"""
                <div class="error-box">
                    <strong>Error:</strong> {result['error']}
                </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Error procesando la expresión: {str(e)}")
    
    # Ayuda y consejos
    with st.expander("💡 Ayuda y Consejos"):
        st.markdown("""
        **Sintaxis soportada:**
        - Operaciones básicas: `+`, `-`, `*`, `/`
        - Exponentes: `x^2` o `x**2`
        - Raíces: `sqrt(x)` o `x^(1/2)`
        - Funciones: `sin(x)`, `cos(x)`, `tan(x)`, `log(x)`, `exp(x)`
        - Constantes: `pi`, `e`
        - Ecuaciones: `2*x + 3 = 7`
        
        **Ejemplos de uso:**
        - Resolver ecuaciones: `2*x + 3 = 7`
        - Factorizar: `x^2 - 4`
        - Simplificar: `(x^2 - 1)/(x - 1)`
        - Operaciones con fracciones: `(2/3) + (1/4)`
        """)

def show_arithmetic_theory():
    """Página de teoría de aritmética"""
    
    st.markdown("# 📚 Teoría - Aritmética")
    
    content = get_arithmetic_content()
    
    # Selector de sección
    sections = [(section['id'], section['title']) for section in content['sections']]
    
    selected_section = st.selectbox(
        "Selecciona una sección:",
        options=[s[0] for s in sections],
        format_func=lambda x: next(s[1] for s in sections if s[0] == x),
        index=0 if 'selected_arithmetic_section' not in st.session_state else 
              [s[0] for s in sections].index(st.session_state.get('selected_arithmetic_section', sections[0][0]))
    )
    
    # Mostrar contenido de la sección
    section_data = get_arithmetic_section(selected_section)
    
    if section_data:
        st.markdown(f"## {section_data['title']}")
        
        # Contenido principal
        st.markdown(section_data['content'], unsafe_allow_html=True)
        
        # Ejemplos
        if 'examples' in section_data and section_data['examples']:
            st.markdown("### 📝 Ejemplos")
            
            for i, example in enumerate(section_data['examples']):
                with st.expander(f"Ejemplo {i+1}: {example['title']}"):
                    st.markdown(f"**Problema:** {example['problem']}")
                    st.markdown("**Solución:**")
                    st.markdown(example['solution'], unsafe_allow_html=True)
        
        # Navegación entre secciones
        col1, col2, col3 = st.columns([1, 2, 1])
        
        current_index = [s[0] for s in sections].index(selected_section)
        
        with col1:
            if current_index > 0:
                if st.button("⬅️ Anterior"):
                    st.session_state.selected_arithmetic_section = sections[current_index - 1][0]
                    st.rerun()
        
        with col3:
            if current_index < len(sections) - 1:
                if st.button("Siguiente ➡️"):
                    st.session_state.selected_arithmetic_section = sections[current_index + 1][0]
                    st.rerun()
        
        # Botón para ir a práctica
        st.markdown("---")
        if st.button("💪 Practicar este tema", type="primary"):
            st.session_state.page = "💪 Práctica - Aritmética"
            st.rerun()

def show_algebra_theory():
    """Página de teoría de álgebra"""
    
    st.markdown("# 📚 Teoría - Álgebra")
    
    content = get_algebra_content()
    
    # Selector de sección
    sections = [(section['id'], section['title']) for section in content['sections']]
    
    selected_section = st.selectbox(
        "Selecciona una sección:",
        options=[s[0] for s in sections],
        format_func=lambda x: next(s[1] for s in sections if s[0] == x),
        index=0 if 'selected_algebra_section' not in st.session_state else 
              [s[0] for s in sections].index(st.session_state.get('selected_algebra_section', sections[0][0]))
    )
    
    # Mostrar contenido de la sección
    section_data = get_algebra_section(selected_section)
    
    if section_data:
        st.markdown(f"## {section_data['title']}")
        
        # Contenido principal
        st.markdown(section_data['content'], unsafe_allow_html=True)
        
        # Ejemplos
        if 'examples' in section_data and section_data['examples']:
            st.markdown("### 📝 Ejemplos")
            
            for i, example in enumerate(section_data['examples']):
                with st.expander(f"Ejemplo {i+1}: {example['title']}"):
                    st.markdown(f"**Problema:** {example['problem']}")
                    st.markdown("**Solución:**")
                    st.markdown(example['solution'], unsafe_allow_html=True)
        
        # Navegación entre secciones
        col1, col2, col3 = st.columns([1, 2, 1])
        
        current_index = [s[0] for s in sections].index(selected_section)
        
        with col1:
            if current_index > 0:
                if st.button("⬅️ Anterior"):
                    st.session_state.selected_algebra_section = sections[current_index - 1][0]
                    st.rerun()
        
        with col3:
            if current_index < len(sections) - 1:
                if st.button("Siguiente ➡️"):
                    st.session_state.selected_algebra_section = sections[current_index + 1][0]
                    st.rerun()
        
        # Botón para ir a práctica
        st.markdown("---")
        if st.button("💪 Practicar este tema", type="primary"):
            st.session_state.page = "💪 Práctica - Álgebra"
            st.rerun()

def show_arithmetic_practice():
    """Página de práctica de aritmética"""
    
    st.markdown("# 💪 Práctica - Aritmética")
    
    # Inicializar estadísticas si no existen
    if 'arithmetic_stats' not in st.session_state:
        st.session_state.arithmetic_stats = {
            'correct': 0,
            'total': 0,
            'streak': 0,
            'best_streak': 0
        }
    
    # Configuración de práctica
    col1, col2, col3 = st.columns(3)
    
    with col1:
        topic = st.selectbox(
            "Tema:",
            ["fraction_operations", "combined_operations", "mcm_mcd", "factorization", "word_problems"],
            format_func=lambda x: {
                "fraction_operations": "Operaciones con Fracciones",
                "combined_operations": "Operaciones Combinadas", 
                "mcm_mcd": "MCM y MCD",
                "factorization": "Factorización",
                "word_problems": "Problemas Verbales"
            }[x]
        )
    
    with col2:
        difficulty = st.selectbox("Dificultad:", ["easy", "medium", "hard"], 
                                format_func=lambda x: {"easy": "Fácil", "medium": "Medio", "hard": "Difícil"}[x])
    
    with col3:
        if st.button("🎲 Nuevo Ejercicio", type="primary"):
            exercise = st.session_state.arithmetic_generator.generate_random_exercise(topic, difficulty)
            st.session_state.current_exercise = exercise
            st.session_state.user_answer = ""
            st.session_state.show_solution = False
    
    # Mostrar estadísticas
    stats = st.session_state.arithmetic_stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Correctas", stats['correct'])
    with col2:
        st.metric("Total", stats['total'])
    with col3:
        accuracy = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
        st.metric("Precisión", f"{accuracy:.1f}%")
    with col4:
        st.metric("Mejor Racha", stats['best_streak'])
    
    # Mostrar ejercicio actual
    if 'current_exercise' in st.session_state:
        exercise = st.session_state.current_exercise
        
        st.markdown("## 📝 Ejercicio")
        st.markdown(exercise['problem'])
        
        # Input para respuesta
        col1, col2 = st.columns([3, 1])
        
        with col1:
            user_answer = st.text_input("Tu respuesta:", key="answer_input")
        
        with col2:
            check_button = st.button("✅ Verificar")
        
        # Verificar respuesta
        if check_button and user_answer:
            is_correct = check_answer(user_answer, exercise['answer'])
            
            # Actualizar estadísticas
            st.session_state.arithmetic_stats['total'] += 1
            
            if is_correct:
                st.session_state.arithmetic_stats['correct'] += 1
                st.session_state.arithmetic_stats['streak'] += 1
                if st.session_state.arithmetic_stats['streak'] > st.session_state.arithmetic_stats['best_streak']:
                    st.session_state.arithmetic_stats['best_streak'] = st.session_state.arithmetic_stats['streak']
                
                st.markdown("""
                <div class="success-box">
                    <h4>🎉 ¡Correcto!</h4>
                    <p>Excelente trabajo. ¡Sigue así!</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.session_state.arithmetic_stats['streak'] = 0
                
                st.markdown("""
                <div class="error-box">
                    <h4>❌ Incorrecto</h4>
                    <p>No te preocupes, revisa la solución y sigue practicando.</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.session_state.show_solution = True
        
        # Mostrar solución si está disponible
        if st.session_state.get('show_solution', False):
            st.markdown("## 💡 Solución")
            st.markdown(f"**Respuesta correcta:** {exercise['answer']}")
            
            if 'solution_steps' in exercise and exercise['solution_steps']:
                st.markdown("**Pasos de solución:**")
                for i, step in enumerate(exercise['solution_steps'], 1):
                    st.markdown(f"{i}. {step}")
    
    else:
        st.info("Haz clic en 'Nuevo Ejercicio' para comenzar a practicar.")

def show_algebra_practice():
    """Página de práctica de álgebra"""
    
    st.markdown("# 💪 Práctica - Álgebra")
    
    # Inicializar estadísticas si no existen
    if 'algebra_stats' not in st.session_state:
        st.session_state.algebra_stats = {
            'correct': 0,
            'total': 0,
            'streak': 0,
            'best_streak': 0
        }
    
    # Configuración de práctica
    col1, col2, col3 = st.columns(3)
    
    with col1:
        topic = st.selectbox(
            "Tema:",
            ["monomios", "polinomios", "productos_notables", "factorizacion"],
            format_func=lambda x: {
                "monomios": "Monomios",
                "polinomios": "Polinomios",
                "productos_notables": "Productos Notables",
                "factorizacion": "Factorización"
            }[x]
        )
    
    with col2:
        difficulty = st.selectbox("Dificultad:", ["easy", "medium", "hard"], 
                                format_func=lambda x: {"easy": "Fácil", "medium": "Medio", "hard": "Difícil"}[x])
    
    with col3:
        if st.button("🎲 Nuevo Ejercicio", type="primary"):
            exercise = st.session_state.algebra_generator.generate_random_exercise(topic, difficulty)
            st.session_state.current_algebra_exercise = exercise
            st.session_state.algebra_user_answer = ""
            st.session_state.show_algebra_solution = False
    
    # Mostrar estadísticas
    stats = st.session_state.algebra_stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Correctas", stats['correct'])
    with col2:
        st.metric("Total", stats['total'])
    with col3:
        accuracy = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
        st.metric("Precisión", f"{accuracy:.1f}%")
    with col4:
        st.metric("Mejor Racha", stats['best_streak'])
    
    # Mostrar ejercicio actual
    if 'current_algebra_exercise' in st.session_state:
        exercise = st.session_state.current_algebra_exercise
        
        st.markdown("## 📝 Ejercicio")
        st.markdown(exercise['problem'])
        
        # Input para respuesta
        col1, col2 = st.columns([3, 1])
        
        with col1:
            user_answer = st.text_input("Tu respuesta:", key="algebra_answer_input")
        
        with col2:
            check_button = st.button("✅ Verificar")
        
        # Verificar respuesta
        if check_button and user_answer:
            is_correct = check_answer(user_answer, exercise['answer'])
            
            # Actualizar estadísticas
            st.session_state.algebra_stats['total'] += 1
            
            if is_correct:
                st.session_state.algebra_stats['correct'] += 1
                st.session_state.algebra_stats['streak'] += 1
                if st.session_state.algebra_stats['streak'] > st.session_state.algebra_stats['best_streak']:
                    st.session_state.algebra_stats['best_streak'] = st.session_state.algebra_stats['streak']
                
                st.markdown("""
                <div class="success-box">
                    <h4>🎉 ¡Correcto!</h4>
                    <p>Excelente trabajo. ¡Sigue así!</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.session_state.algebra_stats['streak'] = 0
                
                st.markdown("""
                <div class="error-box">
                    <h4>❌ Incorrecto</h4>
                    <p>No te preocupes, revisa la solución y sigue practicando.</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.session_state.show_algebra_solution = True
        
        # Mostrar solución si está disponible
        if st.session_state.get('show_algebra_solution', False):
            st.markdown("## 💡 Solución")
            st.markdown(f"**Respuesta correcta:** {exercise['answer']}")
            
            if 'solution_steps' in exercise and exercise['solution_steps']:
                st.markdown("**Pasos de solución:**")
                for i, step in enumerate(exercise['solution_steps'], 1):
                    st.markdown(f"{i}. {step}")
    
    else:
        st.info("Haz clic en 'Nuevo Ejercicio' para comenzar a practicar.")

def show_exam_page():
    """Página de exámenes"""
    
    st.markdown("# 📝 Exámenes")
    
    # Inicializar estado del examen
    if 'exam_state' not in st.session_state:
        st.session_state.exam_state = 'setup'  # setup, active, completed
    
    if st.session_state.exam_state == 'setup':
        show_exam_setup()
    elif st.session_state.exam_state == 'active':
        show_exam_active()
    elif st.session_state.exam_state == 'completed':
        show_exam_results()

def show_exam_setup():
    """Configuración del examen"""
    
    st.markdown("## ⚙️ Configurar Examen")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Temas a incluir:")
        topics = st.multiselect(
            "Selecciona los temas:",
            ["arithmetic", "algebra"],
            default=["arithmetic"],
            format_func=lambda x: {"arithmetic": "Aritmética", "algebra": "Álgebra"}[x]
        )
        
        num_questions = st.slider("Número de preguntas:", 5, 20, 10)
    
    with col2:
        st.markdown("### Configuración:")
        time_limit = st.slider("Tiempo límite (minutos):", 10, 60, 30)
        difficulty = st.selectbox("Dificultad:", ["easy", "medium", "hard"], 
                                index=1,
                                format_func=lambda x: {"easy": "Fácil", "medium": "Medio", "hard": "Difícil"}[x])
    
    # Resumen de configuración
    st.markdown("### 📋 Resumen:")
    st.info(f"""
    - **Temas:** {', '.join([{'arithmetic': 'Aritmética', 'algebra': 'Álgebra'}[t] for t in topics])}
    - **Preguntas:** {num_questions}
    - **Tiempo:** {time_limit} minutos
    - **Dificultad:** {{'easy': 'Fácil', 'medium': 'Medio', 'hard': 'Difícil'}[difficulty]}
    """)
    
    if st.button("🚀 Comenzar Examen", type="primary", disabled=not topics):
        # Generar preguntas del examen
        questions = generate_exam_questions(topics, num_questions, difficulty)
        
        st.session_state.exam_config = {
            'topics': topics,
            'num_questions': num_questions,
            'time_limit': time_limit,
            'difficulty': difficulty,
            'questions': questions,
            'current_question': 0,
            'answers': {},
            'start_time': datetime.now()
        }
        
        st.session_state.exam_state = 'active'
        st.rerun()

def show_exam_active():
    """Examen activo"""
    
    config = st.session_state.exam_config
    current_q = config['current_question']
    questions = config['questions']
    
    # Calcular tiempo restante
    elapsed = datetime.now() - config['start_time']
    time_limit = timedelta(minutes=config['time_limit'])
    remaining = time_limit - elapsed
    
    if remaining.total_seconds() <= 0:
        st.session_state.exam_state = 'completed'
        st.rerun()
    
    # Header con información del examen
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Pregunta", f"{current_q + 1}/{len(questions)}")
    with col2:
        st.metric("Tiempo Restante", f"{int(remaining.total_seconds() // 60)}:{int(remaining.total_seconds() % 60):02d}")
    with col3:
        progress = (current_q + 1) / len(questions)
        st.metric("Progreso", f"{progress:.0%}")
    
    st.progress(progress)
    
    # Pregunta actual
    if current_q < len(questions):
        question = questions[current_q]
        
        st.markdown(f"## Pregunta {current_q + 1}")
        st.markdown(question['problem'])
        
        # Input para respuesta
        answer_key = f"exam_answer_{current_q}"
        user_answer = st.text_input("Tu respuesta:", key=answer_key)
        
        # Botones de navegación
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if current_q > 0:
                if st.button("⬅️ Anterior"):
                    if user_answer:
                        config['answers'][current_q] = user_answer
                    config['current_question'] -= 1
                    st.rerun()
        
        with col2:
            if st.button("💾 Guardar Respuesta"):
                config['answers'][current_q] = user_answer
                st.success("Respuesta guardada")
        
        with col3:
            if current_q < len(questions) - 1:
                if st.button("Siguiente ➡️"):
                    if user_answer:
                        config['answers'][current_q] = user_answer
                    config['current_question'] += 1
                    st.rerun()
            else:
                if st.button("🏁 Finalizar Examen", type="primary"):
                    if user_answer:
                        config['answers'][current_q] = user_answer
                    st.session_state.exam_state = 'completed'
                    st.rerun()
    
    # Botón de emergencia para finalizar
    if st.button("⚠️ Finalizar Examen Ahora"):
        st.session_state.exam_state = 'completed'
        st.rerun()

def show_exam_results():
    """Resultados del examen"""
    
    config = st.session_state.exam_config
    questions = config['questions']
    answers = config['answers']
    
    # Calcular resultados
    correct = 0
    total = len(questions)
    
    results = []
    for i, question in enumerate(questions):
        user_answer = answers.get(i, "")
        is_correct = check_answer(user_answer, question['answer'])
        if is_correct:
            correct += 1
        
        results.append({
            'question': question,
            'user_answer': user_answer,
            'correct_answer': question['answer'],
            'is_correct': is_correct
        })
    
    score = (correct / total) * 100
    
    # Mostrar resultados generales
    st.markdown("# 🎯 Resultados del Examen")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Puntuación", f"{score:.1f}%")
    with col2:
        st.metric("Correctas", f"{correct}/{total}")
    with col3:
        st.metric("Incorrectas", total - correct)
    with col4:
        grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
        st.metric("Calificación", grade)
    
    # Gráfico de resultados
    if score >= 80:
        st.success(f"¡Excelente trabajo! Obtuviste {score:.1f}%")
    elif score >= 60:
        st.warning(f"Buen trabajo, pero puedes mejorar. Obtuviste {score:.1f}%")
    else:
        st.error(f"Necesitas estudiar más. Obtuviste {score:.1f}%")
    
    # Detalles por pregunta
    st.markdown("## 📊 Detalles por Pregunta")
    
    for i, result in enumerate(results):
        with st.expander(f"Pregunta {i+1} - {'✅ Correcta' if result['is_correct'] else '❌ Incorrecta'}"):
            st.markdown(f"**Pregunta:** {result['question']['problem']}")
            st.markdown(f"**Tu respuesta:** {result['user_answer'] or 'Sin respuesta'}")
            st.markdown(f"**Respuesta correcta:** {result['correct_answer']}")
            
            if 'solution_steps' in result['question']:
                st.markdown("**Explicación:**")
                for step in result['question']['solution_steps']:
                    st.markdown(f"- {step}")
    
    # Botones de acción
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Nuevo Examen"):
            st.session_state.exam_state = 'setup'
            if 'exam_config' in st.session_state:
                del st.session_state.exam_config
            st.rerun()
    
    with col2:
        if st.button("📚 Estudiar Temas"):
            st.session_state.page = "🏠 Inicio"
            st.rerun()

def generate_exam_questions(topics, num_questions, difficulty):
    """Genera preguntas para el examen"""
    questions = []
    
    questions_per_topic = num_questions // len(topics)
    remaining = num_questions % len(topics)
    
    for i, topic in enumerate(topics):
        topic_questions = questions_per_topic
        if i < remaining:
            topic_questions += 1
        
        if topic == 'arithmetic':
            generator = st.session_state.arithmetic_generator
            subtopics = ['fraction_operations', 'combined_operations', 'mcm_mcd', 'factorization']
        else:  # algebra
            generator = st.session_state.algebra_generator
            subtopics = ['monomios', 'polinomios', 'productos_notables', 'factorizacion']
        
        for _ in range(topic_questions):
            subtopic = random.choice(subtopics)
            question = generator.generate_random_exercise(subtopic, difficulty)
            questions.append(question)
    
    random.shuffle(questions)
    return questions

def check_answer(user_answer, correct_answer):
    """Verifica si la respuesta del usuario es correcta"""
    try:
        # Normalizar respuestas
        user_clean = str(user_answer).strip().replace(' ', '')
        correct_clean = str(correct_answer).strip().replace(' ', '')
        
        # Comparación directa
        if user_clean.lower() == correct_clean.lower():
            return True
        
        # Intentar evaluación matemática
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
        
        return False
        
    except:
        return False

if __name__ == "__main__":
    main()
