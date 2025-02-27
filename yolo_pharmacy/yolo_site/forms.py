from django import forms
from django.contrib.auth.models import User
from . import models

class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        exclude = ['added_on']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = models.Medicine
        exclude = ['updated_on']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['name', 'job_title', 'contact_no', 'bank_account', 'salary', 'address']

class BillDetailsForm(forms.ModelForm):
    class Meta:
        model = models.BillDetails
        exclude = ['created_on', 'items']

    def clean(self):
        qty = self.data.getlist('quantity[]')
        med_id = self.data.getlist('med_id[]')
        print(qty, med_id)
        cleaned_data = super().clean()

        cleaned_data['items'] = []
        for i in range(len(qty)):
            med = models.Medicine.objects.get(pk=int(med_id[i]))
            if int(qty[i]) > med.stock * med.pack_quantity:
                self.add_error('quantity', 'Quantity ('+qty[i]+') exceeds stock ('+med.stock+') :: '+ med.__str__())

            cleaned_data['items'].append({'med_id': med, 'quantity': int(qty[i])})

        return cleaned_data