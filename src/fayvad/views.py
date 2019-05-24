from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ManageTransport(generic.TemplateView):
    template_name = "transport.html"

class ManageCommon(generic.TemplateView):
    template_name = "common.html"

class ManageDriving(generic.TemplateView):
    template_name = "driving.html"

class ManageRent(generic.TemplateView):
    template_name = "rent.html"
