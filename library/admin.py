from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['book_name','author','quantity']
    
    
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_select_related=['user']
    list_display=['roll','first_name','last_name','session','phone']
    
@admin.register(models.Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display=['student','book','issue_date','return_date']
    
    
@admin.register(models.BorrowRequest)
class BorrowRequestAdmin(admin.ModelAdmin):

    list_display=['student','book','request_date','status']
    list_editable=['status']
    

