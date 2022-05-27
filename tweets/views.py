from django.shortcuts import render
from  django.http import HttpResponse,Http404,JsonResponse
from .models import Tweets

# Create your views here.

def home(request,*args,**kwargs):
    print(args,kwargs)
    #return HttpResponse("<h1>hello world </h1>")
    return render(request,'pages/home.html',context={},status=200)

def tweet_list_view(request):
    tweet_obj = Tweets.objects.all()
    lst = [{"id ": x.id,"content": x.content} for x in tweet_obj]
    data ={
        "response" : lst
    }
    return JsonResponse(data)

def tweet_detail_view(request,tweet_id ,*args,**kwargs):
    data = {
        "id": tweet_id,
        # "image_path" : obj.image.url
    }
    status = 200
    try:
        obj = Tweets.objects.get(id=tweet_id)
        data["content"]= obj.content
    except:
        #raise Http404
        data["message"] = "<b>Not Found</b>"
        status = 404

    #return HttpResponse(f"<h1>hello {tweet_id } - {obj.content}</h1>")
    return JsonResponse(data,status = status)