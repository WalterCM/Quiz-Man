from django.contrib import admin

from .models import Exam, Question, Choice, Tag

class ExamQuestionInline(admin.TabularInline):
    model = Question.exam.through
    extra = 0

class ExamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['exam_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ExamQuestionInline,]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class QuestionTagInline(admin.TabularInline):
    model = Tag.question.through
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline, QuestionTagInline]

admin.site.register(Tag)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Exam, ExamAdmin)
