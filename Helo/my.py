from django.http import HttpResponse
from django.shortcuts import render



def ind(req):
    r=req.POST.get('textva',' ')
    chkbx=req.POST.get('chekva','band hai')
    chdr=req.POST.get('chekdruva','band hai')
    line=req.POST.get('newlineremove','band hai')
    sp=req.POST.get('spacerem','band hai')

    assign=''
    punc='.,;":-"'
    puc="'"
    

    if chkbx=='on':
        bmbuk=''
        for order in r:
            if order not in punc:
                bmbuk+=order
                assign=bmbuk
                
            else:
                pass
        dis=''
        for pak in assign:
            if pak not in puc:
                dis+=pak
                assign=dis
            else:
                pass
            
    else:
        assign=r

    
    
    dsign=''
    if chdr=='on':
        for dt in assign:
            dsign+=dt.upper()
            assign=dsign
    else:
        pass
    
    chsign=''
    if line =='on':
        for just in assign:
            if just!="\n" and just !="\r":
                chsign+=just
                assign=chsign
                
            else:
                chsign+=' '
                assign+=' '

    else:
        pass
    num=-1
    cooku=''
    if sp=='on':
        for s in assign:
            if s!=" ":
                cooku+=s
                assign=cooku
                num+=1 
            else:
                if assign[num]!=' ':
                    cooku+=' '
                    assign=cooku
                    num+=1
                else:
                    pass
    else:
        pass

    d={'name':assign}

    return render(req,'analyze.htm',d)


def ab(re):
    return render(re,'index.htm')