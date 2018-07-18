from django.shortcuts import render, HttpResponse
from django.core import serializers

def index(request):
    return render(request, 'life/index.html')

#   handles a get request
def groups(request):
  if request.method == 'POST':
    print('Hello!')
    return HttpResponse('')
  else:
    all_groups = Groups.objects.all()
    response = serialize('json', all_groups)
    return HttpResponse(response, content_type="application/json")

