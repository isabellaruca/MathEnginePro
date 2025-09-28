"""
Generador de ejercicios para el módulo de Álgebra
"""
import random
import sympy as sp
from sympy import symbols, expand, factor, simplify

def get_random_exercise(topic=None, difficulty='medium'):
    """
    Genera un ejercicio aleatorio de álgebra
    """
    if topic is None:
        topics = ['monomios', 'polinomios', 'productos_notables', 'factorizacion']
        topic = random.choice(topics)
    
    generators = {
        'monomios': generate_monomial_exercise,
        'polinomios': generate_polynomial_exercise,
        'productos_notables': generate_notable_products_exercise,
        'factorizacion': generate_factorization_exercise
    }
    
    generator = generators.get(topic, generate_monomial_exercise)
    return generator(difficulty)

def generate_monomial_exercise(difficulty='medium'):
    """Genera ejercicios de operaciones con monomios"""
    x, y = symbols('x y')
    
    exercises = {
        'easy': [
            {
                'type': 'multiplication',
                'problem': 'Multiplica: $(3x^2) \cdot (4x^3)$',
                'expression': '3*x**2 * 4*x**3',
                'answer': '12*x**5',
                'solution_steps': [
                    'Multiplica los coeficientes: $3 \\times 4 = 12$',
                    'Suma los exponentes de x: $x^2 \\times x^3 = x^{2+3} = x^5$',
                    'Resultado: $12x^5$'
                ]
            },
            {
                'type': 'division',
                'problem': 'Divide: $\\frac{15x^4}{3x^2}$',
                'expression': '15*x**4 / (3*x**2)',
                'answer': '5*x**2',
                'solution_steps': [
                    'Divide los coeficientes: $15 \\div 3 = 5$',
                    'Resta los exponentes de x: $x^4 \\div x^2 = x^{4-2} = x^2$',
                    'Resultado: $5x^2$'
                ]
            }
        ],
        'medium': [
            {
                'type': 'mixed_operations',
                'problem': 'Simplifica: $(2x^2y) \cdot (-3xy^2) + (12x^3y^3) \\div (4xy)$',
                'expression': '2*x**2*y * (-3)*x*y**2 + 12*x**3*y**3 / (4*x*y)',
                'answer': '-6*x**3*y**3 + 3*x**2*y**2',
                'solution_steps': [
                    'Primer término: $(2x^2y) \cdot (-3xy^2) = -6x^3y^3$',
                    'Segundo término: $\\frac{12x^3y^3}{4xy} = 3x^2y^2$',
                    'Suma: $-6x^3y^3 + 3x^2y^2$'
                ]
            }
        ],
        'hard': [
            {
                'type': 'complex_operations',
                'problem': 'Simplifica: $\\frac{(3x^2y)^3 \cdot (2xy^2)^2}{(6x^3y^4)^2}$',
                'expression': '(3*x**2*y)**3 * (2*x*y**2)**2 / (6*x**3*y**4)**2',
                'answer': '1/(4*x**2*y**3)',
                'solution_steps': [
                    'Numerador: $(3x^2y)^3 = 27x^6y^3$ y $(2xy^2)^2 = 4x^2y^4$',
                    'Producto del numerador: $27x^6y^3 \cdot 4x^2y^4 = 108x^8y^7$',
                    'Denominador: $(6x^3y^4)^2 = 36x^6y^8$',
                    'División: $\\frac{108x^8y^7}{36x^6y^8} = 3x^2y^{-1} = \\frac{3x^2}{y}$'
                ]
            }
        ]
    }
    
    return random.choice(exercises[difficulty])

def generate_polynomial_exercise(difficulty='medium'):
    """Genera ejercicios de operaciones con polinomios"""
    exercises = {
        'easy': [
            {
                'type': 'addition',
                'problem': 'Suma: $(2x^2 + 3x - 1) + (x^2 - 2x + 4)$',
                'expression': '(2*x**2 + 3*x - 1) + (x**2 - 2*x + 4)',
                'answer': '3*x**2 + x + 3',
                'solution_steps': [
                    'Agrupa términos semejantes',
                    '$2x^2 + x^2 = 3x^2$',
                    '$3x - 2x = x$',
                    '$-1 + 4 = 3$',
                    'Resultado: $3x^2 + x + 3$'
                ]
            }
        ],
        'medium': [
            {
                'type': 'multiplication',
                'problem': 'Multiplica: $(x + 3)(2x - 1)$',
                'expression': '(x + 3) * (2*x - 1)',
                'answer': '2*x**2 + 5*x - 3',
                'solution_steps': [
                    'Aplica la propiedad distributiva',
                    '$x \cdot 2x = 2x^2$',
                    '$x \cdot (-1) = -x$',
                    '$3 \cdot 2x = 6x$',
                    '$3 \cdot (-1) = -3$',
                    'Suma: $2x^2 - x + 6x - 3 = 2x^2 + 5x - 3$'
                ]
            }
        ],
        'hard': [
            {
                'type': 'complex_multiplication',
                'problem': 'Desarrolla: $(x^2 + 2x - 1)(x - 3)$',
                'expression': '(x**2 + 2*x - 1) * (x - 3)',
                'answer': 'x**3 - x**2 - 7*x + 3',
                'solution_steps': [
                    'Multiplica cada término del primer polinomio por cada término del segundo',
                    '$x^2 \cdot x = x^3$',
                    '$x^2 \cdot (-3) = -3x^2$',
                    '$2x \cdot x = 2x^2$',
                    '$2x \cdot (-3) = -6x$',
                    '$(-1) \cdot x = -x$',
                    '$(-1) \cdot (-3) = 3$',
                    'Suma: $x^3 - 3x^2 + 2x^2 - 6x - x + 3 = x^3 - x^2 - 7x + 3$'
                ]
            }
        ]
    }
    
    return random.choice(exercises[difficulty])

def generate_notable_products_exercise(difficulty='medium'):
    """Genera ejercicios de productos notables"""
    exercises = {
        'easy': [
            {
                'type': 'square_sum',
                'problem': 'Desarrolla: $(x + 4)^2$',
                'expression': '(x + 4)**2',
                'answer': 'x**2 + 8*x + 16',
                'solution_steps': [
                    'Aplica la fórmula $(a + b)^2 = a^2 + 2ab + b^2$',
                    '$a = x$, $b = 4$',
                    '$a^2 = x^2$',
                    '$2ab = 2 \cdot x \cdot 4 = 8x$',
                    '$b^2 = 16$',
                    'Resultado: $x^2 + 8x + 16$'
                ]
            }
        ],
        'medium': [
            {
                'type': 'difference_squares',
                'problem': 'Desarrolla: $(3x + 2)(3x - 2)$',
                'expression': '(3*x + 2) * (3*x - 2)',
                'answer': '9*x**2 - 4',
                'solution_steps': [
                    'Reconoce la diferencia de cuadrados $(a + b)(a - b) = a^2 - b^2$',
                    '$a = 3x$, $b = 2$',
                    '$a^2 = (3x)^2 = 9x^2$',
                    '$b^2 = 2^2 = 4$',
                    'Resultado: $9x^2 - 4$'
                ]
            }
        ],
        'hard': [
            {
                'type': 'cube_sum',
                'problem': 'Desarrolla: $(x + 2)^3$',
                'expression': '(x + 2)**3',
                'answer': 'x**3 + 6*x**2 + 12*x + 8',
                'solution_steps': [
                    'Aplica la fórmula $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$',
                    '$a = x$, $b = 2$',
                    '$a^3 = x^3$',
                    '$3a^2b = 3 \cdot x^2 \cdot 2 = 6x^2$',
                    '$3ab^2 = 3 \cdot x \cdot 4 = 12x$',
                    '$b^3 = 8$',
                    'Resultado: $x^3 + 6x^2 + 12x + 8$'
                ]
            }
        ]
    }
    
    return random.choice(exercises[difficulty])

def generate_factorization_exercise(difficulty='medium'):
    """Genera ejercicios de factorización"""
    exercises = {
        'easy': [
            {
                'type': 'common_factor',
                'problem': 'Factoriza: $6x^2 + 9x$',
                'expression': '6*x**2 + 9*x',
                'answer': '3*x*(2*x + 3)',
                'solution_steps': [
                    'Identifica el factor común',
                    'Factor común de coeficientes: MCD(6, 9) = 3',
                    'Factor común de variables: x',
                    'Factor común total: 3x',
                    'Factorización: $3x(2x + 3)$'
                ]
            }
        ],
        'medium': [
            {
                'type': 'perfect_square_trinomial',
                'problem': 'Factoriza: $x^2 + 6x + 9$',
                'expression': 'x**2 + 6*x + 9',
                'answer': '(x + 3)**2',
                'solution_steps': [
                    'Reconoce el trinomio cuadrado perfecto',
                    'Verifica: $a^2 + 2ab + b^2$ donde $a = x$, $b = 3$',
                    '$x^2 + 2(x)(3) + 3^2 = x^2 + 6x + 9$ ✓',
                    'Factorización: $(x + 3)^2$'
                ]
            }
        ],
        'hard': [
            {
                'type': 'difference_squares',
                'problem': 'Factoriza: $16x^4 - 81$',
                'expression': '16*x**4 - 81',
                'answer': '(4*x**2 + 9)*(4*x**2 - 9)',
                'solution_steps': [
                    'Reconoce la diferencia de cuadrados',
                    '$16x^4 - 81 = (4x^2)^2 - 9^2$',
                    'Aplica $a^2 - b^2 = (a + b)(a - b)$',
                    'Primera factorización: $(4x^2 + 9)(4x^2 - 9)$',
                    'El segundo factor es otra diferencia de cuadrados:',
                    '$4x^2 - 9 = (2x)^2 - 3^2 = (2x + 3)(2x - 3)$',
                    'Factorización completa: $(4x^2 + 9)(2x + 3)(2x - 3)$'
                ]
            }
        ]
    }
    
    return random.choice(exercises[difficulty])
