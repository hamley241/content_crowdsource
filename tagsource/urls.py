__author__ = 'patley'
from django.conf.urls import patterns, url


from tagsource import views

urlpatterns =patterns("",
            # url(r'^$',views.index, name='index'),
            url(r'(?P<tag_id>\d+)/$',views.stickertagvote, name='stickertagvote'),
            # url(r'(?P<sticker_id>\d+)/$', views.details ,name='details'),
            # url(r'(?P<sticker_id>\d+)/results/$', views.results, name='results'),
            # url(r'(?P<sticker_id>\d+)/vote/$', views.vote, name='vote'),
            # url(r'(?P<sticker_id>\d+)/add/$', views.add, name='add'),
            # url(r'(?P<catid>.*)/category/$', views.category, name='category'),
            # url(r'^categories/$', views.cat_list, name='cat_list'),
            # url(r'^sticker/(?P<sticker_nm>.*)/search/$', views.search_stickers, name='search_stickers'),
            # url(r'^sticker/search/$', views.search_stick, name='search_stick'),
            # url(r'^logout/$', views.logger_out, name='tlogout'),
            # url(r'^finale/$', views.gisc_finale, name='finale'),
            # url(r'^dtags/$', views.delete_tags, name='dtags'),
            # url(r'^dresptags/$', views.delete_response_tags, name='dresptags'),
            # url(r'^categjosn/(?P<categ>.*)/$', views.get_categ_json, name='categjson'),
            # url(r'^lang/$', views.language_updater, name='lang'),
)

