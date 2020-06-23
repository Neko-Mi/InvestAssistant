import datetime
import pandas_datareader as pdr
import pandas as pd
from fbprophet import Prophet
import numpy as np

class Predict(object):

    def __init__(self, name):
        self.name = name
        self.load()
        self.data = self.get_data()


    def get_data(self):
        SBER = {"stock_name": self.name, "data":
            pd.read_csv("C:/Projects/diplom/InvestAssistant/main/data/" + self.name + ".csv", header=0,
                        parse_dates=True)}

        pred = pd.DataFrame()
        pred['ds'] = SBER['data'].Date
        pred['y'] = round(SBER['data'].Open, 2)
        pred['y'] = pd.to_numeric(pred['y'])
        pred = pred.dropna()

        return pred


    def load(self):
        aapl = pdr.get_data_yahoo(self.name,
                                  start=datetime.datetime(2010, 1, 1),
                                  end=datetime.datetime.now())
        aapl.to_csv('C:/Projects/diplom/InvestAssistant/main/data/' +
                    self.name + '.csv')


    def prediction(self, mult):
        X = self.data
        year = 252
        month = 21
        train_size = round(year * 3)
        val_size = round(month * 4)
        full_size = train_size + val_size

        # Fit prophet model
        m = Prophet()
        leng = len(X) - full_size
        X = X[leng:]
        m.fit(X[train_size:])

        # Create dataframe with the dates we want to predict
        future = m.make_future_dataframe(periods=mult * month)

        # Eliminate weekend from future dataframe
        future['day'] = future['ds'].dt.weekday
        future = future[future['day'] <= 4]

        # Predict
        forecast = m.predict(future)

        new_forecast = forecast.copy()
        cmp_df = forecast.set_index('ds')[['yhat', 'yhat_lower', 'yhat_upper']] \
            .join(X.set_index('ds'))
        cmp_df['e'] = cmp_df['y'] - cmp_df['yhat']
        cmp_df['p'] = 100 * cmp_df['e'] / cmp_df['y']
        mape = np.mean(abs(cmp_df[-train_size:]['p']))
        # print('MAPE', np.mean(abs(cmp_df[-train_size:]['p'])))


        return new_forecast, mape


    def prediction_month(self, mult):
        forecast, mape = self.prediction(mult)
        y = round(forecast['yhat'][-1:], 2)
        m = round(mape, 2)
        return y, m


    def recommend_date(self, date_future):
        date_now = datetime.datetime.now().date()
        days_to_dividend = date_future - date_now
        month = round(days_to_dividend.days / 21) + 1

        forecast, mape = self.prediction(month)

        date_now = date_now
        date_now = datetime.datetime.strftime(date_now, '%Y-%m-%d')
        date_future = datetime.datetime.strftime(date_future, '%Y-%m-%d')

        ind_start = forecast.index[forecast['ds'] == date_now].to_list()[0]
        ind_end = forecast.index[forecast['ds'] == date_future].to_list()[0]
        new_forecast = forecast[ind_start:ind_end]

        miny = min(new_forecast['yhat'])
        ind = forecast.index[forecast['yhat'] == miny].to_list()[0]
        min_date = forecast['ds'][ind]
        min_date = min_date.date()

        return min_date

    def getPrice(self):
        return self.data['y'][-1:]