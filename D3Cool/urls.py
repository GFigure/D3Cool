"""D3Cool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
from app.views import D3PlanetView, D3ModelCameraView, D3CubePuzzleView, D3PixelGraphView
from app.views import D3LineAvatarView, D3BookFlipView, D3WaveView, D3ExplodClockView
from app.views import D3HeartAnimationView, D3ImagesView, D3ImageBlockView
from app.views import D3UnfoldCube01View, D3UnfoldCube02View, IndexView
from app.views import LandingView, APlayerView


from django.views.static import serve
from D3Cool.settings import STATIC_ROOT

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url('^$', IndexView.as_view(), name='index'),
    url('^D3Planet.html$', D3PlanetView.as_view(), name='D3Planet'),
    url('^D3ModelCamera.html$', D3ModelCameraView.as_view(), name='D3ModelCamera'),
    url('^D3CubePuzzle.html$', D3CubePuzzleView.as_view(), name='D3CubePuzzle'),
    url('^D3PixelGraph.html$', D3PixelGraphView.as_view(), name='D3PixelGraph'),
    url('^D3LineAvatar.html$', D3LineAvatarView.as_view(), name='D3LineAvatar'),
    url('^D3BookFlip.html$', D3BookFlipView.as_view(), name='D3BookFlip'),
    url('^D3Wave.html$', D3WaveView.as_view(), name='D3Wave'),
    url('^D3HeartAnimation.html$', D3HeartAnimationView.as_view(), name='D3HeartAnimation'),
    url('^D3Images.html$', D3ImagesView.as_view(), name='D3Images'),
    url('^D3ImageBlock.html$', D3ImageBlockView.as_view(), name='D3ImageBlock'),
    url('^D3ExplodClock.html$', D3ExplodClockView.as_view(), name='D3ExplodClock'),
    url('^D3UnfoldCube01.html$', D3UnfoldCube01View.as_view(), name='D3UnfoldCube01'),
    url('^D3UnfoldCube02.html$', D3UnfoldCube02View.as_view(), name='D3UnfoldCube02'),

    url('^APlayer.html$', APlayerView.as_view(), name='APlayer'),
    url('^landing.html$', LandingView.as_view(), name='landing'),

    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

]
