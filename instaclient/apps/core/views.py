#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from core.models import HashTag, ImageUrl
from core.forms import SearchHashTagForm
from core.api import InstaApi


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update({
            'form_search_hashtag': SearchHashTagForm(),
            'previous_hashtags': HashTag.objects.order_by('-updated_time').filter(is_defective=False)[:5],
            'most_search_hashtags': HashTag.objects.order_by('-search_count').filter(is_defective=False)[:5],
        })

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        form_search_hashtag = SearchHashTagForm(request.GET)

        if form_search_hashtag.is_valid():
            hashtag = form_search_hashtag.save()

            results = InstaApi(hashtag.get_none_hashtag())
            images = results.get_images()

            all_images_url = [ image.url for image in ImageUrl.objects.all()]
            for image in images:
                image_medium_url = image['low_resolution']['url']

                if not image_medium_url in all_images_url:
                    image_url = ImageUrl(hashtag=hashtag, url=image['low_resolution']['url'])
                    image_url.save()

            context.update({
                'images': images,
                'previous_hashtags': HashTag.objects.order_by('-updated_time').filter(is_defective=False)[:5],
                'most_search_hashtags': HashTag.objects.order_by('-search_count').filter(is_defective=False)[:5],
                'form_search_hashtag': form_search_hashtag,
            })


        else:
            context.update({ 'form_search_hashtag':form_search_hashtag })

        return super(IndexView, self).render_to_response(context)
