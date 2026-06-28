from django.shortcuts import render, redirect, get_object_or_404
from .models import URLShortner
import requests

def home(request):
    if request.method == "POST":
        original_url = request.POST.get("url")

        short_url = URLShortner.generate_short_url()

        while URLShortner.objects.filter(short_url=short_url).exists():
            short_url = URLShortner.generate_short_url()

        short = URLShortner.objects.create(
            original_url=original_url,
            short_url=short_url
        )

        full_url = request.build_absolute_uri(f"/{short.short_url}")

        return render(request, "home.html", {
            "short": short,
            "full_url": full_url
        })

    return render(request, "home.html")

def redirect_to_original(requests, short_url):
    url = get_object_or_404(URLShortner, short_url=short_url)
    url.clicks += 1
    url.save()
    return redirect(url.original_url)
def stats(request):
    urls = URLShortner.objects.all()
    return render(request, "stats.html", {"urls": urls})

# Create your views here.
