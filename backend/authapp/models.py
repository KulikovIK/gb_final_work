from django.contrib.auth.models import AbstractUser
from django.db import models

NULLUBLE = {
    'blank': True,
    'null': True
}

class User(AbstractUser):
    
    phone = models.PositiveIntegerField(
            verbose_name='телефон',
            **NULLUBLE,
            )
    
    phone_code = models.PositiveSmallIntegerField(
            verbose_name='код телефона',
            default=0,
            )
    
    avatar = models.ImageField(
            verbose_name='аватар',
            )
    
    is_deleted = models.BooleanField(
            verbose_name='удален',
            default=False,
            )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        unique_together = ['phone_code', 'phone']

    def __repr__(self):
        return f'{self.pk} | {self.username}'

    def delete(self, *args, **kwargs):
        self.delete = True
        self.save()
