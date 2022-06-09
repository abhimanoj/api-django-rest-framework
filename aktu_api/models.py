from django.db import models
import time
import calendar

class University(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
 
class Courses(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(University, related_name='creator', on_delete=models.CASCADE)
  
class Syllabuses(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    cource = models.ForeignKey(Courses, related_name='cource', on_delete=models.CASCADE)

class UserTable(models.Model):
    enrollment = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey(University, related_name='university', on_delete=models.CASCADE)
    syllabuse = models.ForeignKey(Syllabuses, related_name='syllabuse', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        
        # genrate primary_key
        gmt = time.gmtime()
        enrollment_id = calendar.timegm(gmt)
        enrollment_id = "enr-" + str(enrollment_id)

        self.enrollment = enrollment_id
        super(UserTable, self).save(*args, **kwargs)
   

