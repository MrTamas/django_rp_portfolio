from django.contrib import admin
from blog.models import Post, Category, Comment
from projects.models import Project
class PostAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	pass

class CommentAdmin(admin.ModelAdmin):
	pass

class ProjectAdmin(admin.ModelAdmin):
	pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)