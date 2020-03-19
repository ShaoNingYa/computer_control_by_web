import base64
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, Http404, StreamingHttpResponse
from app_window_show.models import click_message
from django.http import JsonResponse

# Create your views here.
def app_get_main(request):
    return render(request,'index.html')

#def get_new_pic(request):
#    with open("/var/www/html/djangoProjects/cloudup/cloudup/collected_static/new_pic/pic_1583566982.png") as f:
#        yield

def Q_get_new_pic(request):
    def file_iterator(file_name,chunk_size=512):
        with open(file_name, 'rb') as f:
            print(file_name)
            if f:
                yield f.read(chunk_size)
                print("done")
            else:
                print("no done")

    file_name = "/var/www/html/djangoProjects/cloudup/cloudup/collected_static/new_pic/pic_1583566982.png"
    response = StreamingHttpResponse(file_iterator(file_name))

    #response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachement;filename="{0}"'.format(file_name)
    return response



@csrf_exempt
def get_new_pic(request):
    file_name = "/var/www/html/djangoProjects/cloudup/cloudup/collected_static/new_pic/next.jpg"
    file = open(file_name, "rb")
    result = file.read()
    result = base64.b64encode(result)
    return HttpResponse(result)
    #return HttpResponse(result, content_type='image/jpeg')


@csrf_exempt
def push_position(request):
    positon_get = str(request.POST.get("position_get"))
    one_message = click_message(position=positon_get,isClicked=False)
    one_message.save()
    print(">>>>>>>>>>>>" + positon_get)
    return HttpResponse("")

@csrf_exempt
def get_position(request):
    one_message_object = click_message.objects.all().filter(isClicked=False)
    if len(one_message_object) < 1:
        return JsonResponse("none",safe=False)
    
    one_message = one_message_object[0].position
    one_message_object.update(isClicked=True)
    print(">>>>>>>>>>>>" + one_message)
    return JsonResponse(one_message,safe=False)
