from django.db import models


# Create your models here.

class All_books(models.Model):
    book_id = models.CharField(max_length=10)
    book_name = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.book_name


class All_users(models.Model):
	username=models.CharField(max_length=50)
	email=models.EmailField()
	password=models.CharField(max_length=50)

	def __str__(self):
		return self.username
