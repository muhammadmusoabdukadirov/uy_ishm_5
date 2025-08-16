from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=220)

    def __str__(self):
        return self.title
    
    
class Author(models.Model):
    ism = models.CharField(max_length=220)
    bio = models.TextField()
    rasm = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.ism


class Book(models.Model):
    name = models.CharField(max_length=220)
    saxifa = models.PositiveIntegerField(null=True, blank=True)  # manfiy bo‘lmasin
    yili = models.PositiveIntegerField()  # faqat yil uchun
    text = models.TextField()
    views = models.PositiveIntegerField(default=0)  # manfiy bo‘lmasin
    narxi = models.PositiveIntegerField(default=0)  # manfiy bo‘lmasin
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books")
    rasm = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.narxi}"
