from django import forms

class ContactForm(forms.Form):
    name = models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    notes=models.TextField()
    time = models.DateTimeField(auto_now_add=True)