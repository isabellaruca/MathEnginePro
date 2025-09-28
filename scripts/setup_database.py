#!/usr/bin/env python
"""
Script para configurar la base de datos inicial de MathEngine
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mathengine_project.settings')
django.setup()

from django.core.management import execute_from_command_line

def setup_database():
    """Configura la base de datos inicial"""
    print("🔧 Configurando base de datos de MathEngine...")
    
    # Crear migraciones
    print("📝 Creando migraciones...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # Aplicar migraciones
    print("🚀 Aplicando migraciones...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Crear superusuario si no existe
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        print("👤 Creando superusuario admin...")
        User.objects.create_superuser('admin', 'admin@mathengine.com', 'admin123')
        print("✅ Superusuario creado: admin/admin123")
    
    print("✅ Base de datos configurada correctamente!")
    print("\n🎯 Próximos pasos:")
    print("1. Ejecuta: python manage.py runserver")
    print("2. Visita: http://localhost:8000")
    print("3. Admin: http://localhost:8000/admin (admin/admin123)")

if __name__ == '__main__':
    setup_database()
