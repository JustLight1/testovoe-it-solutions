from django.db import models


class Post(models.Model):
    title = models.CharField('Название', max_length=150)
    author = models.CharField('Автор', max_length=50)
    views_count = models.PositiveIntegerField('Количество просмотров',
                                              default=0)
    position = models.PositiveIntegerField('Позиция объявления', default=None)

    class Meta:
        ordering = ['position']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
