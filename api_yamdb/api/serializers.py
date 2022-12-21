from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
import re

from reviews.models import Category, Comment, Genre, Review, Title, User


class SingUpSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)

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
        if data['username'] == 'me':
            raise serializers.ValidationError('Недопустимое имя "me"')
        if User.objects.filter(username=data['username'], email=data['email']).exists():
            return data
        if (user_if or email_if):
            raise serializers.ValidationError('Почта уже использовалась')
        if email_if:
            raise serializers.ValidationError('Почта уже использовалась')
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        return user
    
    class Meta:
        model = User
        fields= ('last_login', 'username', 'first_name', 'last_name', 'bio', 'role')

class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

 
class UsersViewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(required=True, max_length=254)
    first_name = serializers.CharField(required=False, max_length=150)
    last_name = serializers.CharField(required=False, max_length=150)
    bio = serializers.CharField(required=False)
    role = serializers.CharField(required=False, default='user')

    def validate_username(self, value):
        if not re.fullmatch(r'^[\w.@+-]+', value):
            raise serializers.ValidationError('Nickname должен содержать буквы,'
                                               'цифры и символы @.+-_')
        return value

    def validate(self, data,):
        user_if = User.objects.filter(username=data['username']).exists()
        email_if  = User.objects.filter(email=data['email']).exists()
        if (user_if or email_if):
            raise serializers.ValidationError('Почта уже использовалась')
        return data

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

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role',
        )
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


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True, queryset=Genre.objects.all(), slug_field='slug'
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug'
    )

    class Meta:
        model = Title
        fields = '__all__'
