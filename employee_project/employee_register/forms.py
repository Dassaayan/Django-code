from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields='__all__'
        labels={
             "fullname": "Full Name",
             "emp_code": "Emp. Code",
             "mobile": "Mobile number(+91)",
             "position": "Positions"
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields["position"].empty_label="Select"
        self.fields["emp_code"].required=False