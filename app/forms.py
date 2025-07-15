from django import forms
from django.core.exceptions import ValidationError
from app.models import Seller

class Employee(forms.Form):
    ename=forms.CharField(max_length=30)
    job=forms.CharField(max_length=30)
    join_date=forms.DateField()
    sal=forms.FloatField()
    dept=forms.CharField(max_length=30)
    phone_number=forms.IntegerField()

class Student(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=50)
    phone_number=forms.CharField()
    address=forms.CharField(max_length=50,widget=forms.Textarea(attrs={
        'style': 'background-color:pink;'
    }))
    course=forms.CharField(max_length=20)
    DOB=forms.DateField()
    marks=forms.IntegerField()

    def clean_phone_number(self):
        data=str(self.cleaned_data['phone_number'])

        if len(data)==10:
            if data[0] in '6789':
                if data.isdigit():
                    return data
                else:
                    raise ValidationError('it should contin only numbers')
            else:
                raise ValidationError('it should star with 6 or 7 or 8 or 9')
        else:
            raise ValidationError('it should contin 10 numbers')
                
    def clean_name(self):
        data=self.cleaned_data['name']

        if data.isalpha():
            if data[0]!=' ':
                return data
            else:
                raise ValidationError('name should not start with space')
        else:
            raise ValidationError('name should contain only alphabets')

class SellerForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields='__all__'