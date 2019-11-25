from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    reader = models.ForeignKey(
        'Reader', default=None, on_delete=models.SET_NULL, null=True,
    )

    def __str__(self):
        return '\'{title}\' - {author}'.format(
            title=self.title, author=self.author,
        )

    class Meta:
        unique_together = ['title', 'author']


class Reader(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name,
        )

    @property
    def list_of_books(self):
        books = Book.objects.filter(reader=self).values_list('title', 'author')
        return ['\'{title}\' - {author}'.format(
            title=title, author=author,
        ) for title, author in list(books)
        ]

    class Meta:
        unique_together = ['first_name', 'last_name']
