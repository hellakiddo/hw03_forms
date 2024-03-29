from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    """ ORM модель групп """
    title = models.CharField('Название группы', max_length=200)
    slug = models.SlugField('URL адрес', default='some string',
                            unique=True)
    description = models.TextField('Описание группы',
                                   max_length=10000,
                                   default='some string', )

    class Meta:
        """ Отображение в админке """
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'
        ordering = ('-title',)

    def __str__(self):
        return self.title


class Post(models.Model):
    """ ORM модель постов """
    text = models.TextField('Текст поста', max_length=15000)
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор')
    group = models.ForeignKey(Group, blank=True, null=True,
                              on_delete=models.SET_NULL,
                              related_name='posts',
                              verbose_name='Группа')

    class Meta:
        """ Отображение в админке """
        ordering = ('-pub_date',)
        verbose_name_plural = 'Сортировка по дате публикации'

    def __str__(self):
        return self.text[0:30]
