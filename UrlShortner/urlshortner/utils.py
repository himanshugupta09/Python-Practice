from .models import URLShortner
from django.utils import timezone
import io
import qrcode
from django.core.files.base import ContentFile

def save_qr_code(short, full_url):
    qr = qrcode.make(full_url)

    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")

    filename = f"{short.short_url}.png"

    short.qr_code.save(
        filename,
        ContentFile(buffer.getvalue()),
        save=True
    )
def generate_unique_short_code():
    short_code = URLShortner.generate_short_url()

    while URLShortner.objects.filter(short_url=short_code).exists():
        short_code = URLShortner.generate_short_url()

    return short_code

def get_expiry_date(expiry_choice):
    if expiry_choice == "never":
        return None

    return timezone.now() + timezone.timedelta(days=int(expiry_choice))