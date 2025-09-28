# MathEngine - Plataforma de Matemáticas para Ingeniería

MathEngine es una plataforma web integral diseñada para el aprendizaje de matemáticas orientado a estudiantes de ingeniería. Ofrece herramientas interactivas para resolver problemas, estudiar teoría y practicar ejercicios.

## 🚀 Características Principales

### 🧮 Solucionador Matemático
- Resolución paso a paso de expresiones algebraicas
- Soporte para polinomios, factorización y simplificación
- Interfaz visual con teclado matemático
- Renderizado LaTeX para fórmulas

### 📚 Módulos Teóricos
- **Aritmética**: Conjuntos numéricos, operaciones combinadas, fracciones, MCM/MCD
- **Álgebra**: Monomios, polinomios, productos notables, factorización
- Contenido estructurado con ejemplos resueltos
- Navegación por pestañas para fácil acceso

### 🏋️ Práctica Interactiva
- Generación algorítmica de ejercicios únicos
- Múltiples niveles de dificultad
- Retroalimentación inmediata
- Seguimiento de estadísticas de progreso
- Explicaciones paso a paso de soluciones

### 📊 Sistema de Evaluación
- Exámenes personalizables por tema
- Control de tiempo configurable
- Resultados detallados con análisis

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 4.2**: Framework web principal
- **SymPy**: Biblioteca de matemáticas simbólicas
- **Python 3.8+**: Lenguaje de programación

### Frontend
- **Bootstrap 5**: Framework CSS responsivo
- **MathJax 3**: Renderizado de fórmulas matemáticas
- **HTMX**: Interactividad dinámica
- **Font Awesome**: Iconografía

### Base de Datos
- **SQLite**: Base de datos por defecto (desarrollo)
- **PostgreSQL**: Recomendado para producción

## 📦 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
\`\`\`bash
git clone https://github.com/tu-usuario/mathengine.git
cd mathengine
\`\`\`

2. **Crear entorno virtual**
\`\`\`bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
\`\`\`

3. **Instalar dependencias**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. **Configurar base de datos**
\`\`\`bash
python scripts/setup_database.py
\`\`\`

5. **Ejecutar servidor de desarrollo**
\`\`\`bash
python manage.py runserver
\`\`\`

6. **Acceder a la aplicación**
- Aplicación: http://localhost:8000
- Panel de administración: http://localhost:8000/admin
- Usuario admin: `admin` / `admin123`

## 🏗️ Estructura del Proyecto

\`\`\`
mathengine/
├── mathengine_project/          # Configuración principal de Django
├── core/                        # Aplicación principal
│   ├── templates/core/         # Templates del core
│   └── views.py                # Vistas principales
├── topics/                      # Módulos de matemáticas
│   ├── arithmetic/             # Módulo de aritmética
│   └── algebra/                # Módulo de álgebra
├── templates/                   # Templates globales
│   ├── base.html              # Template base
│   ├── arithmetic/            # Templates de aritmética
│   └── algebra/               # Templates de álgebra
├── static/                      # Archivos estáticos
├── scripts/                     # Scripts de utilidad
└── requirements.txt            # Dependencias Python
\`\`\`

## 🎯 Uso de la Plataforma

### Para Estudiantes

1. **Estudiar Teoría**
   - Navega a las secciones de Aritmética o Álgebra
   - Revisa conceptos con ejemplos resueltos
   - Utiliza la navegación por pestañas

2. **Practicar Ejercicios**
   - Selecciona tema y dificultad
   - Resuelve ejercicios generados automáticamente
   - Recibe retroalimentación inmediata
   - Consulta soluciones paso a paso

3. **Resolver Problemas**
   - Usa el solucionador matemático
   - Ingresa expresiones con el teclado virtual
   - Obtén soluciones detalladas

4. **Tomar Exámenes**
   - Configura exámenes personalizados
   - Practica con límite de tiempo
   - Revisa resultados detallados

### Para Educadores

1. **Administración**
   - Accede al panel de administración
   - Gestiona contenido teórico
   - Revisa estadísticas de uso

2. **Personalización**
   - Modifica ejercicios existentes
   - Agrega nuevo contenido teórico
   - Configura parámetros de evaluación

## 🔧 Configuración Avanzada

### Variables de Entorno
\`\`\`bash
# .env
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
DATABASE_URL=sqlite:///db.sqlite3
\`\`\`

### Base de Datos en Producción
\`\`\`python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mathengine_db',
        'USER': 'mathengine_user',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
\`\`\`

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Roadmap

### Versión 2.0
- [ ] Módulo de Cálculo Diferencial
- [ ] Módulo de Cálculo Integral
- [ ] Sistema de usuarios y perfiles
- [ ] Gamificación con logros y puntos

### Versión 2.1
- [ ] Módulo de Ecuaciones Diferenciales
- [ ] Gráficos interactivos con Plotly
- [ ] Exportación de reportes PDF
- [ ] API REST para integraciones

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Equipo

- **Desarrollador Principal**: Tu Nombre
- **Consultor Matemático**: Nombre del Consultor
- **Diseñador UX/UI**: Nombre del Diseñador

## 📞 Soporte

- **Email**: soporte@mathengine.com
- **Documentación**: https://docs.mathengine.com
- **Issues**: https://github.com/tu-usuario/mathengine/issues

---

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella en GitHub!
