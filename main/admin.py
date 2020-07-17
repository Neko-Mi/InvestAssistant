from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from main.predict import Predict
import datetime


from .models import Question, Choice, User, Stock, Answer

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
admin.site.register(Answer)


class ArticleAdmin(admin.ModelAdmin):

    actions = ['calculation']

    def calculation(self, request, queryset):
        for item in queryset.values_list():
            print(item)
            predi = Predict(item[2])

            try:
                stock = Stock.objects.get(id=item[0])
                stock.price = predi.getPrice()

                stock.price_predict, stock.mape = predi.prediction_month(12)
                stock.price_predict_6, mape = predi.prediction_month(6)
                stock.price_predict_3, mape = predi.prediction_month(3)

                date_now = datetime.datetime.now().date()
                dividend_date = stock.reg_day_future - datetime.timedelta(days=2)

                if dividend_date > date_now:
                    stock.rec_day_new = predi.recommend_date(dividend_date)

                stock.save()
            except:
                pass

    calculation.short_description = "рассчитать"

admin.site.register(Stock, ArticleAdmin)