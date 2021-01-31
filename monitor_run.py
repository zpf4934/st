'''
=================================================
@Author ：Andy
@Date   ：2020/7/13 15:48
==================================================
'''

from core import plotK
from core.tools import PlotPE
from core.getData import Data
import pandas as pd
import argparse
import smtplib
import time
import os
import inspect
from email.mime.text import MIMEText
from email.header import Header
from core.log_config import logger

PROJECT_PATH = os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename))

def monitor_mark():
    for mark in ['一级行业指数', '主题指数', '二级行业指数', '价值指数', '债券指数', '基金指数', '成长指数', '策略指数', '综合指数', '规模指数']:
        plotK.plot_kline_chart(mark=mark)

def monitor_pepb():
    pe = PlotPE()
    result = pe.drew_pe(code='all')
    result = result[['code', 'peTTM', 'PEpercentile', 'PBpercentile']]
    result['updateDate'] = time.strftime('%Y-%m-%d')
    low = result[((result['peTTM'] < 20) & (result['PEpercentile'] < 0.3) & (result['PBpercentile'] < 0.3))]
    high = result[((result['peTTM'] > 20) & (result['PEpercentile'] > 0.7) & (result['PBpercentile'] > 0.7))]
    low.sort_values(['peTTM', 'PEpercentile', 'PBpercentile'], inplace=True)
    high.sort_values(['peTTM', 'PEpercentile', 'PBpercentile'], ascending=False, inplace=True)
    low.reset_index(drop=True, inplace=True)
    high.reset_index(drop=True, inplace=True)
    info = pd.read_csv(os.path.join(PROJECT_PATH, 'data_info/证券资料.csv'), usecols=['code','code_name','type','status'])
    low = pd.merge(low, info, how='left', on='code')
    high = pd.merge(high, info, how='left', on='code')
    low.to_csv(os.path.join(PROJECT_PATH, 'mark_cache/低估产品.csv'), index=0)
    high.to_csv(os.path.join(PROJECT_PATH, 'mark_cache/高估产品.csv'), index=0)
    send_mail(low.loc[0:100, ], high.loc[0:100, ])

def send_mail(low, high):
    sender = '1241833581@qq.com'
    password = 'sljscvmzepaujbce'
    smtp_server = 'smtp.qq.com'

    receivers = ['zpf06184934@163.com']

    mail_msg = """
    <p>低估产品</p>
    {}
    <p>高估产品</p>
    {}
    """
    mail_msg = mail_msg.format(low.to_html(), high.to_html())
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header("估值监控", 'utf-8')
    message['To'] = Header("stock", 'utf-8')

    subject = '估值监控'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(smtp_server)
        smtpObj.connect(smtp_server, 465)
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        logger.info("邮件发送成功")
    except smtplib.SMTPException:
        logger.info("Error: 无法发送邮件")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='choose function')
    parser.add_argument('--function', nargs='+', default='monitor_mark',
                        help='input batch size for training (default: 64)')
    args = parser.parse_args()
    while True:
        if time.strftime('%H:%M') == '18:00':
            logger.info('{} start run monitor'.format(time.strftime('%Y-%M-%d %H:%M:%S')))
            data = Data()
            data.update_stock_industry()
            monitor_mark()
            monitor_pepb()
            logger.info('{} finish run monitor'.format(time.strftime('%Y-%M-%d %H:%M:%S')))
        time.sleep(60)