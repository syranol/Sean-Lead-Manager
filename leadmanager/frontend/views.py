from django.shortcuts import render

#When  you create a view method, pass in request
def index(request):
    #render is brought in above
    #render takes in request and whatever template you want to load
    #look into template folder, frontend and then index.html
    return render(request, 'frontend/index.html')