from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed

from django.contrib import admin
admin.autodiscover()

class BlogFeed(Feed):
	title = "Sean's Blog"
	description = "Some ramblings of mine"
	link = "/blog/feed"

	def items(self):
		return Post.objects.all().order_by("-created")[:2]
	def item_title(self, item):
		return item.title
	def item_description(self, item):
		return item.body
	def item_link(self, item):
		return u"blog/%d" % item.id


urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'seanc_blog.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^blog/$', ListView.as_view(
    						queryset=Post.objects.all().order_by("-created")[:2],
    						template_name="blog.html")),

    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(
    						model = Post,
    						template_name="post.html")),

    url(r'^blog/archives/$', ListView.as_view(
    						queryset=Post.objects.all().order_by("-created"),
    						template_name="archives.html")),

    url(r'^blog/tag/(?P<tag>\w+)$', 'tagpage'),

	url(r'^blog/feed/$', BlogFeed()),

    url(r'^admin/', include(admin.site.urls)),
)
