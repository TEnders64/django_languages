from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Language
# Create your views here.
def index (request):
    languages = Language.objects.all()
    return render(request, 'languages/index.html', {'languages' : languages})

def new (request):
    return render(request, 'languages/new.html')

def create (request):
    if request.method == 'POST':
        result = Language.objects.validate_language(name=request.POST['name'])
        if result[0]:
            return redirect(reverse('index'))
        else:
            pass
            # we have errors we need to get back out to the 'new' template
    else:
        return redirect(reverse('index'))

def show (request, id):
    language = Language.objects.get(id=id)
    print language
    return render(request, 'languages/show.html', {'language':language})

def edit (request, id):
    language = Language.objects.get(id=id)
    print language
    return render(request, 'languages/edit.html', {'language':language})

def update (request, id):
    if request.method == 'POST':
        # How do we update a language object?
        pass
    else:
        return redirect(reverse('edit')) #Gosh, I want to send them back to the specific language's edit page!

def delete (request, id):
    pass
