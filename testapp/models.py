from django.db import models

class tb_content(models.Model):
    s_no = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    Title= models.CharField(max_length=1000)
    content= models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
#update goes here 7
# class tb_content(models.Model):
#     s_no = models.AutoField(primary_key=True)
#     userid = models.IntegerField()
#     user_name = models.CharField(max_length=1000)
#     profile_img = models.ImageField(upload_to="pics")
#     Title= models.CharField(max_length=1000)
#     content= models.TextField()
#     active = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, blank=True)
