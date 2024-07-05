from django import forms
import datetime
from .models import *


class OtherEducationForm(forms.ModelForm):
    class Meta:
        model = OtherEducation
        fields = ['user', 'education', 'specialization',
                  'institution', 'grade_point', 'year', 'duration']
        widgets = {
            'user': forms.HiddenInput(),
            'education': forms.Select(choices=model.education_choices, attrs={'class': 'form-select', 'placeholder': 'Education'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Specialization'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institution'}),
            'grade_point': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Grade Points or Percentage'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Passout Year'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        exclude = []
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs['style'] = 'height: 8rem'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('issue_date'):
            if cleaned_data.get('issue_date') > datetime.date.today():
                self.add_error('issue_date', 'Issue date cannot be in future')


class SkillForm(forms.Form):
    name = forms.CharField(max_length=150, label='Skill', widget=forms.TextInput(attrs={
                           'class': 'form-control', 'placeholder': 'Skill', 'id': 'id-skill-name', 'list': 'skill-data-list', 'autocomplete': 'off'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class LanguageForm(forms.Form):
    name = forms.CharField(max_length=150, label='Language', widget=forms.TextInput(attrs={
                           'class': 'form-control', 'placeholder': 'Language', 'id': 'id-language-name', 'list': 'language-data-list', 'autocomplete': 'off'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = []
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs['style'] = 'height: 8rem'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('start_date') and cleaned_data.get('end_date'):
            if cleaned_data.get('start_date') > cleaned_data.get('end_date'):
                self.add_error(
                    'end_date', 'End date cannot be before start date')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = []
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs['style'] = 'height: 8rem'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('start_date') and cleaned_data.get('end_date'):
            if cleaned_data.get('start_date') > cleaned_data.get('end_date'):
                self.add_error(
                    'end_date', 'End date cannot be before start date')


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = []
        widgets = {
            'publication_date':  forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs['style'] = 'height: 8rem'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('publication_date'):
            if cleaned_data.get('publication_date') > datetime.date.today():
                self.add_error('publication_date',
                               'Publication date cannot be in future')


class PatentForm(forms.ModelForm):
    class Meta:
        model = Patent
        exclude = []
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs['style'] = 'height: 8rem'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('issue_date'):
            if cleaned_data.get('issue_date') > datetime.date.today():
                self.add_error('issue_date', 'Issue date cannot be in future')


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        exclude = []
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs['style'] = 'height: 8rem'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('date'):
            if cleaned_data.get('date') > datetime.date.today():
                self.add_error('date', 'Date cannot be in future')


class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        exclude = []
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs['style'] = 'height: 8rem'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('date'):
            if cleaned_data.get('date') > datetime.date.today():
                self.add_error('date', 'Date cannot be in future')


class OtherInfoForm(forms.ModelForm):
    class Meta:
        model = OtherInfo
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            if isinstance(visible.field.widget, forms.Textarea):
                visible.field.widget.attrs['style'] = 'height: 8rem'
