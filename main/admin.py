from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from main.predict import Predict
import datetime


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

    actions = ['calculation']

    def calculation(self, request, queryset):
        for item in queryset.values_list():
            print(item)
            predi = Predict(item[2])

            try:
                stock = Stock.objects.get(id=item[0])
                stock.price = predi.getPrice()
                print('price ok')
                stock.price_predict, stock.mape = predi.prediction_month(12)
                print('prediction_month(12)')
                stock.price_predict_6, mape = predi.prediction_month(6)
                print('prediction_month(6)')
                stock.price_predict_3, mape = predi.prediction_month(3)
                print('prediction_month(3)')

                date_now = datetime.datetime.now().date()
                print('date_now; ', date_now)
                dividend_date = stock.reg_day_future - datetime.timedelta(days=2)
                print('dividend_date; ', dividend_date)

                if dividend_date > date_now:
                    print('popal')
                    stock.rec_day_new = predi.recommend_date(dividend_date)
                    print('recommend_date')

                print('save')
                stock.save()
            except:
                pass






        # self.message_user(request, ngettext(
        #     '%d story was successfully marked as published.',
        #     '%d stories were successfully marked as published.',
        #     selected,
        # ) % selected, messages.SUCCESS)



    calculation.short_description = "рассчитать"

admin.site.register(Stock, ArticleAdmin)