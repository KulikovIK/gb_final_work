from django.db import models
from authapp.models import User, NULLABLE

class Message(models.Model):

    from_user = models.ForeignKey(
            verbose_name='от кого',
            related_name='from_user',
            to=User,
            on_delete=models.CASCADE,
            )

    to_user = models.ForeignKey(
            verbose_name='кому',
            related_name='to_user',
            to=User,
            on_delete=models.CASCADE
            )

    title = models.CharField(
            verbose_name='заголовок',
            max_length=180
            )

    message_text = models.TextField(
            verbose_name='текст сообщения',
            **NULLABLE,
            )
    
    created_at = models.DateTimeField(
            verbose_name='дата создания',
            auto_now_add=True,
            )

    is_deleted = models.BooleanField(
            verbose_name='удалено',
            default=False
            )

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['is_deleted', 'created_at']

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
    
