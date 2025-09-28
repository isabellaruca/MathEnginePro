# MathEngine - Aplicación Streamlit

## 🚀 Migración Completa de Django a Streamlit

Esta es la versión migrada de MathEngine de Django a Streamlit, manteniendo **TODAS** las funcionalidades originales:

### ✅ Funcionalidades Migradas

#### 🔧 Solver Matemático
- ✅ Resolución paso a paso de expresiones matemáticas
- ✅ Soporte para ecuaciones, factorización, simplificación
- ✅ Renderizado LaTeX completo
- ✅ Interfaz visual mejorada

#### 📚 Teoría Completa
- ✅ **Aritmética**: Conjuntos numéricos, operaciones combinadas, fracciones, MCM/MCD
- ✅ **Álgebra**: Monomios, polinomios, productos notables, factorización
- ✅ Navegación entre secciones
- ✅ Ejemplos interactivos con soluciones paso a paso

#### 💪 Sistema de Práctica
- ✅ Generación automática de ejercicios
- ✅ Múltiples niveles de dificultad (Fácil, Medio, Difícil)
- ✅ Estadísticas de progreso en tiempo real
- ✅ Sistema de rachas y precisión
- ✅ Verificación inteligente de respuestas

#### 📝 Sistema de Exámenes
- ✅ Configuración personalizable (temas, tiempo, dificultad)
- ✅ Exámenes cronometrados
- ✅ Navegación entre preguntas
- ✅ Resultados detallados con explicaciones
- ✅ Análisis de rendimiento

### 🎯 Mejoras Adicionales

#### 🎨 Interfaz Mejorada
- ✅ Diseño moderno y responsivo
- ✅ Tema oscuro/claro automático
- ✅ Navegación intuitiva con sidebar
- ✅ Componentes visuales atractivos

#### ⚡ Rendimiento
- ✅ Carga más rápida que Django
- ✅ Sin necesidad de base de datos
- ✅ Deploy simplificado
- ✅ Escalabilidad automática

#### 🔧 Funcionalidades Técnicas
- ✅ Renderizado LaTeX perfecto
- ✅ Generación algorítmica de ejercicios
- ✅ Motor de resolución simbólica con SymPy
- ✅ Verificación matemática inteligente

## 🚀 Instalación y Uso

### Opción 1: Ejecutar Localmente

\`\`\`bash
# Clonar el repositorio
git clone <repository-url>
cd mathengine-streamlit

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run app.py
\`\`\`

### Opción 2: Deploy en Streamlit Cloud

1. Subir el código a GitHub
2. Conectar con Streamlit Cloud
3. Deploy automático desde `streamlit_app.py`

## 📁 Estructura del Proyecto

\`\`\`
mathengine-streamlit/
├── app.py                      # Aplicación principal
├── streamlit_app.py           # Punto de entrada para Streamlit Cloud
├── requirements.txt           # Dependencias
├── utils/
│   ├── __init__.py
│   ├── arithmetic_content.py  # Contenido teórico de aritmética
│   ├── algebra_content.py     # Contenido teórico de álgebra
│   ├── exercise_generators.py # Generadores de ejercicios
│   └── solver_engine.py       # Motor de resolución matemática
└── README_STREAMLIT.md        # Esta documentación
\`\`\`

## 🎓 Uso de la Aplicación

### 🏠 Página Principal
- Acceso rápido a todas las funcionalidades
- Estadísticas de progreso
- Enlaces directos a temas específicos

### 🔧 Solver Matemático
- Ingresa cualquier expresión matemática
- Obtén solución paso a paso
- Ejemplos incluidos para comenzar

### 📚 Teoría
- **Aritmética**: Conceptos fundamentales con ejemplos
- **Álgebra**: Desde monomios hasta factorización
- Navegación secuencial entre temas

### 💪 Práctica
- Selecciona tema y dificultad
- Ejercicios generados automáticamente
- Estadísticas en tiempo real
- Explicaciones detalladas

### 📝 Exámenes
- Configura duración y temas
- Examen cronometrado
- Resultados detallados
- Análisis de rendimiento

## 🔧 Características Técnicas

### Generación de Ejercicios
- **Aritmética**: Fracciones, operaciones combinadas, MCM/MCD, factorización, problemas verbales
- **Álgebra**: Monomios, polinomios, productos notables, factorización

### Motor de Resolución
- Powered by SymPy
- Soporte para ecuaciones y expresiones
- Simplificación automática
- Factorización inteligente

### Verificación de Respuestas
- Comparación simbólica
- Tolerancia a diferentes formatos
- Evaluación matemática precisa

## 🌟 Ventajas sobre Django

1. **Deploy Simplificado**: Sin configuración de servidor
2. **Carga Rápida**: Aplicación más ligera
3. **Interfaz Moderna**: Componentes nativos de Streamlit
4. **Escalabilidad**: Auto-scaling en Streamlit Cloud
5. **Mantenimiento**: Menos código, más funcionalidad

## 🎯 Próximas Mejoras

- [ ] Más tipos de ejercicios
- [ ] Sistema de usuarios persistente
- [ ] Gráficos interactivos
- [ ] Exportación de resultados
- [ ] Modo offline

## 📞 Soporte

Para problemas o sugerencias, crear un issue en el repositorio.

---

**MathEngine Streamlit** - La evolución natural de la plataforma de aprendizaje matemático 🚀
