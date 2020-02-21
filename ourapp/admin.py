from django.contrib import admin
from .models import user, subject, complement, exam, questions, answers, Q_Exam, result, tabel
# Register your models here.
admin.site.register(user)
admin.site.register(subject)
admin.site.register(complement)
admin.site.register(exam)
admin.site.register(questions)
admin.site.register(answers)
admin.site.register(Q_Exam)
admin.site.register(result)
admin.site.register(tabel)
