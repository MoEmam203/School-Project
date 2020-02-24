from django.contrib import admin
from .models import user, subject, complement, exam, questions, answers, Q_Exam, result, tabel

#Editing

class UserAdmin(admin.ModelAdmin):
    list_filter = ['level', 'f_name']
    list_display = ['u_id', 'f_name', 'l_name', 'level']


# Register your models here.
admin.site.register(user, UserAdmin)
admin.site.register(subject)
admin.site.register(complement)
admin.site.register(exam)
admin.site.register(questions)
admin.site.register(answers)
admin.site.register(Q_Exam)
admin.site.register(result)
admin.site.register(tabel)
