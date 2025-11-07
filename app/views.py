from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def cached_view(request):
    return HttpResponse(f"Cached at {timezone.now()} for five minutes")