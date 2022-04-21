from django.contrib import admin
from loginapp.models import Language,Book,BookInstance,Genre,Author

# Register your models here.
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
