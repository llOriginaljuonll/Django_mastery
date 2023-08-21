from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator

# Every letters to Lowercase
class Lowercase(forms.CharField):
  def to_python(self, value):
    return value.lower()
  
# Every letters to Uppercase
class Uppercase(forms.CharField):
  def to_python(self, value):
    return value.upper()

class CandidateForm(forms.ModelForm):
    
    # VALIDATIONS
  firstname = forms.CharField(
      label='First name', min_length=3, max_length=50, 
      validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
      message="Only letters is allowed !")],
      widget=forms.TextInput(attrs={'placeholder': 'First name'})
  )
  lastname = forms.CharField(
      label='Last name', min_length=3, max_length=50, 
      validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
      message="Only letters is allowed !")],
      widget=forms.TextInput(attrs={'placeholder': 'Last name'})
  )

  # Job code always in Uppercase
  job = Uppercase(
      label='Job code', 
      min_length=5, max_length=5, 
      widget=forms.TextInput(attrs={
        'placeholder': 'Example: FR-22'
      })
  )

  # Email always in Lowercase
  email = Lowercase(
      label='Email address', min_length=8, max_length=50, 
      validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
      message="Put a valid email address !")],
      widget=forms.TextInput(attrs={'placeholder': 'Email'})
  )
  # Method 1
  # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))

  # Method 2
  age = forms.CharField(
      label='Your age', min_length=2, max_length=2,
      validators= [RegexValidator(r'^[0-9]*$', 
      message="Only numbers is allowed !")],
      widget=forms.TextInput(attrs={'placeholder': 'Age'})
  )

  experience = forms.BooleanField(label='I have experience', required = False)

  message = forms.CharField(
    label='About you', min_length=50, max_length=1000,
    required=False,
    widget=forms.Textarea(
      attrs={'placeholder':'Talk a little about you', 'rows':5}
      ),
  )

  # # Method 1 (Gender)
  # GENDER = [('M', 'Male'),['F', 'Female']]
  # gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))

  class Meta:
    model = Candidate
    exclude = ['created_at', 'Situation']
    # Labels control
    labels = {
      'gender':'Your gender',
      'smoker':'Do you smoke ? ',
    }
    
    SALARY = (
      ('', 'Salary expectation (month)'),
      ('Between ($3000 and $4000)', 'Between ($3000 and $4000)'),
      ('Between ($4000 and $5000)', 'Between ($4000 and $5000)'),
      ('Between ($5000 and $7000)', 'Between ($5000 and $7000)'),
      ('Between ($7000 and $10000)', 'Between ($7000 and $10000)')
    )

    # Method 2 (Gender)
    GENDER = [('M', 'Male'),['F', 'Female']]

    # OUTSIDE WIDGETS
    widgets = {
      # Phone
      'phone': forms.TextInput(
          attrs={
            'style': 'font-size: 13px', #CSS
            'placeholder': 'Phone',
            'data-mask': '(00) 00000-0000'
          }
        ),
      # Salary
      'salary': forms.Select(
          choices=SALARY,
          attrs={
            'class': 'form-control', #Bootstrap inside the form.py
            
          }
        ),
      'gender': forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check'}),
      'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class': 'btn-check'}),
    }

  # 'SUPER' FUNCION
  def __init__(self, *args, **kwargs):
    super(CandidateForm, self).__init__(*args, **kwargs)

    # ========== CONTROL PANEL (Optional method to control) ===========|
    # Input required
    # self.fields['message'].required = True

    # Input Disabled
    # self.fields['firstname'].disabled = True
    # self.fields['lastname'].disabled = True
    # self.fields['job'].disabled = True

    # Input Readonly
    # self.fields['email'].widget.attrs.update({'readonly':'readonly'})

    # ========== SELECT OPTION ===========|
    self.fields["personality"].choices = [('', 'Select a personality'),] + list(self.fields["personality"].choices)[0:]

    # ========== WIDGET CONTROL ===========|
    self.fields['phone'].widget.attrs.update({'style':'font-size: 18px', 'placeholder':'No phone'})
    

    # ========== WIDGET CONTROL / DISABLED BY 'LOOP FOR' IN [ARRAY] ===========|
    # 1) Readonly
    readonly = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'message']
    for field in readonly:
        self.fields[field].widget.attrs['readonly'] = 'true'

    # 2) Disabled
    disabled = ['personality', 'salary', 'gender', 'smoker', 'experience']
    for field in disabled:
        self.fields[field].widget.attrs['disabled'] = 'true'