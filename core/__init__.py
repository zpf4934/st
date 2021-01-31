'''
=================================================
@Author ：Andy
@Date   ：2020/7/15 10:29
==================================================
'''

import os
import inspect

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)))

if not os.path.exists(os.path.join(PROJECT_PATH, 'column_info')):
    os.makedirs(os.path.join(PROJECT_PATH, 'column_info'))

if not os.path.exists(os.path.join(PROJECT_PATH, 'data_info')):
    os.makedirs(os.path.join(PROJECT_PATH, 'data_info'))

if not os.path.exists(os.path.join(PROJECT_PATH, 'mark_cache')):
    os.makedirs(os.path.join(PROJECT_PATH, 'mark_cache'))

if not os.path.exists(os.path.join(PROJECT_PATH, 'model/config')):
    os.makedirs(os.path.join(PROJECT_PATH, 'model/config'))

if not os.path.exists(os.path.join(PROJECT_PATH, 'model/pkl')):
    os.makedirs(os.path.join(PROJECT_PATH, 'model/pkl'))