from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=40)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)  # Automatic save the date whenever the database is updated.
    slug = models.SlugField(db_index=True, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    # Build one to many relationship with Author model.
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)

    # Build many to many relationship with Tag model.
    tag = models.ManyToManyField(Tag)
