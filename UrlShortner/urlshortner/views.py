import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import URLShortner
from django.utils import timezone
from django.db.models import Q


def home(request):
    if request.method == "POST":
        original_url = request.POST.get("url")
        custom_alias = request.POST.get("custom_code","").strip()
        expiry_choice = request.POST.get("expiry")
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

        expires_at = None
        if expiry_choice != 'never':
            expires_at = timezone.now() + timezone.timedelta(days=int(expiry_choice))
        short = URLShortner.objects.create(
            original_url = original_url,
            short_url = short_url,
            expires_at = expires_at
        )
        return render(request,"home.html", {"short_url": short.short_url})
    return render(request,"home.html")

def redirect_to_original(request, short_url):
    short = get_object_or_404(URLShortner, short_url=short_url)
    print(short.__dict__)
    if short.is_expired:
        return render(request,'expired.hmtl',status=410)
    short.clicks += 1
    short.save()
    return redirect(short.original_url)

def stats(request):
    urls =  URLShortner.objects.filter(
        Q(expires_at__isnull=True) | Q(expires_at__gt=timezone.now())
    )
    return render(request, "stats.html", {"urls": urls})

# Create your views here.
