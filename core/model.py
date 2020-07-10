'''
=================================================
@Author ：Andy
@Date   ：2020/7/8 11:57
==================================================
'''
import datetime
import pandas as pd
import warnings
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation, performance_metrics
from pyecharts.charts import Page
from pyecharts.globals import CurrentConfig

from .tools import RestDay, ProphetPlot

CurrentConfig.ONLINE_HOST = "resources/assets/"

warnings.filterwarnings("ignore")

class ProphetModel():
    def __init__(self, periods=30, metric = "mape", title = "", show_plot=True, show_point=True, show_cross=True, show_components=True):
        self.periods = periods
        self.show_plot = show_plot
        self.show_point = show_point
        self.show_cross = show_cross
        self.show_components = show_components
        self.title = title
        self.metric = metric
        self.forecast = None
        self.prophet = None
        self.future = None
        self.prophet_plot = None
        self.cv_data = None
        self.performance = None
        self.plot = None
        self.point_plot = None
        self.cross_plot = None
        self.components = None

    def fit(self,df,growth='linear', changepoints=None, n_changepoints=25, changepoint_range=0.8, yearly_seasonality='auto',
            weekly_seasonality='auto', daily_seasonality='auto', holidays=None, seasonality_mode='additive',
            seasonality_prior_scale=10.0, uncertainty_samples=1000, stan_backend=None):
        self.prophet = Prophet(growth=growth, changepoints=changepoints, n_changepoints=n_changepoints,
                          changepoint_range=changepoint_range, yearly_seasonality=yearly_seasonality,
                          weekly_seasonality=weekly_seasonality, daily_seasonality=daily_seasonality,
                          holidays=holidays, seasonality_mode=seasonality_mode, seasonality_prior_scale=seasonality_prior_scale,
                          uncertainty_samples=uncertainty_samples, stan_backend=stan_backend)
        data = df[['date', 'close']].rename(columns={'date': 'ds', 'close': 'y'})
        self.prophet.fit(data)
        self.future = self.prophet.make_future_dataframe(periods=self.periods)
        rest = RestDay()
        rest_day = rest.get_rest(pd.to_datetime(data['ds'].max()).year, (pd.to_datetime(data['ds'].max()) + datetime.timedelta(days=self.periods)).year)
        self.future = self.future[~self.future['ds'].isin(rest_day['ds'])]
        self.forecast = self.prophet.predict(self.future)
        self.prophet_plot = ProphetPlot(self.title)
        if self.show_plot:
            self.plot = self.prophet_plot.plot(self.prophet, self.forecast)
        if self.show_point:
            self.point_plot = self.prophet_plot.plot_point(self.prophet, self.forecast)
        if self.show_components:
            self.components = self.prophet.plot_components(self.forecast)

    def cross_validation(self, initial, period, horizon):
        self.cv_data = cross_validation(self.prophet, initial = initial, period = period, horizon = horizon)
        self.performance = performance_metrics(self.cv_data)
        if self.show_cross:
            pre_plot = self.prophet_plot.plot(self.prophet, self.cv_data)
            cross = self.prophet_plot.plot_cross_validation_metric(self.cv_data, self.metric)
            self.cross_plot = Page(layout=Page.SimplePageLayout)
            self.cross_plot.add(pre_plot)
            self.cross_plot.add(cross)