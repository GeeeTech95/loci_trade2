from django.core.exceptions import ObjectDoesNotExist

def core(request) :
    prepend = "https://" if request.is_secure() else "http://"
    host = request.get_host()
    #reg_link  = prepend + host + request.user.user_admin.reg_link
    ctx = {}
    if request.user.is_authenticated  and request.user.is_admin : 
        try : 
            reg_and_ref_link = prepend + host + request.user.user_admin.reg_and_ref_link
            ctx['reg_and_ref_link'] = reg_and_ref_link
           
        except  :
            pass
    else : pass
    ctx['site_name'] = "Loci Trade"
    ctx['site_email'] = "support@loci_trade.com"
    return ctx  


    
        