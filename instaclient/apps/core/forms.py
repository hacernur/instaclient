#-*- coding: utf-8 -*-

from django import forms

from core.models import HashTag


class SearchHashTagForm(forms.ModelForm):
    hashtag = forms.CharField(widget=forms.TextInput(attrs={'placeholder': u' Search HashTag'}), required = True)

    class Meta:
        model = HashTag
        fields = ('hashtag',)
        exclude = ('is_defective', 'created_time', 'updated_time')

    def exist_in_database(self, hashtag):
         return True if hashtag in [ i.hashtag for i in HashTag.objects.all()] else False

    def save(self, commit=True):
        hashtag_instance = super(SearchHashTagForm, self).save(commit=False)

        if commit:
            hashtag = self.cleaned_data['hashtag']

            if not hashtag.startswith('#'):
                hashtag = "#" + hashtag

            if not self.exist_in_database(hashtag):
                hashtag_instance.hashtag = hashtag
                hashtag_instance.search_count = 1
                # Burda aranan hashtag'in olumsuzluğu kontrol edilecek ve
                # ona göre is_defective = True yapılıp kaydedilecek.

                hashtag_instance.save()
            else:
                hashtag_instance = HashTag.objects.get(hashtag=hashtag)
                hashtag_instance.search_count += 1
                hashtag_instance.save()

        return hashtag_instance
