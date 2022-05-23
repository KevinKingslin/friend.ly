from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profilePicture = models.ImageField(upload_to='profilePictures/', null=True, blank=True)
    followerCount = models.IntegerField(default=0)
    followingCount = models.IntegerField(default=0)

class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id','following_user_id'],  name="unique_followers")
        ]
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"

class SearchHistory(models.Model):
    user_id = models.ForeignKey("User", related_name="searchhistory", on_delete=models.CASCADE)
    searched_user = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id','searched_user_id'],  name="unique_searches")
        ]
        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} searched {self.searched_user}"

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    description = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    edited = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add = True, editable=False)

    def __str__(self):
        return str(self.description)

class Like(models.Model):
    user_id = models.ForeignKey(User, related_name='likedBy', on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id} liked {self.post_id}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add = True, editable=False)