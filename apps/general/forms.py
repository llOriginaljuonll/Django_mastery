from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Every letters to Lowercase
class Lowercase(forms.CharField):
  def to_python(self, value):
    return value.lower()
  
# Every letters to Uppercase
class Uppercase(forms.CharField):
  def to_python(self, value):
    return value.upper()

class CandidateForm(forms.ModelForm):
    
  # First name
  firstname = forms.CharField(
      label='First name', min_length=3, max_length=50, 
      validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
      message="Only letters is allowed !")],
      error_messages={'required':'First name cannot be empty.'},
      widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'style': 'font-size: 13px; text-transform: capitalize'
      })
  )

  # Last name
  lastname = forms.CharField(
      label='Last name', min_length=3, max_length=50, 
      validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
      message="Only letters is allowed !")],
      widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
        'style': 'font-size: 13px; text-transform: capitalize'
      })
  )

  # Job code always (Uppercase function)
  job = Uppercase(
      label='Job code',
      min_length=5, max_length=5, 
      widget=forms.TextInput(attrs={
        'placeholder': 'Example: FR-22',
        'style': 'font-size: 13px; text-transform: uppercase'
      })
  )

  # Email always in Lowercase
  email = Lowercase(
      label='Email address', min_length=8, max_length=50, 
      validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
      message="Put a valid email address !")],
      widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'style': 'font-size: 13px; text-transform: lowercase'
      })
  )
  # Method 1
  # age = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))

  # Method 2
  age = forms.CharField(
      label='Your age', min_length=2, max_length=2,
      validators= [RegexValidator(r'^[0-9]*$', 
      message="Only numbers is allowed !")],
      error_messages={'required':'Age field cannot be empty.'},
      widget=forms.TextInput(attrs={
        'placeholder': 'Age',
        'style': 'font-size: 13px;'
      })
  )

  # Experience
  experience = forms.BooleanField(label='I have experience', required = False)

  #Message
  message = forms.CharField(
    label='About you', min_length=50, max_length=1000,
    required=False,
    widget=forms.Textarea(
      attrs={'placeholder':'Talk a little about you',
             'rows': 4,
             'style': 'font-size: 13px;'
      }
    ),
  )

  # File (Upload)
  file = forms.FileField(
    required=True,
    widget=forms.ClearableFileInput(
      attrs={
        'style': 'font-size: 13px;'
      }
    )
  )

  # # Method 1 (Gender)
  # GENDER = [('M', 'Male'),['F', 'Female']]
  # gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER))

  class Meta:
    model = Candidate
    exclude = ['created_at', 'Situation']
    # Labels control
    # labels = {
    #   'gender':'Your gender',
    #   'smoker':'Do you smoke ? ',
    # }
    
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
            'style': 'font-size: 13px;'
          }
        ),
      'gender': forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check'}),
      'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class': 'btn-check'}),
      'personality': forms.Select(attrs={'style': 'font-size: 13px;'})
    }

  # 'SUPER' FUNCION
  def __init__(self, *args, **kwargs):
    super(CandidateForm, self).__init__(*args, **kwargs)

    # ========== CONTROL PANEL (individual <Inputs>) ===========|
    # 1) INPUT REQUIRED
    # self.fields['message'].required = True

    # 2) INPUT DISABLED
    # self.fields['firstname'].disabled = True
    # self.fields['lastname'].disabled = True
    # self.fields['job'].disabled = True

    # 3) INPUT READONLY
    # self.fields['email'].widget.attrs.update({'readonly':'readonly'})

    # 4) SELECT OPTION
    # self.fields["personality"].choices = [('', 'Select a personality'),] + list(self.fields["personality"].choices)[0:]

    # 5) WIDGET (inside/outside)
    # self.fields['phone'].widget.attrs.update({'style':'font-size: 18px', 'placeholder':'No phone'})

    # 6) ERROR MESSAGES 
    # self.fields['firstname'].error_messages.update({
    #   'required': 'Django Mastery Channel'
    # })
    

    # ========== ADVANCED CONTROL PANEL (multiple <Inputs>) ===========|
    # 1) READONLY
    # readonly = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'message']
    # for field in readonly:
    #     self.fields[field].widget.attrs['readonly'] = 'true'

    # # 2) DISABLED
    # disabled = ['personality', 'salary', 'gender', 'smoker', 'experience']
    # for field in disabled:
    #     self.fields[field].widget.attrs['disabled'] = 'true'

    # 3) ERROR MESSAGES 
    # error_messages = ['firstname', 'lastname', 'job', 'email', 'age', 'phone', 'personality', 'salary', 'gender', 'smoker', 'file']
    # for field in error_messages:
    #     self.fields[field].error_messages.update({'required': 'Django Mastery Channel...'})
    # FONT SIZE
    font_size = ['firstname', 'lastname', 'job', 'age']
    for field in font_size:
        self.fields[field].widget.attrs.update({'style':'font-size: 18px'})

  # --------------------------------------- END // SUPER FUNCTION -----------------------------------------------

  # FUNCTION TO PREVENT DUPLICATED ENTRIES
  # Method 1 (loop for)
  # def clean_email(self):
  #     email = self.cleaned_data.get('email')
  #     for obj in Candidate.objects.all():
  #         if obj.email == email:
  #             raise forms.ValidationError('Denined ! ' + email + ' is already registered.')
  #     return email

  # Mehod 2 (if statement w/ filter)
  def clean_email(self):
      email = self.cleaned_data.get('email')
      if Candidate.objects.filter(email = email).exists():
         raise forms.ValidationError('Denined ! {} is already registered.'.format(email))
      return email