from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10, blank=False)
    useremail = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.username


class Todo(models.Model):
    fk_user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="작성자", default=""
    )
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=100, blank=False)
    is_completed = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    fk_username = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="작성자", default=""
    )
    fk_todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE, verbose_name="할일", default=""
    )
    contents = models.TextField(max_length=50, blank=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.contents
