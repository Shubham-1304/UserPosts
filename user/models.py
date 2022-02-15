from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=100,)
    last_name=models.CharField(max_length=100,)
    email=models.CharField(max_length=200,)
    password=models.CharField(max_length=100)
    username=models.CharField(max_length=100,)

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self) -> str:
        return self.text