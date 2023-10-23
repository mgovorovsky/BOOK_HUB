from django.db import models

# Create your models here.

class CopyrightHolder(models.Model):
    name = models.CharField(
        verbose_name="Copyright holder's name",
        unique=True,
        max_length=255
    )
    description = models.TextField(
        verbose_name="Copyright holder's description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}" 
    # def __str__(self):
    #     return f"CopyrightHolder {self.name} ({self.pk})" 


    def get_absolute_url(self):
        return f"/directories/copyrightholder/{self.pk}/"  

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

    copyright_holder = models.ForeignKey(
        "directories.CopyrightHolder",
        on_delete=models.PROTECT,
        verbose_name="Copyright holder name",
        related_name="author_names",
        null=True,
        blank=True

    )
    
    def __str__(self):
        return f"{self.name}"
    # def __str__(self):
    #     return f"Author {self.name} ({self.pk})"
    
    def get_absolute_url(self):
        return f"/directories/author/{self.pk}/"


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
        return f"{self.name}"  
    
    # def __str__(self):
    #     return f"Series {self.name} ({self.pk})"  

    def get_absolute_url(self):
        return f"/directories/series/{self.pk}/"      
    

class BookName(models.Model):
    name = models.CharField(
        verbose_name="Book name",
        max_length=255
    )

    author = models.ForeignKey(
        "directories.Author",
        on_delete=models.PROTECT,
        verbose_name="Author name",
        related_name="book_names"

    )

    series = models.ForeignKey(
        "directories.Series",
        on_delete=models.PROTECT,
        verbose_name="Series name",
        related_name="book_names",
        null=True,
        blank=True

    )

    genre = models.ForeignKey(
        "directories.Genre",
        on_delete=models.PROTECT,
        verbose_name="Genre name",
        related_name="book_names",
        null=True,
        blank=True

    )

    description = models.TextField(
        verbose_name="Book description",
        null=True,
        blank=True
    )

    price = models.DecimalField(
        verbose_name="Book price",
        max_digits=6,
        decimal_places=2,
        default=1
    )

    cover = models.ImageField(
        verbose_name="Order Cover",
        upload_to="order_images/%Y/%m/%d",
        default=1

    )

    def __str__(self):
        return f"{self.name}"
    
    # def __str__(self):
    #     return f"BookName {self.name} ({self.pk})"
    
    def get_absolute_url(self):
        return f"/directories/bookname/{self.pk}/" 


class Currency(models.Model):
    name = models.CharField(
        verbose_name="Currency name",
        unique=True,
        max_length=3
    )
    description = models.TextField(
        verbose_name="Currency description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"
    
    # def __str__(self):
    #     return f"Currency {self.name} ({self.pk})"
    
    def get_absolute_url(self):
        return f"/directories/currency/{self.pk}/"

class Rating(models.Model):
    name = models.IntegerField(
        verbose_name="Rating",
        unique=True,
    )

    def __str__(self):
        return f"{self.name}"
    
    # def __str__(self):
    #     return f"Rating {self.name} ({self.pk})"
    
    def get_absolute_url(self):
        return f"/directories/rating/{self.pk}/"

class AgeLimit(models.Model):
    name = models.CharField(
        verbose_name="Age limit",
        unique=True,
        max_length=3
    )

    def __str__(self):
        return f"{self.name}"
    
    # def __str__(self):
    #     return f"AgeLimit {self.name} ({self.pk})"
    
    def get_absolute_url(self):
        return f"/directories/agelimit/{self.pk}/"


# class PaymentSystem(models.Model):
#     name = models.CharField(
#         verbose_name="Payment system's name",
#         unique=True,
#         max_length=255
#     )
#     description = models.TextField(
#         verbose_name="Payment system's description",
#         null=True,
#         blank=True
#     )

#     def __str__(self):
#         return f"PaymentSystem {self.name} ({self.pk})"

class BookType(models.Model):
    name = models.CharField(
        verbose_name="Book type name",
        unique=True,
        max_length=255
    )
    description = models.TextField(
        verbose_name="Book type description",
        null=True,
        blank=True
    )

    # def __str__(self):
    #     return f"BookType {self.name} ({self.pk})"
    def __str__(self):
        return f"{self.pk}"
    
    def get_absolute_url(self):
        return f"/directories/booktype/{self.pk}/"


class Genre(models.Model):
    name = models.CharField(
        verbose_name="Genre name",
        unique=True,
        max_length=255
    )
    description = models.TextField(
        verbose_name="Genre description",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"
    
    # def __str__(self):
    #     return f"Genre {self.name} ({self.pk})"
    
    def get_absolute_url(self):
        return f"/directories/genre/{self.pk}/"


     