from django.contrib import admin
from .models import Question, Answer, Option

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # list_display = ['tittle', 'id']
    # search_fields = ['tittle','id']
    # list_per_page = 10
    ...

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # list_display = ['id']
    # search_fields = ['answer','id']
    # list_per_page = 10
    ...

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    ...