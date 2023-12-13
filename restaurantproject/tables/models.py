from django.db import models


# Create your models here.
class Tables(models.Model):
    table_number = models.PositiveIntegerField(verbose_name='Номер столика')
    number_of_seats = models.PositiveIntegerField(verbose_name='Кількість місць')
    table_shape = models.CharField(max_length=70, verbose_name='Форма столика')
    coordinates_x = models.PositiveIntegerField(verbose_name='Координата по Х')
    coordinates_y = models.PositiveIntegerField(verbose_name='Координата по Y')
    table_width = models.PositiveIntegerField(verbose_name='Ширина')
    table_height = models.PositiveIntegerField(verbose_name='Довжина')

    def __str__(self):
        return str(self.table_number)


    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'


class Tables_orders(models.Model):
    date = models.DateField(verbose_name='Дата')
    table_number = models.PositiveIntegerField(verbose_name='Номер столика')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
