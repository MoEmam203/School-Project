from django.db import models

# Create your models here.
# UserTabel
class user(models.Model):
    BLOOD_TYPE=(
    ('a-','A-'),
    ('a+','A+'),
    ('b+','B+'),
    ('b-','B+'),
    ('o+','O+'),
    ('o-','O-'),
    ('ab+','AB+'),
    ('ab-','AB-'),
    )

    HUMAN_TYPE=(
    ('m','Male'),
    ('f','Female'),
    )

    u_id        = models.IntegerField()
    f_name      = models.CharField(max_length=100)
    l_name      = models.CharField(max_length=100)
    password    = models.CharField(max_length=50)
    email       = models.EmailField(blank=True)
    phone_number= models.CharField(max_length=11)
    address     = models.CharField(max_length=50)
    dob         = models.DateField()
    blood_type  = models.CharField(max_length=3, choices=BLOOD_TYPE)
    img         = models.ImageField(upload_to='User_Pics',blank=True)
    job         = models.CharField(max_length=20,blank=True)
    age         = models.IntegerField(default=7)
    type        = models.CharField(max_length=10,choices=HUMAN_TYPE)


    def __str__(self):
        return str(self.u_id)+"- "+self.f_name+" "+self.l_name


#SubjectsTabel
class subject(models.Model):
    code        = models.CharField(max_length=10,primary_key=True)
    name        = models.CharField(max_length=50)
    description = models.TextField()
    date        = models.DateField()
    order       = models.IntegerField()
    user_id     = models.IntegerField()

    def __str__(self):
        return self.code+" "+self.name


#ComplementTabel
class complement(models.Model):
    c_id        = models.IntegerField()
    title       = models.CharField(max_length=50)
    content     = models.TextField()
    user_id     = models.IntegerField()

    def __str__(self):
        return self.title


#ExamTabel
class exam(models.Model):
    e_id        = models.IntegerField(primary_key=True)
    subject_id  = models.IntegerField()
    title       = models.CharField(max_length=50)

    def __str__(self):
        return str(self.e_id)


#QuestionsTabel
class questions(models.Model):
    q_id        = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=50)
    describe    = models.CharField(max_length=100)
    img         = models.ImageField(upload_to='Q_Pics')

    def __str__(self):
        return str(self.q_id)


#AnswersTabel
class answers(models.Model):
    ANSWER_TYPE=(
    ('a','a'),
    ('b','b'),
    ('c','c'),
    ('d','d'),
    )

    a_id        = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=50)
    q_id        = models.IntegerField()
    type        = models.CharField(max_length=50,choices=ANSWER_TYPE)

    def __str__(self):
        return str(self.a_id)



#Questions-Exam Tabel
class Q_Exam(models.Model):
    e_id        = models.IntegerField()
    q_id        = models.IntegerField()

    def __str__(self):
        return str(self.e_id)+" "+str(self.q_id)


#ResultTabel
class result(models.Model):
    r_id        = models.IntegerField()
    exam_id     = models.IntegerField()
    student_id  = models.IntegerField()
    result      = models.IntegerField()

    def __str__(self):
        return str(self.r_id)+" "+str(self.student_id)


#Tabels Tabel
class tabel(models.Model):
    Type=(
    ('B','Basic'),
    ('S','Spare'),
    )
    t_id        = models.IntegerField()
    date        = models.DateField()
    order       = models.IntegerField()
    sub_id      = models.IntegerField()
    e_id        = models.IntegerField()
    type        = models.CharField(max_length=10,choices=Type)


    def __str__(self):
        return str(self.t_id)
