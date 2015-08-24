from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Details", {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    #diff.short_description = 'Last Modified'
    list_display = ('question_text', 'pub_date', 'diff')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
