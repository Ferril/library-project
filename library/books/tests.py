from rest_framework.test import APITestCase
from library.books.models import Book, Reader


class BookAPITestCase(APITestCase):

    def setUp(self):

        self.url = 'http://127.0.0.1:8000/api/books/'
        self.title = 'test_title'
        self.author = 'test_author'
        self.data = {
            'book':
                {
                 'title': self.title,
                 'author': self.author,
                },
        }

        self.reader = Reader.objects.create(
            first_name='reader1',
            last_name='reader1',
        )

        Book.objects.bulk_create(
            [
                Book(
                    title='{title}{part}'.format(title=self.title, part=part),
                    author=self.author,
                    reader=self.reader,
                )
                for part in range(5)
            ]
        )

    def test_create(self):
        response = self.client.post(self.url, self.data, format='json')
        book = Book.objects.get(title=self.title, author=self.author)

        self.assertEqual(response.status_code, 201)
        self.assertEqual((book.title, book.author), (self.title, self.author))

    def test_read(self):
        books = Book.objects.all().count()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(books, len(response.json()))

    def test_update(self):
        book_to_update = Book.objects.all().first()
        book_to_update.reader = None
        book_to_update.save()

        self.assertEqual(book_to_update.reader, None)

        new_title = 'new_test_title'
        upd_data = {
            'book': {
                'title': new_title,
                'author': book_to_update.author,
                'reader': self.reader.id,
            },
        }
        url = '{url}{id}'.format(url=self.url, id=book_to_update.id)
        response = self.client.put(url, upd_data, format='json')
        updated_book = Book.objects.get(id=book_to_update.id)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(updated_book.title, new_title)
        self.assertEqual(
            updated_book.reader.first_name, self.reader.first_name,
        )

    def test_delete(self):
        book_to_delete = Book.objects.all().first()
        books_count = Book.objects.all().count()
        url = '{url}{id}'.format(url=self.url, id=book_to_delete.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

        deleted_book = Book.objects.filter(id=book_to_delete.id)
        self.assertEqual(len(deleted_book), 0)

        books_new_count = Book.objects.all().count()
        self.assertEqual(books_count - books_new_count, 1)


class ReaderAPITestCase(APITestCase):

    def setUp(self):

        self.url = 'http://127.0.0.1:8000/api/readers/'
        self.reader_first_name = 'reader'
        self.reader_last_name = 'readerovich'
        self.data = {
            'reader':
                {
                 'first_name': self.reader_first_name,
                 'last_name': self.reader_last_name,
                },
        }

        self.reader = Reader.objects.create(
            first_name='reader1',
            last_name='reader1',
        )

        Reader.objects.bulk_create(
            [
                Reader(
                    first_name='{reader_first_name}{num}'.format(
                        reader_first_name=self.reader_first_name, num=num,
                    ),
                    last_name=self.reader_last_name,
                )
                for num in range(5)
            ],
        )

    def test_create(self):
        response = self.client.post(self.url, self.data, format='json')
        reader = Reader.objects.get(
            first_name=self.reader_first_name, last_name=self.reader_last_name,
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            (reader.first_name, reader.last_name),
            (self.reader_first_name, self.reader_last_name),
        )

    def test_read(self):
        readers = Reader.objects.all().count()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(readers, len(response.json()['readers']))

    def test_update(self):
        reader_to_update = Reader.objects.all().first()
        new_name = 'new_reader_name'
        upd_data = {
            'reader': {
                'first_name': new_name,
                'last_name': self.reader_last_name,
            }
        }
        url = '{url}{id}'.format(url=self.url, id=reader_to_update.id)
        response = self.client.put(url, upd_data, format='json')
        updated_reader = Reader.objects.get(id=reader_to_update.id)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(updated_reader.first_name, new_name)

    def test_delete(self):
        reader_to_delete = Reader.objects.all().first()
        readers_count = Reader.objects.all().count()
        url = '{url}{id}'.format(url=self.url, id=reader_to_delete.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

        deleted_reader = Reader.objects.filter(id=reader_to_delete.id)
        self.assertEqual(len(deleted_reader), 0)

        reader_new_count = Reader.objects.all().count()
        self.assertEqual(readers_count - reader_new_count, 1)
