from django.db import models
from django.db.models import CheckConstraint, Q


class Worker(models.Model):
    """Модель работника.
    #### Attrs:
    - name (str):
        Имя работника.
    - phone_number (str):
        Номер телефона.
    """

    name = models.CharField(max_length=255, verbose_name="Имя")
    phone_number = models.CharField(max_length=255, verbose_name="Номер телефона")

    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(phone_number__regex=r"[^\d\+\-]"),
                name="phone_number_valid_format",
            ),
        ]
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self) -> str:
        return self.name


class Store(models.Model):
    """Модель магазина.
    #### Attrs:
     - title(str)
     Название магазина.
     - worker(FK)
     Работник. Связь один ко многим к модели работника.
    """

    title = models.CharField(max_length=255, verbose_name="Магазин")
    worker = models.ForeignKey(
        Worker,
        on_delete=models.PROTECT,
        verbose_name="Работник",
        related_name="workers",
    )

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self) -> str:
        return self.title


class Visit(models.Model):
    """Модель посещения.
    #### Attrs:
     - visit_date(DateTime):
    Время посещения.
     - store(FK)
     Магазин. Связь один ко многим к моделью магазина.
     - lattitude(float)
     Широта.
     - longitude(float)
     Долгота.
    """

    visit_date = models.DateTimeField(verbose_name="Время посещения", auto_now_add=True)
    store = models.ForeignKey(
        Store, on_delete=models.PROTECT, verbose_name="Maгазины", related_name="stores"
    )
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"

    def __str__(self) -> str:
        formatted_date = self.visit_date.strftime("%Y-%m-%d %H:%M")
        return f"Посещение {self.store.title} в {formatted_date}"
