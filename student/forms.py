from django.forms import ModelForm
from .models import file

class fileform(ModelForm):
    class Meta:
        model = file
        fields = {'file_name', 'project_id', 'file_content'}