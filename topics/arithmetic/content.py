"""
Contenido teórico para el módulo de Aritmética
Este archivo contiene toda la teoría, ejemplos y explicaciones del tema
"""

ARITHMETIC_CONTENT = {
    'title': 'Aritmética',
    'description': 'Fundamentos de la aritmética y operaciones básicas',
    'sections': [
        {
            'id': 'conjuntos_numericos',
            'title': 'Conjuntos Numéricos',
            'content': '''
            <h4>Conjuntos Numéricos Fundamentales</h4>
            <p>Los números se organizan en diferentes conjuntos con propiedades específicas:</p>
            
            <div class="row">
                <div class="col-md-6">
                    <h5>Números Naturales (ℕ)</h5>
                    <p>$$\\mathbb{N} = \\{1, 2, 3, 4, 5, ...\\}$$</p>
                    <p>Se usan para contar objetos.</p>
                </div>
                <div class="col-md-6">
                    <h5>Números Enteros (ℤ)</h5>
                    <p>$$\\mathbb{Z} = \\{..., -2, -1, 0, 1, 2, ...\\}$$</p>
                    <p>Incluyen números negativos y el cero.</p>
                </div>
            </div>
            
            <div class="row mt-3">
                <div class="col-md-6">
                    <h5>Números Racionales (ℚ)</h5>
                    <p>$$\\mathbb{Q} = \\left\\{\\frac{a}{b} : a, b \\in \\mathbb{Z}, b \\neq 0\\right\\}$$</p>
                    <p>Números que se pueden expresar como fracción.</p>
                </div>
                <div class="col-md-6">
                    <h5>Números Reales (ℝ)</h5>
                    <p>Incluyen racionales e irracionales como $\\pi$ y $\\sqrt{2}$.</p>
                </div>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Clasificación de Números',
                    'problem': 'Clasifica los siguientes números: 5, -3, 1/2, √2, π',
                    'solution': '''
                    <ul>
                        <li><strong>5:</strong> Natural, Entero, Racional, Real</li>
                        <li><strong>-3:</strong> Entero, Racional, Real</li>
                        <li><strong>1/2:</strong> Racional, Real</li>
                        <li><strong>√2:</strong> Irracional, Real</li>
                        <li><strong>π:</strong> Irracional, Real</li>
                    </ul>
                    '''
                }
            ]
        },
        {
            'id': 'operaciones_combinadas',
            'title': 'Operaciones Combinadas',
            'content': '''
            <h4>Jerarquía de Operaciones</h4>
            <p>Para resolver expresiones con múltiples operaciones, seguimos este orden:</p>
            
            <ol class="list-group list-group-numbered">
                <li class="list-group-item bg-dark">
                    <strong>Paréntesis</strong> ( ), Corchetes [ ], Llaves { }
                </li>
                <li class="list-group-item bg-dark">
                    <strong>Exponentes y Raíces</strong> $x^n$, $\\sqrt{x}$
                </li>
                <li class="list-group-item bg-dark">
                    <strong>Multiplicación y División</strong> (de izquierda a derecha)
                </li>
                <li class="list-group-item bg-dark">
                    <strong>Suma y Resta</strong> (de izquierda a derecha)
                </li>
            </ol>
            
            <div class="alert alert-info mt-3">
                <strong>Regla Nemotécnica:</strong> <em>PEMDAS</em> o <em>BODMAS</em>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Operación Combinada',
                    'problem': 'Resolver: $2 + 3 \\times (4^2 - 2 \\times 5)$',
                    'solution': '''
                    <div class="step-by-step">
                        <p><strong>Paso 1:</strong> Resolver el exponente</p>
                        <p>$2 + 3 \\times (16 - 2 \\times 5)$</p>
                        
                        <p><strong>Paso 2:</strong> Multiplicación dentro del paréntesis</p>
                        <p>$2 + 3 \\times (16 - 10)$</p>
                        
                        <p><strong>Paso 3:</strong> Resta dentro del paréntesis</p>
                        <p>$2 + 3 \\times 6$</p>
                        
                        <p><strong>Paso 4:</strong> Multiplicación</p>
                        <p>$2 + 18$</p>
                        
                        <p><strong>Resultado:</strong> $20$</p>
                    </div>
                    '''
                }
            ]
        },
        {
            'id': 'fracciones',
            'title': 'Fracciones',
            'content': '''
            <h4>Operaciones con Fracciones</h4>
            <p>Una fracción representa una parte de un todo: $\\frac{a}{b}$ donde $a$ es el numerador y $b$ el denominador.</p>
            
            <div class="row">
                <div class="col-md-6">
                    <h5>Suma y Resta</h5>
                    <p>$$\\frac{a}{c} \\pm \\frac{b}{c} = \\frac{a \\pm b}{c}$$</p>
                    <p>Para denominadores diferentes:</p>
                    <p>$$\\frac{a}{b} \\pm \\frac{c}{d} = \\frac{ad \\pm bc}{bd}$$</p>
                </div>
                <div class="col-md-6">
                    <h5>Multiplicación</h5>
                    <p>$$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{ac}{bd}$$</p>
                    
                    <h5>División</h5>
                    <p>$$\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c} = \\frac{ad}{bc}$$</p>
                </div>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Suma de Fracciones',
                    'problem': 'Calcular: $\\frac{2}{3} + \\frac{1}{4}$',
                    'solution': '''
                    <p><strong>Paso 1:</strong> Encontrar denominador común</p>
                    <p>MCM(3, 4) = 12</p>
                    
                    <p><strong>Paso 2:</strong> Convertir fracciones</p>
                    <p>$\\frac{2}{3} = \\frac{8}{12}$ y $\\frac{1}{4} = \\frac{3}{12}$</p>
                    
                    <p><strong>Paso 3:</strong> Sumar numeradores</p>
                    <p>$\\frac{8}{12} + \\frac{3}{12} = \\frac{11}{12}$</p>
                    '''
                }
            ]
        },
        {
            'id': 'mcm_mcd',
            'title': 'MCM y MCD',
            'content': '''
            <h4>Máximo Común Divisor y Mínimo Común Múltiplo</h4>
            
            <div class="row">
                <div class="col-md-6">
                    <h5>MCD (Máximo Común Divisor)</h5>
                    <p>El mayor número que divide exactamente a dos o más números.</p>
                    <p><strong>Método:</strong> Factorización prima y tomar factores comunes con menor exponente.</p>
                </div>
                <div class="col-md-6">
                    <h5>MCM (Mínimo Común Múltiplo)</h5>
                    <p>El menor número que es múltiplo de dos o más números.</p>
                    <p><strong>Método:</strong> Factorización prima y tomar todos los factores con mayor exponente.</p>
                </div>
            </div>
            
            <div class="alert alert-success mt-3">
                <strong>Relación importante:</strong> $MCD(a,b) \\times MCM(a,b) = a \\times b$
            </div>
            ''',
            'examples': [
                {
                    'title': 'Calcular MCD y MCM',
                    'problem': 'Encontrar MCD(12, 18) y MCM(12, 18)',
                    'solution': '''
                    <p><strong>Factorización prima:</strong></p>
                    <p>12 = 2² × 3</p>
                    <p>18 = 2 × 3²</p>
                    
                    <p><strong>MCD:</strong> Factores comunes con menor exponente</p>
                    <p>MCD(12, 18) = 2¹ × 3¹ = 6</p>
                    
                    <p><strong>MCM:</strong> Todos los factores con mayor exponente</p>
                    <p>MCM(12, 18) = 2² × 3² = 36</p>
                    
                    <p><strong>Verificación:</strong> 6 × 36 = 216 = 12 × 18 ✓</p>
                    '''
                }
            ]
        }
    ]
}

def get_theory_content():
    """Retorna el contenido teórico completo"""
    return ARITHMETIC_CONTENT

def get_section_content(section_id):
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
        <h6>Recordatorio: Suma de Fracciones</h6>
        <p>Para sumar fracciones con diferentes denominadores:</p>
        <ol>
            <li>Encuentra el denominador común (MCM)</li>
            <li>Convierte ambas fracciones al mismo denominador</li>
            <li>Suma solo los numeradores</li>
            <li>Simplifica si es posible</li>
        </ol>
        ''',
        'order_operations': '''
        <h6>Recordatorio: Orden de Operaciones</h6>
        <p>Recuerda la jerarquía PEMDAS:</p>
        <ol>
            <li><strong>P</strong>aréntesis</li>
            <li><strong>E</strong>xponentes</li>
            <li><strong>M</strong>ultiplicación y <strong>D</strong>ivisión (izq. a der.)</li>
            <li><strong>A</strong>dición y <strong>S</strong>ustracción (izq. a der.)</li>
        </ol>
        ''',
        'factorization': '''
        <h6>Recordatorio: Factorización</h6>
        <p>Para factorizar un número:</p>
        <ol>
            <li>Divide por números primos empezando por 2</li>
            <li>Continúa hasta que el cociente sea 1</li>
            <li>Expresa como producto de potencias de primos</li>
        </ol>
        '''
    }
    
    return explanations.get(error_type, '<p>Revisa la teoría correspondiente para entender mejor este concepto.</p>')
