from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext


from .models import Question, Choice, User, Stock

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
# admin.site.register(Stock)


# @admin.register(Stock)
# # class StockAdmin(admin.ModelAdmin):
# #     # list_display = ('surname', 'name', 'remove_button')
# #     # search_fields = ('surname', 'name')
# #     # list_filter = ('surname', 'name')
# #
# #     def remove_button(self, obj):
# #         return '<a class="button" href="{}">Delete</a>'.format(reverse('admin:workers_worker_delete', args=[obj.pk]))
# #     remove_button.short_description = ''
# #     remove_button.allow_tags = True

class ArticleAdmin(admin.ModelAdmin):

    actions = ['make_published']

    def make_published(self, request, queryset):
        selected = queryset.update(rec_day_new='2000-01-01')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            selected,
        ) % selected, messages.SUCCESS)

    make_published.short_description = "Mark selected stories as published"

admin.site.register(Stock, ArticleAdmin)