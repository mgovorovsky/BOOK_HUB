from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        verbose_name="Author's name",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Autor's description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Author {self.name} ({self.pk})"
    

class BookName(models.Model):
    name = models.CharField(
        verbose_name="Book's name",
        max_length=255
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        verbose_name="Author's name",

    )

    description = models.TextField(
        verbose_name="Book's description",
        null=True,
        blank=True
    )


    def __str__(self):
        return f"BookName {self.name} ({self.pk})"