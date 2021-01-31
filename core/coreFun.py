'''
=================================================
@Author ：Andy
@Date   ：2020/6/23 16:17
==================================================
'''

import baostock as bs
import inspect
import os
import pandas as pd
from core.log_config import logger

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)))

class CoreFun():
    def __init__(self, verbose = 0):
        self.verbose = verbose
        self.login()
        self.data_info = self.load_data_info()

    def log(self, message, rs):
        if self.verbose == 1:
            logger.info(message + rs.error_msg)
        else:
            if rs.error_code != '0':
                logger.error(message + rs.error_msg)

    def login(self):
        lg = bs.login()
        self.log('login respond  error_msg:', lg)

    def logout(self):
        bs.logout()

    def load_data_info(self, path_data_info = os.path.join(PROJECT_PATH,'column_info')):
        list_configs = os.listdir(path_data_info)
        result = {}
        for config in list_configs:
            if config.endswith('.csv'):
                result[config.replace('.csv', '')] = pd.read_csv(os.path.join(path_data_info, config), engine='python')
        return result

    # 获取历史A股K线数据
    def query_history_k_data_plus(self, code, start, end = None, frequency = 'd', adjustflag = '3'):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        start：开始日期（包含），格式“YYYY-MM-DD”，为空时取2015-01-01；
        end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日；
        frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取。
        adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权。
        '''
        if frequency == 'd':
            fields = ','.join(self.data_info['query_history_k_data_plus_d']['参数名称'].values.tolist())
        elif frequency in ['w','m']:
            fields = ','.join(self.data_info['query_history_k_data_plus_w&m']['参数名称'].values.tolist())
        elif frequency in ['5','15','30','60']:
            fields = ','.join(self.data_info['query_history_k_data_plus_5&15&30&60']['参数名称'].values.tolist())

        rs = bs.query_history_k_data_plus(code, fields, start_date=start, end_date = end,
                                          frequency = frequency, adjustflag=adjustflag)
        self.log('query_history_k_data_plus respond  error_msg:', rs)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

        return result

    # 查询除权除息信息
    def query_dividend_data(self, code, year, yearType = 'report'):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        year：年份，如：2017。此参数不可为空；
        yearType：年份类别，默认为"report":预案公告年份，可选项"operate":除权除息年份。此参数不可为空。
        '''
        data_list = []
        rs = bs.query_dividend_data(code=code, year=year, yearType=yearType)
        self.log('query_dividend_data respond  error_msg:', rs)
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)

    # 查询复权因子信息
    def query_adjust_factor(self, code, start_date = None, end_date = None):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        start_date：开始日期，为空时默认为2015-01-01，包含此日期；
        end_date：结束日期，为空时默认当前日期，包含此日期。
        '''
        rs_list = []
        rs = bs.query_adjust_factor(code=code, start_date=start_date, end_date=end_date)
        self.log('query_adjust_factor respond  error_msg:', rs)
        while (rs.error_code == '0') & rs.next():
            rs_list.append(rs.get_row_data())
        result = pd.DataFrame(rs_list, columns=rs.fields)
        return result

    # 季频盈利能力
    def query_profit_data(self, code, year = None, quarter = None):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        year：统计年份，为空时默认当前年；
        quarter：统计季度，可为空，默认当前季度。不为空时只有4个取值：1，2，3，4。
        '''
        profit_list = []
        rs = bs.query_profit_data(code=code, year=year, quarter=quarter)
        self.log('query_profit_data respond  error_msg:', rs)
        while (rs.error_code == '0') & rs.next():
            profit_list.append(rs.get_row_data())
        result = pd.DataFrame(profit_list, columns=rs.fields)
        return result

    # 季频营运能力
    def query_operation_data(self, code, year = None, quarter = None):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        year：统计年份，为空时默认当前年；
        quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。
        '''
        operation_list = []
        rs_operation = bs.query_operation_data(code=code, year=year, quarter=quarter)
        self.log('query_operation_data respond  error_msg:', rs_operation)
        while (rs_operation.error_code == '0') & rs_operation.next():
            operation_list.append(rs_operation.get_row_data())
        result_operation = pd.DataFrame(operation_list, columns=rs_operation.fields)
        return result_operation

    # 季频成长能力
    def query_growth_data(self, code, year = None, quarter = None):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        year：统计年份，为空时默认当前年；
        quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。
        '''
        growth_list = []
        rs_growth = bs.query_growth_data(code=code, year=year, quarter=quarter)
        self.log('query_growth_data respond  error_msg:', rs_growth)
        while (rs_growth.error_code == '0') & rs_growth.next():
            growth_list.append(rs_growth.get_row_data())
        result_growth = pd.DataFrame(growth_list, columns=rs_growth.fields)
        return result_growth

    # 季频偿债能力
    def query_balance_data(self, code, year = None, quarter = None):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        year：统计年份，为空时默认当前年；
        quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。
        '''
        balance_list = []
        rs_balance = bs.query_balance_data(code=code, year=year, quarter=quarter)
        self.log('query_balance_data respond  error_msg:', rs_balance)
        while (rs_balance.error_code == '0') & rs_balance.next():
            balance_list.append(rs_balance.get_row_data())
        result_balance = pd.DataFrame(balance_list, columns=rs_balance.fields)
        return result_balance

    # 季频现金流量
    def query_cash_flow_data(self, code, year = None, quarter = None):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        year：统计年份，为空时默认当前年；
        quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。
        '''
        cash_flow_list = []
        rs_cash_flow = bs.query_cash_flow_data(code=code, year=year, quarter=quarter)
        self.log('query_cash_flow_data respond  error_msg:', rs_cash_flow)
        while (rs_cash_flow.error_code == '0') & rs_cash_flow.next():
            cash_flow_list.append(rs_cash_flow.get_row_data())
        result_cash_flow = pd.DataFrame(cash_flow_list, columns=rs_cash_flow.fields)
        return result_cash_flow

    # 季频杜邦指数
    def query_dupont_data(self, code, year = None, quarter = None):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        year：统计年份，为空时默认当前年；
        quarter：统计季度，为空时默认当前季度。不为空时只有4个取值：1，2，3，4。
        '''
        dupont_list = []
        rs_dupont = bs.query_dupont_data(code=code, year=year, quarter=quarter)
        self.log('query_dupont_data respond  error_msg:', rs_dupont)
        while (rs_dupont.error_code == '0') & rs_dupont.next():
            dupont_list.append(rs_dupont.get_row_data())
        result_profit = pd.DataFrame(dupont_list, columns=rs_dupont.fields)
        return result_profit

    # 季频公司业绩快报
    def query_performance_express_report(self, code, start_date, end_date):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        start_date：开始日期，发布日期或更新日期在这个范围内；
        end_date：结束日期，发布日期或更新日期在这个范围内。
        '''
        rs = bs.query_performance_express_report(code, start_date=start_date, end_date=end_date)
        self.log('query_performance_express_report respond  error_msg:', rs)

        result_list = []
        while (rs.error_code == '0') & rs.next():
            result_list.append(rs.get_row_data())
        result = pd.DataFrame(result_list, columns=rs.fields)
        return result

    # 季频公司业绩预告
    def query_forcast_report(self,code, start_date, end_date):
        '''
        code：股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。此参数不可为空；
        start_date：开始日期，发布日期或更新日期在这个范围内；
        end_date：结束日期，发布日期或更新日期在这个范围内。
        '''
        rs_forecast = bs.query_forecast_report(code, start_date=start_date, end_date=end_date)
        self.log('query_forecast_reprot respond  error_msg:', rs_forecast)
        rs_forecast_list = []
        while (rs_forecast.error_code == '0') & rs_forecast.next():
            # 分页查询，将每页信息合并在一起
            rs_forecast_list.append(rs_forecast.get_row_data())
        result_forecast = pd.DataFrame(rs_forecast_list, columns=rs_forecast.fields)
        return result_forecast

    # 交易日查询
    def query_trade_dates(self, start_date = None, end_date = None):
        '''
        start_date：开始日期，为空时默认为2015-01-01。
        end_date：结束日期，为空时默认为当前日期。
        '''
        rs = bs.query_trade_dates(start_date=start_date, end_date=end_date)
        self.log('query_trade_dates respond  error_msg:', rs)
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 证券代码查询
    def query_all_stock(self, day = None):
        '''
        day：需要查询的交易日期，为空时默认当前日期
        '''
        rs = bs.query_all_stock(day=day)
        self.log('query_all_stock respond  error_msg:', rs)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 证券基本资料
    def query_stock_basic(self,code = None, code_name = None):
        '''
        code：A股股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。可以为空；
        code_name：股票名称，支持模糊查询，可以为空。
        '''
        if code:
            rs = bs.query_stock_basic(code=code)
        else:
            rs = bs.query_stock_basic(code_name=code_name)  # 支持模糊查询
        self.log('query_stock_basic respond  error_msg:', rs)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 存款利率
    def query_deposit_rate_data(self, start_date = None,end_date = None):
        '''
        start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
        end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空。
        '''
        rs = bs.query_deposit_rate_data(start_date=start_date, end_date=end_date)
        self.log('query_deposit_rate_data respond  error_msg:', rs)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 贷款利率
    def query_loan_rate_data(self, start_date = None, end_date = None):
        '''
        start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
        end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空。
        '''
        rs = bs.query_loan_rate_data(start_date=start_date, end_date=end_date)
        self.log('query_loan_rate_data respond  error_msg:', rs)

        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 存款准备金率
    def query_required_reserve_ratio_data(self,start_date = None, end_date = None):
        '''
        start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
        end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
        yearType:年份类别，默认为0，查询公告日期；1查询生效日期。
        '''
        rs = bs.query_required_reserve_ratio_data(start_date=start_date, end_date=end_date)
        self.log('query_required_reserve_ratio_data respond  error_msg:', rs)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 货币供应量
    def query_money_supply_data_month(self, start_date = None, end_date = None):
        '''
        start_date：开始日期，格式XXXX-XX，发布日期在这个范围内，可以为空；
        end_date：结束日期，格式XXXX-XX，发布日期在这个范围内，可以为空。
        '''
        rs = bs.query_money_supply_data_month(start_date=start_date, end_date=end_date)
        self.log('query_money_supply_data_month respond  error_msg:', rs)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 货币供应量(年底余额)
    def query_money_supply_data_year(self, start_date = None, end_date = None):
        '''
        start_date：开始日期，格式XXXX，发布日期在这个范围内，可以为空；
        end_date：结束日期，格式XXXX，发布日期在这个范围内，可以为空。
        '''
        rs = bs.query_money_supply_data_year(start_date=start_date, end_date=end_date)
        self.log('query_money_supply_data_year respond  error_msg:', rs)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 银行间同业拆放利率
    def query_shibor_data(self, start_date = None, end_date = None):
        '''
        start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
        end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空。
        '''
        rs = bs.query_shibor_data(start_date=start_date, end_date=end_date)
        self.log('query_shibor_data respond  error_msg:', rs)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        return result

    # 行业分类
    def query_stock_industry(self,code = None, date = None):
        '''
        code：A股股票代码，sh或sz.+6位数字代码，或者指数代码，如：sh.601398。sh：上海；sz：深圳。可以为空；
        date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。
        '''
        rs = bs.query_stock_industry(code = code, date = date)
        self.log('query_stock_industry respond  error_msg:', rs)

        industry_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            industry_list.append(rs.get_row_data())
        result = pd.DataFrame(industry_list, columns=rs.fields)
        return result

    # 上证50成分股
    def query_sz50_stocks(self,date = None):
        '''
        date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。
        '''
        rs = bs.query_sz50_stocks(date = date)
        self.log('query_sz50  error_msg:', rs)

        # 打印结果集
        sz50_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            sz50_stocks.append(rs.get_row_data())
        result = pd.DataFrame(sz50_stocks, columns=rs.fields)
        return result

    # 沪深300成分股
    def query_hs300_stocks(self, date = None):
        '''
        date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。
        '''
        rs = bs.query_hs300_stocks(date = date)
        self.log('query_hs300  error_msg:', rs)

        # 打印结果集
        hs300_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            hs300_stocks.append(rs.get_row_data())
        result = pd.DataFrame(hs300_stocks, columns=rs.fields)
        return result

    # 中证500成分股
    def query_zz500_stocks(self, date = None):
        '''
        date：查询日期，格式XXXX-XX-XX，为空时默认最新日期。
        '''
        rs = bs.query_zz500_stocks(date = date)
        self.log('query_zz500  error_msg:', rs)

        # 打印结果集
        zz500_stocks = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            zz500_stocks.append(rs.get_row_data())
        result = pd.DataFrame(zz500_stocks, columns=rs.fields)
        return result

if __name__ == '__main__':
    d = DownData()
    logger.info(d.query_zz500_stocks())
    bs.logout()