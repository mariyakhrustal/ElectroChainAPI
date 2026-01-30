from django.db import models


class Network(models.Model):
    """
    Представляет звено торговой сети электроники.
    Уровень (level) рассчитывается автоматически в методе save() на основе иерархии поставщиков.
    """

    name = models.CharField(
        max_length=350, help_text="Введите название звена сети", verbose_name="Название звена сети"
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clients",
        help_text="Укажите поставщика",
        verbose_name="Поставщик",
    )
    debt = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Укажите задолженность перед поставщиком",
        verbose_name="Задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Укажите время создания", verbose_name="Время создания"
    )
    level = models.PositiveIntegerField(editable=False, default=0, verbose_name="Уровень поставщика в иерархии")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    def save(self, *args, **kwargs):
        """
        Рассчитывает уровень иерархии перед сохранением:
        если поставщик отсутствует — уровень 0, иначе уровень поставщика + 1.
        """
        if self.supplier:
            self.level = self.supplier.level + 1
        else:
            self.level = 0
        super().save(*args, **kwargs)


class Contact(models.Model):
    """Представляет контактные данные звена торговой сети электроники."""

    email = models.EmailField(max_length=150, help_text="Введите почту", verbose_name="Почта")
    country = models.CharField(max_length=100, help_text="Введите страну", verbose_name="Страна")
    city = models.CharField(max_length=100, help_text="Введите город", verbose_name="Город")
    street = models.CharField(max_length=100, help_text="Введите улицу", verbose_name="Улица")
    house_number = models.CharField(max_length=20, help_text="Введите номер дома", verbose_name="Номер дома")
    network = models.OneToOneField(
        Network,
        on_delete=models.CASCADE,
        related_name="contact",
        help_text="Введите звено сети",
        verbose_name="Звено сети",
    )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"


class Product(models.Model):
    """Представляет товар звена торговой сети электроники."""

    name = models.CharField(max_length=350, help_text="Введите название продукта", verbose_name="Название продукта")
    model = models.CharField(
        max_length=350, help_text="Введите модель продукта", verbose_name="Название модели продукта"
    )
    release_date = models.DateField(
        help_text="Укажите дату выхода продукта на рынок", verbose_name="Дата выхода продукта на рынок"
    )
    network = models.ForeignKey(
        Network,
        on_delete=models.CASCADE,
        related_name="products",
        help_text="Введите звено сети",
        verbose_name="Звено сети",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
