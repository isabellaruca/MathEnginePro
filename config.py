"""
Configuración global de la aplicación MathEngine
"""

import streamlit as st

# Configuración de la aplicación
APP_CONFIG = {
    'title': 'MathEngine - Plataforma de Matemáticas',
    'icon': '🧮',
    'layout': 'wide',
    'sidebar_state': 'expanded'
}

# Configuración de temas
THEMES = {
    'primary_color': '#667eea',
    'secondary_color': '#764ba2',
    'success_color': '#4caf50',
    'error_color': '#f44336',
    'warning_color': '#ff9800',
    'info_color': '#2196f3'
}

# Configuración de ejercicios
EXERCISE_CONFIG = {
    'difficulties': ['easy', 'medium', 'hard'],
    'difficulty_labels': {
        'easy': 'Fácil',
        'medium': 'Medio', 
        'hard': 'Difícil'
    },
    'arithmetic_topics': {
        'fraction_operations': 'Operaciones con Fracciones',
        'combined_operations': 'Operaciones Combinadas',
        'mcm_mcd': 'MCM y MCD',
        'factorization': 'Factorización',
        'word_problems': 'Problemas Verbales'
    },
    'algebra_topics': {
        'monomios': 'Monomios',
        'polinomios': 'Polinomios', 
        'productos_notables': 'Productos Notables',
        'factorizacion': 'Factorización'
    }
}

# Configuración de exámenes
EXAM_CONFIG = {
    'min_questions': 5,
    'max_questions': 20,
    'default_questions': 10,
    'min_time': 10,
    'max_time': 60,
    'default_time': 30,
    'available_topics': ['arithmetic', 'algebra'],
    'topic_labels': {
        'arithmetic': 'Aritmética',
        'algebra': 'Álgebra'
    }
}

def init_session_state():
    """Inicializa el estado de la sesión con valores por defecto"""
    
    # Estadísticas de aritmética
    if 'arithmetic_stats' not in st.session_state:
        st.session_state.arithmetic_stats = {
            'correct': 0,
            'total': 0,
            'streak': 0,
            'best_streak': 0
        }
    
    # Estadísticas de álgebra
    if 'algebra_stats' not in st.session_state:
        st.session_state.algebra_stats = {
            'correct': 0,
            'total': 0,
            'streak': 0,
            'best_streak': 0
        }
    
    # Estado del examen
    if 'exam_state' not in st.session_state:
        st.session_state.exam_state = 'setup'
    
    # Secciones seleccionadas
    if 'selected_arithmetic_section' not in st.session_state:
        st.session_state.selected_arithmetic_section = 'conjuntos_numericos'
    
    if 'selected_algebra_section' not in st.session_state:
        st.session_state.selected_algebra_section = 'monomios'
    
    # Estados de solución
    if 'show_solution' not in st.session_state:
        st.session_state.show_solution = False
    
    if 'show_algebra_solution' not in st.session_state:
        st.session_state.show_algebra_solution = False

def get_custom_css():
    """Retorna el CSS personalizado para la aplicación"""
    return """
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
        
        .info-box {
            background: #e3f2fd;
            padding: 1rem;
            border-radius: 5px;
            border-left: 3px solid #2196f3;
            color: #1565c0;
        }
        
        .warning-box {
            background: #fff3e0;
            padding: 1rem;
            border-radius: 5px;
            border-left: 3px solid #ff9800;
            color: #ef6c00;
        }
        
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }
        
        .metric-card {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .progress-bar {
            background: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            height: 20px;
        }
        
        .progress-fill {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            height: 100%;
            transition: width 0.3s ease;
        }
        
        .exam-timer {
            background: #ffebee;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            color: #c62828;
            font-weight: bold;
            text-align: center;
        }
        
        .question-nav {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin: 1rem 0;
        }
        
        .question-nav-item {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .question-nav-item.answered {
            background: #4caf50;
            color: white;
        }
        
        .question-nav-item.current {
            background: #2196f3;
            color: white;
        }
        
        .question-nav-item.unanswered {
            background: #e0e0e0;
            color: #666;
        }
    </style>
    """
