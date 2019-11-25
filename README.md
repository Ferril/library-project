# Description

It's a simple library application in the style of ReST Api. Implements CRUD database operation via ReST.
Contains Book and Reader models. Book could be assigned to a reader.

# CRUD app

The app consists of three microservices.

- The application server is written in Django and DRF. 
Gunicorn python WSGI HTTP server is used to connect the proxy server to the application server.

- Proxy server on nginx with basic settings.
 
- PostgreSQL database.

# Build and run

- Clone the repository to your computer.
- Configure `.env.dev` and rename to `.env`.
- From the root directory of the project, run `docker-compose build`.
- Start docker-compose `docker-compose up -d`
- The app is ready to use.

# How to use

API url - `http://localhost:8000/api/`
### Endpoints:
- `books/` - POST - adds a new book to db. 
Format - {'book': {'title': book_title, 'author': book_author, 'description': (can be empty), 'reader': reader_id (can be empty)}}
- `books/` - GET - returns a list of books and their assignment to readers. Use header 'Accept: text/csv' to return data in csv format, otherwise it returns json.
- `books/book_id` - PUT, DELETE - changes/deletes selected book.
- `readers/` - POST - adds a new reader to db. 
Format - {'reader' : {'first_name': first_name, 'last_name': last_name}}
- `readers/` - GET - returns a list of readers in json format.
- `readers/reader_id` - PUT, DELETE - changes/deletes selected reader.

### Example

`curl -X GET --header 'Accept: text/csv' 'http://localhost:8000/api/books/'`
