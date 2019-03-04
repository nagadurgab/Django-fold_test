from django.forms import ModelForm
#from folders.views import dirstruc

from django import forms
from . import views 

class DisplayForm(forms.ModelForm):
    	folders=dirstruc()
    	print(folders)
    	def __init__(self, *args, **kwargs):
    		super().__init__(*args, **kwargs)
    		if 'id' in self.data:
    			try:
    				sub_fold = int(self.data.get('id'))
    				sub_folders=os.listdir('C:/Users/NagaDurga/Documents/'+sub_fold)
    			except (ValueError, TypeError):
    			 pass  # invalid input from the client; ignore and fallback to empty City queryset







          