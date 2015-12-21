from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from tagsource.models import *
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
from functools import wraps
import base64
from django.http import JsonResponse
import logging

logger = logging.getLogger('taggie')


def stickertagvote(request,tag_id):
    print
    logger.info("tag id is "+str(tag_id))
    try:
        t = Tag.objects.get(pk=tag_id)
        t.upvotes += 1
        t.save()
    except:
        return JsonResponse({"stat":"success","error":"no sticker with that id"})
    return JsonResponse({"stat":"success"})
