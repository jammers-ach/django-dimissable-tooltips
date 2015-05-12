from django.shortcuts import render
from .models import DissmissableToolTip,HasSeen
from django.http import JsonResponse

def hide_popup(request):
    if('p' in request.GET):
        template_id = request.GET['p']
        dtt,created = DissmissableToolTip.objects.get_or_create(unique_id=template_id,defaults={'text':'Template not set:%s'% template_id})
        hs,created = HasSeen.objects.get_or_create(user=request.user,dtt=dtt)


        return JsonResponse({'ok':True})


def get_popup(request):
    if('p' in request.GET):
        template_id = request.GET['p']
        dtt,created = DissmissableToolTip.objects.get_or_create(unique_id=template_id,defaults={'text':'Template not set:%s'% template_id})
        hs = HasSeen.objects.filter(user=request.user,dtt=dtt).exists()

        return JsonResponse({'ok':True,
                             'text':dtt.text,
                             'id':dtt.id,
                             'seen':hs})


