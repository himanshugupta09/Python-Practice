import re

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import URLShortner
from .utils import (
    generate_unique_short_code,
    get_expiry_date,
    save_qr_code,
)


def home(request):

    if request.method == "POST":

        original_url = request.POST.get("url")
        custom_alias = request.POST.get("custom_code", "").strip()
        expiry_choice = request.POST.get("expiry")

        # Validate alias
        if custom_alias:

            if not re.match(r"^[A-Za-z0-9_-]+$", custom_alias):
                return render(request, "home.html", {
                    "error": "Alias can only contain letters, numbers, hyphens (-), and underscores (_)."
                })

            if URLShortner.objects.filter(short_url=custom_alias).exists():
                return render(request, "home.html", {
                    "error": "Custom alias already exists."
                })

            short_code = custom_alias

        else:
            short_code = generate_unique_short_code()

        short = URLShortner.objects.create(
            original_url=original_url,
            short_url=short_code,
            expires_at=get_expiry_date(expiry_choice)
        )

        full_url = request.build_absolute_uri(
            reverse("redirect", args=[short.short_url])
        )

        save_qr_code(short, full_url)

        return render(request, "home.html", {
            "short": short,
            "full_url": full_url,
        })

    return render(request, "home.html")


def redirect_to_original(request, short_url):

    short = get_object_or_404(URLShortner, short_url=short_url)

    if short.is_expired:
        return render(request, "expired.html", status=410)

    short.clicks += 1
    short.save(update_fields=["clicks"])

    return redirect(short.original_url)


def stats(request):

    urls = URLShortner.objects.active_urls()

    return render(request, "stats.html", {
        "urls": urls,
        "base_url": request.build_absolute_uri("/")[:-1],
    })