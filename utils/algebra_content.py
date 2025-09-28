"""
Contenido teórico para el módulo de Álgebra
Migrado desde el proyecto Django original
"""

ALGEBRA_CONTENT = {
    'title': 'Álgebra',
    'description': 'Fundamentos del álgebra: monomios, polinomios y operaciones algebraicas',
    'sections': [
        {
            'id': 'monomios',
            'title': 'Monomios',
            'content': '''
            #### ¿Qué es un Monomio?
            Un **monomio** es una expresión algebraica que consta de un solo término formado por:
            - **Coeficiente:** número que multiplica a las variables
            - **Parte literal:** variables con sus exponentes
            
            $$ax^m y^n z^p$$
            
            donde $a$ es el coeficiente y $x^m y^n z^p$ es la parte literal.
            
            #### Grado de un Monomio
            El **grado** de un monomio es la suma de todos los exponentes de sus variables.
            
            **Ejemplos:**
            - $5x^3$ → Grado: 3
            - $-2x^2y^4$ → Grado: 2 + 4 = 6
            - $7xyz^2$ → Grado: 1 + 1 + 2 = 4
            - $-8$ → Grado: 0 (monomio constante)
            
            #### Monomios Semejantes
            Dos monomios son **semejantes** si tienen la misma parte literal (mismas variables con los mismos exponentes).
            
            **Ejemplos de monomios semejantes:**
            - $3x^2y$ y $-7x^2y$ → Semejantes
            - $5ab^3$ y $\\frac{1}{2}ab^3$ → Semejantes
            - $2x^2$ y $3x^3$ → NO semejantes (diferentes exponentes)
            ''',
            'examples': [
                {
                    'title': 'Identificar Monomios Semejantes',
                    'problem': 'Identifica cuáles de los siguientes monomios son semejantes: $3x^2y$, $-5x^2y$, $2xy^2$, $7x^2y$',
                    'solution': '''
                    **Análisis de cada monomio:**
                    - $3x^2y$ → Parte literal: $x^2y$
                    - $-5x^2y$ → Parte literal: $x^2y$
                    - $2xy^2$ → Parte literal: $xy^2$
                    - $7x^2y$ → Parte literal: $x^2y$
                    
                    **Respuesta:** Los monomios $3x^2y$, $-5x^2y$ y $7x^2y$ son semejantes porque tienen la misma parte literal $x^2y$.
                    
                    El monomio $2xy^2$ NO es semejante a los otros porque su parte literal es $xy^2$.
                    '''
                }
            ]
        },
        {
            'id': 'operaciones_monomios',
            'title': 'Operaciones con Monomios',
            'content': '''
            #### Suma y Resta de Monomios
            Solo se pueden sumar o restar monomios **semejantes**.
            Se suman o restan los coeficientes y se conserva la parte literal.
            
            $$ax^m + bx^m = (a + b)x^m$$
            
            **Ejemplos:**
            - $5x^2 + 3x^2 = 8x^2$
            - $7xy - 2xy = 5xy$
            - $-3a^2b + 8a^2b = 5a^2b$
            
            #### Multiplicación de Monomios
            Para multiplicar monomios:
            1. Se multiplican los coeficientes
            2. Se multiplican las partes literales (sumando exponentes de la misma base)
            
            $$ax^m \\cdot bx^n = (a \\cdot b)x^{m+n}$$
            
            **Ejemplos:**
            - $3x^2 \\cdot 4x^3 = 12x^5$
            - $-2xy \\cdot 5x^2y^3 = -10x^3y^4$
            - $6a^2b \\cdot (-3ab^2) = -18a^3b^3$
            
            #### División de Monomios
            Para dividir monomios:
            1. Se dividen los coeficientes
            2. Se dividen las partes literales (restando exponentes de la misma base)
            
            $$\\frac{ax^m}{bx^n} = \\frac{a}{b}x^{m-n}$$ (donde $b \\neq 0$ y $m \\geq n$)
            
            **Ejemplos:**
            - $\\frac{12x^5}{3x^2} = 4x^3$
            - $\\frac{-15x^3y^4}{5xy^2} = -3x^2y^2$
            - $\\frac{8a^4b^2}{-2a^2b} = -4a^2b$
            ''',
            'examples': [
                {
                    'title': 'Operaciones Combinadas con Monomios',
                    'problem': 'Simplifica: $(3x^2y) \\cdot (-2xy^3) + (6x^3y^4) \\div (2xy)$',
                    'solution': '''
                    **Paso 1:** Resolver la multiplicación
                    $(3x^2y) \\cdot (-2xy^3) = -6x^3y^4$
                    
                    **Paso 2:** Resolver la división
                    $\\frac{6x^3y^4}{2xy} = 3x^2y^3$
                    
                    **Paso 3:** Sumar los resultados
                    $-6x^3y^4 + 3x^2y^3$
                    
                    **Resultado:** Como los monomios no son semejantes, no se pueden sumar más.
                    Respuesta final: $-6x^3y^4 + 3x^2y^3$
                    '''
                }
            ]
        },
        {
            'id': 'polinomios',
            'title': 'Polinomios',
            'content': '''
            #### ¿Qué es un Polinomio?
            Un **polinomio** es una expresión algebraica formada por la suma de varios monomios.
            
            $$P(x) = a_nx^n + a_{n-1}x^{n-1} + ... + a_1x + a_0$$
            
            donde $a_n, a_{n-1}, ..., a_1, a_0$ son los coeficientes y $n$ es el grado del polinomio.
            
            #### Clasificación por Número de Términos
            - **Monomio:** 1 término → $3x^2$
            - **Binomio:** 2 términos → $2x + 5$
            - **Trinomio:** 3 términos → $x^2 + 3x - 2$
            - **Cuatrinomio:** 4 términos
            - **Polinomio:** más de 4 términos
            
            #### Clasificación por Grado
            - **Grado 0:** Constante → $5$
            - **Grado 1:** Lineal → $2x + 3$
            - **Grado 2:** Cuadrático → $x^2 + 4x - 1$
            - **Grado 3:** Cúbico → $2x^3 - x^2 + 5x + 2$
            - **Grado 4:** Cuártico → $x^4 + 3x^2 - 7$
            
            #### Términos de un Polinomio
            En un polinomio ordenado de mayor a menor grado:
            - **Término principal:** el de mayor grado
            - **Término independiente:** el que no tiene variable (grado 0)
            - **Coeficiente principal:** coeficiente del término de mayor grado
            
            **Ejemplo:** $P(x) = 3x^4 - 2x^3 + 5x - 7$
            - Grado: 4
            - Término principal: $3x^4$
            - Coeficiente principal: 3
            - Término independiente: -7
            ''',
            'examples': [
                {
                    'title': 'Identificar Características de Polinomios',
                    'problem': 'Para el polinomio $P(x) = -2x^5 + 4x^3 - x^2 + 8x - 3$, identifica: grado, término principal, coeficiente principal, término independiente y clasifícalo.',
                    'solution': '''
                    **Análisis del polinomio:** $P(x) = -2x^5 + 4x^3 - x^2 + 8x - 3$
                    
                    - **Grado:** 5 (mayor exponente)
                    - **Término principal:** $-2x^5$
                    - **Coeficiente principal:** -2
                    - **Término independiente:** -3
                    - **Clasificación por términos:** Polinomio (5 términos)
                    - **Clasificación por grado:** Quíntico (grado 5)
                    '''
                }
            ]
        },
        {
            'id': 'productos_notables',
            'title': 'Productos Notables',
            'content': '''
            #### Productos Notables Fundamentales
            Los productos notables son multiplicaciones que aparecen frecuentemente y tienen fórmulas específicas.
            
            #### 1. Cuadrado de una Suma
            $$(a + b)^2 = a^2 + 2ab + b^2$$
            
            **Ejemplo:** $(x + 3)^2 = x^2 + 6x + 9$
            
            #### 2. Cuadrado de una Diferencia
            $$(a - b)^2 = a^2 - 2ab + b^2$$
            
            **Ejemplo:** $(2x - 5)^2 = 4x^2 - 20x + 25$
            
            #### 3. Diferencia de Cuadrados
            $$(a + b)(a - b) = a^2 - b^2$$
            
            **Ejemplo:** $(x + 4)(x - 4) = x^2 - 16$
            
            #### 4. Cubo de una Suma
            $$(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$
            
            **Ejemplo:** $(x + 2)^3 = x^3 + 6x^2 + 12x + 8$
            
            #### 5. Cubo de una Diferencia
            $$(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$
            
            **Ejemplo:** $(x - 1)^3 = x^3 - 3x^2 + 3x - 1$
            
            #### 6. Suma y Diferencia de Cubos
            $$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$
            $$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$
            
            **Estrategia para Recordar**
            Para $(a \\pm b)^2$: "El cuadrado del primero, más/menos el doble del primero por el segundo, más el cuadrado del segundo"
            ''',
            'examples': [
                {
                    'title': 'Aplicación de Productos Notables',
                    'problem': 'Desarrolla usando productos notables: $(2x + 3y)^2 - (2x - 3y)^2$',
                    'solution': '''
                    **Paso 1:** Aplicar cuadrado de suma y diferencia
                    $(2x + 3y)^2 = (2x)^2 + 2(2x)(3y) + (3y)^2 = 4x^2 + 12xy + 9y^2$
                    $(2x - 3y)^2 = (2x)^2 - 2(2x)(3y) + (3y)^2 = 4x^2 - 12xy + 9y^2$
                    
                    **Paso 2:** Restar las expresiones
                    $(4x^2 + 12xy + 9y^2) - (4x^2 - 12xy + 9y^2)$
                    $= 4x^2 + 12xy + 9y^2 - 4x^2 + 12xy - 9y^2$
                    $= 24xy$
                    
                    **Método alternativo:** Reconocer como diferencia de cuadrados
                    $(2x + 3y)^2 - (2x - 3y)^2 = [(2x + 3y) + (2x - 3y)][(2x + 3y) - (2x - 3y)]$
                    $= [4x][6y] = 24xy$
                    '''
                }
            ]
        },
        {
            'id': 'factorizacion',
            'title': 'Factorización',
            'content': '''
            #### ¿Qué es la Factorización?
            La **factorización** es el proceso inverso a la multiplicación. Consiste en expresar un polinomio como el producto de factores más simples.
            
            $$\\text{Polinomio} = \\text{Factor}_1 \\times \\text{Factor}_2 \\times ... \\times \\text{Factor}_n$$
            
            #### Métodos de Factorización
            
            **1. Factor Común**
            Se extrae el factor común de todos los términos.
            **Ejemplo:** $6x^3 + 9x^2 - 3x = 3x(2x^2 + 3x - 1)$
            
            **2. Agrupación**
            Se agrupan términos para encontrar factores comunes.
            **Ejemplo:** $ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y)$
            
            **3. Trinomio Cuadrado Perfecto**
            Se reconoce la forma $a^2 \\pm 2ab + b^2 = (a \\pm b)^2$
            **Ejemplo:** $x^2 + 6x + 9 = (x + 3)^2$
            
            **4. Diferencia de Cuadrados**
            Se aplica $a^2 - b^2 = (a + b)(a - b)$
            **Ejemplo:** $25x^2 - 16 = (5x + 4)(5x - 4)$
            
            **5. Trinomio de la Forma $x^2 + bx + c$**
            Se buscan dos números que sumados den $b$ y multiplicados den $c$.
            **Ejemplo:** $x^2 + 5x + 6 = (x + 2)(x + 3)$
            Porque $2 + 3 = 5$ y $2 \\times 3 = 6$
            
            **6. Trinomio de la Forma $ax^2 + bx + c$ (a ≠ 1)**
            Se puede usar el método de factorización por agrupación o fórmula cuadrática.
            **Ejemplo:** $2x^2 + 7x + 3 = (2x + 1)(x + 3)$
            
            #### Estrategia General
            1. Buscar factor común primero
            2. Contar términos y reconocer patrones
            3. Aplicar el método apropiado
            4. Verificar multiplicando los factores
            ''',
            'examples': [
                {
                    'title': 'Factorización Completa',
                    'problem': 'Factoriza completamente: $12x^3 - 27x$',
                    'solution': '''
                    **Paso 1:** Buscar factor común
                    $12x^3 - 27x = 3x(4x^2 - 9)$
                    
                    **Paso 2:** Reconocer diferencia de cuadrados en el paréntesis
                    $4x^2 - 9 = (2x)^2 - 3^2 = (2x + 3)(2x - 3)$
                    
                    **Paso 3:** Escribir la factorización completa
                    $12x^3 - 27x = 3x(2x + 3)(2x - 3)$
                    
                    **Verificación:**
                    $3x(2x + 3)(2x - 3) = 3x(4x^2 - 9) = 12x^3 - 27x$ ✓
                    '''
                }
            ]
        }
    ]
}

def get_algebra_content():
    """Retorna el contenido teórico completo"""
    return ALGEBRA_CONTENT

def get_algebra_section(section_id):
    """Retorna el contenido de una sección específica"""
    for section in ALGEBRA_CONTENT['sections']:
        if section['id'] == section_id:
            return section
    return None

def get_explanation_for_error(error_type):
    """
    Retorna explicación específica basada en el tipo de error cometido
    """
    explanations = {
        'monomial_operations': '''
        #### Recordatorio: Operaciones con Monomios
        Para multiplicar monomios:
        1. Multiplica los coeficientes
        2. Suma los exponentes de la misma base
        
        Para dividir monomios:
        1. Divide los coeficientes
        2. Resta los exponentes de la misma base
        ''',
        'polynomial_operations': '''
        #### Recordatorio: Operaciones con Polinomios
        Para sumar/restar polinomios:
        1. Agrupa términos semejantes
        2. Suma/resta los coeficientes
        
        Para multiplicar polinomios:
        1. Aplica la propiedad distributiva
        2. Multiplica cada término del primer polinomio por cada término del segundo
        ''',
        'notable_products': '''
        #### Recordatorio: Productos Notables
        Fórmulas principales:
        - $(a + b)^2 = a^2 + 2ab + b^2$
        - $(a - b)^2 = a^2 - 2ab + b^2$
        - $(a + b)(a - b) = a^2 - b^2$
        ''',
        'factorization': '''
        #### Recordatorio: Factorización
        Pasos para factorizar:
        1. Busca factor común primero
        2. Identifica el tipo de expresión
        3. Aplica el método apropiado
        4. Verifica multiplicando
        '''
    }
    
    return explanations.get(error_type, 'Revisa la teoría correspondiente para entender mejor este concepto.')
