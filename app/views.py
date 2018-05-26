from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')

class D3PlanetView(View):

    def get(self, request):
        return render(request, 'D3Planet.html')


class D3ModelCameraView(View):

    def get(self, request):
        return render(request, 'D3ModelCamera.html')

class D3CubePuzzleView(View):

    def get(self, request):
        return render(request, 'D3CubePuzzle.html')


class D3PixelGraphView(View):

    def get(self, request):
        return render(request, 'D3PixelGraph.html')

class D3LineAvatarView(View):

    def get(self, request):
        return render(request, 'D3LineAvatar.html')

class D3BookFlipView(View):

    def get(self, request):
        return render(request, 'D3BookFlip.html')

class D3WaveView(View):

    def get(self, request):
        return render(request, 'D3Wave.html')

class D3HeartAnimationView(View):

    def get(self, request):
        return render(request, 'D3HeartAnimation.html')

class D3ImagesView(View):

    def get(self, request):
        return render(request, 'D3Images.html')


class D3ImageBlockView(View):

    def get(self, request):
        return render(request, 'D3ImageBlock.html')

class D3ExplodClockView(View):

    def get(self, request):
        return render(request, 'D3ExplodClock.html')

class D3UnfoldCube01View(View):

    def get(self, request):
        return render(request, 'D3UnfoldCube01.html')

class D3UnfoldCube02View(View):

    def get(self, request):
        return render(request, 'D3UnfoldCube02.html')

