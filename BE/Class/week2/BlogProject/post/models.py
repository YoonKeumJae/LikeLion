# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# class Blog(models.Model):
#     blogName = models.CharField(max_length=20)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.blogName

# class Category(models.Model):
#     categoryName = models.CharField(max_length=20)
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.categoryName

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.title

# class Tag(models.Model):
#     tagName = models.CharField(max_length=20)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.tagName

# class TagPost(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)

# class Comment(models.Model):
#     comment = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     #cascade: 탈퇴 시(삭제 시) 다 날아감
#     def __str__ (self):
#         return self.comment

#     """
#     foreignkey에서 매개변수가 두개 있어야 한다는데, cascade를 꼭 줘야하나? 다른거 안됨?
#     """
