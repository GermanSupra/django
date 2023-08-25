from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2
    )

    auction = models.BooleanField(
        verbose_name="Торг",
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редоктирования"
    )
    user = models.ForeignKey(
        to=User,
        verbose_name="пользователь",
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="advertisements/",
        verbose_name="изображение",
    )

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )

        return self.created_at.strftime("%d.%m.%y в %H:%M")

    @admin.display(description="Дата обновления")
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: blue; font-weight": bold;>Обновлено в {}</span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%y в %H:%M")

    @admin.display(description="Фотография")
    def show_image(self):
        if self.image:
            return format_html(
                '<img src={} style="width: 40px; height: 40px;"/>', self.image.url
            )
        else:
            return format_html(
                '<span style="color: red;">Нету фото<span/>'
            )

    def __str__(self):
        return f"id {self.id} title {self.title} price {self.price}"

    class Meta:
        db_table = "advertisement"
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
