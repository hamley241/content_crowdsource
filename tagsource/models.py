import datetime
from django.db import models
from django.utils import timezone
import json


class Sticker(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=20)
    like = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date added',auto_now_add=True, blank=True)
    class Meta:
        unique_together= (('name', 'category'),)

    def __str__(self):
        return ''.join([self.category,'-',self.name[4:]]).strip(".png")

    def is_hot(self,threshold_rating):
        if self.rating >= threshold_rating:
            return True
    def get_like(self):
        return self.like

    def update_likes(self, increment):
        self.like += increment

    def was_recently_added(self, stale_threshold=7):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=stale_threshold)

    def get_tags(self):
        for tag in self.tag_set.all():
            return ""

    def get_tag_set(self):
        for tg in self.get_tag_set():
            print tg.name


    @staticmethod
    def get_category_stickers(category):
        return Sticker.objects.filter(category=category)



class Tag(models.Model):
    sticker = models.ForeignKey(Sticker)
    name = models.CharField(max_length=100 )
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    #theme =["THEME","EMOTION","FEELING","BEHAVIOUR","REACTION","SMILEY","RESPONSE","GENERAL","OTHER","REGIONAL"]
    theme = models.CharField(max_length=20,default="NA")
    lang = models.CharField(max_length=20,default='NA')
    def __str__(self):
        return self.name
    def change_lang(self,langua):
        self.lang = langua
        self.save()


