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


class Series(models.Model):
    name = models.CharField(
        verbose_name="Series's name",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Series's description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Series {self.name} ({self.pk})"        
    

class BookName(models.Model):
    name = models.CharField(
        verbose_name="Books",
        max_length=255
    )

    author = models.ForeignKey(
        "directories.Author",
        on_delete=models.PROTECT,
        verbose_name="Author's name",
        related_name="book_names"

    )

    description = models.TextField(
        verbose_name="Book's description",
        null=True,
        blank=True
    )


    def __str__(self):
        return f"BookName {self.name} ({self.pk})"


class Currency(models.Model):
    name = models.CharField(
        verbose_name="Currency name",
        max_length=3
    )
    description = models.TextField(
        verbose_name="Currency descrnameiption",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Currency {self.name} ({self.pk})"

class Rating(models.Model):
    name = models.IntegerField(
        verbose_name="Rating",
    )

    def __str__(self):
        return f"Rating {self.name} ({self.pk})"

class AgeLimit(models.Model):
    name = models.CharField(
        verbose_name="Age limit",
        max_length=3
    )

    def __str__(self):
        return f"AgeLimit {self.name} ({self.pk})"


class PaymentSystem(models.Model):
    name = models.CharField(
        verbose_name="Payment system's name",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Payment system's description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"PaymentSystem {self.name} ({self.pk})"


class TextFormat(models.Model):
    name = models.CharField(
        verbose_name="Format name",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Format description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"TextFormat {self.name} ({self.pk})"


class BookType(models.Model):
    name = models.CharField(
        verbose_name="Book type name",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Book type description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"BookType {self.name} ({self.pk})"


class Genre(models.Model):
    name = models.CharField(
        verbose_name="Genre name",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Genre description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Genre {self.name} ({self.pk})"


class CopyrightHolder(models.Model):
    name = models.CharField(
        verbose_name="Copyright holder's name",
        max_length=255
    )
    description = models.TextField(
        verbose_name="Copyright holder's description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"CopyrightHolder {self.name} ({self.pk})"        