#-*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class CommonModel(models.Model):
    created_time = models.DateTimeField(verbose_name=_(u"Created Time"), auto_now_add=True, editable=False)
    updated_time = models.DateTimeField(verbose_name=_(u"Updated Time"), auto_now=True, editable=False)

    class Meta:
        abstract = True


class HashTag(CommonModel):
    hashtag = models.CharField(verbose_name=_(u"HashTag"), max_length=100)
    search_count = models.PositiveIntegerField(verbose_name=_(u"Search Count"), default=0)
    is_defective = models.BooleanField(verbose_name=_(u'Defective HashTag'), default=False)

    class Meta:
        verbose_name = _(u"Hashtag")
        verbose_name_plural = _(u"HashTags")

    def get_none_hashtag(self):
        return self.hashtag[1:]

    def __str__(self):
        return self.hashtag

    def save(self, *args, **kwargs):
        if not self.hashtag.startswith("#"):
            self.hashtag = "#" + self.hashtag

        return super(HashTag, self).save(*args, **kwargs)


class ImageUrl(CommonModel):
    url = models.CharField(verbose_name=_(u"URL"), max_length=500)
    hashtag = models.ForeignKey(verbose_name=_(u"HashTag"), to=HashTag)

    class Meta:
        verbose_name = _(u"Image Url")
        verbose_name_plural = _(u"Image Urls")

    def download_image_link(self):
        return "<a href='%s' target='_blank' download>%s</a>" % (self.url, _('Download'))

    download_image_link.allow_tags = True
    download_image_link.short_description = _("Download")

    def show_image_link(self):
        return "<a href='%s' target='_blank'>%s</a>" % (self.url, _('Show'))


    show_image_link.allow_tags = True
    show_image_link.short_description = _("Show")

    def __str__(self):
        return self.url
