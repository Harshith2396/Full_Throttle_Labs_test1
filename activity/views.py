from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Myuser,Activity_period
class activity(View):
    def get(self,request):
            lists=[]
            all=Myuser.object.values('email','user_id','tz','name')
            for i in all:
                acti=Activity_period.objects.filter(email=i['email']).values('start_time','end_time')
                lists.append({'id':i['user_id'],'real_name':i['name'],'tz':i['tz'],'activity_period':list(acti)})
            return JsonResponse({"ok":True,'members':lists})