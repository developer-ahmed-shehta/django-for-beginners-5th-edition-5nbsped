from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    context = {  # new
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }

    return render(request,"CompanyWebsite/home.html",context)

class AboutPageView(TemplateView): # new
    template_name = "CompanyWebsite/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context
