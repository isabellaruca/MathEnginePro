"""
Generador de ejercicios para el módulo de Aritmética
Este archivo contiene funciones que crean problemas algorítmicamente
"""

import random
import sympy as sp
from sympy import gcd, lcm, factorint, latex
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


# Instancia global del generador
generator = ArithmeticExerciseGenerator()

def get_random_exercise(topic=None, difficulty='medium'):
    """Función de conveniencia para generar ejercicios"""
    return generator.generate_random_exercise(topic, difficulty)
