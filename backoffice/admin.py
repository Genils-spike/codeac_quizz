from django.contrib import admin
from .models import User_profil, Quizz, Question, Answer, Tag

admin.site.register(Quizz)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User_profil)