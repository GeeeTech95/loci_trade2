from django.views.generic import View,TemplateView,ListView,DetailView
from django.views.generic.edit import  DeleteView,UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from wallet.models import Transaction
from .models import Settings as ModelSetting
from .forms import SettingsForm
from django.utils import timezone

class AdminBase(UserPassesTestMixin,LoginRequiredMixin,) :

    def get_user(self) :
        return None
    
    def test_func(self) :
        
        try :
            admin = self.request.user.user_admin
            self.admin = admin
        except : return False
        if not admin.is_active : return False

        #check if free plan has expired
        if admin.free_plan_expired :
            #return False
            pass

        if True :
            #self.request.user.date_joined.timedelta(days=settings.FREE_PLAN_DURATION) < timezone.now() :
            #admin.free_plan_expired = True
            #admin.save()
            #return False
            pass

 
        return True 



class Dashboard(AdminBase,View) :
    template_name = 'admin-dashboard.html'

    def get(self,request,*args,**kwargs) :
        transaction_history = Transaction.objects.filter(user__admin = request.user).order_by('-date')[:8]
        prepend = "https://" if request.is_secure() else "http://"
        host = request.get_host()
        try :
            reg_link  = prepend + host + request.user.user_admin.reg_link
            reg_and_ref_link = prepend + host + request.user.user_admin.reg_and_ref_link
        except :
            pass
        return render(request,self.template_name,locals())    


class Settings(AdminBase,View) :
    model = ModelSetting
    form_class = SettingsForm
    template_name = "form.html"

    def get(self,request,*args,**kwargs) :
        form = self.form_class(instance=self.model.objects.get(admin = request.user.user_admin))
        form_title = "Admin Settings"
        return render(request,self.template_name,locals())

    def post(self,request,*args,**kwargs) :  
        form = self.form_class(request.POST) 
        if form.is_valid() :
            for field in form.fields.keys() :
                try : setattr(request.user.user_admin.settings,field,form.cleaned_data.get(field))
                except TypeError : continue
            request.user.user_admin.settings.save() 
            return HttpResponseRedirect(reverse('admin-dashboard'))
        else :
            return render(request,self.template_name,locals())


class Members(AdminBase,View) :
    template_name = 'members.html'

    def get(self,request,*args,**kwargs) :
        members = request.user.users.all().order_by('-name','-username')
        return render(request,self.template_name,locals())


