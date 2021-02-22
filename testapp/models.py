from django.db import models

class tb_content(models.Model):
    s_no = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    Title= models.CharField(max_length=1000)
    content= models.TextField()