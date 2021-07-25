from django.views.generic import CreateView,View,TemplateView,ListView,DetailView
from django.views.generic.edit import  DeleteView,UpdateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from .models import WalletAddress
from .dashboard import AdminBase
from .forms import TransactionForm
from wallet.models import Transaction, Wallet
from core.mail import Email




class CreateTransaction(AdminBase,CreateView) :
    model = Transaction
    template_name = 'form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('admin-dashboard')

    def get(self,request,*args,**kwargs) :
        try :
            user = Wallet.objects.get(wallet_id = kwargs.get('wallet_id',None))
        except :
            return HttpResponse("Invalid request")    
        form = self.form_class(admin=request.user,initial = {'user' : user,'status' : 'Approved'})
        form_title = "Create Transaction"
        return render(request,self.template_name,locals())

    def post(self,request,*args,**kwargs) :
        form = self.form_class(admin=request.user,data=request.POST) 
        if form.is_valid() :
            form.save(commit  = False) 
            user = form.cleaned_data['user']
            user.user_wallet.funded_earning =+ form.cleaned_data['amount']
            user.save() 
            form.instance.status  = "Approved"
            transact = form.save()
            if form.cleaned_data['send_transaction_email'] or self.admin.enable_transaction_emails :
                mail = Email(send_type = "alert")
                mail.transaction_email(transact)
            return HttpResponseRedirect(self.success_url)

        else :
            form = self.form_class(admin=request.user,initial = {'user' : request.user,'status' : 'Approved'})
            return render(request,self.template_name,locals())    
    


class TransactionHistory(ListView) :
    model = Transaction
    context_object_name = 'transaction_history'
    template_name = 'transaction-history.html'

    def get_queryset(self) :
        return self.model.objects.filter(user__admin = self.request.user).order_by('-date')
