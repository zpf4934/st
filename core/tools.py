'''
=================================================
@Author ：Andy
@Date   ：2020/6/24 12:01
==================================================
'''

import warnings
from typing import List, Sequence, Union

import stockstats
import talib
import os
import inspect
import time
import datetime
import emoji
import random
import numpy as np
import pandas as pd
from core import plotK
from core.log_config import logger
from core.getData import Data
from fbprophet import Prophet
from fbprophet.diagnostics import performance_metrics
from pyecharts import options as opts
from pyecharts.charts import Kline, Line, Bar, Grid, Scatter, EffectScatter, Page
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig
from workalendar.asia import China


warnings.filterwarnings("ignore")

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)))
CurrentConfig.ONLINE_HOST = os.path.join(PROJECT_PATH, "core/resources/assets/")


# def plotK(data):
#     df = data[['date', 'open', 'high', 'low', 'close', 'volume']]
#     df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'},
#               inplace=True)
#     df.sort_values(by='date', ascending=True, inplace=True)
#     df['date'] = pd.to_datetime(df['date'])
#     df.set_index(['date'], inplace=True)
#     df = df.astype(float)
#
#     kwargs = dict(type='candle', mav=(2, 4, 6), volume=True, figratio=(19, 8), figscale=0.85)
#
#     mpf.plot(df, **kwargs, style='charles')

class Tools():
    def __init__(self):
        self.useful_target = []

    def calculate_ma(self, day_count: int, data):
        result: List[Union[float, str]] = []
        for i in range(len(data)):
            if i < day_count:
                result.append("-")
                continue
            sum_total = 0.0
            for j in range(day_count):
                sum_total += float(data[i - j][1])
            result.append(abs(float("%.3f" % (sum_total / day_count))))
        return result

    def add_tag(self, data, n_changepoints = 100):
        df = data[['date','open','close','low','high','volume']]

        m = Prophet(changepoint_range=0.9, n_changepoints = n_changepoints)
        m.fit(df[['date', 'close']].rename(columns={'date': 'ds', 'close': 'y'}))

        change_points = m.changepoints[np.abs(np.nanmean(m.params['delta'], axis=0)) >= 0.01].astype(str).values.tolist()

        df['tag'] = np.where(df['date'].isin(change_points), 1, 0)
        df.loc[0,'tag'] = 1
        return df

    def add_dif(self, data):
        result12: List[Union[float, str]] = []
        result26: List[Union[float, str]] = []

        df = data[['date','open','close','low','high','volume','amount']]
        array_df = df.values
        for i in range(len(array_df)):
            if i < 11:
                result12.append(np.nan)
            if i < 25:
                result26.append(np.nan)
            if i == 11:
                result12.append(array_df[:12, 2].astype(np.float).mean().round(2))
            if i == 25:
                result26.append(array_df[:26, 2].astype(np.float).mean().round(2))
            if i > 11:
                result12.append(((2 * float(array_df[i][2]) + 11 * result12[-1]) / 13).round(2))
            if i > 25:
                result26.append(((2 * float(array_df[i][2]) + 25 * result26[-1]) / 27).round(2))
        dif = [np.nan] * 25 + (np.array(result12[25:]) - np.array(result26[25:])).round(2).tolist()
        df['dif'] = dif
        return df

    def add_dea(self, data):
        dea: List[Union[float, str]] = []

        df = data[['date', 'open', 'close', 'low', 'high', 'volume', 'amount', 'dif']]
        array_df = df.values
        for i in range(len(array_df)):
            if i < 33:
                dea.append(np.nan)
            elif i == 33:
                dea.append(np.round(array_df[25:34, -1].mean(), 2))
            else:
                dea.append(np.round((2 * array_df[i][-1] + 8 * dea[-1]) / 10, 2))
        df['dea'] = dea
        return df

    def add_macd(self, data):
        macd: List[Union[float, str]] = []

        df = data[['date', 'open', 'close', 'low', 'high', 'volume', 'amount', 'dif', 'dea']]
        array_df = df.values
        for i in range(len(array_df)):
            if array_df[i][7] == np.nan or array_df[i][8] == np.nan:
                macd.append(np.nan)
                continue
            else:
                macd.append(np.round(2 * (array_df[i][7] - array_df[i][8]), 2))
        df['macd'] = macd
        return df

    def str_of_num(self, num):
        def strofsize(num, level):
            if level >= 2:
                return num, level
            elif num >= 10000:
                num /= 10000
                level += 1
                return strofsize(num, level)
            else:
                return num, level

        units = ['', '万', '亿']
        num, level = strofsize(num, 0)
        if level > len(units):
            level -= 1
        return '{}{}'.format(round(num, 3), units[level])

    def volume_ma(self, day_count: int, data):
        result: List[Union[float, str]] = []
        data = np.array(data, dtype=np.float)
        mean = np.mean(data)
        if '万' in self.str_of_num(mean):
            divisor = 10000
        elif '亿' in self.str_of_num(mean):
            divisor = 10000 * 10000
        else:
            divisor = 1

        for i in range(len(data)):
            if i < day_count:
                result.append("-")
                continue
            sum_total = 0.0
            for j in range(day_count):
                sum_total += float(data[i - j])
            result.append(abs(float("%.2f" % (sum_total / day_count / divisor))))
        return result

    def get_change_vol(self, data):
        data = np.array(data, dtype=np.float)
        mean = np.mean(data)
        if '万' in self.str_of_num(mean):
            self.label_name = "万手"
            return np.round(data/10000, 3).tolist()
        elif '亿' in self.str_of_num(mean):
            self.label_name = "亿手"
            return np.round(data/10000/10000, 3).tolist()
        else:
            self.label_name = "手"
            return data.tolist()

    def add_kdj(self, df):
        try:
            low_list = df['low'].rolling(9, min_periods=9).min()
            low_list.fillna(value=df['low'].expanding().min(), inplace=True)
            high_list = df['high'].rolling(9, min_periods=9).max()
            high_list.fillna(value=df['high'].expanding().max(), inplace=True)

            rsv = (df['close'] - low_list) / (high_list - low_list) * 100

            df['K'] = np.round(pd.DataFrame(rsv).ewm(com=2).mean(), 2)
            df['D'] = np.round(df['K'].ewm(com=2).mean(), 2)
            df['J'] = np.round(3 * df['K'] - 2 * df['D'], 2)
            self.useful_target.append('KDJ')
        except Exception as e:
            logger.error(e)
        return df

    def add_rsi(self, df):
        try:
            df['RSI1'] = np.round(talib.RSI(df.close, timeperiod=6), 2)
            df['RSI2'] = np.round(talib.RSI(df.close, timeperiod=12), 2)
            df['RSI3'] = np.round(talib.RSI(df.close, timeperiod=24), 2)
            self.useful_target.append('RSI')
        except Exception as e:
            logger.error(e)
        return df

    def add_boll(self, df):
        try:
            df['UPPER'], df['BOLL'], df['LOWER'] = talib.BBANDS(df.close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
            df['UPPER'] = np.round(df['UPPER'], 2)
            df['BOLL'] = np.round(df['BOLL'], 2)
            df['LOWER'] = np.round(df['LOWER'], 2)
            self.useful_target.append('BOLL')
        except Exception as e:
            logger.error(e)
        return df

    def add_wr(self, df):
        try:
            df['WR2'] = np.round(abs(talib.WILLR(df.high, df.low, df.close, timeperiod=6)), 2)
            df['WR1'] = np.round(abs(talib.WILLR(df.high, df.low, df.close, timeperiod=10)), 2)
            self.useful_target.append('WR')
        except Exception as e:
            logger.error(e)
        return df

    def add_dmi(self, df):
        try:
            df['PDI'] = np.round(talib.PLUS_DI(df.high, df.low, df.close), 2)
            df['MDI'] = np.round(talib.MINUS_DI(df.high, df.low, df.close), 2)
            df['ADX'] = np.round(talib.ADX(df.high, df.low, df.close) * 2, 2)
            df['ADXR'] = np.round(talib.ADXR(df.high, df.low, df.close) * 2, 2)
            self.useful_target.append('DMI')
        except Exception as e:
            logger.error(e)
        return df

    def add_bbiboll(self, df):
        try:
            df['BBIBOLL'] = np.round((talib.SMA(df.close, timeperiod=3) + talib.SMA(df.close, timeperiod=6) +
                                      talib.SMA(df.close, timeperiod=12) + talib.SMA(df.close, timeperiod=24)) / 4, 2)
            df['UPR'] = np.round(df['BBIBOLL'] + 3 * df['BBIBOLL'].rolling(10, min_periods=10).std(), 2)
            df['DWN'] = np.round(df['BBIBOLL'] - 3 * df['BBIBOLL'].rolling(10, min_periods=10).std(), 2)
            self.useful_target.append('BBIBOLL')
        except Exception as e:
            logger.error(e)
        return df

    def add_roc(self, df):
        try:
            df['ROC'] = np.round(talib.ROC(df.close, timeperiod=12), 2)
            df['MAROC'] = np.round(talib.SMA(df.ROC, timeperiod=6), 2)
            self.useful_target.append('ROC')
        except Exception as e:
            logger.error(e)
        return df

    def add_psy(self, df):
        try:
            difference = df.close[1:].values - df.close[:-1].values
            difference = np.append(0, difference)
            difference_dir = np.where(difference > 0, 1, 0)
            psy = np.zeros((len(df.close),))
            psy[:12] *= np.nan
            for i in range(12, len(df.close)):
                psy[i] = (difference_dir[i - 12 + 1:i + 1].sum()) / 12
            df['PSY'] = np.round(psy * 100, 2)
            df['PSYMA'] = np.round(talib.SMA(df['PSY'], timeperiod=6), 2)
            self.useful_target.append('PSY')
        except Exception as e:
            logger.error(e)
        return df

    def add_obv(self, df):
        try:
            df['OBV'] = np.round(talib.OBV(df.high, df.volume), 2)
            df['OBVMA'] = np.round(talib.SMA(df.OBV), 2)
            self.useful_target.append('OBV')
        except Exception as e:
            logger.error(e)
        return df

    def add_cci(self, df):
        try:
            df['CCI'] = np.round(talib.CCI(df.high, df.low, df.close), 2)
            self.useful_target.append('CCI')
        except Exception as e:
            logger.error(e)
        return df

    def add_trix(self, df):
        try:
            df['TRIX'] = np.round(talib.TRIX(df.close, timeperiod=12), 2)
            df['MATRIX'] = np.round(talib.SMA(df.TRIX, timeperiod=9), 2)
            self.useful_target.append('TRIX')
        except Exception as e:
            logger.error(e)
        return df

    def add_dma(self, df):
        try:
            df['DIF'] = np.round(
                df['close'].rolling(10, min_periods=10).mean() - df['close'].rolling(50, min_periods=50).mean(), 2)
            df['DIFMA'] = np.round(talib.SMA(df.DIF, timeperiod=10), 2)
            self.useful_target.append('DMA')
        except Exception as e:
            logger.error(e)
        return df

    def add_expma(self, df):
        try:
            df['EMA12'] = np.round(talib.EMA(df.close, timeperiod=12), 2)
            df['EMA50'] = np.round(talib.EMA(df.close, timeperiod=50), 2)
            self.useful_target.append('EXPMA')
        except Exception as e:
            logger.error(e)
        return df

    def add_bias(self, df):
        try:
            df['BIAS1'] = np.round(
                (df.close - talib.SMA(df.close, timeperiod=6)) / talib.SMA(df.close, timeperiod=6) * 100,
                2)
            df['BIAS2'] = np.round(
                (df.close - talib.SMA(df.close, timeperiod=12)) / talib.SMA(df.close, timeperiod=12) * 100, 2)
            df['BIAS3'] = np.round(
                (df.close - talib.SMA(df.close, timeperiod=24)) / talib.SMA(df.close, timeperiod=24) * 100, 2)
            self.useful_target.append('BIAS')
        except Exception as e:
            logger.error(e)
        return df

    def add_vr(self, df):
        try:
            stockStat = stockstats.StockDataFrame.retype(df)
            df = df.reset_index()
            df['VR'] = np.round(stockStat['vr'].values, 2)
            df.loc[df[df['VR'] == np.inf].index, 'VR'] = np.nan
            df['MAVR'] = np.round(talib.SMA(df.VR, timeperiod=6), 2)
            self.useful_target.append('VR')
        except Exception as e:
            logger.error(e)
        return df

    def get_target(self,df):
        df = df[['date','open','close','low','high','volume','amount']]
        df.dropna(inplace=True)
        df = df.astype({'open':np.float64,'close':np.float64,'low':np.float64,'high':np.float64,'volume':np.float64,'amount':np.float64})
        df = self.add_dif(df)
        df = self.add_dea(df)
        df = self.add_macd(df)
        self.useful_target.append('MACD')
        df = self.add_vr(df)
        df = self.add_kdj(df)
        df = self.add_rsi(df)
        df = self.add_boll(df)
        df = self.add_wr(df)
        df = self.add_dmi(df)
        df = self.add_bbiboll(df)
        df = self.add_roc(df)
        df = self.add_psy(df)
        df = self.add_obv(df)
        df = self.add_cci(df)
        df = self.add_trix(df)
        df = self.add_dma(df)
        df = self.add_expma(df)
        df = self.add_bias(df)
        cols = ['date','open','close','low','high','volume','amount','macd','dif','dea','VR','MAVR','K','D','J','RSI1',
                 'RSI2','RSI3','UPPER','BOLL','LOWER','WR2','WR1','PDI','MDI','ADX','ADXR','BBIBOLL','UPR','DWN','ROC',
                 'MAROC','PSY','PSYMA','OBV','OBVMA','CCI','TRIX','MATRIX','DIF','DIFMA','EMA12','EMA50','BIAS1','BIAS2',
                 'BIAS3']
        temp = []
        for col in cols:
            if col not in df.columns:
                temp.append(col)
        cols = list(set(cols) - set(temp))
        df = df[cols]
        return df


class ProfessionalKlineChart(Tools):
    def __init__(self, mark_line_show = False, title = "K线周期图表", target = 'all', width="98%",height="700px"):
        self.mark_line_show = mark_line_show
        self.title = title
        self.width = width
        self.height = height
        self.target = target
        self.useful_target = []

    def init_data(self, data):
        df = self.get_target(data)
        return df

    def split_data(self, origin_data) -> dict:
        spl_data = {}
        spl_data['datas'] = origin_data[['open','close','low','high','volume','amount']].values.tolist()
        spl_data['times'] = origin_data['date'].values.tolist()
        spl_data['vols'] = np.round(origin_data['volume'].values.tolist(), 0)
        spl_data['macds'] = origin_data['macd'].values.tolist()
        spl_data['difs'] = origin_data['dif'].values.tolist()
        spl_data['deas'] = origin_data['dea'].values.tolist()
        if 'VR' in self.useful_target:
            spl_data['VR'] = origin_data.VR.values.tolist()
            spl_data['MAVR'] = origin_data.MAVR.values.tolist()
        if 'KDJ' in self.useful_target:
            spl_data['K'] = origin_data.K.values.tolist()
            spl_data['D'] = origin_data.D.values.tolist()
            spl_data['J'] = origin_data.J.values.tolist()
        if 'RSI' in self.useful_target:
            spl_data['RSI1'] = origin_data.RSI1.values.tolist()
            spl_data['RSI2'] = origin_data.RSI2.values.tolist()
            spl_data['RSI3'] = origin_data.RSI3.values.tolist()
        if 'BOLL' in self.useful_target:
            spl_data['UPPER'] = origin_data.UPPER.values.tolist()
            spl_data['BOLL'] = origin_data.BOLL.values.tolist()
            spl_data['LOWER'] = origin_data.LOWER.values.tolist()
        if 'WR' in self.useful_target:
            spl_data['WR2'] = origin_data.WR2.values.tolist()
            spl_data['WR1'] = origin_data.WR1.values.tolist()
        if 'DMI' in self.useful_target:
            spl_data['PDI'] = origin_data.PDI.values.tolist()
            spl_data['MDI'] = origin_data.MDI.values.tolist()
            spl_data['ADX'] = origin_data.ADX.values.tolist()
            spl_data['ADXR'] = origin_data.ADXR.values.tolist()
        if 'BBIBOLL' in self.useful_target:
            spl_data['BBIBOLL'] = origin_data.BBIBOLL.values.tolist()
            spl_data['UPR'] = origin_data.UPR.values.tolist()
            spl_data['DWN'] = origin_data.DWN.values.tolist()
        if 'ROC' in self.useful_target:
            spl_data['ROC'] = origin_data.ROC.values.tolist()
            spl_data['MAROC'] = origin_data.MAROC.values.tolist()
        if 'PSY' in self.useful_target:
            spl_data['PSY'] = origin_data.PSY.values.tolist()
            spl_data['PSYMA'] = origin_data.PSYMA.values.tolist()
        if 'OBV' in self.useful_target:
            spl_data['OBV'] = origin_data.OBV.values.tolist()
            spl_data['OBVMA'] = origin_data.OBVMA.values.tolist()
        if 'CCI' in self.useful_target:
            spl_data['CCI'] = origin_data.CCI.values.tolist()
        if 'TRIX' in self.useful_target:
            spl_data['TRIX'] = origin_data.TRIX.values.tolist()
            spl_data['MATRIX'] = origin_data.MATRIX.values.tolist()
        if 'DMA' in self.useful_target:
            spl_data['DIF'] = origin_data.DIF.values.tolist()
            spl_data['DIFMA'] = origin_data.DIFMA.values.tolist()
        if 'EXPMA' in self.useful_target:
            spl_data['EMA12'] = origin_data.EMA12.values.tolist()
            spl_data['EMA50'] = origin_data.EMA50.values.tolist()
        if 'BIAS' in self.useful_target:
            spl_data['BIAS1'] = origin_data.BIAS1.values.tolist()
            spl_data['BIAS2'] = origin_data.BIAS2.values.tolist()
            spl_data['BIAS3'] = origin_data.BIAS3.values.tolist()
        return spl_data

    def split_data_part(self, data) -> Sequence:
        mark_line_data = []
        idx = 0
        tag = 0
        vols = 0
        for i in range(len(data["times"])):
            if data["datas"][i][5] != 0 and tag == 0:
                idx = i
                vols = data["datas"][i][4]
                tag = 1
            elif tag == 1:
                vols += data["datas"][i][4]
            if data["datas"][i][5] != 0 and tag == 1:
                idx = i
                vols = data["datas"][i][4]
                tag = 2
            elif tag == 2:
                vols += data["datas"][i][4]
            if data["datas"][i][5] != 0 and tag == 2:
                mark_line_data.append(
                    [
                        {
                            "xAxis": idx,
                            "yAxis": float("%.2f" % data["datas"][idx][3])
                            if data["datas"][idx][1] > data["datas"][idx][0]
                            else float("%.2f" % data["datas"][idx][2]),
                            "value": self.str_of_num(round(vols / (i - idx + 1), 2)),
                        },
                        {
                            "xAxis": i,
                            "yAxis": float("%.2f" % data["datas"][i][3])
                            if data["datas"][i][1] > data["datas"][i][0]
                            else float("%.2f" % data["datas"][i][2]),
                        },
                    ]
                )
                idx = i
                vols = data["datas"][i][4]
        return mark_line_data

    def macd(self,data):
        bar_2 = (
            Bar()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="MACD",
                y_axis=data["macds"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                itemstyle_opts=opts.ItemStyleOpts(
                    color=JsCode(
                        """
                            function(params) {
                                var colorList;
                                if (params.data >= 0) {
                                  colorList = '#ef232a';
                                } else {
                                  colorList = '#14b143';
                                }
                                return colorList;
                            }
                            """
                    )
                ),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        line_2 = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="DIF",
                y_axis=data["difs"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="DEA",
                y_axis=data["deas"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(color="#7D26CD", opacity=0.5, width=2),
            )
        )
        # 最下面的柱状图和折线图
        overlap_bar_line_2 = bar_2.overlap(line_2)

        return overlap_bar_line_2

    def kdj(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="K",
                y_axis=data["K"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="D",
                y_axis=data["D"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(color="#7D26CD",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="J",
                y_axis=data["J"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(color="#4F4F4F",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line


    def rsi(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="RSI1",
                y_axis=data["RSI1"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="RSI2",
                y_axis=data["RSI2"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="RSI3",
                y_axis=data["RSI3"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#4F4F4F",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def boll(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="BOLL",
                y_axis=data["BOLL"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="UPPER",
                y_axis=data["UPPER"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="LOWER",
                y_axis=data["LOWER"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#4F4F4F",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def wr(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="WR1",
                y_axis=data["WR1"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="WR2",
                y_axis=data["WR2"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def dmi(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="PDI",
                y_axis=data["PDI"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="MDI",
                y_axis=data["MDI"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="ADX",
                y_axis=data["ADX"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#4F4F4F",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="ADXR",
                y_axis=data["ADXR"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def bbiboll(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="BBIBOLL",
                y_axis=data["BBIBOLL"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="UPR",
                y_axis=data["UPR"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="DWN",
                y_axis=data["DWN"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#4F4F4F",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def roc(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="ROC",
                y_axis=data["ROC"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="MAROC",
                y_axis=data["MAROC"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def psy(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="PSY",
                y_axis=data["PSY"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="PSYMA",
                y_axis=data["PSYMA"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def obv(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="OBV",
                y_axis=data["OBV"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="OBVMA",
                y_axis=data["OBVMA"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def cci(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="CCI",
                y_axis=data["CCI"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def trix(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="TRIX",
                y_axis=data["TRIX"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="MATRIX",
                y_axis=data["MATRIX"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def dma(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="DIF",
                y_axis=data["DIF"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="DIFMA",
                y_axis=data["DIFMA"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def expma(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="EMA12",
                y_axis=data["EMA12"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="EMA50",
                y_axis=data["EMA50"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def bias(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="BIAS1",
                y_axis=data["BIAS1"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="BIAS2",
                y_axis=data["BIAS2"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="BIAS3",
                y_axis=data["BIAS3"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#4F4F4F",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def vr(self, data):
        line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="VR",
                y_axis=data["VR"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#0000FF",opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="MAVR",
                y_axis=data["MAVR"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(
                color="#7D26CD",opacity=0.5, width=2),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=2,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    grid_index=2,
                    split_number=4,
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top='1.4%', orient='horizontal'),
            )
        )

        return line

    def draw_chart(self, data):
        kline = (
            Kline()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="KLine",
                y_axis=data["datas"],
                itemstyle_opts=opts.ItemStyleOpts(
                    color="#ef232a",
                    color0="#14b143",
                    border_color="#ef232a",
                    border_color0="#14b143",
                ),
                markpoint_opts=opts.MarkPointOpts(
                    data=[
                        opts.MarkPointItem(type_="max", name="最大值"),
                        opts.MarkPointItem(type_="min", name="最小值"),
                    ],
                    label_opts=opts.LabelOpts(position="inside", color="#000000")
                ),
                # markline_opts=opts.MarkLineOpts(
                #     label_opts=opts.LabelOpts(
                #         position="middle", color="blue", font_size=12, is_show = self.mark_line_show
                #     ),
                #     data=self.split_data_part(data),
                #     symbol=["circle", "none"],
                # ),
            )
            #     .set_series_opts(
            #     markarea_opts=opts.MarkAreaOpts(is_silent=True, data=self.split_data_part(data))
            # )
                .set_global_opts(
                title_opts=opts.TitleOpts(title=self.title, pos_left="0"),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    is_scale=True,
                    grid_index=0,
                    boundary_gap=False,
                    axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                    split_number=20,
                    min_="dataMin",
                    max_="dataMax",
                ),
                yaxis_opts=opts.AxisOpts(
                    is_scale=True,
                    grid_index=0,
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    name="价格",
                    type_="value",
                    axislabel_opts=opts.LabelOpts(formatter="{value} ¥")
                ),
                datazoom_opts=[
                    opts.DataZoomOpts(
                        is_show=False, type_="inside", xaxis_index=[0, 0, 0], range_start=90, range_end=100
                    ),
                    opts.DataZoomOpts(
                        is_show=True, xaxis_index=[0, 1, 2], pos_top="97%", range_start=90, range_end=100
                    ),
                    opts.DataZoomOpts(is_show=False, xaxis_index=[0, 1, 2], pos_top = '5%', range_start=90, range_end=100),
                ],
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis",
                    axis_pointer_type="cross",
                    background_color="rgba(245, 245, 245, 0.8)",
                    border_width=1,
                    border_color="#ccc",
                    textstyle_opts=opts.TextStyleOpts(color="#000"),
                ),
                axispointer_opts=opts.AxisPointerOpts(
                    is_show=True,
                    link=[{"xAxisIndex": "all"}],
                    label=opts.LabelOpts(background_color="#777"),
                ),
                toolbox_opts=opts.ToolboxOpts(is_show=True,
                                              pos_top="4%",
                                              pos_left='right',
                                              feature={
                                                  "saveAsImage": {"name":self.title, "type":"jpeg"},
                                                  "dataView": {},
                                                  "restore": {},
                                              }),
                legend_opts=opts.LegendOpts(is_show=True, pos_left='40%', pos_top='1.4%', orient='horizontal'),
            )
        )

        kline_line = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="MA5",
                y_axis=self.calculate_ma(day_count=5, data=data['datas']),
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                series_name="MA10",
                y_axis=self.calculate_ma(day_count=10, data=data['datas']),
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                series_name="MA20",
                y_axis=self.calculate_ma(day_count=20, data=data['datas']),
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                series_name="MA30",
                y_axis=self.calculate_ma(day_count=30, data=data['datas']),
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=0,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    grid_index=0,
                    split_number=3,
                    axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                    axislabel_opts=opts.LabelOpts(is_show=True),
                ),
            )
        )
        # Overlap Kline + Line
        overlap_kline_line = kline.overlap(kline_line)

        # Bar-1
        bar_1 = (
            Bar()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="Volumn",
                y_axis=self.get_change_vol(data['vols']),
                xaxis_index=1,
                yaxis_index=1,
                label_opts=opts.LabelOpts(is_show=False),
                itemstyle_opts=opts.ItemStyleOpts(
                    color=JsCode(
                        """
                    function(params) {
                        var colorList;
                        if (barData[params.dataIndex][1] > barData[params.dataIndex][0]) {
                            colorList = '#ef232a';
                        } else {
                            colorList = '#14b143';
                        }
                        return colorList;
                    }
                    """
                    )
                ),
            )
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    grid_index=1,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    name=self.label_name,
                    type_="value",
                    axislabel_opts=opts.LabelOpts(formatter="{value}"),
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_left='15%', pos_top = '1.4%', orient='horizontal'),
            )
        )

        line_1 = (
            Line()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="VOL5",
                y_axis=self.volume_ma(day_count=5, data=data['vols']),
                xaxis_index=1,
                yaxis_index=1,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="VOL10",
                y_axis=self.volume_ma(day_count=10, data=data['vols']),
                xaxis_index=1,
                yaxis_index=1,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
            )
        )

        overlap_bar_line_1 = bar_1.overlap(line_1)
        if self.target == 'all':
            result = {}
            for i in ['MACD','KDJ','RSI','BOLL','WR','DMI','BBIBOLL','ROC','PSY','OBV','CCI','TRIX','DMA','EXPMA','BIAS','VR']:
                if i == 'MACD':
                    target = self.macd(data)
                elif i == 'KDJ':
                    target = self.kdj(data)
                elif i == 'RSI':
                    target = self.rsi(data)
                elif i == 'BOLL':
                    target = self.boll(data)
                elif i == 'WR':
                    target = self.wr(data)
                elif i == 'DMI':
                    target = self.dmi(data)
                elif i == 'BBIBOLL':
                    target = self.bbiboll(data)
                elif i == 'ROC':
                    target = self.roc(data)
                elif i == 'PSY':
                    target = self.psy(data)
                elif i == 'OBV':
                    target = self.obv(data)
                elif i == 'CCI':
                    target = self.cci(data)
                elif i == 'TRIX':
                    target = self.trix(data)
                elif i == 'DMA':
                    target = self.dma(data)
                elif i == 'EXPMA':
                    target = self.expma(data)
                elif i == 'BIAS':
                    target = self.bias(data)
                elif i == 'VR':
                    target = self.vr(data)

                # 最后的 Grid
                grid_chart = Grid(init_opts=opts.InitOpts(width=self.width, height=self.height))

                # 这个是为了把 data.datas 这个数据写入到 html 中,还没想到怎么跨 series 传值
                # demo 中的代码也是用全局变量传的
                grid_chart.add_js_funcs("var barData = {}".format(data["datas"]))

                # K线图和 MA5 的折线图
                grid_chart.add(
                    overlap_kline_line,
                    grid_opts=opts.GridOpts(pos_left="4%", pos_right="1%", height="55%"),
                )
                # Volumn 柱状图
                grid_chart.add(
                    overlap_bar_line_1,
                    grid_opts=opts.GridOpts(
                        pos_left="4%", pos_right="1%", pos_top="70%", height="10%"
                    ),
                )
                # MACD DIFS DEAS
                grid_chart.add(
                    target,
                    grid_opts=opts.GridOpts(
                        pos_left="4%", pos_right="1%", pos_top="82%", height="14%"
                    ),
                )

                result[i] = grid_chart
            return  result
        else:
            if self.target not in self.useful_target:
                self.target = 'MACD'
            if self.target == 'MACD':
                target = self.macd(data)
            elif self.target == 'KDJ':
                target = self.kdj(data)
            elif self.target == 'RSI':
                target = self.rsi(data)
            elif self.target == 'BOLL':
                target = self.boll(data)
            elif self.target == 'WR':
                target = self.wr(data)
            elif self.target == 'DMI':
                target = self.dmi(data)
            elif self.target == 'BBIBOLL':
                target = self.bbiboll(data)
            elif self.target == 'ROC':
                target = self.roc(data)
            elif self.target == 'PSY':
                target = self.psy(data)
            elif self.target == 'OBV':
                target = self.obv(data)
            elif self.target == 'CCI':
                target = self.cci(data)
            elif self.target == 'TRIX':
                target = self.trix(data)
            elif self.target == 'DMA':
                target = self.dma(data)
            elif self.target == 'EXPMA':
                target = self.expma(data)
            elif self.target == 'BIAS':
                target = self.bias(data)
            elif self.target == 'VR':
                target = self.vr(data)
            else:
                logger.error(self.target + ' is not in target')
                return
            # 最后的 Grid
            grid_chart = Grid(init_opts=opts.InitOpts(width=self.width, height=self.height))

            # 这个是为了把 data.datas 这个数据写入到 html 中,还没想到怎么跨 series 传值
            # demo 中的代码也是用全局变量传的
            grid_chart.add_js_funcs("var barData = {}".format(data["datas"]))

            # K线图和 MA5 的折线图
            grid_chart.add(
                overlap_kline_line,
                grid_opts=opts.GridOpts(pos_left="4%", pos_right="1%", height="55%"),
            )
            # Volumn 柱状图
            grid_chart.add(
                overlap_bar_line_1,
                grid_opts=opts.GridOpts(
                    pos_left="4%", pos_right="1%", pos_top="70%", height="10%"
                ),
            )
            # MACD DIFS DEAS
            grid_chart.add(
                target,
                grid_opts=opts.GridOpts(
                    pos_left="4%", pos_right="1%", pos_top="82%", height="14%"
                ),
            )
            return grid_chart

    def draw(self, data):
        data = data.replace('',np.nan)
        data.dropna(subset=['close'], inplace=True)
        if data.size == 0:
            return None
        df = self.init_data(data)
        df = df.fillna('_')
        spl_data = self.split_data(origin_data=df)

        return self.draw_chart(spl_data)

class JieQi():
    def __init__(self):
        self.c_list=[]
        self.C_list_21 = [3.87, 18.73, 5.63, 20.646, 4.81, 20.1, 5.52, 21.04, 5.678, 21.37, 7.108, 22.83,
                          7.5, 23.13, 7.646, 23.042, 8.318, 23.438, 7.438, 22.36, 7.18, 21.94, 5.4055, 20.12]
        self.C_list_20 = [4.6295, 19.4599, 6.3826, 21.4155, 5.59,20.888, 6.318, 21.86, 6.5, 22.2, 7.928,
                          23.65, 8.35,  23.95, 8.44, 23.822, 9.098, 24.218, 8.218, 23.08, 7.9, 22.6, 6.11, 20.84]
        self.name_Arr = ["立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
                         "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"]
        self.result = pd.DataFrame()

    ## 特殊年份特殊节气进行纠正
    def rectify_year(self,year,jieqiid,day):
        ## 特殊年份
        rectify_year = [2026,2084,1911,2008,1902,1928,1925,2016,1922,2002,1927,1942,2089,2089,1978,1954,1918,2021,1982,2082,2019,2021]
        ## 特殊节气
        rectify_jieqi = [1,3,6,7,8,9,10,10,11,12,14,15,17,18,19,20,21,21,22,22,23]
        ## 偏移量
        rectify_offset = [-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,1,-1,1]
        pop2 = -1
        if year in rectify_year:
            if year == 2089:
                pop1 = rectify_year.index(year) ## 找到位置
                pop2 = pop1+1
            else:
                pop1 = rectify_year.index(year) ## 找到位置

            if rectify_jieqi[pop1] == jieqiid:
                day = day + int(rectify_offset[pop1])
            if rectify_jieqi[pop2] == jieqiid:
                day = day + int(rectify_offset[pop2])
        return day


    #计算节气日期，并创建文件
    def creat_year_jieqi(self,year):
            year_pre = year//100
            if year_pre == 19:
                C_arr = self.C_list_20
            elif year_pre == 20:
                C_arr = self.C_list_21

            year_num = year%100
            list_arr = []
            for i in range(0, 24):
                C = C_arr[i]
                ## 注意：凡闰年3月1日前闰年数要减一，即：L=[(Y-1)/4],因为小寒、大寒、立春、雨水这两个节气都小于3月1日,所以 y = y-1
                if i == 0 or i == 1 or i == 22 or i == 23:
                    if self.comrun(year):
                        days = (year_num * 0.2422 + C) // 1 - ((year_num-1)// 4)
                    else:
                        days = (year_num * 0.2422 + C) // 1 - (year_num // 4)
                else:
                    days = (year_num * 0.2422 + C) // 1 - (year_num // 4)

                ## 特殊年份节气进行纠正
                days = self.rectify_year(year,i,days)

                days = int(days)
                days = '%02d' % days
                y = int(year_num // 1)
                m = i // 2 + 2
                if m == 13:
                    m = 1
                m = '%02d' % m
                y = '%02d' % y
                strs = "{3}{0}-{1}-{2}".format(str(y), str(m), str(days),str(year_pre))
                item = dict(year=str(year), name=self.name_Arr[i], jieqiid=str(i + 1), time=strs)
                self.result = self.result.append(item, ignore_index=True)

    ## 算是否是闰年
    def comrun(self,year):
        i = 0
        if (year % 4) != 0 :
            i=0
        elif ((year % 100) == 0) & ((year % 400) != 0):
            i=0
        else:
            i=1
        return i

    def get_jieqi(self, start = 1900, end = 2100):
        jieqi = JieQi()
        year_list = tqdm(list(range(start,end)))
        for year in year_list:
            year_list.set_description(f"计算{year}年节气")
            jieqi.creat_year_jieqi(year)
        return jieqi.result

class RestDay():
    def date_to_week(self, start_time, end_time):
        df = pd.DataFrame()
        df['ds'] = pd.date_range(start=start_time, end=end_time)
        df['holiday'] = df['ds'].dt.dayofweek + 1
        df = df[(df['holiday'] == 6) | (df['holiday'] == 7)]
        df['holiday'] = df['holiday'].replace({6: 'Saturday', 7: 'Sunday'})
        df['ds'] = df['ds'].map(lambda x: x.strftime('%Y-%m-%d'))
        return df

    def cal_festival(self, years):
        cal = China()
        lis = []
        assert isinstance(years, list), "years must be list"
        for ye in years:
            for x, v in cal.holidays(ye):
                lis.append([x.strftime('%Y-%m-%d'), v])
        df = pd.DataFrame(data=lis, columns=['ds', 'holiday'])
        return df

    def get_rest(self, start_year, end_year):
        years = list(range(start_year, end_year + 1))
        weekend = self.date_to_week(str(start_year), str(end_year + 1))
        try:
            holiday = self.cal_festival(years)
        except Exception as e:
            logger.error(e)
        result = pd.concat([weekend, holiday], ignore_index=1)
        result.drop_duplicates('ds', keep='last', inplace=True)
        return result

class ProphetPlot():
    def __init__(self, title = "", width="98%",height="700px"):
        self.title = title
        self.width = width
        self.height = height

    def plot(self, m, forecast):
        diff_values = np.round(forecast['yhat_upper'] - forecast['yhat_lower'], 2).tolist()

        line = (Line()
            .add_xaxis(xaxis_data=forecast['ds'].astype(str).tolist())
            .add_yaxis(
            series_name="yhat_lower",
            stack="总量",
            y_axis=np.round(forecast['yhat_lower'], 2).tolist(),
            is_smooth=True,
            is_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(is_show=True, opacity=0),
        )
            .add_yaxis(
            series_name="diff",
            stack="总量",
            y_axis=diff_values,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.3),
            is_smooth=True,
            is_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(is_show=True, opacity=0)
        )
        )

        line1 = (Line()
            .add_xaxis(xaxis_data=forecast['ds'].astype(str).tolist())
            .add_yaxis(
            series_name="yhat",
            y_axis=np.round(forecast['yhat'], 2).tolist(),
            is_smooth=True,
            is_symbol_show=True,
            symbol_size=5,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(is_show=True, opacity=1, width=2),
        )
        )

        if 'y' in forecast.columns:
            new_data = forecast
        else:
            new_data = pd.merge(forecast, m.history, how='left', on='ds')[['ds', 'y']]

        scatter = (
            Scatter(init_opts=opts.InitOpts(width=self.width, height=self.height))
                .add_xaxis(new_data['ds'].astype(str).tolist())
                .add_yaxis(series_name="price",
                           y_axis=np.round(new_data['y'], 2).tolist(),
                           symbol_size=3,
                           label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title=self.title),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    min_="dataMin",
                    max_="dataMax",
                    grid_index=0,
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                toolbox_opts=opts.ToolboxOpts(is_show=True,
                                              feature={
                                                  "saveAsImage": {"name": self.title, "type": "jpeg"},
                                                  "dataView": {},
                                                  "restore": {},
                                              }),
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis",
                    axis_pointer_type="cross",
                    background_color="rgba(245, 245, 245, 0.8)",
                    border_width=1,
                    border_color="#ccc",
                    textstyle_opts=opts.TextStyleOpts(color="#000"),
                ),
                datazoom_opts=[
                    opts.DataZoomOpts(
                        is_show=False,
                        xaxis_index=0,
                        type_="inside",
                        range_start=0,
                        range_end=100,
                    ),
                    opts.DataZoomOpts(
                        is_show=True,
                        xaxis_index=0,
                        type_="slider",
                        range_start=0,
                        range_end=100,
                    ),
                ],
            )
        )
        lines = line.overlap(line1)
        scatter_line = scatter.overlap(lines)
        return scatter_line

    def get_changes_point(self, m, forecast):
        changepoints = m.changepoints[np.abs(np.nanmean(m.params['delta'], axis=0)) >= 0.01].astype(str).values.tolist()
        mark_point_date = []
        for point in changepoints:
            mark_point_date.append(
                {'xAxis': point, 'yAxis': np.round(m.history.loc[m.history['ds'] == point]['y'].values[0], 2),
                 'value': np.round(m.history.loc[m.history['ds'] == point]['y'].values[0], 2)})
        return mark_point_date

    def plot_point(self, m, forecast):

        mark_point_date = self.get_changes_point(m, forecast)

        diff_values = np.round(forecast['yhat_upper'] - forecast['yhat_lower'], 2).tolist()

        line = (Line()
            .add_xaxis(xaxis_data=forecast['ds'].astype(str).tolist())
            .add_yaxis(
            series_name="yhat_lower",
            stack="总量",
            y_axis=np.round(forecast['yhat_lower'], 2).tolist(),
            is_smooth=True,
            is_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(is_show=True, opacity=0),
        )
            .add_yaxis(
            series_name="diff",
            stack="总量",
            y_axis=diff_values,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.3),
            is_smooth=True,
            is_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(is_show=True, opacity=0)
        )
        )

        line1 = (Line()
            .add_xaxis(xaxis_data=forecast['ds'].astype(str).tolist())
            .add_yaxis(
            series_name="yhat",
            y_axis=np.round(forecast['yhat'], 2).tolist(),
            is_smooth=True,
            is_symbol_show=True,
            symbol_size=5,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(is_show=True, opacity=1, width=2),
            markpoint_opts=opts.MarkPointOpts(
                data=mark_point_date,
                symbol='pin',
                # symbol_size=10,
            ),
        )
        )

        new_data = pd.merge(forecast, m.history, how='left', on='ds')[['ds', 'y']]

        scatter = (
            Scatter(init_opts=opts.InitOpts(width=self.width, height=self.height))
                .add_xaxis(new_data['ds'].astype(str).tolist())
                .add_yaxis(series_name="price",
                           y_axis=np.round(new_data['y'], 2).tolist(),
                           symbol_size=3,
                           label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title=self.title),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    min_="dataMin",
                    max_="dataMax",
                    grid_index=0,
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                toolbox_opts=opts.ToolboxOpts(is_show=True,
                                              feature={
                                                  "saveAsImage": {"name": self.title, "type": "jpeg"},
                                                  "dataView": {},
                                                  "restore": {},
                                              }),
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis",
                    axis_pointer_type="cross",
                    background_color="rgba(245, 245, 245, 0.8)",
                    border_width=1,
                    border_color="#ccc",
                    textstyle_opts=opts.TextStyleOpts(color="#000"),
                ),
                datazoom_opts=[
                    opts.DataZoomOpts(
                        is_show=False,
                        xaxis_index=0,
                        type_="inside",
                        range_start=50,
                        range_end=100,
                    ),
                    opts.DataZoomOpts(
                        is_show=True,
                        xaxis_index=0,
                        type_="slider",
                        range_start=50,
                        range_end=100,
                    ),
                ],
            )
        )
        lines = line.overlap(line1)
        scatter_line = scatter.overlap(lines)
        return scatter_line

    def plot_cross_validation_metric(self, df_cv, metric, rolling_window=0.1):
        df_none = performance_metrics(df_cv, metrics=[metric], rolling_window=-1)
        df_h = performance_metrics(df_cv, metrics=[metric], rolling_window=0.1)

        # Some work because matplotlib does not handle timedelta
        # Target ~10 ticks.
        tick_w = max(df_none['horizon'].astype('timedelta64[ns]')) / 10.
        # Find the largest time resolution that has <1 unit per bin.
        dts = ['D', 'h', 'm', 's', 'ms', 'us', 'ns']
        dt_names = [
            'days', 'hours', 'minutes', 'seconds', 'milliseconds', 'microseconds',
            'nanoseconds'
        ]
        dt_conversions = [
            24 * 60 * 60 * 10 ** 9,
            60 * 60 * 10 ** 9,
            60 * 10 ** 9,
            10 ** 9,
            10 ** 6,
            10 ** 3,
            1.,
        ]
        for i, dt in enumerate(dts):
            if np.timedelta64(1, dt) < np.timedelta64(tick_w, 'ns'):
                break

        x_plt = df_none['horizon'].astype('timedelta64[ns]').astype(np.int64) / float(dt_conversions[i])
        x_plt_h = df_h['horizon'].astype('timedelta64[ns]').astype(np.int64) / float(dt_conversions[i])
        scatter = (
            Scatter(init_opts=opts.InitOpts(width=self.width, height=self.height))
                .add_xaxis(x_plt.values.tolist())
                .add_yaxis(series_name=metric,
                           y_axis=np.round(df_none[metric], 2).tolist(),
                           symbol_size=3,
                           label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title=self.title),
                xaxis_opts=opts.AxisOpts(
                    type_="value",
                    grid_index=0,
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis",
                    axis_pointer_type="cross",
                    background_color="rgba(245, 245, 245, 0.8)",
                    border_width=1,
                    border_color="#ccc",
                    textstyle_opts=opts.TextStyleOpts(color="#000"),
                ),
                toolbox_opts=opts.ToolboxOpts(is_show=True,
                                              feature={
                                                  "saveAsImage": {"name": self.title, "type": "jpeg"},
                                                  "dataView": {},
                                                  "restore": {},
                                              }),
                datazoom_opts=[
                    opts.DataZoomOpts(
                        is_show=False,
                        xaxis_index=0,
                        type_="inside",
                        range_start=50,
                        range_end=100,
                    ),
                    opts.DataZoomOpts(
                        is_show=True,
                        xaxis_index=0,
                        type_="slider",
                        range_start=50,
                        range_end=100,
                    ),
                ],
            )
        )
        line = (Line()
            .add_xaxis(xaxis_data=x_plt_h.values.tolist())
            .add_yaxis(
            series_name=metric + "_avg",
            y_axis=np.round(df_h[metric], 2).tolist(),
            is_smooth=True,
            is_symbol_show=False,
            symbol_size=5,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(is_show=True, opacity=1, width=2),
            )
        )
        return scatter.overlap(line)

class PlotPE():
    def each(self,x, y, name):
        e = (
            Scatter()
            .add_xaxis([x])
            .add_yaxis(name, [y],itemstyle_opts=opts.ItemStyleOpts(color="#FFFFFF"),
                      label_opts = opts.LabelOpts(is_show=False))
        )
        return e

    def drew(self, df, name = "PE"):
        if name == "PE":
            col = 'peTTM'
            percen = 'PEpercentile'
        else:
            col = 'peTTM'
            percen = 'PBpercentile'
        if df.size == 0:
            logger.error("df is NULL")
            return
        else:
            i = 0
            for index in df.index:
                i += 1
                if i == 1:
                    code = df.loc[index,'code']
                    x = float(df.loc[index,percen])
                    y = float(df.loc[index,col])
                    base = (
                        Scatter(init_opts=opts.InitOpts(width="97%", height="700px"))
                            .add_xaxis([x])
                            .add_yaxis(code, [y], symbol_size=8, itemstyle_opts=opts.ItemStyleOpts(color="#FFFFFF"),
                                       label_opts=opts.LabelOpts(is_show=False))
                            .set_series_opts(
                            markline_opts=opts.MarkLineOpts(is_silent=True,
                                                            data=[{"xAxis": 0.7}, {"xAxis": 0.3}, {"yAxis": 20}],
                                                            linestyle_opts=opts.LineStyleOpts(color="#00FF00")),
                            markarea_opts=opts.MarkAreaOpts(
                                is_silent=True,
                                data=[[{"xAxis": 0, "yAxis": 20, "itemStyle": {"color": "#0000CD"}},
                                       {"xAxis": 0.3, "yAxis": 0}],
                                      [{"xAxis": 0, "yAxis": 100, "itemStyle": {"color": "#FFA500"}},
                                       {"xAxis": 0.3, "yAxis": 20}],
                                      [{"xAxis": 0.3, "yAxis": 20, "itemStyle": {"color": "#FFA500"}},
                                       {"xAxis": 0.7, "yAxis": 0}],
                                      [{"xAxis": 0.3, "yAxis": 100, "itemStyle": {"color": "#FFA500"}},
                                       {"xAxis": 0.7, "yAxis": 20}],
                                      [{"xAxis": 0.7, "yAxis": 20, "itemStyle": {"color": "#FFA500"}},
                                       {"xAxis": 1, "yAxis": 0}],
                                      [{"xAxis": 0.7, "yAxis": 100, "itemStyle": {"color": "#DC143C"}},
                                       {"xAxis": 1, "yAxis": 20}]]
                            )
                        )
                            .set_global_opts(title_opts=opts.TitleOpts(title=name),
                                             xaxis_opts=opts.AxisOpts(type_="value", min_=0, max_=1),
                                             yaxis_opts=opts.AxisOpts(type_="value", min_=0, max_=100, name=name),
                                             legend_opts=opts.LegendOpts(is_show=False),
                                             tooltip_opts=opts.TooltipOpts(
                                                 trigger="axis",
                                                 axis_pointer_type="cross",
                                                 background_color="rgba(245, 245, 245, 0.8)",
                                                 border_width=1,
                                                 border_color="#ccc",
                                                 textstyle_opts=opts.TextStyleOpts(color="#000"),
                                             ),
                                             toolbox_opts=opts.ToolboxOpts(is_show=True,
                                                                           pos_top="4%",
                                                                           pos_left='right',
                                                                           feature={
                                                                               "saveAsImage": {"name": name,
                                                                                               "type": "jpeg"},
                                                                               "dataView": {},
                                                                               "restore": {},
                                                                           }),
                                             )
                    )
                else:
                    code = df.loc[index, 'code']
                    x = float(df.loc[index, percen])
                    y = float(df.loc[index, col])
                    e = self.each(x, y, code)
                    base = base.overlap(e)
            return base

    def get_cache(self,  clear_cache = False):
        if clear_cache:
            return None
        mark_cache_path = os.path.join(PROJECT_PATH, 'mark_cache', 'PEPB.npz')
        if os.path.exists(mark_cache_path):
            cache_data = np.load(mark_cache_path, allow_pickle = True)
        else:
            cache_data = None
        return cache_data

    def save_cache(self):
        if self.cache_data is None:
            return
        mark_cache_path = os.path.join(PROJECT_PATH, 'mark_cache')
        if not os.path.exists(mark_cache_path):
            os.makedirs(mark_cache_path)
        np.savez(os.path.join(mark_cache_path, 'PEPB.npz'), **self.cache_data)

    def down_data(self, code):
        i = 0
        if self.cache_data:
            self.cache_data = dict(self.cache_data)
            if code in self.cache_data.keys():
                df = pd.DataFrame(self.cache_data.get(code), columns = ['date','peTTM','pbMRQ'])
                date = df['date'].max()
                date = (pd.to_datetime(date) + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            else:
                date = '1990-01-01'
        else:
            self.cache_data = {}
            date = '1990-01-01'
        if date <= datetime.datetime.now().strftime('%Y-%m-%d'):
            while i < 3:
                try:
                    data = Data(code, start=date)
                    data.get_query_history_k_data_plus()
                    i = 3
                except Exception as e:
                    logger.error(e)
                    time.sleep(random.randint(0, 5))
                    i += 1
            data.query_history_k_data_plus = data.query_history_k_data_plus[['date','peTTM','pbMRQ']]
            data.query_history_k_data_plus.replace('', np.nan, inplace=True)
            data.query_history_k_data_plus.dropna(subset=['peTTM','pbMRQ'], inplace = True)
            if code not in self.cache_data.keys():
                if data.query_history_k_data_plus.size > 0:
                    self.cache_data[code] = data.query_history_k_data_plus
                    return data.query_history_k_data_plus
                else:
                    return None
            else:
                self.cache_data[code] = pd.concat([df, data.query_history_k_data_plus], ignore_index = True)
                return self.cache_data[code]
        return df


    def drew_pe(self, code = None):
        code_list = []
        if code is not None:
            if isinstance(code,str):
                if code == 'all':
                    df = pd.read_csv(os.path.join(PROJECT_PATH,'data_info','证券资料.csv'))
                    df = df[~df['code_name'].str.contains('ST') & (df['type'] == 1) & (df['status'] == 1)]
                    code_list = df['code'].values.tolist()
                else:
                    code_list = [code]
            elif isinstance(code,list):
                code_list = code
            else:
                logger.error("code type is error")
                return
        else:
            logger.error("code is None")
            return
        result = pd.DataFrame(columns = ['code','peTTM','PEpercentile','pbMRQ','PBpercentile'])
        start = time.time()
        self.cache_data = self.get_cache()
        for i in range(len(code_list)):
            plotK.clearout()
            end = time.time()
            logger.info('\r' + '进度{} {}/{}:[{}]{:.2f}% {:.2f}s'.format(code_list[i],
                                                                 i + 1,
                                                                 len(code_list),
                                                                 emoji.emojize(':rocket:') * int(
                                                                     (i + 1) * 30 / len(code_list)) + '   ' * int(
                                                                     (1 - ((i + 1) / len(code_list))) * 30),
                                                                 float((i + 1) / len(code_list) * 100),
                                                                 end - start
                                                                 ),
                  )
            data = self.down_data(code_list[i])
            data.sort_values(by = 'date',inplace=True)
            data.reset_index(drop = True, inplace = True)
            col_data = data.dropna(subset = ['peTTM'])['peTTM'].values.tolist()
            col_data = [float(i) for i in col_data]
            col_data = sorted(list(set(col_data)))
            pevalue = float(data.loc[data.index.max(),'peTTM'])
            if pevalue is np.nan:
                continue
            index = col_data.index(pevalue) + 1
            PEpercentile = np.round(index/(len(col_data) + 1), 2)

            col_data = data.dropna(subset=['pbMRQ'])['pbMRQ'].values.tolist()
            col_data = [float(i) for i in col_data]
            col_data = sorted(list(set(col_data)))
            pbvalue = float(data.loc[data.index.max(), 'pbMRQ'])
            if pbvalue is np.nan:
                continue
            index = col_data.index(pbvalue) + 1
            PBpercentile = np.round(index / (len(col_data) + 1), 2)

            if result.index.max() is np.nan:
                index = 0
            else:
                index = result.index.max() + 1
            result.loc[index] = [code_list[i], abs(pevalue), PEpercentile, abs(pbvalue), PBpercentile]
        self.save_cache()
        if code == 'all':
            i = 0
            chartPE = Page(layout=Page.SimplePageLayout, js_host='../core/resources/assets/')
            chartPB = Page(layout=Page.SimplePageLayout, js_host='../core/resources/assets/')
            while i < result.size:
                chart = self.drew(result.loc[i:i + 800, ], 'PE')
                if chart:
                    chartPE.add(chart)
                chart = self.drew(result.loc[i:i + 800, ], 'PB')
                if chart:
                    chartPB.add(chart)
                i += 801
            chartPE.render(os.path.join(PROJECT_PATH, 'mark_html/pe.html'))
            chartPB.render(os.path.join(PROJECT_PATH, 'mark_html/pb.html'))
            return result
        else:
            chart = Page(layout=Page.SimplePageLayout)
            pechart = self.drew(result, 'PE')
            if pechart:
                chart.add(pechart)
            pbchart = self.drew(result, 'PB')
            if pbchart:
                chart.add(pbchart)
            return chart, result

class PlotXGB():
    def drew(self, x, y_lab, y2_pre):
        chart = (
            Line(init_opts=opts.InitOpts(width="97%", height="700px"))
                .add_xaxis(
                xaxis_data=x
            )
                .add_yaxis(
                series_name="实际值",
                is_smooth=True,
                symbol="emptyCircle",
                is_symbol_show=False,
                color="#d14a61",
                y_axis=y_lab,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=2),
            )
                .add_yaxis(
                series_name="预测值",
                is_smooth=True,
                symbol="emptyCircle",
                is_symbol_show=False,
                color="#6e9ef1",
                y_axis=y2_pre,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=2),
            )
                .set_global_opts(
                legend_opts=opts.LegendOpts(),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    axisline_opts=opts.AxisLineOpts(
                        is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                    ),
                ),
                datazoom_opts=[
                    opts.DataZoomOpts(
                        is_show=False, type_="inside", xaxis_index=[0], range_start=90, range_end=100
                    ),
                    opts.DataZoomOpts(
                        is_show=True, xaxis_index=[0], pos_top="97%", range_start=90, range_end=100
                    ),
                ],
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
                ),
            )
        )
        return chart

class PlotLSTM(PlotXGB):
    pass