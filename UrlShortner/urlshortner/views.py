import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import URLShortner

def home(request):
    if request.method == "POST":
        original_url = request.POST.get("url")
        custom_alias = request.POST.get("custom_alias","").strip()
        if custom_alias:
            if not re.match(r'^[A-Za-z0-9_-]+$', custom_alias):
                return render(request, "home.html", {
                    "error": "Alias can only contain letters, numbers, hyphens (-), and underscores (_)."
                })
        short_url = None
        if len(custom_alias) > 0:
            if URLShortner.objects.filter(short_url=custom_alias).exists():
                return render(request, "home.html", {
                    "error": "Custom alias already exists. Please choose a different one."
                })
            short_url = custom_alias

        else:
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

def redirect_to_original(request, short_url):
    url = get_object_or_404(URLShortner, short_url=short_url)
    url.clicks += 1
    url.save()
    return redirect(url.original_url)
def stats(request):
    urls = URLShortner.objects.all()
    return render(request, "stats.html", {"urls": urls})

# Create your views here.
