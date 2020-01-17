from django import forms
from .models import BlogData

class PostForm(forms.Form):
    search_data = forms.CharField(required=False)

    def clean_search_data(self):
        data = self.cleaned_data['search_data']

        return data
    # class Meta:
    #     model = BlogData
    #     fields = ('title', 'tag',)
