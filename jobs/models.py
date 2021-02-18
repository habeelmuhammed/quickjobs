from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField()
    password = models.CharField(max_length=250)

    def isExists(self):
        if Register.objects.filter(email=self.email):
            return True
        return False

    def isExists1(self):
        if Register.objects.filter(name=self.name):
            return True
        return False

    def m1(self):
        if Register.objects.filter(name=self.name):
            return True
        return False


class jobpro(models.Model):
    id = models.IntegerField(primary_key=True)
    location1 = models.CharField(max_length=250)
    jobdes = models.CharField(max_length=1000)
    jobimg = models.FileField()
    relation = models.ForeignKey(Register,on_delete=models.CASCADE)


class jobseek(models.Model):
    location2=models.CharField(max_length=250)
    relation2=models.ForeignKey(Register,on_delete=models.CASCADE)

class jobselection(models.Model):
    jobdes = models.CharField(max_length=1000)
    relation3 = models.ForeignKey(Register,on_delete=models.CASCADE)
