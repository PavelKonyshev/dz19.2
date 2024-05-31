from django.db import models
# Создание класса Категория
class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название категории",
    )
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


# Создание класса продукт
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="products/", blank=True, null=True, verbose_name="Фото продукта"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="Products",
    )
    price = models.IntegerField(
        verbose_name="Цена продукта",
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
    )
    updated_at = models.DateField(
        verbose_name="Дата изменения",
    )
    manufactured_at = models.DateField(
        verbose_name="Дата изготовления",
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.name} {self.description} {self.price}"

    class Meta:
        verbose_name = "Продукт"  # Настройка для наименования одного объекта
        verbose_name_plural = "Продукты"  # Настройка для наименования набора объектов
        ordering = ["name", "price"]




