from django import forms

from .models import Post, Comment, DoorayMessage


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')


class DoorayForm(forms.ModelForm):

    class Meta:
        model = DoorayMessage
        fields = ('text', 'title', 'imageUrl')
