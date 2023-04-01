from django.db import models


class Station(models.Model):
    name = models.CharField('Название станции', max_length=255)
    url_free = models.CharField('URL потока для бесплатной версии', max_length=255, null=True, blank=True)
    url_paid = models.CharField('URL потока для платной версии', max_length=255, null=True, blank=True)
    order = models.PositiveIntegerField('Порядковый номер', null=True)
    paid = models.BooleanField('Платная станция', default=False)
    active = models.BooleanField('Активная станция', default=True,
                                 help_text='Если станция неактивна, она не будет возвращаться в запросе')

    miniature = models.ImageField('Изображение миниатюры', upload_to='images/', null=True, blank=True)
    bg_image = models.ImageField('Изображение для фона', upload_to='images/', null=True, blank=True)
    poster = models.ImageField('Обложка', upload_to='images/', null=True, blank=True)
    buy_trek = models.FileField('Трек перед покупкой', upload_to='files/', null=True, blank=True)

    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order',)


class Track(models.Model):
    name = models.CharField('Название трека', max_length=255)
    file = models.FileField('Файл', upload_to='tracks/', null=True, blank=True)

    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

