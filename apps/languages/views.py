from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
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
        print result
        if result[0]:
            return redirect(reverse('index'))
        else:
            print "+============"
            for message in result[1]:
                messages.error(request, message)
            return redirect(reverse('new'))
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
        if len(request.POST['name'])<2:
            messages.error(request, 'Name must be at least 2 characters')
            return redirect(reverse('edit', kwargs={'id':id}))
        else:
            language = Language.objects.get(id=id)
            language.name = request.POST['name']
            print language.name
            language.save()
            return redirect(reverse('show', kwargs={'id':id}))
    else:
        return redirect(reverse('edit', kwargs={'id':id})) #Gosh, I want to send them back to the specific language's edit page!

def delete (request, id):
    pass
