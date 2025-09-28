"""
Generadores de ejercicios para aritmética y álgebra
Migrado y adaptado desde el proyecto Django original
"""

import random
import sympy as sp
from sympy import gcd, lcm, factorint, latex, symbols, expand, factor
from fractions import Fraction

class ArithmeticExerciseGenerator:
    """Clase principal para generar ejercicios de aritmética"""
    
    def __init__(self):
        self.difficulty_levels = ['easy', 'medium', 'hard']
    
    def generate_random_exercise(self, topic=None, difficulty='medium'):
        """
        Genera un ejercicio aleatorio del tema especificado
        """
        topics = [
            'fraction_operations',
            'combined_operations', 
            'mcm_mcd',
            'factorization',
            'word_problems'
        ]
        
        if topic is None:
            topic = random.choice(topics)
        
        generators = {
            'fraction_operations': self.generate_fraction_exercise,
            'combined_operations': self.generate_combined_operations,
            'mcm_mcd': self.generate_mcm_mcd_exercise,
            'factorization': self.generate_factorization_exercise,
            'word_problems': self.generate_word_problem
        }
        
        return generators[topic](difficulty)
    
    def generate_fraction_exercise(self, difficulty='medium'):
        """
        Genera ejercicios de operaciones con fracciones
        """
        operations = ['+', '-', '*', '/']
        operation = random.choice(operations)
        
        if difficulty == 'easy':
            # Fracciones simples con denominadores pequeños
            num1, den1 = random.randint(1, 5), random.randint(2, 6)
            num2, den2 = random.randint(1, 5), random.randint(2, 6)
        elif difficulty == 'medium':
            # Fracciones con denominadores medianos
            num1, den1 = random.randint(1, 10), random.randint(2, 12)
            num2, den2 = random.randint(1, 10), random.randint(2, 12)
        else:  # hard
            # Fracciones más complejas
            num1, den1 = random.randint(1, 20), random.randint(2, 20)
            num2, den2 = random.randint(1, 20), random.randint(2, 20)
        
        # Crear fracciones usando SymPy para cálculos exactos
        frac1 = sp.Rational(num1, den1)
        frac2 = sp.Rational(num2, den2)
        
        # Calcular resultado según la operación
        if operation == '+':
            result = frac1 + frac2
            problem_text = f"Calcular: $\\frac{{{num1}}}{{{den1}}} + \\frac{{{num2}}}{{{den2}}}$"
        elif operation == '-':
            result = frac1 - frac2
            problem_text = f"Calcular: $\\frac{{{num1}}}{{{den1}}} - \\frac{{{num2}}}{{{den2}}}$"
        elif operation == '*':
            result = frac1 * frac2
            problem_text = f"Calcular: $\\frac{{{num1}}}{{{den1}}} \\times \\frac{{{num2}}}{{{den2}}}$"
        else:  # division
            result = frac1 / frac2
            problem_text = f"Calcular: $\\frac{{{num1}}}{{{den1}}} \\div \\frac{{{num2}}}{{{den2}}}$"
        
        return {
            'type': 'fraction_operations',
            'problem': problem_text,
            'answer': str(result),
            'answer_latex': latex(result),
            'solution_steps': self._generate_fraction_steps(frac1, frac2, operation),
            'error_type': 'fraction_addition' if operation in ['+', '-'] else 'fraction_multiplication'
        }
    
    def generate_combined_operations(self, difficulty='medium'):
        """
        Genera ejercicios de operaciones combinadas con jerarquía
        """
        if difficulty == 'easy':
            # Operaciones simples con paréntesis
            a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
            expression = f"{a} + {b} * {c}"
            problem_text = f"Resolver: ${a} + {b} \\times {c}$"
        elif difficulty == 'medium':
            # Incluir paréntesis y exponentes
            a, b, c, d = random.randint(1, 8), random.randint(1, 5), random.randint(2, 4), random.randint(1, 6)
            expression = f"{a} + {b} * ({c}**2 - {d})"
            problem_text = f"Resolver: ${a} + {b} \\times ({c}^2 - {d})$"
        else:  # hard
            # Operaciones más complejas
            a, b, c, d, e = random.randint(1, 6), random.randint(1, 4), random.randint(2, 3), random.randint(1, 5), random.randint(1, 4)
            expression = f"({a} + {b}) * {c}**2 - {d} * {e}"
            problem_text = f"Resolver: $({a} + {b}) \\times {c}^2 - {d} \\times {e}$"
        
        # Evaluar usando SymPy
        result = sp.sympify(expression)
        
        return {
            'type': 'combined_operations',
            'problem': problem_text,
            'answer': str(result),
            'answer_latex': latex(result),
            'solution_steps': self._generate_operation_steps(expression),
            'error_type': 'order_operations'
        }
    
    def generate_mcm_mcd_exercise(self, difficulty='medium'):
        """
        Genera ejercicios de MCM y MCD
        """
        if difficulty == 'easy':
            # Números pequeños
            a, b = random.randint(6, 20), random.randint(6, 20)
        elif difficulty == 'medium':
            # Números medianos
            a, b = random.randint(12, 50), random.randint(12, 50)
        else:  # hard
            # Números más grandes o tres números
            if random.choice([True, False]):
                a, b = random.randint(20, 100), random.randint(20, 100)
            else:
                # Tres números para mayor dificultad
                a, b, c = random.randint(12, 30), random.randint(12, 30), random.randint(12, 30)
                mcd_result = gcd(gcd(a, b), c)
                mcm_result = lcm(lcm(a, b), c)
                
                return {
                    'type': 'mcm_mcd',
                    'problem': f"Calcular MCD({a}, {b}, {c}) y MCM({a}, {b}, {c})",
                    'answer': f"MCD = {mcd_result}, MCM = {mcm_result}",
                    'answer_latex': f"MCD = {mcd_result}, MCM = {mcm_result}",
                    'solution_steps': self._generate_mcm_mcd_steps([a, b, c]),
                    'error_type': 'factorization'
                }
        
        # Caso de dos números
        mcd_result = gcd(a, b)
        mcm_result = lcm(a, b)
        
        return {
            'type': 'mcm_mcd',
            'problem': f"Calcular MCD({a}, {b}) y MCM({a}, {b})",
            'answer': f"MCD = {mcd_result}, MCM = {mcm_result}",
            'answer_latex': f"MCD = {mcd_result}, MCM = {mcm_result}",
            'solution_steps': self._generate_mcm_mcd_steps([a, b]),
            'error_type': 'factorization'
        }
    
    def generate_factorization_exercise(self, difficulty='medium'):
        """
        Genera ejercicios de factorización en números primos
        """
        if difficulty == 'easy':
            number = random.randint(12, 50)
        elif difficulty == 'medium':
            number = random.randint(50, 200)
        else:  # hard
            number = random.randint(200, 500)
        
        # Factorizar usando SymPy
        factors = factorint(number)
        
        # Crear representación en LaTeX
        factor_latex = " \\times ".join([f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in factors.items()])
        
        return {
            'type': 'factorization',
            'problem': f"Factorizar en números primos: {number}",
            'answer': factor_latex,
            'answer_latex': f"{number} = {factor_latex}",
            'solution_steps': self._generate_factorization_steps(number),
            'error_type': 'factorization'
        }
    
    def generate_word_problem(self, difficulty='medium'):
        """
        Genera problemas verbales contextualizados
        """
        problem_types = [
            'farmer_problem',
            'recipe_problem', 
            'money_problem',
            'time_problem'
        ]
        
        problem_type = random.choice(problem_types)
        
        if problem_type == 'farmer_problem':
            return self._generate_farmer_problem(difficulty)
        elif problem_type == 'recipe_problem':
            return self._generate_recipe_problem(difficulty)
        elif problem_type == 'money_problem':
            return self._generate_money_problem(difficulty)
        else:
            return self._generate_time_problem(difficulty)
    
    def _generate_farmer_problem(self, difficulty):
        """Genera problema del granjero con fracciones"""
        total_animals = random.randint(20, 100)
        
        # Generar fracciones que sumen menos que 1
        denominators = [3, 4, 5, 6, 8]
        den1, den2 = random.sample(denominators, 2)
        
        # Asegurar que las fracciones sean válidas
        num1 = random.randint(1, den1 - 1)
        remaining = sp.Rational(1) - sp.Rational(num1, den1)
        
        # Encontrar numerador válido para la segunda fracción
        max_num2 = int(remaining * den2)
        if max_num2 < 1:
            num2 = 1
            den2 = random.randint(den2, 10)
        else:
            num2 = random.randint(1, min(max_num2, den2 - 1))
        
        sold_fraction1 = sp.Rational(num1, den1)
        sold_fraction2 = sp.Rational(num2, den2)
        total_sold = sold_fraction1 + sold_fraction2
        
        # Calcular animales vendidos y restantes
        animals_sold = int(total_animals * total_sold)
        animals_remaining = total_animals - animals_sold
        
        problem_text = f"""
        Un granjero tiene {total_animals} vacas. El lunes vende $\\frac{{{num1}}}{{{den1}}}$ de sus vacas,
        y el martes vende $\\frac{{{num2}}}{{{den2}}}$ del total original.
        ¿Cuántas vacas le quedan?
        """
        
        return {
            'type': 'word_problems',
            'problem': problem_text,
            'answer': str(animals_remaining),
            'answer_latex': f"{animals_remaining} \\text{{ vacas}}",
            'solution_steps': [
                f"Total de vacas: {total_animals}",
                f"Vendidas el lunes: $\\frac{{{num1}}}{{{den1}}} \\times {total_animals} = {int(total_animals * sold_fraction1)}$",
                f"Vendidas el martes: $\\frac{{{num2}}}{{{den2}}} \\times {total_animals} = {int(total_animals * sold_fraction2)}$",
                f"Total vendidas: {animals_sold}",
                f"Vacas restantes: {total_animals} - {animals_sold} = {animals_remaining}"
            ],
            'error_type': 'fraction_addition'
        }
    
    def _generate_recipe_problem(self, difficulty):
        """Genera problema de receta con fracciones"""
        ingredients = ['harina', 'azúcar', 'mantequilla', 'huevos']
        ingredient = random.choice(ingredients)
        
        original_servings = random.choice([4, 6, 8])
        new_servings = random.choice([2, 3, 12, 16])
        
        # Cantidad original como fracción
        num, den = random.randint(1, 4), random.choice([2, 3, 4])
        original_amount = sp.Rational(num, den)
        
        # Calcular nueva cantidad
        ratio = sp.Rational(new_servings, original_servings)
        new_amount = original_amount * ratio
        
        problem_text = f"""
        Una receta para {original_servings} personas requiere $\\frac{{{num}}}{{{den}}}$ tazas de {ingredient}.
        ¿Cuántas tazas se necesitan para {new_servings} personas?
        """
        
        return {
            'type': 'word_problems',
            'problem': problem_text,
            'answer': str(new_amount),
            'answer_latex': f"{latex(new_amount)} \\text{{ tazas}}",
            'solution_steps': [
                f"Receta original: {original_servings} personas, $\\frac{{{num}}}{{{den}}}$ tazas",
                f"Nueva receta: {new_servings} personas",
                f"Proporción: $\\frac{{{new_servings}}}{{{original_servings}}} = {latex(ratio)}$",
                f"Nueva cantidad: $\\frac{{{num}}}{{{den}}} \\times {latex(ratio)} = {latex(new_amount)}$"
            ],
            'error_type': 'fraction_multiplication'
        }
    
    def _generate_money_problem(self, difficulty):
        """Genera problema de dinero con operaciones combinadas"""
        initial_money = random.randint(50, 200)
        spent1 = random.randint(10, initial_money // 3)
        earned = random.randint(5, 30)
        spent2 = random.randint(5, 25)
        
        final_money = initial_money - spent1 + earned - spent2
        
        problem_text = f"""
        María tenía ${initial_money}. Gastó ${spent1} en el almuerzo, 
        luego ganó ${earned} haciendo un trabajo, y finalmente gastó ${spent2} en transporte.
        ¿Cuánto dinero le queda?
        """
        
        return {
            'type': 'word_problems',
            'problem': problem_text,
            'answer': str(final_money),
            'answer_latex': f"\\${final_money}",
            'solution_steps': [
                f"Dinero inicial: $\\${initial_money}$",
                f"Después del almuerzo: $\\${initial_money} - \\${spent1} = \\${initial_money - spent1}$",
                f"Después del trabajo: $\\${initial_money - spent1} + \\${earned} = \\${initial_money - spent1 + earned}$",
                f"Después del transporte: $\\${initial_money - spent1 + earned} - \\${spent2} = \\${final_money}$"
            ],
            'error_type': 'order_operations'
        }
    
    def _generate_time_problem(self, difficulty):
        """Genera problema de tiempo con fracciones"""
        total_hours = random.choice([8, 12, 24])
        
        # Fracciones de tiempo
        activities = ['estudiando', 'trabajando', 'durmiendo', 'ejercitándose']
        activity = random.choice(activities)
        
        num, den = random.randint(1, 3), random.choice([4, 6, 8])
        time_fraction = sp.Rational(num, den)
        time_spent = time_fraction * total_hours
        
        problem_text = f"""
        En un día de {total_hours} horas, Pedro pasa $\\frac{{{num}}}{{{den}}}$ del tiempo {activity}.
        ¿Cuántas horas pasa {activity}?
        """
        
        return {
            'type': 'word_problems',
            'problem': problem_text,
            'answer': str(time_spent),
            'answer_latex': f"{latex(time_spent)} \\text{{ horas}}",
            'solution_steps': [
                f"Total de horas: {total_hours}",
                f"Fracción del tiempo {activity}: $\\frac{{{num}}}{{{den}}}$",
                f"Horas {activity}: $\\frac{{{num}}}{{{den}}} \\times {total_hours} = {latex(time_spent)}$"
            ],
            'error_type': 'fraction_multiplication'
        }
    
    def _generate_fraction_steps(self, frac1, frac2, operation):
        """Genera pasos detallados para operaciones con fracciones"""
        steps = []
        
        if operation in ['+', '-']:
            # Para suma y resta, mostrar proceso de denominador común
            if frac1.q != frac2.q:  # Denominadores diferentes
                common_den = lcm(frac1.q, frac2.q)
                new_num1 = frac1.p * (common_den // frac1.q)
                new_num2 = frac2.p * (common_den // frac2.q)
                
                steps.append(f"Denominador común: MCM({frac1.q}, {frac2.q}) = {common_den}")
                steps.append(f"Convertir fracciones: $\\frac{{{new_num1}}}{{{common_den}}}$ y $\\frac{{{new_num2}}}{{{common_den}}}$")
                
                if operation == '+':
                    steps.append(f"Sumar numeradores: $\\frac{{{new_num1} + {new_num2}}}{{{common_den}}} = \\frac{{{new_num1 + new_num2}}}{{{common_den}}}$")
                else:
                    steps.append(f"Restar numeradores: $\\frac{{{new_num1} - {new_num2}}}{{{common_den}}} = \\frac{{{new_num1 - new_num2}}}{{{common_den}}}$")
        
        elif operation == '*':
            steps.append(f"Multiplicar numeradores y denominadores")
            steps.append(f"$\\frac{{{frac1.p} \\times {frac2.p}}}{{{frac1.q} \\times {frac2.q}}} = \\frac{{{frac1.p * frac2.p}}}{{{frac1.q * frac2.q}}}$")
        
        else:  # division
            steps.append(f"Multiplicar por el recíproco")
            steps.append(f"$\\frac{{{frac1.p}}}{{{frac1.q}}} \\times \\frac{{{frac2.q}}}{{{frac2.p}}} = \\frac{{{frac1.p * frac2.q}}}{{{frac1.q * frac2.p}}}$")
        
        return steps
    
    def _generate_operation_steps(self, expression):
        """Genera pasos para operaciones combinadas"""
        # Esta es una implementación simplificada
        # En una versión completa, se analizaría la expresión paso a paso
        return [
            "Aplicar jerarquía de operaciones (PEMDAS)",
            "Resolver paréntesis primero",
            "Calcular exponentes",
            "Realizar multiplicaciones y divisiones",
            "Realizar sumas y restas"
        ]
    
    def _generate_mcm_mcd_steps(self, numbers):
        """Genera pasos para calcular MCM y MCD"""
        steps = []
        
        # Factorización de cada número
        for num in numbers:
            factors = factorint(num)
            factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors.items()])
            steps.append(f"{num} = {factor_str}")
        
        steps.append("MCD: tomar factores comunes con menor exponente")
        steps.append("MCM: tomar todos los factores con mayor exponente")
        
        return steps
    
    def _generate_factorization_steps(self, number):
        """Genera pasos para factorización prima"""
        steps = []
        temp = number
        factors = []
        
        # Proceso de factorización
        divisor = 2
        while divisor * divisor <= temp:
            while temp % divisor == 0:
                factors.append(divisor)
                temp //= divisor
                steps.append(f"{temp * divisor} ÷ {divisor} = {temp}")
            divisor += 1
        
        if temp > 1:
            factors.append(temp)
        
        return steps


class AlgebraExerciseGenerator:
    """Clase principal para generar ejercicios de álgebra"""
    
    def __init__(self):
        self.difficulty_levels = ['easy', 'medium', 'hard']
        self.x = symbols('x')
        self.y = symbols('y')
    
    def generate_random_exercise(self, topic=None, difficulty='medium'):
        """
        Genera un ejercicio aleatorio del tema especificado
        """
        topics = ['monomios', 'polinomios', 'productos_notables', 'factorizacion']
        
        if topic is None:
            topic = random.choice(topics)
        
        generators = {
            'monomios': self.generate_monomial_exercise,
            'polinomios': self.generate_polynomial_exercise,
            'productos_notables': self.generate_notable_products_exercise,
            'factorizacion': self.generate_factorization_exercise
        }
        
        return generators[topic](difficulty)
    
    def generate_monomial_exercise(self, difficulty='medium'):
        """Genera ejercicios de operaciones con monomios"""
        
        operations = ['multiply', 'divide', 'add_subtract']
        operation = random.choice(operations)
        
        if difficulty == 'easy':
            # Monomios simples
            coef1, exp1 = random.randint(1, 5), random.randint(1, 3)
            coef2, exp2 = random.randint(1, 5), random.randint(1, 3)
        elif difficulty == 'medium':
            # Monomios con coeficientes negativos
            coef1, exp1 = random.randint(-8, 8), random.randint(1, 4)
            coef2, exp2 = random.randint(-8, 8), random.randint(1, 4)
            if coef1 == 0: coef1 = 1
            if coef2 == 0: coef2 = 1
        else:  # hard
            # Monomios con múltiples variables
            coef1, exp1 = random.randint(-10, 10), random.randint(1, 5)
            coef2, exp2 = random.randint(-10, 10), random.randint(1, 5)
            if coef1 == 0: coef1 = 1
            if coef2 == 0: coef2 = 1
        
        if operation == 'multiply':
            mono1 = coef1 * self.x**exp1
            mono2 = coef2 * self.x**exp2
            result = mono1 * mono2
            
            problem_text = f"Multiplicar: $({latex(mono1)}) \\cdot ({latex(mono2)})$"
            
            solution_steps = [
                f"Multiplicar coeficientes: ${coef1} \\times {coef2} = {coef1 * coef2}$",
                f"Sumar exponentes: $x^{{{exp1}}} \\times x^{{{exp2}}} = x^{{{exp1 + exp2}}}$",
                f"Resultado: ${latex(result)}$"
            ]
            
        elif operation == 'divide':
            # Asegurar que la división sea exacta
            if exp1 < exp2:
                exp1, exp2 = exp2, exp1
                coef1, coef2 = coef2, coef1
            
            mono1 = coef1 * self.x**exp1
            mono2 = coef2 * self.x**exp2
            result = mono1 / mono2
            
            problem_text = f"Dividir: $\\frac{{{latex(mono1)}}}{{{latex(mono2)}}}$"
            
            solution_steps = [
                f"Dividir coeficientes: $\\frac{{{coef1}}}{{{coef2}}} = {sp.Rational(coef1, coef2)}$",
                f"Restar exponentes: $\\frac{{x^{{{exp1}}}}}{{x^{{{exp2}}}}} = x^{{{exp1 - exp2}}}$",
                f"Resultado: ${latex(result)}$"
            ]
            
        else:  # add_subtract
            # Solo monomios semejantes se pueden sumar
            mono1 = coef1 * self.x**exp1
            mono2 = coef2 * self.x**exp1  # Mismo exponente
            
            if random.choice([True, False]):
                result = mono1 + mono2
                problem_text = f"Sumar: $({latex(mono1)}) + ({latex(mono2)})$"
                operation_text = "Sumar"
            else:
                result = mono1 - mono2
                problem_text = f"Restar: $({latex(mono1)}) - ({latex(mono2)})$"
                operation_text = "Restar"
            
            solution_steps = [
                f"Los monomios son semejantes (misma parte literal: $x^{{{exp1}}}$)",
                f"{operation_text} coeficientes: ${coef1} {'+' if operation_text == 'Sumar' else '-'} {coef2} = {coef1 + coef2 if operation_text == 'Sumar' else coef1 - coef2}$",
                f"Resultado: ${latex(result)}$"
            ]
        
        return {
            'type': 'monomios',
            'problem': problem_text,
            'answer': latex(result),
            'answer_latex': latex(result),
            'solution_steps': solution_steps,
            'error_type': 'monomial_operations'
        }
    
    def generate_polynomial_exercise(self, difficulty='medium'):
        """Genera ejercicios de operaciones con polinomios"""
        
        operations = ['add', 'subtract', 'multiply']
        operation = random.choice(operations)
        
        if difficulty == 'easy':
            # Polinomios simples
            poly1 = random.randint(1, 5) * self.x + random.randint(1, 10)
            poly2 = random.randint(1, 5) * self.x + random.randint(1, 10)
        elif difficulty == 'medium':
            # Polinomios cuadráticos
            poly1 = random.randint(1, 3) * self.x**2 + random.randint(-5, 5) * self.x + random.randint(-10, 10)
            poly2 = random.randint(1, 3) * self.x + random.randint(-5, 5)
        else:  # hard
            # Polinomios más complejos
            poly1 = random.randint(1, 2) * self.x**3 + random.randint(-3, 3) * self.x**2 + random.randint(-5, 5) * self.x + random.randint(-10, 10)
            poly2 = random.randint(1, 2) * self.x**2 + random.randint(-3, 3) * self.x + random.randint(-5, 5)
        
        if operation == 'add':
            result = poly1 + poly2
            problem_text = f"Sumar: $({latex(poly1)}) + ({latex(poly2)})$"
            
            solution_steps = [
                "Agrupar términos semejantes",
                f"Resultado: ${latex(result)}$"
            ]
            
        elif operation == 'subtract':
            result = poly1 - poly2
            problem_text = f"Restar: $({latex(poly1)}) - ({latex(poly2)})$"
            
            solution_steps = [
                "Cambiar signos del segundo polinomio",
                "Agrupar términos semejantes",
                f"Resultado: ${latex(result)}$"
            ]
            
        else:  # multiply
            result = expand(poly1 * poly2)
            problem_text = f"Multiplicar: $({latex(poly1)}) \\cdot ({latex(poly2)})$"
            
            solution_steps = [
                "Aplicar propiedad distributiva",
                "Multiplicar cada término del primer polinomio por cada término del segundo",
                "Agrupar términos semejantes",
                f"Resultado: ${latex(result)}$"
            ]
        
        return {
            'type': 'polinomios',
            'problem': problem_text,
            'answer': latex(result),
            'answer_latex': latex(result),
            'solution_steps': solution_steps,
            'error_type': 'polynomial_operations'
        }
    
    def generate_notable_products_exercise(self, difficulty='medium'):
        """Genera ejercicios de productos notables"""
        
        products = ['square_sum', 'square_diff', 'diff_squares', 'cube_sum', 'cube_diff']
        product_type = random.choice(products)
        
        if difficulty == 'easy':
            a, b = random.randint(1, 5), random.randint(1, 5)
        elif difficulty == 'medium':
            a, b = random.randint(1, 8), random.randint(1, 8)
        else:  # hard
            a, b = random.randint(1, 10), random.randint(1, 10)
        
        if product_type == 'square_sum':
            # (a + b)²
            expr = (a * self.x + b)**2
            result = expand(expr)
            problem_text = f"Desarrollar: $({a}x + {b})^2$"
            formula = "(a + b)^2 = a^2 + 2ab + b^2"
            
        elif product_type == 'square_diff':
            # (a - b)²
            expr = (a * self.x - b)**2
            result = expand(expr)
            problem_text = f"Desarrollar: $({a}x - {b})^2$"
            formula = "(a - b)^2 = a^2 - 2ab + b^2"
            
        elif product_type == 'diff_squares':
            # (a + b)(a - b)
            expr = (a * self.x + b) * (a * self.x - b)
            result = expand(expr)
            problem_text = f"Desarrollar: $({a}x + {b})({a}x - {b})$"
            formula = "(a + b)(a - b) = a^2 - b^2"
            
        elif product_type == 'cube_sum':
            # (a + b)³
            expr = (a * self.x + b)**3
            result = expand(expr)
            problem_text = f"Desarrollar: $({a}x + {b})^3$"
            formula = "(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3"
            
        else:  # cube_diff
            # (a - b)³
            expr = (a * self.x - b)**3
            result = expand(expr)
            problem_text = f"Desarrollar: $({a}x - {b})^3$"
            formula = "(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3"
        
        solution_steps = [
            f"Aplicar la fórmula: ${formula}$",
            f"Sustituir valores: $a = {a}x$, $b = {b}$",
            f"Resultado: ${latex(result)}$"
        ]
        
        return {
            'type': 'productos_notables',
            'problem': problem_text,
            'answer': latex(result),
            'answer_latex': latex(result),
            'solution_steps': solution_steps,
            'error_type': 'notable_products'
        }
    
    def generate_factorization_exercise(self, difficulty='medium'):
        """Genera ejercicios de factorización"""
        
        factorization_types = ['common_factor', 'perfect_square', 'diff_squares', 'trinomial']
        fact_type = random.choice(factorization_types)
        
        if difficulty == 'easy':
            coeffs = [1, 2, 3, 4, 5]
        elif difficulty == 'medium':
            coeffs = [1, 2, 3, 4, 5, 6, 8, 9]
        else:  # hard
            coeffs = [1, 2, 3, 4, 5, 6, 8, 9, 12, 16]
        
        if fact_type == 'common_factor':
            # Factor común
            common = random.choice([2, 3, 4, 5])
            a, b = random.choice(coeffs), random.choice(coeffs)
            
            poly = common * a * self.x**2 + common * b * self.x
            factored = factor(poly)
            
            problem_text = f"Factorizar: ${latex(poly)}$"
            
            solution_steps = [
                f"Identificar factor común: ${common}x$",
                f"Extraer factor común: ${latex(factored)}$"
            ]
            
        elif fact_type == 'perfect_square':
            # Trinomio cuadrado perfecto
            a = random.choice([1, 2, 3, 4])
            b = random.choice([1, 2, 3, 4, 5])
            
            poly = a**2 * self.x**2 + 2*a*b * self.x + b**2
            factored = factor(poly)
            
            problem_text = f"Factorizar: ${latex(poly)}$"
            
            solution_steps = [
                "Reconocer trinomio cuadrado perfecto: $a^2 + 2ab + b^2 = (a + b)^2$",
                f"Identificar: $a = {a}x$, $b = {b}$",
                f"Factorizar: ${latex(factored)}$"
            ]
            
        elif fact_type == 'diff_squares':
            # Diferencia de cuadrados
            a = random.choice([1, 2, 3, 4])
            b = random.choice([1, 2, 3, 4, 5])
            
            poly = a**2 * self.x**2 - b**2
            factored = factor(poly)
            
            problem_text = f"Factorizar: ${latex(poly)}$"
            
            solution_steps = [
                "Reconocer diferencia de cuadrados: $a^2 - b^2 = (a + b)(a - b)$",
                f"Identificar: $a = {a}x$, $b = {b}$",
                f"Factorizar: ${latex(factored)}$"
            ]
            
        else:  # trinomial
            # Trinomio de la forma x² + bx + c
            # Buscar dos números que sumados den b y multiplicados den c
            factors_c = [(1, 6), (2, 3), (1, 8), (2, 4), (1, 12), (3, 4)]
            p, q = random.choice(factors_c)
            
            if random.choice([True, False]):
                p = -p
            if random.choice([True, False]):
                q = -q
            
            b = p + q
            c = p * q
            
            poly = self.x**2 + b * self.x + c
            factored = factor(poly)
            
            problem_text = f"Factorizar: ${latex(poly)}$"
            
            solution_steps = [
                f"Buscar dos números que sumados den ${b}$ y multiplicados den ${c}$",
                f"Los números son ${p}$ y ${q}$",
                f"Factorizar: ${latex(factored)}$"
            ]
        
        return {
            'type': 'factorizacion',
            'problem': problem_text,
            'answer': latex(factored),
            'answer_latex': latex(factored),
            'solution_steps': solution_steps,
            'error_type': 'factorization'
        }
