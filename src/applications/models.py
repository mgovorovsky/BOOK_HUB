from django.db import models
from django.contrib.auth import get_user_model
from django.urls import path, include, reverse_lazy

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Customer",
        on_delete=models.PROTECT
    )

    order_bookname = models.ForeignKey(
        "directories.BookName",
        verbose_name="Book name",
        on_delete=models.PROTECT
    )

    summ  = models.DecimalField(
        verbose_name="Order summ",
        max_digits=6,
        decimal_places=2
    )

    order_currency = models.ForeignKey(
        "directories.Currency",
        verbose_name="Currency",
        on_delete=models.PROTECT
    )

    cover = models.ImageField(
        verbose_name="Order Cover",
        upload_to="order_images/%Y/%m/%d",

    )

# доп. разерешине
    class Meta:
        permissions =[
            ("Вася-Петря", "Vasia and Pethja")

        ]

    def __str__(self) -> str:
        return f"Order for User { self.user.username } {self.summ} {self.order_currency.name}"

    # используется для всех view одинаковый
    def get_absolute_url(self):
        return reverse_lazy("applications:order_detail", kwargs={"pk": self.pk}) # замена ссылки на постоянную

        # return f"/applications/order/{self.pk}/"



    # name = models.CharField(
    #     verbose_name="Author's name",
    #     max_length=255
    # )
    # description = models.TextField(
    #     verbose_name="Autor's description",
    #     null=True,
    #     blank=True
    # )

    # def __str__(self):
    #     return f"Author {self.name} ({self.pk})"