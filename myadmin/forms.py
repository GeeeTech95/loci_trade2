from django.forms import ModelForm
from django import forms
from wallet.models import Transaction
from .models import Settings

class SettingsForm(ModelForm) :
    
    class Meta() :
        model = Settings
        exclude = ['admin']


class SendMailForm(forms.Form)  :

    def __init__(self,*args, **kwargs) :  
        """ admin is a user instance of the admin"""
        super(SendMailForm,self).__init__(*args, **kwargs)

    #users  = forms.ModelMultipleChoiceField(queryset=myadmin.users.all(),help_text="You can select one or multiple users")
    subject = forms.CharField(required = True,help_text="topic of email") 
    message = forms.CharField(required = True,widget=forms.Textarea)        


class TransactionForm(ModelForm) :
    def __init__(self, admin=None,update=False,*args, **kwargs) :   
        choices = (('BONUS','BONUS'),('AIR DROP','AIR DROP'),('REFERAL EARNING','REFERAL EARNING'))
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.admin = admin
        if admin : 
            self.fields['user'] = forms.ModelChoiceField(admin.users.all() )
            self.fields['transaction_type'] = forms.ChoiceField(choices= choices)
    
    
    send_transaction_email = forms.BooleanField(help_text = "we would send a transaction email,if you leave tick this ")

    class Meta() :
        model = Transaction 
        fields = ['user','transaction_type','amount','description']   



    #class DeleteCoinForm(forms.Form) :
    #pin = forms.CharField()
    #pk = forms.CharField()