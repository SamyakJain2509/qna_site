from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    asker = models.ForeignKey(User, on_delete=models.CASCADE)
    date_asked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    date_answered = models.DateTimeField(auto_now_add=True)
    answerer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-date_answered',)

    def __str__(self):
        return f"Answer to '{self.question}'"

