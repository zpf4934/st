'''
=================================================
@Author ：Andy
@Date   ：2020/7/17 14:03
==================================================
'''
import threading
import inspect
import json
import os
import sys
import time

from bs4 import BeautifulSoup
import pandas as pd
from django.shortcuts import render

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename))))

sys.path.append(PROJECT_PATH)
import monitor_run
from core import plotK
from core.log_config import logger
from core.tools import PlotPE, ProfessionalKlineChart
from core.getData import Data
from core.model import ProphetModel, XGBModel, LSTMModel

global monitor
# 接收POST请求数据
def index(request):
    global monitor
    ctx = {}
    if monitor:
        ctx['monitor'] = monitor
    return render(request, "index.html", ctx)

def core(request):
    global monitor
    ctx = {}
    if monitor:
        ctx['monitor'] = monitor
    if request.POST:
        code = request.POST['code'].strip()
        start_date = request.POST['start_date'].strip()
        target = request.POST['target'].strip()
        periods = int(request.POST['periods'])
        if 'PEPB' in request.POST.keys():
            chart = pepb(code)
            if chart is not None:
                ctx['chart'] = chart
        elif 'KLine' in request.POST.keys():
            chart = kline(code, start_date, target)
            if chart is not None:
                ctx['chart'] = chart
        elif 'del' in request.POST.keys():
            del_code(code)
            monitor = get_monitor()
            if monitor:
                ctx['monitor'] = monitor
        elif 'add' in request.POST.keys():
            add_code(code)
            monitor = get_monitor()
            if monitor:
                ctx['monitor'] = monitor
        elif 'XGB' in request.POST.keys():
            chart = xgb_model(code,start_date)
            if chart is not None:
                ctx['chart'] = chart
        elif 'PROPHET' in request.POST.keys():
            chart = prophet_model(code, start_date, periods)
            if chart is not None:
                ctx['chart'] = chart
        elif 'LSTM' in request.POST.keys():
            chart = lstm_model(code, start_date, periods)
            if chart is not None:
                ctx['chart'] = chart

    return render(request, 'index.html', ctx)

def mark(request):
    cxt = {}
    url = request.path_info.split('/', 2)[-1]
    with open(os.path.join(PROJECT_PATH, 'mark_html', url), 'r') as fr:
        html = fr.read()
    soup_html = BeautifulSoup(html, 'html.parser')
    result = ''
    for chil in soup_html.body.children:
        result += str(chil)
    cxt['mark'] = result
    return render(request, 'MARK_INDEX.html', cxt)

def pe(request):
    cxt = {}
    url = request.path_info.split('/', 2)[-1]
    with open(os.path.join(PROJECT_PATH, 'mark_html', url), 'r') as fr:
        html = fr.read()
    soup_html = BeautifulSoup(html, 'html.parser')
    result = ''
    for chil in soup_html.body.children:
        result += str(chil)
    cxt['pe'] = result
    return render(request, 'PE_INDEX.html', cxt)

def pb(request):
    cxt = {}
    url = request.path_info.split('/', 2)[-1]
    with open(os.path.join(PROJECT_PATH, 'mark_html', url), 'r') as fr:
        html = fr.read()
    soup_html = BeautifulSoup(html, 'html.parser')
    result = ''
    for chil in soup_html.body.children:
        result += str(chil)
    cxt['pb'] = result
    return render(request, 'PB_INDEX.html', cxt)

def prophet_model(code, start, periods):
    prop = ProphetModel(code, start, periods=periods)
    df = prop.init_data()
    fit = False
    if df is None:
        return None
    if os.path.exists(os.path.join(PROJECT_PATH, 'model/config/prophetparam')):
        with open(os.path.join(PROJECT_PATH, 'model/config/prophetparam'), 'r') as fr:
            param = json.loads(fr.read())
            if 'fit' in param.keys():
                fit = param['fit']
            param['fit'] = False
        with open(os.path.join(PROJECT_PATH, 'model/config/prophetparam'), 'w') as fw:
            fw.write(json.dumps(param))
        param.pop('fit')
    else:
        param = {}
    if prop.fit(df, fit=fit, **param):
        prop.cross_plot.add(prop.plot)
        prop.cross_plot.add(prop.point_plot)
        if fit or not os.path.exists(os.path.join(PROJECT_PATH, 'model/pkl', code + '_prop.pkl')):
            prop.cross_validation()
    if prop.cross_plot is None:
        return None
    prop.cross_plot.render('prop_temp.html')
    with open('prop_temp.html', 'r') as fr:
        html = fr.read()
    soup_html = BeautifulSoup(html, 'html.parser')
    result = ''
    for chil in soup_html.body.children:
        result += str(chil)
    os.remove('prop_temp.html')
    return result

def xgb_model(code, start_date):
    xgb = XGBModel(code, start=start_date)
    xgb.init_data()
    fit = False
    if os.path.exists(os.path.join(PROJECT_PATH, 'model/config/xgbparam')):
        with open(os.path.join(PROJECT_PATH, 'model/config/xgbparam'), 'r') as fr:
            param = json.loads(fr.read())
            if 'fit' in param.keys():
                fit = param['fit']
            param['fit'] = False
        with open(os.path.join(PROJECT_PATH, 'model/config/xgbparam'), 'w') as fw:
            fw.write(json.dumps(param))
        param.pop('fit')
    else:
        param = {}
    xgb.fit(fit=fit, eval_metric = 'mae', verbose = 1, **param)
    if xgb.chart is None:
        return None
    xgb.chart.render('xgb_temp.html')
    with open('xgb_temp.html', 'r') as fr:
        html = fr.read()
    soup_html = BeautifulSoup(html, 'html.parser')
    result = ''
    for chil in soup_html.body.children:
        result += str(chil)
    os.remove('xgb_temp.html')
    return result

def lstm_model(code, start_date, periods):
    fit = False
    if os.path.exists(os.path.join(PROJECT_PATH, 'model/config/lstmparam')):
        with open(os.path.join(PROJECT_PATH, 'model/config/lstmparam'), 'r') as fr:
            param = json.loads(fr.read())
            if 'fit' in param.keys():
                fit = param['fit']
            param['fit'] = False
        with open(os.path.join(PROJECT_PATH, 'model/config/lstmparam'), 'w') as fw:
            fw.write(json.dumps(param))
        param.pop('fit')
    else:
        param = {}

    lstm = LSTMModel(code, periods, start=start_date, **param)
    lstm.init_data()
    lstm.fit(fit=fit)

    if lstm.chart is None:
        return None
    lstm.chart.render('lstm_temp.html')
    with open('lstm_temp.html', 'r') as fr:
        html = fr.read()
    soup_html = BeautifulSoup(html, 'html.parser')
    result = ''
    for chil in soup_html.body.children:
        result += str(chil)
    os.remove('lstm_temp.html')
    return result

def info(request):
    ctx = {}
    if monitor:
        ctx['monitor'] = monitor
    code_info = get_code_info(request)
    ctx['info'] = code_info
    return render(request, 'index.html', ctx)

def pepb(code):
    pe = PlotPE()
    chart, result = pe.drew_pe(code)
    if chart is None:
        return None
    chart.render('pe_temp.html')
    with open('pe_temp.html', 'r') as fr:
        html = fr.read()
    soup_html = BeautifulSoup(html, 'html.parser')
    result = ''
    for chil in soup_html.body.children:
        result += str(chil)
    os.remove('pe_temp.html')
    return result

def kline(code, start_date, target):
    title = plotK.get_name(code)
    data = Data(code, start_date)
    data.get_query_history_k_data_plus()
    data.logout()
    chart = ProfessionalKlineChart(title=title, target=target)
    chart = chart.draw(data.query_history_k_data_plus)
    if chart is None:
        return None
    chart.render('kline_temp.html')
    with open('kline_temp.html', 'r') as fr:
        html = fr.read()
    soup_html = BeautifulSoup(html, 'html.parser')
    result = ''
    for chil in soup_html.body.children:
        result += str(chil)
    os.remove('kline_temp.html')
    return result


def get_monitor():
    if os.path.exists(os.path.join(PROJECT_PATH, 'mark_cache/monitor')):
        with open(os.path.join(PROJECT_PATH, 'mark_cache/monitor'), 'r') as fr:
            result = json.loads(fr.read())
        if len(result) > 0:
            div = '''
                <div class="header_down container wrapper clearfix bigmegamenu">
                            <nav class="wsmenu slideLeft clearfix">
                                <ul class="mobile-sub wsmenu-list">
                                {}
                                </ul>
                            </nav>
                </div>
            '''

            li = '''
            <li>
                <span class="wsmenu-click"></span>
                <a type="button" value="{}" class="btn" onclick="addValue(this)">{}</a>
            </li>
            '''
            li_list = []
            for i in sorted(list(set(result))):
                li_list.append(li.format(i,i))
            div = div.format('\n'.join(li_list))
            return div
        else:
            return None
    else:
        return None

def get_code_info(request):
    if '行业分类' in request.path_info and os.path.exists(os.path.join(PROJECT_PATH, 'data_info/行业分类.csv')):
        data_info = pd.read_csv(os.path.join(PROJECT_PATH, 'data_info/行业分类.csv'))
    elif '证券资料' in request.path_info and os.path.exists(os.path.join(PROJECT_PATH, 'data_info/证券资料.csv')):
        data_info = pd.read_csv(os.path.join(PROJECT_PATH, 'data_info/证券资料.csv'))
    elif '今日低估' in request.path_info and os.path.exists(os.path.join(PROJECT_PATH, 'mark_cache/低估产品.csv')):
        data_info = pd.read_csv(os.path.join(PROJECT_PATH, 'mark_cache/低估产品.csv'))
    elif '今日高估' in request.path_info and os.path.exists(os.path.join(PROJECT_PATH, 'mark_cache/高估产品.csv')):
        data_info = pd.read_csv(os.path.join(PROJECT_PATH, 'mark_cache/高估产品.csv'))
    else:
        return None
    columns = data_info.columns
    div = """
    <div class=" container" style="overflow: auto;height:85%;margin: 10px auto">
        <table class="hovertable" style="width: 100%">
        {}
        </table>
    </div>
    """
    tr = '''<tr onmouseover="this.style.backgroundColor='#ffff66';" onmouseout="this.style.backgroundColor='#d4e3e5';">{}</tr>'''
    th = '''<th>{}</th>'''
    td = '''<td>{}</td>'''
    th_list = []
    tr_list = []
    for col in columns:
        th_list.append(th.format(col))
    tr_list.append(tr.format('\n'.join(th_list)))
    for index in data_info.index:
        td_list = []
        for col in columns:
            if col == 'code':
                a = '<button type="button" value="{}" onclick="addValue(this)">{}</button>'.format(data_info.loc[index, col], data_info.loc[index, col])
                td_list.append(td.format(a))
            else:
                td_list.append(td.format(data_info.loc[index, col]))
        tr_list.append(tr.format('\n'.join(td_list)))
    div = div.format('\n'.join(tr_list))
    return div

def del_code(code):
    logger.info(code)
    if os.path.exists(os.path.join(PROJECT_PATH, 'mark_cache/monitor')):
        with open(os.path.join(PROJECT_PATH, 'mark_cache/monitor'), 'r') as fr:
            result = json.loads(fr.read())
        if code in result:
            result.remove(code)
        with open(os.path.join(PROJECT_PATH, 'mark_cache/monitor'), 'w') as fw:
            fw.write(json.dumps(result))

def add_code(code):
    if os.path.exists(os.path.join(PROJECT_PATH, 'mark_cache/monitor')):
        with open(os.path.join(PROJECT_PATH, 'mark_cache/monitor'), 'r') as fr:
            result = json.loads(fr.read())
        if code in result:
            return
        else:
            result.append(code)
    else:
        result = [code]
    with open(os.path.join(PROJECT_PATH, 'mark_cache/monitor'), 'w') as fw:
        fw.write(json.dumps(result))

def add_prophetparam(request):
    ctx = {}
    if monitor:
        ctx['monitor'] = monitor
    param = """
            <div style="width: 90%; text-align: center; margin: 50px auto">
            <form action="/setprophetparam" method="get">
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>changepoints:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="changepoints" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>n_changepoints:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="n_changepoints" value=25 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>changepoint_range:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="changepoint_range" value=0.8 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>yearly_seasonality:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="yearly_seasonality" value="auto" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>weekly_seasonality:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="weekly_seasonality" value="auto" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>daily_seasonality:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="daily_seasonality" value="auto" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>holidays:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="holidays" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>seasonality_prior_scale:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="seasonality_prior_scale" value=10.0 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>holidays_prior_scale:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="holidays_prior_scale" value=10.0 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>changepoint_prior_scale:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="changepoint_prior_scale" value=0.05 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>mcmc_samples:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="mcmc_samples" value=0 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>interval_width:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="interval_width" value=0.8 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>uncertainty_samples:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="uncertainty_samples" value=1000 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>stan_backend:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="stan_backend" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>growth:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <section>
                    <select style="width: 80%;background: #B0E0E6;" name="growth">
                        <option>linear</option>
                        <option>logistic</option>
                    </select>
                </section>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>seasonality_mode:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <section>
                    <select style="width: 80%;background: #B0E0E6;" name="seasonality_mode">
                        <option>additive</option>
                        <option>multiplicative</option>
                    </select>
                </section>
                </div>
                <div>
                    <button type="submit" style="margin: 20px auto;width: 100px;background: #FFF8DC">提交</button>
                </div>
            </form>
        </div>
    """
    ctx['param'] = param
    return render(request, 'index.html', ctx)

def set_prophetparam(request):
    ctx = {}
    param = {}
    int_param = ['n_changepoints','mcmc_samples','uncertainty_samples']
    float_param = ['changepoint_range','seasonality_prior_scale','holidays_prior_scale','changepoint_prior_scale','interval_width']
    if monitor:
        ctx['monitor'] = monitor
    for key in request.GET.keys():
        value = request.GET[key]
        if value == 'None':
            param[key] = None
        else:
            try:
                if key in int_param:
                    param[key] = int(value)
                elif key in float_param:
                    param[key] = float(value)
                else:
                    param[key] = value
            except Exception as e:
                logger.error(e)
                return render(request, 'index.html', ctx)
    with open(os.path.join(PROJECT_PATH, 'model/config/prophetparam'), 'w') as fw:
        param['fit'] = True
        fw.write(json.dumps(param))
    return render(request, 'index.html', ctx)

def add_xgbparam(request):
    ctx = {}
    if monitor:
        ctx['monitor'] = monitor
    param = """
            <div style="width: 90%; text-align: center; margin: 50px auto">
            <form action="/setxgbparam" method="get">
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>max_depth:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="max_depth" value=5 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>learning_rate:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="learning_rate" value=1 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>n_jobs:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="n_jobs" value=3 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>gamma:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="gamma" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>min_child_weight:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="min_child_weight" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>max_delta_step:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="max_delta_step" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>subsample:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="subsample" value=0.8 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>colsample_bytree:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="colsample_bytree" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>colsample_bylevel:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="colsample_bylevel" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>colsample_bynode:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="colsample_bynode" value=0.8 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>reg_alpha:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="reg_alpha" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>reg_lambda:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="reg_lambda" value=0.00005 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>scale_pos_weight:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="scale_pos_weight" value="None" style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>booster:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <section>
                    <select style="width: 80%;background: #B0E0E6;" name="booster">
                        <option>gblinear</option>
                        <option>gbtree</option>
                        <option>dart</option>
                    </select>
                </section>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>importance_type:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <section>
                    <select style="width: 80%;background: #B0E0E6;" name="importance_type">
                        <option>gain</option>
                        <option>weight</option>
                        <option>cover</option>
                        <option>total_gain</option>
                        <option>total_cover</option>
                    </select>
                </section>
                </div>
                <div>
                    <button type="submit" style="margin: 20px auto;width: 100px;background: #FFF8DC">提交</button>
                </div>
            </form>
        </div>
    """
    ctx['param'] = param
    return render(request, 'index.html', ctx)

def set_xgbparam(request):
    ctx = {}
    param = {}
    int_param = ['max_depth','n_jobs','min_child_weight','max_delta_step']
    float_param = ['max_delta_step','gamma','subsample','colsample_bytree','colsample_bylevel','colsample_bynode',
                   'reg_alpha','reg_lambda','scale_pos_weight']
    if monitor:
        ctx['monitor'] = monitor
    for key in request.GET.keys():
        value = request.GET[key]
        if value == 'None':
            continue
        else:
            try:
                if key in int_param:
                    param[key] = int(value)
                elif key in float_param:
                    param[key] = float(value)
                else:
                    param[key] = value
            except Exception as e:
                logger.error(e)
                return render(request, 'index.html', ctx)
    with open(os.path.join(PROJECT_PATH, 'model/config/xgbparam'), 'w') as fw:
        param['fit'] = True
        fw.write(json.dumps(param))
    return render(request, 'index.html', ctx)

def add_lstmparam(request):
    ctx = {}
    if monitor:
        ctx['monitor'] = monitor
    param = """
            <div style="width: 90%; text-align: center; margin: 50px auto">
            <form action="/setlstmparam" method="get">
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>hidden_size:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="hidden_size" value=8 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>num_layers:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="num_layers" value=5 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>batch_size:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="batch_size" value=50 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>epoch:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="epoch" value=100 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;background: #87CECB;">
                    <label>lr:</label>
                </div>
                <div style="display: inline-block;width: 15%;">
                    <input type="text" name="lr" value=0.001 style="background: #B0E0E6;" \>
                </div>
                <div style="display: inline-block;width: 15%;">
                </div>
                <div style="display: inline-block;width: 15%;">
                </div>
                <div>
                    <button type="submit" style="margin: 20px auto;width: 100px;background: #FFF8DC">提交</button>
                </div>
            </form>
        </div>
    """
    ctx['param'] = param
    return render(request, 'index.html', ctx)

def set_lstmparam(request):
    ctx = {}
    param = {}
    int_param = ['hidden_size','num_layers','batch_size','epoch','n_tep']
    float_param = ['lr']
    if monitor:
        ctx['monitor'] = monitor
    for key in request.GET.keys():
        value = request.GET[key]
        if value == 'None':
            continue
        else:
            try:
                if key in int_param:
                    param[key] = int(value)
                elif key in float_param:
                    param[key] = float(value)
                else:
                    param[key] = value
            except Exception as e:
                logger.error(e)
                return render(request, 'index.html', ctx)
    with open(os.path.join(PROJECT_PATH, 'model/config/lstmparam'), 'w') as fw:
        param['fit'] = True
        fw.write(json.dumps(param))
    return render(request, 'index.html', ctx)

def update_task():
    logger.info('{} start run monitor'.format(time.strftime('%Y-%M-%d %H:%M:%S')))
    data = Data()
    data.update_stock_industry()
    monitor_run.monitor_mark()
    monitor_run.monitor_pepb()
    logger.info('{} finish run monitor'.format(time.strftime('%Y-%M-%d %H:%M:%S')))

def update(request):
    ctx = {}
    if monitor:
        ctx['monitor'] = monitor
    t = threading.Thread(target=update_task, daemon=True)
    t.start()
    return render(request, 'index.html', ctx)


def page_not_found(request, exception):
    return render(request, '404.html')

def page_error(request):
    return render(request, '500.html')

monitor = get_monitor()