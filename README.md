# diario_personal_django
Educativo y de Aprendizaje Personal

---
## Tabla de Contenidos
- [Tecnologías](#Tecnologías)
- [Configuración Inicial](#configuración-Inicial)
- [Creación del Modelo](#creación-del-modelo)
---
# Tecnologías
- Django: Framework web en Python.
- postgresql: PostgreSQL
--- 
# Configuración Inicial 
1. Entorno virtual 
    ```bash 
    python -m venv venv

2. Activar el entorno virtual
    ```bash 
    venv\Scripts\activate

3. Actualizamos los pip
    ```bash
    python.exe -m pip install --upgrade pip

4. Instamos las dependencias del archivo requirements.txt
    ```bash
    pip freeze > requirements.txt

6. Crear el proyecto de django crud
    ```bash 
    django-admin startproject diary_project

7. Ingresamos al diary_project
    ```bash 
    cd diary_project

9. Creamos la aplicacion llamada diary
    ```bash     
    python manage.py startapp diary


10. Configuración de /settings.py 
    ```bash 
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'diary',
    ]

11. Generamos las migraciones
    ```bash 
    python manage.py migrate

12. Creamos el super usuario
    ```bash 
    python manage.py createsuperuser

13. Corremos el Servidor
    ```bash
    python manage.py runserver

14. Verificamos el superusuario en   
# Creación del Modelo 

11. creamos del modelo en diary/models.py
    ```bash
    from django.db import models

    # Create your models here.
    class Entry(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title

12. registramos el modelo en en el panel de admin diary/admin.py
    ```bash
    from django.contrib import admin
    from models import Entry
    # Register your models here.
    admin.site.register(Entry)


13. Migramos el modelo 
    ```bash
    python manage.py makemigrations 
    python manage.py migrate

14. Corremos el Servidor
    ```bash
    python manage.py runserver 

15. Verificamos que no haya ningun error http://127.0.0.1:8000/admin/entry/

16. Creamos una url en la aplicación diary 
    ```bash
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.entry_list, name='entry-list'),
    ]

17. Agregamos al proyecto diary_project 
    ```bash	
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('diary.urls')),
    ]

18. Creamos las urls en diary/urls.py
    ```bash	
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.entry_list, name='entry-list'),
        path('', views.entry_detail, name='entry-detail'),
    ]
19. Creamos las views en diary/views.py
    ```bash	
    from django.shortcuts import render, get_object_or_404
    from .models import Entry


    # Create your views here.
    def entry_list(request):
        entries = Entry.objects.order_by("created")
        return render(request, 'diary/entry_list.html', {'entries': entries})

    def entry_detail(request, id):
        entry = get_object_or_404(Entry, id=id)
        return render(request,  'diary/entry_detail.html', {'entry': entry})

20. hacemos en diary el templates\diary\base.html
    ```bash	
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    </head>

    <body>
        <div class="container">
            <div class="row text-center mt-4 p-2">
                <h1><a href="/">Entradas de Mi Diario Personal</a></h1>
            </div>
            <div class="row">
                {% block content %}
                {% endblock %}
            </div>
        </div>


    </body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>

    </html>

21. templates\diary\entry_list.html
    ```bash	
    {% extends 'diary/base.html' %}
    {% block content %}

    <div class="grid">
        <ul class="list-group">
            {% for entry in entries %}
            <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">{{entry.title}}</h5>
                <small>{{entry.created | date:'Y-m-d H:i'}}</small>
            </div>
            {% endfor %}
        </ul>

    </div>
    {% endblock %}
22. templates\diary\entry_list.html
    ```bash
    {% extends 'diary/base.html' %}
    {% block content %}

    <div class="grid">
        <ul class="list-group">
            {% for entry in entries %}
            <a href="{%  url 'entry-detail' entry.id %}" class="list-group-item list-group-item-action">
                <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">{{entry.title}}</h5>
                    <small>{{entry.created | date:'Y-m-d H:i'}}</small>
                </div>
            </a>
            {% endfor %}
        </ul>

    </div>
    {% endblock %}
