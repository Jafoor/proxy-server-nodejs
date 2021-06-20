from django import forms
from App_Event.models import CreateEvent, EventType

class CreateEventSubmit(forms.ModelForm):

    event_pic = forms.FileField(
        required = True,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'value':"{{ org.org_pic.value }}",
                'required' : True
            }
        )
    )

    title = forms.CharField(
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'Title of Event (max 6 words)',
                'required' : True
            }
        )
    )

    sort_description = forms.CharField(
        required = True,
        widget = forms.Textarea(
            attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'Maximum 20 words',
                'cols':20,
                'rows':5,
                'required' : True
            }
        )
    )

    event_type = forms.ModelChoiceField(queryset=EventType.objects.all(), empty_label="Choose Your Event Type", required = True, widget=forms.Select(attrs={'class': 'form-control'}))

    need_amount = forms.IntegerField(
        required=True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type':'number',
                'placeholder': '10000',
                'required' : True
            }
        )

    )

    endtime = forms.DateTimeField(
        required = True,
        widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local', 'class': 'form-control', 'required' : True})
    )

    extra_img1 = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'required' : False
            }
        )
    )

    extra_img2 = forms.FileField(
        required = False,
        widget = forms.FileInput(
            attrs={
                'class': 'form-control',
                'type':'file',
                'placeholder': '',
                'accept':"image/*",
                'required' : False
            }
        )
    )

    terms_and_condition = forms.BooleanField(
        required = True,
        widget = forms.CheckboxInput(
            attrs={
                'class': 'iCheck-helper',
                'type': 'checkbox',
                'required' : True
            }
        )

    )
    class Meta:
        model = CreateEvent
        fields = ('title', 'event_type', 'event_pic', 'sort_description', 'description', 'need_amount', 'endtime', 'terms_and_condition', 'extra_img1', 'extra_img2' )
