from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=200)

    def __str__(self):
        return self.name
    

class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=10)
    year=models.IntegerField()
    emp=models.ForeignKey(Emp, on_delete=models.CASCADE, default=0)


class Education(models.Model):
    ssc=models.IntegerField()
    hsc=models.IntegerField()
    grad=models.IntegerField()
    emp=models.OneToOneField(Emp, on_delete=models.CASCADE)


class Education2(Emp):
    ssc=models.IntegerField()
    hsc=models.IntegerField()
    grad=models.IntegerField()


class Project(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField(max_length=200)
    emp=models.ManyToManyField(Emp)

    def get_emplist(self):
        return ' , '.join([str(i) for i in self.emp.all()])
