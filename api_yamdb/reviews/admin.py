from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Comment, Genre, GenreTitle, Review, Title, User


class UserResourse(resources.ModelResource):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name'
        )
        export_order = (
            'id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name'
        )


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResourse
    list_display = (
        'id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name'
    )


class TitleResourse(resources.ModelResource):

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'category')
        export_order = ('id', 'name', 'year', 'category')


class TitleAdmin(ImportExportModelAdmin):
    resource_class = TitleResourse
    list_display = ('id', 'name', 'year', 'category')


class CategoryResourse(resources.ModelResource):

    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResourse
    list_display = ('name', 'slug')


class GenreResourse(resources.ModelResource):

    class Meta:
        model = Genre


class GenreAdmin(ImportExportModelAdmin):
    resource_class = GenreResourse
    list_display = ('name', 'slug')


class ReviewResourse(resources.ModelResource):
    title = fields.Field(attribute='title_id', column_name='title_id')

    class Meta:
        model = Review
        fields = ('id', 'title', 'text', 'author', 'score', 'pub_date')
        export_order = ('id', 'title', 'text', 'author', 'score', 'pub_date')


class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResourse
    list_display = ('id', 'title', 'text', 'author', 'score', 'pub_date')


class CommentResourse(resources.ModelResource):
    review = fields.Field(attribute='review_id', column_name='review_id')

    class Meta:
        model = Comment
        fields = ('id', 'review', 'text', 'author', 'pub_date')
        export_order = ('id', 'review', 'text', 'author', 'pub_date')


class CommentAdmin(ImportExportModelAdmin):
    resource_class = CommentResourse
    list_display = ('id', 'review', 'text', 'author', 'pub_date')


class GenreTitleResourse(resources.ModelResource):
    title = fields.Field(attribute='title_id', column_name='title_id')
    genre = fields.Field(attribute='genre_id', column_name='genre_id')

    class Meta:
        model = GenreTitle


class GenreTitleAdmin(ImportExportModelAdmin):
    resource_class = GenreTitleResourse


admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(GenreTitle, GenreTitleAdmin)
admin.site.register(User, UserAdmin)
