from django.views.generic import TemplateView

class FAQView(TemplateView):
   template_name = "templates/front/index.html"  # chemin vers le template à afficher