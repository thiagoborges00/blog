from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status','created','publish','author')
    #search_fields = ('title','body')  barra de pesquisa
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',) # permite pesquisar autor pelo id do autor
    date_hierarchy = 'publish' #links navegaveis de data
    ordering = ('status','publish')
