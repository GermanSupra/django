from django.contrib import admin

from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "created_date", "updated_date", "show_image", "auction"]
    list_filter = ["created_at", "auction"]
    actions = ["make_auction_as_false", "make_auction_as_true"]
    fieldsets = (
        (
            "Общее", {
                "fields": ("title", "description", "user", "image"),
            }
         ),
        (
            "Финансы", {
                "fields": ("price", "auction"),
                "classes": ["collapse"]
            }
        )
    )

    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
