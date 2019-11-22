from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    reader = models.ForeignKey(
        'Reader', default=None, on_delete=models.SET_NULL, null=True,
    )

    def __str__(self):
        return '\'{}\' - {}'.format(self.title, self.author)

    class Meta:
        unique_together = ['title', 'author']


class Reader(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def list_of_books(self):
        books = Book.objects.filter(reader=self).values_list('title', 'author')
        return ['\'{title}\' - {author}'.format(
            title=title, author=author,
        ) for title, author in [book for book in books]]

    class Meta:
        unique_together = ['first_name', 'last_name']
