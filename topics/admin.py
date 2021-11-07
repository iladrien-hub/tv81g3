from django.contrib import admin
from .models import Student, ScientificDirector, BachelorTopic


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')


@admin.register(ScientificDirector)
class ScientificDirectorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')


@admin.register(BachelorTopic)
class BachelorTopicAdmin(admin.ModelAdmin):
    search_fields = ('title', 'year', )

    list_display = ('theme_title', 'students', 'director', 'year')
    ordering = ('title', 'year', 'director', )

    def students(self, obj):
        return ", ".join(f'{student.last_name} {student.first_name[0]}. {student.patronymic[0]}.' for student in obj.student_set.all())

    def theme_title(self, obj):
        return (obj.title[:75] + '..') if len(obj.title) > 75 else obj.title