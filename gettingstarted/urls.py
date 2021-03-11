from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import polls.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("databaseadd/", hello.views.databaseadd, name="databaseadd"),

    path('', polls.views.index, name='index'),
    path('<int:question_id>/', polls.views.detail, name='detail'),
    path('<int:question_id>/results/', polls.views.results, name='results'),
    path('<int:question_id>/vote/', polls.views.vote, name='vote'),
    path('<int:question_id>/', polls.views.detail, name='detail'),
]
  ]
