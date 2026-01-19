from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def homeView(request):
    """View function for the home page of ExampleApp."""
    return render(request, "index.html")