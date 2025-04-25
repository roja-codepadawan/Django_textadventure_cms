from django.contrib import admin
from .models import Story, Chapter, Choice, Variable

class ChoiceInline(admin.TabularInline):
    model = Choice
    fk_name = 'from_chapter'
    extra = 1

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'story', 'is_start')
    list_filter = ('story',)
    inlines = [ChoiceInline]

class VariableAdmin(admin.ModelAdmin):
    list_display = ('name', 'default_value', 'story')
    list_filter = ('story',)

admin.site.register(Story)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Choice)
admin.site.register(Variable, VariableAdmin)
