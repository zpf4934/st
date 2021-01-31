'''
======================================
# @Author : Andy
# @Date   : 2020-07-04 19:20 
======================================
'''


import datetime
import inspect
import os
import sys
import time
import warnings

import emoji
import pandas as pd

from core.getData import Data
from core.log_config import logger
from core.tools import ProfessionalKlineChart

warnings.filterwarnings("ignore")

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)))

def clearout():
    os.system('cls' if os.name == 'nt' else 'clear')
    if 'ipykernel' in sys.modules:
        from IPython.display import clear_output as clear
        clear()

def get_name(code):
    path_data_info = os.path.join(PROJECT_PATH, 'data_info')
    data_info = pd.read_csv(os.path.join(path_data_info, "证券资料.csv"))
    return data_info.loc[data_info['code'] == code, 'code_name'].values[0]

def get_cache(mark, clear_cache):
    if clear_cache:
        return None
    mark_cache_path = os.path.join(PROJECT_PATH, 'mark_cache', mark + '.csv')
    if os.path.exists(mark_cache_path):
        cache_data = pd.read_csv(mark_cache_path)
    else:
        cache_data = None
    return cache_data

def save_cache(mark, cache_data):
    mark_cache_path = os.path.join(PROJECT_PATH, 'mark_cache')
    if not os.path.exists(mark_cache_path):
        os.makedirs(mark_cache_path)
    cache_data.to_csv(os.path.join(mark_cache_path, mark + '.csv'), index = 0)

def save_html(mark, charts, name):
    is_index = False
    path_mark_html = os.path.join(PROJECT_PATH, 'mark_html', mark)
    if not os.path.exists(path_mark_html):
        os.makedirs(path_mark_html)
    for index, html in charts.items():
        if index == 'MACD' and name == '上证指数' and mark == '综合指数':
            html.render(os.path.join(PROJECT_PATH, 'mark_html/mark_index.html'))
        html.render(os.path.join(path_mark_html, name + '-' + index + '.html'))


def plot_mark(mark, start_date, mark_line_show = False, clear_cache = False):
    cache_data = get_cache(mark, clear_cache)
    path_data_info = os.path.join(PROJECT_PATH, 'data_info')
    mark_info = pd.read_csv(os.path.join(path_data_info, mark + ".csv"))
    i = 0
    start = time.time()
    for code in mark_info['指数代码']:
        name = mark_info.loc[mark_info['指数代码']==code,'指数简称'].values[0]
        i += 1
        logger.info('\nDraw chart: {}=>{}'.format(mark, name))
        draw = ProfessionalKlineChart(mark_line_show = mark_line_show,
                                          title=name)
        if cache_data is not None and cache_data[cache_data['code'] == code].size > 0:
            start_date = (pd.to_datetime(cache_data[cache_data['code'] == code]['date'].max()) + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        if start_date <= datetime.datetime.now().strftime('%Y-%m-%d'):
            data = Data(code, start_date)
            data.get_query_history_k_data_plus()
            data.logout()
            if cache_data is not None:
                data.query_history_k_data_plus = pd.concat([cache_data[cache_data['code'] == code], data.query_history_k_data_plus],
                                                            ignore_index=True).sort_values(by='date')
            if data.query_history_k_data_plus.size == 0:
                logger.warning('data.query_history_k_data_plus and cache_data is NULL')
            else:
                data.query_history_k_data_plus.drop_duplicates(subset = ['date','code'], inplace = True)
                chart = draw.draw(data.query_history_k_data_plus)
                save_html(mark, chart, name)
                cache_data = pd.concat([cache_data, data.query_history_k_data_plus], ignore_index=True)
                cache_data.drop_duplicates(subset = ['date','code'], inplace = True)
        else:
            logger.error("date is out of today!")
        clearout()
        end = time.time()
        logger.info('\r' + '进度 {}/{}:[{}]{:.2f}% {:.2f}s'.
              format(i, len(mark_info), emoji.emojize(':rocket:') * int(i * 30 / len(mark_info)) + '   ' * int((1 - (i / len(mark_info))) * 30),
                     float(i / len(mark_info) * 100), end - start))
    save_cache(mark, cache_data)

def plot_kline_chart(code = None, mark = None, start_date = '2010-01-01', target = 'MACD', mark_line_show = False):
    '''
    :param code: 股票代码
    :param mark: 指数 [一级行业指数，主题指数，二级行业指数，价值指数，债券指数，基金指数，成长指数，策略指数，综合指数，规模指数]
    :param start_date:
    :return:
    '''

    if code is None and mark is None:
        logger.error("code and mark is None!")
    if code:
        title = get_name(code)
        data = Data(code, start_date)
        data.get_query_history_k_data_plus()
        data.logout()
        chart = ProfessionalKlineChart(mark_line_show = mark_line_show, title=title, target = target)
        return chart.draw(data.query_history_k_data_plus)
    if mark:
        plot_mark(mark=mark, start_date=start_date, mark_line_show=mark_line_show)
        logger.info("draw chart finish")