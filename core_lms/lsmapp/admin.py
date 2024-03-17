from django.contrib import admin
from .models import Book,Author,Loan


class LoanAdmin(admin.ModelAdmin):
    empty_value_display = "None"
    list_display = [field.name for field in Loan._meta.fields if field.name != 'loan_id']
    fields = [field.name for field in Loan._meta.fields if field.name != 'loan_id'] 

class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = "None"
    list_display = [field.name for field in Author._meta.fields if field.name != 'author_id']
    fields = [field.name for field in Author._meta.fields if field.name != 'author_id']    

class BookAdmin(admin.ModelAdmin):
    empty_value_display = "None"
    list_display = [field.name for field in Book._meta.fields if field.name != 'book_id']
    fields = [field.name for field in Book._meta.fields if field.name != 'book_id']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Loan,LoanAdmin)
