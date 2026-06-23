import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone
from unfold.admin import ModelAdmin
from .models import ContactRequest


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = (
        f'attachment; filename="contacts_{timezone.now().strftime("%Y%m%d")}.csv"'
    )
    response.write("\ufeff")
    writer = csv.writer(response)
    writer.writerow(["Дата", "Ім'я", "Компанія", "Email", "Телефон", "Тема", "Повідомлення", "Опрацьовано"])
    for obj in queryset:
        writer.writerow([
            obj.created_at.strftime("%d.%m.%Y %H:%M"),
            obj.name, obj.company, obj.email, obj.phone,
            obj.get_subject_display(), obj.message,
            "Так" if obj.is_processed else "Ні",
        ])
    return response

export_csv.short_description = "Експорт у CSV"


@admin.register(ContactRequest)
class ContactRequestAdmin(ModelAdmin):
    list_display = ("name", "company", "email", "phone", "subject", "created_at", "is_processed")
    list_editable = ("is_processed",)
    list_filter = ("subject", "is_processed")
    search_fields = ("name", "company", "email")
    readonly_fields = ("name", "company", "email", "phone", "subject", "message", "created_at")
    actions = [export_csv]

    def has_add_permission(self, request):
        return False
