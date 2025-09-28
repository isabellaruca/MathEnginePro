"""
Contenido teórico para el módulo de Álgebra
Este archivo contiene toda la teoría, ejemplos y explicaciones del tema
"""

ALGEBRA_CONTENT = {
    'title': 'Álgebra',
    'description': 'Fundamentos del álgebra: monomios, polinomios y operaciones algebraicas',
    'sections': [
        {
            'id': 'monomios',
            'title': 'Monomios',
            'content': '''
            <h4>¿Qué es un Monomio?</h4>
            <div class="definition-box">
                <p>Un <strong>monomio</strong> es una expresión algebraica que consta de un solo término formado por:</p>
                <ul>
                    <li><strong>Coeficiente:</strong> número que multiplica a las variables</li>
                    <li><strong>Parte literal:</strong> variables con sus exponentes</li>
                </ul>
                <div class="math-display">$$ax^m y^n z^p$$</div>
                <p>donde $a$ es el coeficiente y $x^m y^n z^p$ es la parte literal.</p>
            </div>
            
            <h5>Grado de un Monomio</h5>
            <p>El <strong>grado</strong> de un monomio es la suma de todos los exponentes de sus variables.</p>
            
            <div class="example-box">
                <h6>Ejemplos:</h6>
                <ul>
                    <li>$5x^3$ → Grado: 3</li>
                    <li>$-2x^2y^4$ → Grado: 2 + 4 = 6</li>
                    <li>$7xyz^2$ → Grado: 1 + 1 + 2 = 4</li>
                    <li>$-8$ → Grado: 0 (monomio constante)</li>
                </ul>
            </div>
            
            <h5>Monomios Semejantes</h5>
            <p>Dos monomios son <strong>semejantes</strong> si tienen la misma parte literal (mismas variables con los mismos exponentes).</p>
            
            <div class="example-box">
                <h6>Ejemplos de monomios semejantes:</h6>
                <ul>
                    <li>$3x^2y$ y $-7x^2y$ → Semejantes</li>
                    <li>$5ab^3$ y $\frac{1}{2}ab^3$ → Semejantes</li>
                    <li>$2x^2$ y $3x^3$ → NO semejantes (diferentes exponentes)</li>
                </ul>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Identificar Monomios Semejantes',
                    'problem': 'Identifica cuáles de los siguientes monomios son semejantes: $3x^2y$, $-5x^2y$, $2xy^2$, $7x^2y$',
                    'solution': '''
                    <p><strong>Análisis de cada monomio:</strong></p>
                    <ul>
                        <li>$3x^2y$ → Parte literal: $x^2y$</li>
                        <li>$-5x^2y$ → Parte literal: $x^2y$</li>
                        <li>$2xy^2$ → Parte literal: $xy^2$</li>
                        <li>$7x^2y$ → Parte literal: $x^2y$</li>
                    </ul>
                    <p><strong>Respuesta:</strong> Los monomios $3x^2y$, $-5x^2y$ y $7x^2y$ son semejantes porque tienen la misma parte literal $x^2y$.</p>
                    <p>El monomio $2xy^2$ NO es semejante a los otros porque su parte literal es $xy^2$.</p>
                    '''
                }
            ]
        },
        {
            'id': 'operaciones_monomios',
            'title': 'Operaciones con Monomios',
            'content': '''
            <h4>Suma y Resta de Monomios</h4>
            <div class="definition-box">
                <p>Solo se pueden sumar o restar monomios <strong>semejantes</strong>.</p>
                <p>Se suman o restan los coeficientes y se conserva la parte literal.</p>
                <div class="math-display">$$ax^m + bx^m = (a + b)x^m$$</div>
            </div>
            
            <div class="example-box">
                <h6>Ejemplos:</h6>
                <ul>
                    <li>$5x^2 + 3x^2 = 8x^2$</li>
                    <li>$7xy - 2xy = 5xy$</li>
                    <li>$-3a^2b + 8a^2b = 5a^2b$</li>
                </ul>
            </div>
            
            <h4>Multiplicación de Monomios</h4>
            <div class="definition-box">
                <p>Para multiplicar monomios:</p>
                <ol>
                    <li>Se multiplican los coeficientes</li>
                    <li>Se multiplican las partes literales (sumando exponentes de la misma base)</li>
                </ol>
                <div class="math-display">$$ax^m \cdot bx^n = (a \cdot b)x^{m+n}$$</div>
            </div>
            
            <div class="example-box">
                <h6>Ejemplos:</h6>
                <ul>
                    <li>$3x^2 \cdot 4x^3 = 12x^5$</li>
                    <li>$-2xy \cdot 5x^2y^3 = -10x^3y^4$</li>
                    <li>$6a^2b \cdot (-3ab^2) = -18a^3b^3$</li>
                </ul>
            </div>
            
            <h4>División de Monomios</h4>
            <div class="definition-box">
                <p>Para dividir monomios:</p>
                <ol>
                    <li>Se dividen los coeficientes</li>
                    <li>Se dividen las partes literales (restando exponentes de la misma base)</li>
                </ol>
                <div class="math-display">$$\frac{ax^m}{bx^n} = \frac{a}{b}x^{m-n}$$ (donde $b \neq 0$ y $m \geq n$)</div>
            </div>
            
            <div class="example-box">
                <h6>Ejemplos:</h6>
                <ul>
                    <li>$\frac{12x^5}{3x^2} = 4x^3$</li>
                    <li>$\frac{-15x^3y^4}{5xy^2} = -3x^2y^2$</li>
                    <li>$\frac{8a^4b^2}{-2a^2b} = -4a^2b$</li>
                </ul>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Operaciones Combinadas con Monomios',
                    'problem': 'Simplifica: $(3x^2y) \cdot (-2xy^3) + (6x^3y^4) \div (2xy)$',
                    'solution': '''
                    <p><strong>Paso 1:</strong> Resolver la multiplicación</p>
                    <p>$(3x^2y) \cdot (-2xy^3) = -6x^3y^4$</p>
                    
                    <p><strong>Paso 2:</strong> Resolver la división</p>
                    <p>$\frac{6x^3y^4}{2xy} = 3x^2y^3$</p>
                    
                    <p><strong>Paso 3:</strong> Sumar los resultados</p>
                    <p>$-6x^3y^4 + 3x^2y^3$</p>
                    
                    <p><strong>Resultado:</strong> Como los monomios no son semejantes, no se pueden sumar más.</p>
                    <p>Respuesta final: $-6x^3y^4 + 3x^2y^3$</p>
                    '''
                }
            ]
        },
        {
            'id': 'polinomios',
            'title': 'Polinomios',
            'content': '''
            <h4>¿Qué es un Polinomio?</h4>
            <div class="definition-box">
                <p>Un <strong>polinomio</strong> es una expresión algebraica formada por la suma de varios monomios.</p>
                <div class="math-display">$$P(x) = a_nx^n + a_{n-1}x^{n-1} + ... + a_1x + a_0$$</div>
                <p>donde $a_n, a_{n-1}, ..., a_1, a_0$ son los coeficientes y $n$ es el grado del polinomio.</p>
            </div>
            
            <h5>Clasificación por Número de Términos</h5>
            <div class="row">
                <div class="col-md-6">
                    <ul>
                        <li><strong>Monomio:</strong> 1 término → $3x^2$</li>
                        <li><strong>Binomio:</strong> 2 términos → $2x + 5$</li>
                        <li><strong>Trinomio:</strong> 3 términos → $x^2 + 3x - 2$</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <ul>
                        <li><strong>Cuatrinomio:</strong> 4 términos</li>
                        <li><strong>Polinomio:</strong> más de 4 términos</li>
                    </ul>
                </div>
            </div>
            
            <h5>Clasificación por Grado</h5>
            <div class="example-box">
                <ul>
                    <li><strong>Grado 0:</strong> Constante → $5$</li>
                    <li><strong>Grado 1:</strong> Lineal → $2x + 3$</li>
                    <li><strong>Grado 2:</strong> Cuadrático → $x^2 + 4x - 1$</li>
                    <li><strong>Grado 3:</strong> Cúbico → $2x^3 - x^2 + 5x + 2$</li>
                    <li><strong>Grado 4:</strong> Cuártico → $x^4 + 3x^2 - 7$</li>
                </ul>
            </div>
            
            <h5>Términos de un Polinomio</h5>
            <p>En un polinomio ordenado de mayor a menor grado:</p>
            <ul>
                <li><strong>Término principal:</strong> el de mayor grado</li>
                <li><strong>Término independiente:</strong> el que no tiene variable (grado 0)</li>
                <li><strong>Coeficiente principal:</strong> coeficiente del término de mayor grado</li>
            </ul>
            
            <div class="example-box">
                <h6>Ejemplo: $P(x) = 3x^4 - 2x^3 + 5x - 7$</h6>
                <ul>
                    <li>Grado: 4</li>
                    <li>Término principal: $3x^4$</li>
                    <li>Coeficiente principal: 3</li>
                    <li>Término independiente: -7</li>
                </ul>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Identificar Características de Polinomios',
                    'problem': 'Para el polinomio $P(x) = -2x^5 + 4x^3 - x^2 + 8x - 3$, identifica: grado, término principal, coeficiente principal, término independiente y clasifícalo.',
                    'solution': '''
                    <p><strong>Análisis del polinomio:</strong> $P(x) = -2x^5 + 4x^3 - x^2 + 8x - 3$</p>
                    
                    <ul>
                        <li><strong>Grado:</strong> 5 (mayor exponente)</li>
                        <li><strong>Término principal:</strong> $-2x^5$</li>
                        <li><strong>Coeficiente principal:</strong> -2</li>
                        <li><strong>Término independiente:</strong> -3</li>
                        <li><strong>Clasificación por términos:</strong> Polinomio (5 términos)</li>
                        <li><strong>Clasificación por grado:</strong> Quíntico (grado 5)</li>
                    </ul>
                    '''
                }
            ]
        },
        {
            'id': 'operaciones_polinomios',
            'title': 'Operaciones con Polinomios',
            'content': '''
            <h4>Suma y Resta de Polinomios</h4>
            <div class="definition-box">
                <p>Para sumar o restar polinomios:</p>
                <ol>
                    <li>Se agrupan los términos semejantes</li>
                    <li>Se suman o restan los coeficientes de términos semejantes</li>
                    <li>Se conserva la parte literal</li>
                </ol>
            </div>
            
            <div class="example-box">
                <h6>Ejemplo:</h6>
                <p>$(3x^2 + 2x - 5) + (x^2 - 4x + 7)$</p>
                <p>$= 3x^2 + x^2 + 2x - 4x - 5 + 7$</p>
                <p>$= 4x^2 - 2x + 2$</p>
            </div>
            
            <h4>Multiplicación de Polinomios</h4>
            <div class="definition-box">
                <p>Para multiplicar polinomios se aplica la <strong>propiedad distributiva</strong>:</p>
                <p>Cada término del primer polinomio se multiplica por cada término del segundo.</p>
            </div>
            
            <div class="example-box">
                <h6>Ejemplo:</h6>
                <p>$(2x + 3)(x - 1)$</p>
                <p>$= 2x \cdot x + 2x \cdot (-1) + 3 \cdot x + 3 \cdot (-1)$</p>
                <p>$= 2x^2 - 2x + 3x - 3$</p>
                <p>$= 2x^2 + x - 3$</p>
            </div>
            
            <h4>División de Polinomios</h4>
            <div class="definition-box">
                <p>La división de polinomios sigue el algoritmo:</p>
                <div class="math-display">$$\text{Dividendo} = \text{Divisor} \times \text{Cociente} + \text{Resto}$$</div>
                <p>Se puede realizar por <strong>división larga</strong> o <strong>regla de Ruffini</strong> (para divisores de la forma $x - a$).</p>
            </div>
            
            <h5>Regla de Ruffini</h5>
            <p>Se usa para dividir un polinomio por $(x - a)$:</p>
            <div class="example-box">
                <h6>Ejemplo: Dividir $x^3 - 2x^2 + x - 2$ entre $(x - 2)$</h6>
                <p>Coeficientes: [1, -2, 1, -2], $a = 2$</p>
                <table class="table table-sm table-bordered">
                    <tr><td></td><td>1</td><td>-2</td><td>1</td><td>-2</td></tr>
                    <tr><td>2</td><td></td><td>2</td><td>0</td><td>2</td></tr>
                    <tr><td></td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
                </table>
                <p>Cociente: $x^2 + 1$, Resto: 0</p>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Multiplicación de Binomios',
                    'problem': 'Desarrolla: $(3x - 2)(2x + 5)$',
                    'solution': '''
                    <p><strong>Aplicando la propiedad distributiva:</strong></p>
                    <p>$(3x - 2)(2x + 5)$</p>
                    <p>$= 3x \cdot 2x + 3x \cdot 5 + (-2) \cdot 2x + (-2) \cdot 5$</p>
                    <p>$= 6x^2 + 15x - 4x - 10$</p>
                    <p>$= 6x^2 + 11x - 10$</p>
                    
                    <p><strong>Verificación usando FOIL:</strong></p>
                    <ul>
                        <li><strong>F</strong>irst: $3x \cdot 2x = 6x^2$</li>
                        <li><strong>O</strong>uter: $3x \cdot 5 = 15x$</li>
                        <li><strong>I</strong>nner: $(-2) \cdot 2x = -4x$</li>
                        <li><strong>L</strong>ast: $(-2) \cdot 5 = -10$</li>
                    </ul>
                    <p>Resultado: $6x^2 + 11x - 10$</p>
                    '''
                }
            ]
        },
        {
            'id': 'productos_notables',
            'title': 'Productos Notables',
            'content': '''
            <h4>Productos Notables Fundamentales</h4>
            <p>Los productos notables son multiplicaciones que aparecen frecuentemente y tienen fórmulas específicas.</p>
            
            <div class="row">
                <div class="col-md-6">
                    <h5>1. Cuadrado de una Suma</h5>
                    <div class="math-display">$$(a + b)^2 = a^2 + 2ab + b^2$$</div>
                    <div class="example-box">
                        <p><strong>Ejemplo:</strong></p>
                        <p>$(x + 3)^2 = x^2 + 6x + 9$</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <h5>2. Cuadrado de una Diferencia</h5>
                    <div class="math-display">$$(a - b)^2 = a^2 - 2ab + b^2$$</div>
                    <div class="example-box">
                        <p><strong>Ejemplo:</strong></p>
                        <p>$(2x - 5)^2 = 4x^2 - 20x + 25$</p>
                    </div>
                </div>
            </div>
            
            <div class="row mt-4">
                <div class="col-md-6">
                    <h5>3. Diferencia de Cuadrados</h5>
                    <div class="math-display">$$(a + b)(a - b) = a^2 - b^2$$</div>
                    <div class="example-box">
                        <p><strong>Ejemplo:</strong></p>
                        <p>$(x + 4)(x - 4) = x^2 - 16$</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <h5>4. Cubo de una Suma</h5>
                    <div class="math-display">$$(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$</div>
                    <div class="example-box">
                        <p><strong>Ejemplo:</strong></p>
                        <p>$(x + 2)^3 = x^3 + 6x^2 + 12x + 8$</p>
                    </div>
                </div>
            </div>
            
            <div class="row mt-4">
                <div class="col-md-6">
                    <h5>5. Cubo de una Diferencia</h5>
                    <div class="math-display">$$(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$</div>
                    <div class="example-box">
                        <p><strong>Ejemplo:</strong></p>
                        <p>$(x - 1)^3 = x^3 - 3x^2 + 3x - 1$</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <h5>6. Suma y Diferencia de Cubos</h5>
                    <div class="math-display">$$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$</div>
                    <div class="math-display">$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$</div>
                </div>
            </div>
            
            <div class="alert alert-info mt-4">
                <h6><i class="fas fa-lightbulb me-2"></i>Estrategia para Recordar</h6>
                <p>Para $(a \pm b)^2$: "El cuadrado del primero, más/menos el doble del primero por el segundo, más el cuadrado del segundo"</p>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Aplicación de Productos Notables',
                    'problem': 'Desarrolla usando productos notables: $(2x + 3y)^2 - (2x - 3y)^2$',
                    'solution': '''
                    <p><strong>Paso 1:</strong> Aplicar cuadrado de suma y diferencia</p>
                    <p>$(2x + 3y)^2 = (2x)^2 + 2(2x)(3y) + (3y)^2 = 4x^2 + 12xy + 9y^2$</p>
                    <p>$(2x - 3y)^2 = (2x)^2 - 2(2x)(3y) + (3y)^2 = 4x^2 - 12xy + 9y^2$</p>
                    
                    <p><strong>Paso 2:</strong> Restar las expresiones</p>
                    <p>$(4x^2 + 12xy + 9y^2) - (4x^2 - 12xy + 9y^2)$</p>
                    <p>$= 4x^2 + 12xy + 9y^2 - 4x^2 + 12xy - 9y^2$</p>
                    <p>$= 24xy$</p>
                    
                    <p><strong>Método alternativo:</strong> Reconocer como diferencia de cuadrados</p>
                    <p>$(2x + 3y)^2 - (2x - 3y)^2 = [(2x + 3y) + (2x - 3y)][(2x + 3y) - (2x - 3y)]$</p>
                    <p>$= [4x][6y] = 24xy$</p>
                    '''
                }
            ]
        },
        {
            'id': 'factorizacion',
            'title': 'Factorización',
            'content': '''
            <h4>¿Qué es la Factorización?</h4>
            <div class="definition-box">
                <p>La <strong>factorización</strong> es el proceso inverso a la multiplicación. Consiste en expresar un polinomio como el producto de factores más simples.</p>
                <div class="math-display">$$\text{Polinomio} = \text{Factor}_1 \times \text{Factor}_2 \times ... \times \text{Factor}_n$$</div>
            </div>
            
            <h5>Métodos de Factorización</h5>
            
            <h6>1. Factor Común</h6>
            <p>Se extrae el factor común de todos los términos.</p>
            <div class="example-box">
                <p><strong>Ejemplo:</strong> $6x^3 + 9x^2 - 3x = 3x(2x^2 + 3x - 1)$</p>
            </div>
            
            <h6>2. Agrupación</h6>
            <p>Se agrupan términos para encontrar factores comunes.</p>
            <div class="example-box">
                <p><strong>Ejemplo:</strong> $ax + ay + bx + by = a(x + y) + b(x + y) = (a + b)(x + y)$</p>
            </div>
            
            <h6>3. Trinomio Cuadrado Perfecto</h6>
            <p>Se reconoce la forma $a^2 \pm 2ab + b^2 = (a \pm b)^2$</p>
            <div class="example-box">
                <p><strong>Ejemplo:</strong> $x^2 + 6x + 9 = (x + 3)^2$</p>
            </div>
            
            <h6>4. Diferencia de Cuadrados</h6>
            <p>Se aplica $a^2 - b^2 = (a + b)(a - b)$</p>
            <div class="example-box">
                <p><strong>Ejemplo:</strong> $25x^2 - 16 = (5x + 4)(5x - 4)$</p>
            </div>
            
            <h6>5. Trinomio de la Forma $x^2 + bx + c$</h6>
            <p>Se buscan dos números que sumados den $b$ y multiplicados den $c$.</p>
            <div class="example-box">
                <p><strong>Ejemplo:</strong> $x^2 + 5x + 6 = (x + 2)(x + 3)$</p>
                <p>Porque $2 + 3 = 5$ y $2 \times 3 = 6$</p>
            </div>
            
            <h6>6. Trinomio de la Forma $ax^2 + bx + c$ (a ≠ 1)</h6>
            <p>Se puede usar el método de factorización por agrupación o fórmula cuadrática.</p>
            <div class="example-box">
                <p><strong>Ejemplo:</strong> $2x^2 + 7x + 3 = (2x + 1)(x + 3)$</p>
            </div>
            
            <div class="alert alert-warning mt-4">
                <h6><i class="fas fa-exclamation-triangle me-2"></i>Estrategia General</h6>
                <ol>
                    <li>Buscar factor común primero</li>
                    <li>Contar términos y reconocer patrones</li>
                    <li>Aplicar el método apropiado</li>
                    <li>Verificar multiplicando los factores</li>
                </ol>
            </div>
            ''',
            'examples': [
                {
                    'title': 'Factorización Completa',
                    'problem': 'Factoriza completamente: $12x^3 - 27x$',
                    'solution': '''
                    <p><strong>Paso 1:</strong> Buscar factor común</p>
                    <p>$12x^3 - 27x = 3x(4x^2 - 9)$</p>
                    
                    <p><strong>Paso 2:</strong> Reconocer diferencia de cuadrados en el paréntesis</p>
                    <p>$4x^2 - 9 = (2x)^2 - 3^2 = (2x + 3)(2x - 3)$</p>
                    
                    <p><strong>Paso 3:</strong> Escribir la factorización completa</p>
                    <p>$12x^3 - 27x = 3x(2x + 3)(2x - 3)$</p>
                    
                    <p><strong>Verificación:</strong></p>
                    <p>$3x(2x + 3)(2x - 3) = 3x(4x^2 - 9) = 12x^3 - 27x$ ✓</p>
                    '''
                }
            ]
        }
    ]
}

def get_theory_content():
    """Retorna el contenido teórico completo"""
    return ALGEBRA_CONTENT

def get_section_content(section_id):
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
        <h6>Recordatorio: Operaciones con Monomios</h6>
        <p>Para multiplicar monomios:</p>
        <ol>
            <li>Multiplica los coeficientes</li>
            <li>Suma los exponentes de la misma base</li>
        </ol>
        <p>Para dividir monomios:</p>
        <ol>
            <li>Divide los coeficientes</li>
            <li>Resta los exponentes de la misma base</li>
        </ol>
        ''',
        'polynomial_operations': '''
        <h6>Recordatorio: Operaciones con Polinomios</h6>
        <p>Para sumar/restar polinomios:</p>
        <ol>
            <li>Agrupa términos semejantes</li>
            <li>Suma/resta los coeficientes</li>
        </ol>
        <p>Para multiplicar polinomios:</p>
        <ol>
            <li>Aplica la propiedad distributiva</li>
            <li>Multiplica cada término del primer polinomio por cada término del segundo</li>
        </ol>
        ''',
        'notable_products': '''
        <h6>Recordatorio: Productos Notables</h6>
        <p>Fórmulas principales:</p>
        <ul>
            <li>$(a + b)^2 = a^2 + 2ab + b^2$</li>
            <li>$(a - b)^2 = a^2 - 2ab + b^2$</li>
            <li>$(a + b)(a - b) = a^2 - b^2$</li>
        </ul>
        ''',
        'factorization': '''
        <h6>Recordatorio: Factorización</h6>
        <p>Pasos para factorizar:</p>
        <ol>
            <li>Busca factor común primero</li>
            <li>Identifica el tipo de expresión</li>
            <li>Aplica el método apropiado</li>
            <li>Verifica multiplicando</li>
        </ol>
        '''
    }
    
    return explanations.get(error_type, '<p>Revisa la teoría correspondiente para entender mejor este concepto.</p>')
