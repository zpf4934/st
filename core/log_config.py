'''
=================================================
@Author ：Andy
@Date   ：2020/7/16 10:00
==================================================
'''

import logging

logger = logging.getLogger('stock')
fmt = '%(asctime)s [%(name)s] %(pathname)s %(funcName)s %(lineno)s %(levelname)s - %(message)s'
logging.basicConfig(format=fmt)
logger.setLevel(logging.DEBUG)

# PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)))
#
# logger = logging.getLogger('stock')  # 获取logger对象
# fmter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s [%(lineno)d]: %(message)s', datefmt='%a %d %b %Y %H:%M:%S')
# if not os.path.exists(os.path.join(PROJECT_PATH, 'log')):  # 如果没有log这个目录，则创建该目录
#     os.makedirs(os.path.join(PROJECT_PATH, 'log'))  # 创建存储日志的目录
# hdlr = TimedRotatingFileHandler(os.path.join(PROJECT_PATH, 'log/stock.log'), when='D', interval=1, backupCount=7)  # 将日志输出到磁盘文件上
# hdlr.setFormatter(fmt=fmter)  # Formatter对象定义了最终log信息的顺序,结构和内容
# logger.addHandler(hdlr=hdlr)  # 使用logger.addHandler(handler)添加多个规则，就可以让一个logger记录多个日志
# logging.basicConfig(level=logging.ERROR)  # 等级设置设为WARNING
