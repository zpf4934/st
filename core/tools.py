'''
=================================================
@Author ：Andy
@Date   ：2020/6/24 12:01
==================================================
'''

import warnings
from typing import List, Sequence, Union

import mplfinance as mpf
import numpy as np
import pandas as pd
import sys
from fbprophet import Prophet
from fbprophet.diagnostics import performance_metrics
from pyecharts import options as opts
from pyecharts.charts import Kline, Line, Bar, Grid, Scatter
from pyecharts.commons.utils import JsCode
from tqdm import tqdm
from workalendar.asia import China

warnings.filterwarnings("ignore")

import logging
logger = logging.getLogger('model')
logger.setLevel(logging.ERROR)


def plotK(data):
    df = data[['date', 'open', 'high', 'low', 'close', 'volume']]
    df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'},
              inplace=True)
    df.sort_values(by='date', ascending=True, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index(['date'], inplace=True)
    df = df.astype(float)

    kwargs = dict(type='candle', mav=(2, 4, 6), volume=True, figratio=(19, 8), figscale=0.85)

    mpf.plot(df, **kwargs, style='charles')

class Tools():
    def get_screen_size(self):
        if sys.platform == 'linux' or sys.platform == 'darwin':
            return '1000px', '700px'
        else:
            import win32api, win32con
            width = int(win32api.GetSystemMetrics(win32con.SM_CXSCREEN) * 0.98)
            height = int(win32api.GetSystemMetrics(win32con.SM_CYSCREEN) * 0.98)
            return str(width) + 'px', str(height) + 'px'

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

        df = data[['date','open','close','low','high','volume','tag']]
        array_df = df.values
        for i in range(len(array_df)):
            if i < 11:
                result12.append("-")
            if i < 25:
                result26.append("-")
            if i == 11:
                result12.append(array_df[:12, 2].astype(np.float).mean().round(2))
            if i == 25:
                result26.append(array_df[:26, 2].astype(np.float).mean().round(2))
            if i > 11:
                result12.append(((2 * float(array_df[i][2]) + 11 * result12[-1]) / 13).round(2))
            if i > 25:
                result26.append(((2 * float(array_df[i][2]) + 25 * result26[-1]) / 27).round(2))
        dif = ["-"] * 25 + (np.array(result12[25:]) - np.array(result26[25:])).round(2).tolist()
        df['dif'] = dif
        return df

    def add_dea(self, data):
        dea: List[Union[float, str]] = []

        df = data[['date', 'open', 'close', 'low', 'high', 'volume', 'tag', 'dif']]
        array_df = df.values
        for i in range(len(array_df)):
            if i < 33:
                dea.append("-")
            elif i == 33:
                dea.append(np.round(array_df[25:34, -1].mean(), 2))
            else:
                dea.append(np.round((2 * array_df[i][-1] + 8 * dea[-1]) / 10, 2))
        df['dea'] = dea
        return df

    def add_macd(self, data):
        macd: List[Union[float, str]] = []

        df = data[['date', 'open', 'close', 'low', 'high', 'volume', 'tag', 'dif', 'dea']]
        array_df = df.values
        for i in range(len(array_df)):
            if array_df[i][7] == "-" or array_df[i][8] == "-":
                macd.append("-")
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

class ProfessionalKlineBrush(Tools):
    def __init__(self, title = "K线周期图表", width="98%",height="700px"):
        self.title = title
        self.width = width
        self.height = height

    def split_data(self, data):
        category_data = []
        values = []
        volumes = []

        for i in range(len(data)):
            category_data.append(data[i][0])
            values.append(data[i][1:])
            volumes.append(data[i][5])
        return {"categoryData": category_data, "values": values, "volumes": volumes}


    def draw_charts(self, chart_data):
        kline_data = [data[:-1] for data in chart_data["values"]]
        kline = (
            Kline()
                .add_xaxis(xaxis_data=chart_data["categoryData"])
                .add_yaxis(
                series_name="K",
                y_axis=kline_data,
                itemstyle_opts=opts.ItemStyleOpts(color="#ec0000", color0="#00da3c"),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title=self.title, pos_left="0"),
                legend_opts=opts.LegendOpts(is_show=True, pos_left="40%"
                ),
                datazoom_opts=[
                    opts.DataZoomOpts(
                        is_show=False,
                        type_="inside",
                        xaxis_index=[0, 0],
                        range_start=90,
                        range_end=100,
                    ),
                    opts.DataZoomOpts(
                        is_show=True,
                        xaxis_index=[0, 1],
                        type_="slider",
                        pos_top="85%",
                        range_start=90,
                        range_end=100,
                    ),
                ],
                yaxis_opts=opts.AxisOpts(
                    is_scale=True,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    name="价格",
                    type_="value",
                    axislabel_opts=opts.LabelOpts(formatter="{value} ¥")
                ),
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
                                              feature={
                                                  "saveAsImage":{"name":self.title, "type":"jpeg"},
                                                  "dataView":{},
                                                  "restore":{},
                                              }),
            )
        )

        line = (
            Line()
                .add_xaxis(xaxis_data=chart_data["categoryData"])
                .add_yaxis(
                series_name="MA5",
                y_axis=self.calculate_ma(day_count=5, data=chart_data["values"]),
                is_smooth=True,
                is_hover_animation=False,
                linestyle_opts=opts.LineStyleOpts(width=2, opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                series_name="MA10",
                y_axis=self.calculate_ma(day_count=10, data=chart_data["values"]),
                is_smooth=True,
                is_hover_animation=False,
                linestyle_opts=opts.LineStyleOpts(width=2, opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                series_name="MA20",
                y_axis=self.calculate_ma(day_count=20, data=chart_data["values"]),
                is_smooth=True,
                is_hover_animation=False,
                linestyle_opts=opts.LineStyleOpts(width=2, opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                series_name="MA30",
                y_axis=self.calculate_ma(day_count=30, data=chart_data["values"]),
                is_smooth=True,
                is_hover_animation=False,
                linestyle_opts=opts.LineStyleOpts(width=2, opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(xaxis_opts=opts.AxisOpts(type_="category"),)
        )

        bar = (
            Bar()
                .add_xaxis(xaxis_data=chart_data["categoryData"])
                .add_yaxis(
                series_name="Volume",
                y_axis=self.get_change_vol(chart_data["volumes"]),
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
                    is_scale=True,
                    grid_index=1,
                    boundary_gap=True,
                    min_="dataMin",
                    max_="dataMax",
                ),
                yaxis_opts=opts.AxisOpts(
                    name=self.label_name,
                    type_="value",
                    axislabel_opts=opts.LabelOpts(formatter="{value}"),
                    grid_index=1,
                    is_scale=True,
                    split_number=2,
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
                legend_opts=opts.LegendOpts(is_show=True, pos_left='15%'),
            )
        )

        line_1 = (
            Line()
                .add_xaxis(xaxis_data=chart_data["categoryData"])
                .add_yaxis(
                series_name="VOL5",
                y_axis=self.volume_ma(day_count=5, data=chart_data['volumes']),
                xaxis_index=1,
                yaxis_index=1,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=2, opacity=0.5),
            )
                .add_yaxis(
                series_name="VOL10",
                y_axis=self.volume_ma(day_count=10, data=chart_data['volumes']),
                xaxis_index=1,
                yaxis_index=1,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=2, opacity=0.5),
            )
        )

        overlap_bar_line_2 = bar.overlap(line_1)

        # Kline And Line
        overlap_kline_line = kline.overlap(line)

        # Grid Overlap + Bar
        grid_chart = Grid(
            init_opts=opts.InitOpts(
                width=self.width,
                height=self.height,
                animation_opts=opts.AnimationOpts(animation=True),
            )
        )

        grid_chart.add_js_funcs("var barData = {}".format(chart_data["values"]))

        grid_chart.add(
            overlap_kline_line,
            grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", height="50%"),
        )
        grid_chart.add(
            overlap_bar_line_2,
            grid_opts=opts.GridOpts(
                pos_left="10%", pos_right="8%", pos_top="63%", height="16%"
            ),
        )

        return grid_chart

    def draw(self, df):
        data = df[['date','open','close','low','high','volume']]
        chart_data = self.split_data(data.values.tolist())
        return self.draw_charts(chart_data)



class ProfessionalKlineChart(Tools):
    def __init__(self, mark_line_show = False, title = "K线周期图表", width="98%",height="700px"):
        self.mark_line_show = mark_line_show
        self.title = title
        self.width = width
        self.height = height

    def init_data(self, data):
        df = data[['date','open','close','low','high','volume']]
        df = df.astype({'open':np.float,'close':np.float,'low':np.float,'high':np.float,'volume':np.float})
        df = self.add_tag(df)
        df = self.add_dif(df)
        df = self.add_dea(df)
        df = self.add_macd(df)
        df = df[['date', 'open', 'close', 'low', 'high', 'volume', 'tag', 'macd', 'dif', 'dea']]
        return df

    def split_data(self, origin_data) -> dict:
        datas = []
        times = []
        vols = []
        macds = []
        difs = []
        deas = []

        for i in range(len(origin_data)):
            datas.append(origin_data[i][1:])
            times.append(origin_data[i][0:1][0])
            vols.append(origin_data[i][5])
            macds.append(origin_data[i][7])
            difs.append(origin_data[i][8])
            deas.append(origin_data[i][9])
        vols = [int(v) for v in vols]

        return {
            "datas": datas,
            "times": times,
            "vols": vols,
            "macds": macds,
            "difs": difs,
            "deas": deas,
        }

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

    def draw_chart(self, data):
        kline = (
            Kline()
                .add_xaxis(xaxis_data=data["times"])
                .add_yaxis(
                series_name="K",
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
                    ]
                ),
                markline_opts=opts.MarkLineOpts(
                    label_opts=opts.LabelOpts(
                        position="middle", color="blue", font_size=12, is_show = self.mark_line_show
                    ),
                    data=self.split_data_part(data),
                    symbol=["circle", "none"],
                ),
            )
                .set_series_opts(
                markarea_opts=opts.MarkAreaOpts(is_silent=True, data=self.split_data_part(data))
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title=self.title, pos_left="0"),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    is_scale=True,
                    boundary_gap=False,
                    axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                    split_number=20,
                    min_="dataMin",
                    max_="dataMax",
                ),
                yaxis_opts=opts.AxisOpts(
                    is_scale=True,
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                    name="价格",
                    type_="value",
                    axislabel_opts=opts.LabelOpts(formatter="{value} ¥")
                ),
                # tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
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
                    grid_index=1,
                    axislabel_opts=opts.LabelOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    grid_index=1,
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

        # Bar-2 (Overlap Bar + Line)
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
                legend_opts=opts.LegendOpts(is_show=True, pos_right='5%', pos_top = '1.4%', orient='horizontal'),
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
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
            )
                .add_yaxis(
                series_name="DEA",
                y_axis=data["deas"],
                xaxis_index=2,
                yaxis_index=2,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(opacity=0.5, width=2),
            )
        )
        # 最下面的柱状图和折线图
        overlap_bar_line_2 = bar_2.overlap(line_2)

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
            overlap_bar_line_2,
            grid_opts=opts.GridOpts(
                pos_left="4%", pos_right="1%", pos_top="82%", height="14%"
            ),
        )
        return  grid_chart

    def draw(self, data):
        df = self.init_data(data)
        spl_data = self.split_data(origin_data=df.values.tolist())
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