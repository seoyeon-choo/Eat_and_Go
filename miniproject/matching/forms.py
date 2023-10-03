from django import forms
from matching.models import MatchingPost

class MatchingPostForm(forms.ModelForm):
    class Meta:
        model = MatchingPost #사용할 모델
        fields = ['subject', 'content'] #MatchingPostForm에서 사용할 MatchingPost 모델의 속성

        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

        labels = {
            'subject': '제목',
            'content': '내용',
        }

