from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'form':TFO}
    if request.method=='POST':
        fd=TopicForm(request.POST)
        if fd.is_valid():
            tn=fd.cleaned_data['topic_name']
            T=Topic.objects.get_or_create(topic_name=tn)[0]
            T.save()
            return HttpResponse('topic is inserted ')
    return render(request,'insert_topic.html',d)



def topic_modelform(request):
    TMFO=ModelTopicForm()
    d={'form':TMFO}
    if request.method=='POST':
        FD=ModelTopicForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('topic is inserted successfully')
    return render(request,'topic_modelform.html',d)

def webpage_modelform(request):
    WMFO=ModelWebpageForm()
    d={'form':WMFO}

    if request.method=='POST':
        FD=ModelWebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('webpage is created successfully')
    return render(request,'webpage_modelform.html',d)


def access_modelform(request):
    ARFO=ModelAcessForm()
    d={'form':ARFO}
    
    if request.method=='POST':
        FD=ModelAcessForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('AccessRecord is created successfully')
    return render(request,'access_modelform.html',d)