from django.contrib import admin
from .models import Book,Genre,Language,Author,BookInstance

from datetime import date # to calculate due date

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

# Inline View for BookInstance

class BookInstanceInline(admin.TabularInline):
    extra = 0
    model=BookInstance

# List Display Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','isbn','display_genre','display_language')
    list_filter = ('author','language',)
    inlines = [BookInstanceInline]

admin.site.register(Book,BookAdmin)

# Inline View for Book
class BookInline(admin.TabularInline):
    extra = 0
    model = Book


#List Display Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
    list_filter = ('date_of_death',)
    fields = ['last_name','first_name',('date_of_birth','date_of_death')]
    inlines = [BookInline]
admin.site.register(Author,AuthorAdmin)


#List Display Book Copies

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','borrower','status','due_back')
    list_filter = ('status','due_back',)
    fieldsets = (('Book Details',{'fields':('book','borrower','imprint','id')}),
                 ('Availability',{'fields':('status','due_back')}),
                 )
admin.site.register(BookInstance,BookInstanceAdmin)