from django.conf import settings
from django.db import models


class InterviewSession(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    role = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20, default="medium")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class QuestionAnswer(models.Model):
    session = models.ForeignKey(
        InterviewSession,
        on_delete=models.CASCADE,
        related_name="questions",
    )
    question = models.TextField()
    answer = models.TextField(blank=True)
    feedback = models.TextField(blank=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.question[:50]