from catalog.models import *
genres=Genre.objects.all()
for i in range(50):
    b=Book.objects.create(title=f'book{i}',summary=f'sum{i}',isbn=f'isbn{i}')
    b.genre.set(genres)