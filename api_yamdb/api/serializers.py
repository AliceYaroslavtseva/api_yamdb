import re

from rest_framework import serializers
from django.core.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from reviews.models import Category, Comment, Genre, Review, Title, User


class SingUpSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)

    class Meta:
        model = User
        fields= ('username', 'email')

    def validate_username(self, value):
        if not re.fullmatch(r'^[\w.@+-]+', value):
            raise serializers.ValidationError('Nickname должен содержать буквы,'
                                               'цифры и символы @.+-_')
        if value == 'me':
            raise serializers.ValidationError('Недопустимое имя "me"')
        return value

    def validate(self, data):
        user_if = User.objects.filter(username=data['username']).exists()
        email_if  = User.objects.filter(email=data['email']).exists()
        if user_if:
            if not email_if:
                raise serializers.ValidationError('Имя уже использовалась')
        if email_if:
            if not user_if:
                raise serializers.ValidationError('Почта уже использовалось')
        if User.objects.filter(username=data['username'], email=data['email']).exists():
            return data
        return data


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UsersViewSerializer(serializers.ModelSerializer):

    def validate_username(self, value):
        if not re.fullmatch(r'^[\w.@+-]+', value):
            raise serializers.ValidationError('Nickname должен содержать буквы,'
                                               'цифры и символы @.+-_')
        return value

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class MeSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(read_only=True)

    def validate_username(self, value):
        if not re.fullmatch(r'^[\w.@+-]+', value):
            raise serializers.ValidationError('Nickname должен содержать буквы,'
                                               'цифры и символы @.+-_')
        return value

    class Meta:
        model = User
        fields = ('username', 'email', 'bio', 'role',
                  'first_name', 'last_name')
        read_only_fields = ('role',)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate(self, data):
        author = self.context['request'].user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if self.context['request'].method == 'POST':
            if Review.objects.filter(title=title, author=author).exists():
                raise ValidationError('Только один отзыв на произведение')
        return data

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'name', 'slug'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = 'name', 'slug'


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для not SAFE.METHODS."""
    """Поле жанр и категория ввводится как slug."""
    genre = serializers.SlugRelatedField(
        many=True, queryset=Genre.objects.all(), slug_field='slug'
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug'
    )

    class Meta:
        model = Title
        fields = '__all__'


class TitleVisualSerializer(serializers.ModelSerializer):
    """Сериализатор для SAFE.METHODS."""
    """Поле жанр и категории выводится как словарь"""
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(
        source='reviews__score__avg', read_only=True
    )

    class Meta:
        model = Title
        fields = '__all__'
