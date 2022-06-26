from django.shortcuts import render
from  django.http import HttpResponse,Http404,JsonResponse
from .models import Twits

# Create your views here.

def home(request,*args,**kwargs):
    print(args,kwargs)
    #return HttpResponse("<h1>hello world </h1>")
    return render(request,'pages/home.html',context={},status=200)

def twit_list_view(request):
    twit_obj = Twits.objects.all()
    print(twit_obj)
    lst = [{"id ": x.id,"content": x.content} for x in twit_obj]
    data ={
        "response" : lst
    }
    return JsonResponse(data)

def twit_detail_view(request,twit_id ,*args,**kwargs):
    data = {
        "id": twit_id,
        # "image_path" : obj.image.url
    }
    status = 200
    try:
        obj = Twits.objects.get(id=twit_id)
        data["content"]= obj.content
    except:
        #raise Http404
        data["message"] = "<b>Not Found</b>"
        status = 404

    #return HttpResponse(f"<h1>hello {tweet_id } - {obj.content}</h1>")
    return JsonResponse(data,status = status)