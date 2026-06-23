import html
import logging
from django.conf import settings
from django.core.mail import send_mail
from django.template.response import TemplateResponse
from .forms import ContactForm
from .models import ContactRequest

logger = logging.getLogger("src")


def contact_submit(request):
    if request.method != "POST":
        from django.http import HttpResponseNotAllowed
        return HttpResponseNotAllowed(["POST"])

    form = ContactForm(request.POST)

    if form.is_valid():
        contact = form.save()

        # Відправляємо email
        subject_label = contact.get_subject_display()
        name_safe = html.escape(contact.name)
        company_safe = html.escape(contact.company or "—")
        message_safe = html.escape(contact.message)

        body = (
            f"Нове звернення з сайту\n\n"
            f"Ім'я: {name_safe}\n"
            f"Компанія: {company_safe}\n"
            f"Email: {contact.email}\n"
            f"Телефон: {contact.phone or '—'}\n"
            f"Категорія продукту: {subject_label}\n\n"
            f"Повідомлення:\n{message_safe}"
        )

        try:
            send_mail(
                subject=f"[Nikola] {subject_label} від {name_safe}",
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception:
            logger.exception("Не вдалося надіслати email для ContactRequest pk=%s", contact.pk)

        return TemplateResponse(request, "partials/_contact_success.html", {})

    # Повертаємо форму з помилками
    return TemplateResponse(request, "partials/_contact_form.html", {"form": form})
