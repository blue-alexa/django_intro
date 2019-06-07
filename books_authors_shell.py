from apps.books_and_authors_app.models import Books, Authors

# create 5 books
Books.objects.create(title="C Sharp", desc="")
Books.objects.create(title="Java", desc="")
Books.objects.create(title="Python", desc="")
Books.objects.create(title="PHP", desc="")
Books.objects.create(title="Ruby", desc="")

# create 5 authors
Authors.objects.create(first_name="Jane", last_name="Austen")
Authors.objects.create(first_name="Emily", last_name="Dickinson")
Authors.objects.create(first_name="Fyodor", last_name="Dostoevksy")
Authors.objects.create(first_name="William", last_name="Shakespeare")
Authors.objects.create(first_name="Lau", last_name="Tzu")

# change the name of the C Sharp to C#
book = Books.objects.get(title="C Sharp")
book.title = "C#"
book.save()

# change the first name of the 4th author to Bill
author = Authors.objects.all()[3]
author.first_name = "Bill"
author.save()

# Assign the first author to the first 2 books
author = Authors.objects.all()[0]
book1 = Books.objects.all()[0]
book2 = Books.objects.all()[1]
author.books.add(book1)
author.books.add(book2)

# Assign the second author to the first 3 books
author = Authors.objects.all()[1]
for book in Books.objects.all()[:3]:
    author.books.add(book)

# Assign the third author to the first 4 books
author = Authors.objects.all()[2]
for book in Books.objects.all()[:4]:
    author.books.add(book)

# Assign the fourth author to the first 5 books
author = Authors.objects.all()[3]
for book in Books.objects.all()[:5]:
    author.books.add(book)

# Retrieve all the authors for the 3rd book
Books.objects.all()[2].authors.all()

# Remove the first author of the 3rd book
book = Books.objects.all()[2]
author = book.authors.first()
book.authors.remove(author)

# Add the 5th author as one of the authors of the 2nd book
book = Books.objects.all()[1]
book.authors.add(Authors.objects.all()[4])

# Find all the books that the 3rd author is part of
author = Authors.objects.all()[2]
Books.objects.filter(authors__in=[author])

# Find all the authors that contribute to the 5th book
Books.objects.all()[4].authors.all()



































