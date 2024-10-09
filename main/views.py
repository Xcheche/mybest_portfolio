from django.shortcuts import render
from .models import About, Service, Education, Experience
# Create your views here.
def index(request):
    about = About.published.all()  # Get only published About entries
    services = Service.published.all()  # Get only published Service entries
    experience = Experience.published.all()  # Get only published Experience entries
    education = Education.published.all()  # Get only published Education entries

    # Check if About is empty
    if not about:
        about = None
        
    # Check if Service is empty
    if not services:
        services = None

    # Check if Education is empty
    if not education:
        education = None

    # Check if Experience is empty
    if not experience:
        experience = None

    return render(
        request,
        "main/index.html",
        {
            "about": about,
            "services": services,
            "education": education,
            "experience": experience,
        },
    )