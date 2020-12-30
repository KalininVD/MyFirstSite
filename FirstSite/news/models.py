from django.db import models


class Articles(models.Model):
    title = models.CharField('Название статьи', max_length=50)
    company = models.CharField('Название компании', max_length=20, default='')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
