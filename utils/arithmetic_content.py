"""
Contenido teórico para el módulo de Aritmética
Migrado desde el proyecto Django original
"""

ARITHMETIC_CONTENT = {
    'title': 'Aritmética',
    'description': 'Fundamentos de la aritmética y operaciones básicas',
    'sections': [
        {
            'id': 'conjuntos_numericos',
            'title': 'Conjuntos Numéricos',
            'content': '''
            #### Conjuntos Numéricos Fundamentales
            Los números se organizan en diferentes conjuntos con propiedades específicas:
            
            **Números Naturales (ℕ)**
            $$\\mathbb{N} = \\{1, 2, 3, 4, 5, ...\\}$$
            Se usan para contar objetos.
            
            **Números Enteros (ℤ)**
            $$\\mathbb{Z} = \\{..., -2, -1, 0, 1, 2, ...\\}$$
            Incluyen números negativos y el cero.
            
            **Números Racionales (ℚ)**
            $$\\mathbb{Q} = \\left\\{\\frac{a}{b} : a, b \\in \\mathbb{Z}, b \\neq 0\\right\\}$$
            Números que se pueden expresar como fracción.
            
            **Números Reales (ℝ)**
            Incluyen racionales e irracionales como π y √2.
            ''',
            'examples': [
                {
                    'title': 'Clasificación de Números',
                    'problem': 'Clasifica los siguientes números: 5, -3, 1/2, √2, π',
                    'solution': '''
                    - **5:** Natural, Entero, Racional, Real
                    - **-3:** Entero, Racional, Real
                    - **1/2:** Racional, Real
                    - **√2:** Irracional, Real
                    - **π:** Irracional, Real
                    '''
                }
            ]
        },
        {
            'id': 'operaciones_combinadas',
            'title': 'Operaciones Combinadas',
            'content': '''
            #### Jerarquía de Operaciones
            Para resolver expresiones con múltiples operaciones, seguimos este orden:
            
            1. **Paréntesis** ( ), Corchetes [ ], Llaves { }
            2. **Exponentes y Raíces** $x^n$, $\\sqrt{x}$
            3. **Multiplicación y División** (de izquierda a derecha)
            4. **Suma y Resta** (de izquierda a derecha)
            
            **Regla Nemotécnica:** *PEMDAS* o *BODMAS*
            ''',
            'examples': [
                {
                    'title': 'Operación Combinada',
                    'problem': 'Resolver: $2 + 3 \\times (4^2 - 2 \\times 5)$',
                    'solution': '''
                    **Paso 1:** Resolver el exponente
                    $2 + 3 \\times (16 - 2 \\times 5)$
                    
                    **Paso 2:** Multiplicación dentro del paréntesis
                    $2 + 3 \\times (16 - 10)$
                    
                    **Paso 3:** Resta dentro del paréntesis
                    $2 + 3 \\times 6$
                    
                    **Paso 4:** Multiplicación
                    $2 + 18$
                    
                    **Resultado:** $20$
                    '''
                }
            ]
        },
        {
            'id': 'fracciones',
            'title': 'Fracciones',
            'content': '''
            #### Operaciones con Fracciones
            Una fracción representa una parte de un todo: $\\frac{a}{b}$ donde $a$ es el numerador y $b$ el denominador.
            
            **Suma y Resta**
            $$\\frac{a}{c} \\pm \\frac{b}{c} = \\frac{a \\pm b}{c}$$
            
            Para denominadores diferentes:
            $$\\frac{a}{b} \\pm \\frac{c}{d} = \\frac{ad \\pm bc}{bd}$$
            
            **Multiplicación**
            $$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{ac}{bd}$$
            
            **División**
            $$\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c} = \\frac{ad}{bc}$$
            ''',
            'examples': [
                {
                    'title': 'Suma de Fracciones',
                    'problem': 'Calcular: $\\frac{2}{3} + \\frac{1}{4}$',
                    'solution': '''
                    **Paso 1:** Encontrar denominador común
                    MCM(3, 4) = 12
                    
                    **Paso 2:** Convertir fracciones
                    $\\frac{2}{3} = \\frac{8}{12}$ y $\\frac{1}{4} = \\frac{3}{12}$
                    
                    **Paso 3:** Sumar numeradores
                    $\\frac{8}{12} + \\frac{3}{12} = \\frac{11}{12}$
                    '''
                }
            ]
        },
        {
            'id': 'mcm_mcd',
            'title': 'MCM y MCD',
            'content': '''
            #### Máximo Común Divisor y Mínimo Común Múltiplo
            
            **MCD (Máximo Común Divisor)**
            El mayor número que divide exactamente a dos o más números.
            **Método:** Factorización prima y tomar factores comunes con menor exponente.
            
            **MCM (Mínimo Común Múltiplo)**
            El menor número que es múltiplo de dos o más números.
            **Método:** Factorización prima y tomar todos los factores con mayor exponente.
            
            **Relación importante:** $MCD(a,b) \\times MCM(a,b) = a \\times b$
            ''',
            'examples': [
                {
                    'title': 'Calcular MCD y MCM',
                    'problem': 'Encontrar MCD(12, 18) y MCM(12, 18)',
                    'solution': '''
                    **Factorización prima:**
                    12 = 2² × 3
                    18 = 2 × 3²
                    
                    **MCD:** Factores comunes con menor exponente
                    MCD(12, 18) = 2¹ × 3¹ = 6
                    
                    **MCM:** Todos los factores con mayor exponente
                    MCM(12, 18) = 2² × 3² = 36
                    
                    **Verificación:** 6 × 36 = 216 = 12 × 18 ✓
                    '''
                }
            ]
        }
    ]
}

def get_arithmetic_content():
    """Retorna el contenido teórico completo"""
    return ARITHMETIC_CONTENT

def get_arithmetic_section(section_id):
    """Retorna el contenido de una sección específica"""
    for section in ARITHMETIC_CONTENT['sections']:
        if section['id'] == section_id:
            return section
    return None

def get_explanation_for_error(error_type):
    """
    Retorna explicación específica basada en el tipo de error cometido
    """
    explanations = {
        'fraction_addition': '''
        #### Recordatorio: Suma de Fracciones
        Para sumar fracciones con diferentes denominadores:
        1. Encuentra el denominador común (MCM)
        2. Convierte ambas fracciones al mismo denominador
        3. Suma solo los numeradores
        4. Simplifica si es posible
        ''',
        'order_operations': '''
        #### Recordatorio: Orden de Operaciones
        Recuerda la jerarquía PEMDAS:
        1. **P**aréntesis
        2. **E**xponentes
        3. **M**ultiplicación y **D**ivisión (izq. a der.)
        4. **A**dición y **S**ustracción (izq. a der.)
        ''',
        'factorization': '''
        #### Recordatorio: Factorización
        Para factorizar un número:
        1. Divide por números primos empezando por 2
        2. Continúa hasta que el cociente sea 1
        3. Expresa como producto de potencias de primos
        '''
    }
    
    return explanations.get(error_type, 'Revisa la teoría correspondiente para entender mejor este concepto.')
