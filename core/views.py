"""Views for Core."""

from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.detail import DetailView

from .models import SiteData, Guest


# Create your views here.
class Home(DetailView):
    """View to home."""
    model = Guest
    template_name = 'core/home.html'

    def get(self, request, **kwargs):
        """Get method"""
        slug = kwargs.get('slug')
        guest = Guest.objects.filter(slug=slug)

        return render(
            request,
            self.template_name,
            {
                'site':
                    SiteData.objects.order_by('-created_at')[0],
                'guest': guest[0] if guest else None
            }
        )


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')
