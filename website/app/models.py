from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followee")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    
    def __str__(self) -> str:
        return f"{self.user} {self.follower}"
    

class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender")
    to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reciever")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.from_user} {self.to_user}"
    
    