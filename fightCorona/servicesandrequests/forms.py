from django import forms
from .models import Request, District, State
from bootstrap_modal_forms.forms import BSModalForm


class RequestForm(forms.ModelForm):
    #state = forms.ChoiceField(choices=[st.state_name for st in State.objects.all()])
    #district = forms.ChoiceField()

    class Meta:
        model = Request
        fields = [
            'service',
            'sub_service',
            'request_name',
            'state',
            'district',
            'area',
            'contact',
            'whatsapp',
            'email_address',
            'people_capacity'
        ]
        widgets = {
            'service': forms.Select(attrs={'style': 'width:70%'}),
            'sub_service': forms.Select(attrs={'style': 'width:70%'}),
            'request_name': forms.TextInput(attrs={'style': 'width:70%'}),
            'state': forms.Select(attrs={'style': 'width:70%'}),
            'district': forms.Select(attrs={'style': 'width:70%', 'class': 'select'}),
            'area': forms.Select(attrs={'style': 'width:70%'}),
            'contact': forms.TextInput(attrs={'style': 'width:70%'}),
            'whatsapp': forms.TextInput(attrs={'style': 'width:70%'}),
            'email_address': forms.TextInput(attrs={'style': 'width:70%'}),
            'people_capacity': forms.TextInput(attrs={'style': 'width:70%'})
        }

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, *kwargs)
        if args[0] is not None:
            arg_dict = dict(args[0].lists())
            print(arg_dict)
            state = arg_dict['state'][0]
            district = arg_dict['district'][0]
            if state != '':
                print("value of state is: "+str(state))
                self.fields['district'].choices = list(
                    District.objects.filter(state_id=state).values_list('district_id', 'district_name'))
            else:
                self.fields['district'].choices = []
