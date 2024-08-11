from django import forms
from django.contrib.contenttypes.models import ContentType

from products.models import Game, GiftCard
from .models import CartItem


class CartItemForm(forms.ModelForm):
    content_object = forms.ModelChoiceField(queryset=Game.objects.all(), required=False, label='Product')
    # content_type = forms.ModelChoiceField(queryset=ContentType.objects.filter(model__in=['game', 'giftcard']))
    
    class Meta:
        model = CartItem
        fields = ['cart', 'content_type', 'content_object', 'quantity']
        exclude = ['content_object',]
        
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            if self.instance.content_type.model == 'game':
                self.fields['content_object'].queryset = Game.objects.all()
            elif self.instance.content_type.model == 'giftcard':
                self.fields['content_object'].queryset = GiftCard.objects.all()
                
    def clean(self):    
        cleaned_data = super().clean()
        content_type = cleaned_data.get('content_type')
        content_object = cleaned_data.get('content_object')
        
        if content_type and content_object:
            if content_type.model != content_object._meta.model_name: 
                raise forms.ValidationError('Content type and object do not match.')
            
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.object_id = self.cleaned_data['content_object'].id
        instance.content_type = ContentType.objects.get_for_model(self.cleaned_data['content_object'])
        if commit:
            instance.save()
        return instance