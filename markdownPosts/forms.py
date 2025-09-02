from django import forms

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleanedData = super().clean()
        title = cleanedData.get('title')
        body = cleanedData.get('body')

        if len(title) < 5:
            raise forms.ValidationError("Title is too short. It sould be greater than 5 characters")
        
        if len(body) < 20:
            raise forms.ValidationError("Body does not have enough content. It should be greater than 20 characters")