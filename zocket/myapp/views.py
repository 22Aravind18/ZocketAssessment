from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import User

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User added successfully!")
    else:
        form = UserForm()
    return render(request, 'myapp/index.html', {'form': form})

def search(request):
    query = request.GET.get('q', '')
    if query:
        try:
            user = User.objects.get(name__iexact=query)
            return HttpResponse(f"Name: {user.name}, Age: {user.age}")
        except User.DoesNotExist:
            return HttpResponse("User not found")
    return render(request, 'myapp/search.html')