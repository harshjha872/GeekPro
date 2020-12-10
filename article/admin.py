from django.contrib import admin

# Register your models here.


from .models import Article,Contact

admin.site.register(Article)
admin.site.register(Contact)