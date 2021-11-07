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

    list_display = ('title', 'students', 'director', 'year')
    ordering = ('title', 'year', 'director', )

    def students(self, obj):
        return ", ".join(str(student) for student in obj.student_set.all())