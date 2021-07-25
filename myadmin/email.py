from django.views.generic import View,TemplateView,ListView,DetailView
from django.views.generic.edit import  DeleteView,UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render

from core.mail import Email
from .forms import SendMailForm
from .dashboard import AdminBase



class SendCustomMail(AdminBase,View) :
    form_class = SendMailForm
    success_url = reverse_lazy('admin-dashboard')
    template_name = 'form.html'
    email_template = 'custom-email.html'


    def  get(self,request,*args,**kwargs)  :
        wallet_id = kwargs.get('wallet_id',None)
        if not wallet_id : 
            pass
        form = self.form_class(admin = request.user)
        form_title = 'Send Custom Email'
        return render(request,self.template_name,locals())

    def  post(self,request,*args,**kwargs)  :
        form = self.form_class(request.POST) 
        ctx = {}
        if form.is_valid() :
            sub = form.cleaned_data['subject']  
            email = form.cleaned_data['receiver_email']
            message = form.cleaned_data['message']
            receivers = form.cleaned_data['users']
            receivers = [user.email for user in receivers]
            mail = Email(send_type="support")
            ctx['custom_message'] = message
            ctx['subject'] = sub
            mail.send_html_email([receivers],sub,self.email_template,ctx)
            return HttpResponseRedirect(self.success_url)

        else : 
            return render(request,self.template_name,locals())




