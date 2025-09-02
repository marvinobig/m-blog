from django import forms

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)

    def publish(self):
        pass 