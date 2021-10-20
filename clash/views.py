from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.checks import messages
import re

def result(request):
    
        if(request.method == "POST"):
            input = request.POST['input']
            formating_choice = request.POST['category']
            if(formating_choice == 'num'):
                pattern = re.compile(r'[1-9]\d[1-9]\d*|[1-9]\d\d\d+')
            elif(formating_choice == 'date'):
                pattern = re.compile(r'([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])')
            elif(formating_choice == 'quote'):
                pattern = re.compile(r"'(.*)'")
            elif(formating_choice == 'ipadd'):
                pattern = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
                match = pattern.findall(input)[0]
                if(0<=int(match[0:3])<=127):
                    return render(request,'clash/result.html',{
                        'addr':match,'class':'class A'
                    })
                elif(128<=int(match[0:3])<=191):
                    return render(request,'clash/result.html',{
                        'addr':match,'class':'class B'
                    })
                elif(192<=int(match[0:3])<=223):
                    return render(request,'clash/result.html',{
                        'addr':match,'class':'class C'
                    })
                elif(224<=int(match[0:3])<=239):
                    return render(request,'clash/result.html',{
                        'addr':match,'class':'class D'
                    })
                elif(240<=int(match[0:3])<=255):
                    return render(request,'clash/result.html',{
                        'addr':match,'class':'class E'
                    })
                else:
                    return render(request,'clash/result.html',{
                        'class':'Input ivalid select proper category.'
                    })
            elif(formating_choice == "macadd"):
                pattern = re.compile(r'[A-F0-9a-f]{2}[-:][A-F0-9a-f]{2}[-:][A-F0-9a-f]{2}[-:][A-F0-9a-f]{2}[-:][A-F0-9a-f]{2}[-:][A-F0-9a-f]{2}')
            elif(formating_choice == "snake"):
                def func(x):
                    char = x.group(0)
                    return "_"+char.lower()
                pattern = re.compile(r'([A-Z])')
                match = pattern.sub(func,input)
                return render(request,'clash/result.html',{'class':match})
            match = pattern.findall(input)
            if(len(match) == 0):
                return render(request,'clash/result.html',{'class':'Input ivalid select proper category.'})
            return render(request,"clash/result.html",{'output':match})
        return render(request, "clash/result.html")

        

