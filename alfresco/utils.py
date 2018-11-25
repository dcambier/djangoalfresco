from .models                 import Document
from django.contrib.auth     import logout
from django.http             import HttpResponseRedirect
from alfresco.authentication import get_ticket
from properties.p            import Property

def clear_database():
    for document in Document.objects.all():
        document.file.delete()
        document.delete()

def check_token(request):
    if request.user.is_authenticated:
        password = request.user.password
        response = get_ticket(password)

        if response.status_code != 200:
            return None
        else:
            return password
        
    else:
        return None

def percentage(percent, whole):
  return (percent * whole) / 100.0