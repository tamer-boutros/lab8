from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.
def create(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
  contacts = Contact.objects.all().order_by('name','profession')
  form = ContactForm()
  return render(request, "create.html", {"form": form, "contacts":contacts})

def display(request):
  contacts = Contact.objects.all()
  return render(request, "display.html", {"contacts":contacts})

def display_sorted(request):
  contacts = Contact.objects.all().order_by('name','profession')
  return render(request, "display.html", {"contacts":contacts})

def edit(request, name):
  contact = Contact.objects.get(name=name)
  if request.method == "POST":
    form = ContactForm(request.POST, instance=contact)
    if form.is_valid():
      form.save()
  form = ContactForm(instance=contact)
  return render(request, "edit.html", {"form": form})
  # return redirect("main:display")

def delete(request, name):
  contact = Contact.objects.get(name=name)
  contact.delete()
  #return redirect("main:display")
  return render(request, "display.html")


def search_by_name(request, name):
  contacts = Contact.objects.filter(name__contains=name)
  return render(request, "display.html", {"contacts":contacts})

def search_by_phone(request, tel):
  contacts = Contact.objects.filter(telephone1__contains=tel)
  return render(request, "display.html", {"contacts":contacts})

def search_by_profession(request, profession):
  contacts = Contact.objects.filter(profession__contains=profession).order_by('name','profession')
  return render(request, "display.html", {"contacts":contacts})



def compare_fields(request, name1, name2):
  contact1 = Contact.objects.get(name=name1)
  contact2 = Contact.objects.get(name=name2)

  if contact1.profession == contact2.profession and contact1.telephone1 == contact2.telephone1 and contact1.telephone2 == contact2.telephone2:
    return render(request, "display.html", {"contact1":contact1, "contact2":contact2, "result":"True"})
  else:
    return render(request, "display.html", {"contact1":contact1, "contact2":contact2, "result":"False"})


def main(request):
    return render(request, 'mainmenu.html')
  
def bynamepage(request):
    return render(request, 'byname.html')

def bytelpage(request):
    return render(request, 'bytel.html')
  
def comparepage(request):
    return render(request, 'compare.html')
  
def byprofpage(request):
    return render(request, 'byprof.html')
  
  
  

