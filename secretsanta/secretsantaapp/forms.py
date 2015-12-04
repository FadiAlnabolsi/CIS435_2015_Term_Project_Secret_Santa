from django import forms
from django.contrib.auth.forms import AuthenticationForm

from secretsantaapp.models import SecretSantaGroup

class SecretSantaGroupForm(forms.ModelForm):

	class Meta:
		model = SecretSantaGroup
		fields = (
				'group_name',
			)


