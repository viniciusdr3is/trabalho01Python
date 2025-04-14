import os
from django.shortcuts import render
from django.conf import settings

UPLOAD_FOLDER = os.path.join(settings.BASE_DIR, 'galeria', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def index(request):
    images = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
    return render(request, 'galeria/index.html', {'images': images})