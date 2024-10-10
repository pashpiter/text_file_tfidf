from django.db import models


class Document(models.Model):
    file = models.FileField(
        verbose_name='Обрабатываемый документ',
        upload_to='text_handler/'
    )
    name = models.CharField(
        verbose_name='Название документа',
        max_length=50,
        blank=False
    )


class Word(models.Model):
    word = models.CharField(
        verbose_name='Слово',
        max_length=20
    )
    count = models.IntegerField(
        verbose_name='Количество слов в тексте',
        default=1
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='word',
        verbose_name='Документ'
    )
