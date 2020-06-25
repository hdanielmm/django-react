from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'frontend/index.html') # Automáticamente va a templates/frontend/index.html