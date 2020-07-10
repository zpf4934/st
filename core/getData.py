'''
======================================
# @Author : Andy
# @Date   : 2020-06-27 19:03 
======================================
'''

import inspect
import numpy as np
import os
import pandas as pd

from .coreFun import CoreFun

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)))

class Data():
    def __init__(self, code, start):
        self.cf = CoreFun()
        self.code = code
        self.start = start
        self.query_history_k_data_plus = None
        self.query_profit_data = None
        self.query_operation_data = None
        self.query_growth_data = None
        self.query_balance_data = None
        self.query_cash_flow_data = None
        self.query_dupont_data = None
        self.query_performance_express_report = None
        self.query_forcast_report = None
        self.query_deposit_rate_data = None
        self.query_loan_rate_data = None
        self.query_required_reserve_ratio_data = None
        self.query_money_supply_data_month = None
        self.query_money_supply_data_year = None
        self.query_shibor_data = None
        self.all_data = None

    def get_query_history_k_data_plus(self):
        self.query_history_k_data_plus = self.cf.query_history_k_data_plus(code=self.code, start=self.start)
        self.query_history_k_data_plus['year'] = pd.to_datetime(self.query_history_k_data_plus['date']).dt.year
        self.query_history_k_data_plus['month'] = pd.to_datetime(self.query_history_k_data_plus['date']).dt.month
        self.query_history_k_data_plus['quarter'] = pd.PeriodIndex(pd.to_datetime(self.query_history_k_data_plus['date']),
                                                              freq='Q')

    def get_query_profit_data(self):
        years = list(set(self.query_history_k_data_plus.year.values.tolist()))
        profit_list = []
        for year in years:
            for quarter in ['1', '2', '3', '4']:
                self.query_profit_data = self.cf.query_profit_data(code=self.code, year=year, quarter=quarter)
                profit_list.append(self.query_profit_data)
        self.query_profit_data = pd.concat(profit_list)

        self.query_profit_data['year'] = pd.to_datetime(self.query_profit_data['statDate']).dt.year
        self.query_profit_data['quarter'] = pd.PeriodIndex(pd.to_datetime(self.query_profit_data['statDate']), freq='Q')


    def get_query_operation_data(self):
        years = list(set(self.query_history_k_data_plus.year.values.tolist()))
        operation_list = []
        for year in years:
            for quarter in ['1', '2', '3', '4']:
                self.query_operation_data = self.cf.query_operation_data(code=self.code, year=year, quarter=quarter)
                operation_list.append(self.query_operation_data)
        self.query_operation_data = pd.concat(operation_list)

        self.query_operation_data['year'] = pd.to_datetime(self.query_operation_data['statDate']).dt.year
        self.query_operation_data['quarter'] = pd.PeriodIndex(pd.to_datetime(self.query_operation_data['statDate']), freq='Q')

    def get_query_growth_data(self):
        years = list(set(self.query_history_k_data_plus.year.values.tolist()))
        growth_list = []
        for year in years:
            for quarter in ['1', '2', '3', '4']:
                self.query_growth_data = self.cf.query_growth_data(code=self.code, year=year, quarter=quarter)
                growth_list.append(self.query_growth_data)
        self.query_growth_data = pd.concat(growth_list)

        self.query_growth_data['year'] = pd.to_datetime(self.query_growth_data['statDate']).dt.year
        self.query_growth_data['quarter'] = pd.PeriodIndex(pd.to_datetime(self.query_growth_data['statDate']), freq='Q')

    def get_query_balance_data(self):
        years = list(set(self.query_history_k_data_plus.year.values.tolist()))
        balance_list = []
        for year in years:
            for quarter in ['1', '2', '3', '4']:
                self.query_balance_data = self.cf.query_balance_data(code=self.code, year=year, quarter=quarter)
                balance_list.append(self.query_balance_data)
        self.query_balance_data = pd.concat(balance_list)

        self.query_balance_data['year'] = pd.to_datetime(self.query_balance_data['statDate']).dt.year
        self.query_balance_data['quarter'] = pd.PeriodIndex(pd.to_datetime(self.query_balance_data['statDate']), freq='Q')

    def get_query_cash_flow_data(self):
        years = list(set(self.query_history_k_data_plus.year.values.tolist()))
        cash_list = []
        for year in years:
            for quarter in ['1', '2', '3', '4']:
                self.query_cash_flow_data = self.cf.query_cash_flow_data(code=self.code, year=year, quarter=quarter)
                cash_list.append(self.query_cash_flow_data)
        self.query_cash_flow_data = pd.concat(cash_list)

        self.query_cash_flow_data['year'] = pd.to_datetime(self.query_cash_flow_data['statDate']).dt.year
        self.query_cash_flow_data['quarter'] = pd.PeriodIndex(pd.to_datetime(self.query_cash_flow_data['statDate']), freq='Q')

    def get_query_dupont_data(self):
        years = list(set(self.query_history_k_data_plus.year.values.tolist()))
        dupont_list = []
        for year in years:
            for quarter in ['1', '2', '3', '4']:
                self.query_dupont_data = self.cf.query_dupont_data(code=self.code, year=year, quarter=quarter)
                dupont_list.append(self.query_dupont_data)
        self.query_dupont_data = pd.concat(dupont_list)

        self.query_dupont_data['year'] = pd.to_datetime(self.query_dupont_data['statDate']).dt.year
        self.query_dupont_data['quarter'] = pd.PeriodIndex(pd.to_datetime(self.query_dupont_data['statDate']), freq='Q')

    def get_query_performance_express_report(self):
        self.query_performance_express_report = self.cf.query_performance_express_report(code=self.code,
                                                                               start_date=self.query_history_k_data_plus.date.min(),
                                                                               end_date=self.query_history_k_data_plus.date.max())
        self.query_performance_express_report['year'] = pd.to_datetime(
            self.query_performance_express_report['performanceExpStatDate']).dt.year
        self.query_performance_express_report.sort_values(by='performanceExpStatDate', inplace=True)
        self.query_performance_express_report.drop_duplicates(subset='year', keep='last', inplace=True)

    def get_query_forcast_report(self):
        self.query_forcast_report = self.cf.query_forcast_report(code=self.code,
                                                       start_date=self.query_history_k_data_plus.date.min(),
                                                       end_date=self.query_history_k_data_plus.date.max())
        self.query_forcast_report['year'] = pd.to_datetime(self.query_forcast_report['profitForcastExpStatDate']).dt.year
        self.query_forcast_report.sort_values(by='profitForcastExpStatDate', inplace=True)
        self.query_forcast_report.drop_duplicates(subset='year', keep='last', inplace=True)

    def get_query_deposit_rate_data(self):
        self.query_deposit_rate_data = self.cf.query_deposit_rate_data()

        for i in range(1, len(self.query_deposit_rate_data)):
            for col in self.query_deposit_rate_data.columns:
                if self.query_deposit_rate_data.loc[i][col] == '' and self.query_deposit_rate_data.loc[i - 1][col] != '':
                    self.query_deposit_rate_data.loc[i][col] = self.query_deposit_rate_data.loc[i - 1][col]

        sort_pubDate = sorted(self.query_deposit_rate_data['pubDate'].values.tolist())
        sort_date = sorted(self.query_history_k_data_plus['date'].values.tolist())

        i = 0
        deposit = []
        for j in range(len(sort_date)):
            while i + 1 < len(sort_pubDate):
                if sort_date[j] >= sort_pubDate[i] and sort_date[j] < sort_pubDate[i + 1]:
                    temp = self.query_deposit_rate_data[self.query_deposit_rate_data['pubDate'] == sort_pubDate[i]].copy()
                    temp.loc[temp.index[0], 'pubDate'] = sort_date[j]
                    deposit.append(temp)
                    break
                elif sort_date[j] < sort_pubDate[i]:
                    break
                else:
                    i += 1
            if i + 1 >= len(sort_pubDate):
                break

        while j < len(sort_date):
            temp = self.query_deposit_rate_data[self.query_deposit_rate_data['pubDate'] == sort_pubDate[-1]].copy()
            temp.loc[temp.index[0], 'pubDate'] = sort_date[j]
            deposit.append(temp)
            j += 1
        self.query_deposit_rate_data = pd.concat(deposit)
        self.query_deposit_rate_data.rename(columns={'pubDate': 'date'}, inplace=True)

    def get_query_loan_rate_data(self):
        self.query_loan_rate_data = self.cf.query_loan_rate_data()

        for i in range(1, len(self.query_loan_rate_data)):
            for col in self.query_loan_rate_data.columns:
                if self.query_loan_rate_data.loc[i][col] == '' and self.query_loan_rate_data.loc[i - 1][col] != '':
                    self.query_loan_rate_data.loc[i][col] = self.query_loan_rate_data.loc[i - 1][col]

        sort_pubDate = sorted(self.query_loan_rate_data['pubDate'].values.tolist())
        sort_date = sorted(self.query_history_k_data_plus['date'].values.tolist())

        i = 0
        deposit = []
        for j in range(len(sort_date)):
            while i + 1 < len(sort_pubDate):
                if sort_date[j] >= sort_pubDate[i] and sort_date[j] < sort_pubDate[i + 1]:
                    temp = self.query_loan_rate_data[self.query_loan_rate_data['pubDate'] == sort_pubDate[i]].copy()
                    temp.loc[temp.index[0], 'pubDate'] = sort_date[j]
                    deposit.append(temp)
                    break
                elif sort_date[j] < sort_pubDate[i]:
                    break
                else:
                    i += 1
            if i + 1 >= len(sort_pubDate):
                break

        while j < len(sort_date):
            temp = self.query_loan_rate_data[self.query_loan_rate_data['pubDate'] == sort_pubDate[-1]].copy()
            temp.loc[temp.index[0], 'pubDate'] = sort_date[j]
            deposit.append(temp)
            j += 1
        self.query_loan_rate_data = pd.concat(deposit)
        self.query_loan_rate_data.rename(columns={'pubDate': 'date'}, inplace=True)

    def get_query_required_reserve_ratio_data(self):
        self.query_required_reserve_ratio_data = self.cf.query_required_reserve_ratio_data()

        for i in range(1, len(self.query_required_reserve_ratio_data)):
            for col in self.query_required_reserve_ratio_data.columns:
                if self.query_required_reserve_ratio_data.loc[i][col] == '' and self.query_required_reserve_ratio_data.loc[i - 1][
                    col] != '':
                    self.query_required_reserve_ratio_data.loc[i][col] = self.query_required_reserve_ratio_data.loc[i - 1][col]

        sort_pubDate = sorted(self.query_required_reserve_ratio_data['effectiveDate'].values.tolist())
        sort_date = sorted(self.query_history_k_data_plus['date'].values.tolist())

        i = 0
        deposit = []
        for j in range(len(sort_date)):
            while i + 1 < len(sort_pubDate):
                if sort_date[j] >= sort_pubDate[i] and sort_date[j] < sort_pubDate[i + 1]:
                    temp = self.query_required_reserve_ratio_data[
                        self.query_required_reserve_ratio_data['effectiveDate'] == sort_pubDate[i]].copy()
                    temp.loc[temp.index[0], 'effectiveDate'] = sort_date[j]
                    deposit.append(temp)
                    break
                elif sort_date[j] < sort_pubDate[i]:
                    break
                else:
                    i += 1
            if i + 1 >= len(sort_pubDate):
                break

        while j < len(sort_date):
            temp = self.query_required_reserve_ratio_data[
                self.query_required_reserve_ratio_data['effectiveDate'] == sort_pubDate[-1]].copy()
            temp.loc[temp.index[0], 'effectiveDate'] = sort_date[j]
            deposit.append(temp)
            j += 1

        self.query_required_reserve_ratio_data = pd.concat(deposit)
        self.query_required_reserve_ratio_data.rename(columns={'effectiveDate': 'date'}, inplace=True)

    def get_query_money_supply_data_month(self):
        self.query_money_supply_data_month = self.cf.query_money_supply_data_month()

        for i in range(1, len(self.query_money_supply_data_month)):
            for col in self.query_money_supply_data_month.columns:
                if self.query_money_supply_data_month.loc[i][col] == '' and self.query_money_supply_data_month.loc[i - 1][
                    col] != '':
                    self.query_money_supply_data_month.loc[i][col] = self.query_money_supply_data_month.loc[i - 1][col]
        self.query_money_supply_data_month['statYear'] = self.query_money_supply_data_month.statYear.astype(np.int64)
        self.query_money_supply_data_month['statMonth'] = self.query_money_supply_data_month.statMonth.astype(np.int64)

    def get_query_money_supply_data_year(self):
        self.query_money_supply_data_year = self.cf.query_money_supply_data_year()

        for i in range(1, len(self.query_money_supply_data_year)):
            for col in self.query_money_supply_data_year.columns:
                if self.query_money_supply_data_year.loc[i][col] == '' and self.query_money_supply_data_year.loc[i - 1][
                    col] != '':
                    self.query_money_supply_data_year.loc[i][col] = self.query_money_supply_data_year.loc[i - 1][col]
        self.query_money_supply_data_year['statYear'] = self.query_money_supply_data_year.statYear.astype(np.int64)

    def get_query_shibor_data(self):
        self.query_shibor_data = self.cf.query_shibor_data()

    def logout(self):
        self.cf.logout()

    def down_data(self):
        self.get_query_history_k_data_plus()
        self.get_query_balance_data()
        self.get_query_cash_flow_data()
        self.get_query_dupont_data()
        self.get_query_forcast_report()
        self.get_query_deposit_rate_data()
        self.get_query_growth_data()
        self.get_query_loan_rate_data()
        self.get_query_money_supply_data_month()
        self.get_query_money_supply_data_year()
        self.get_query_operation_data()
        self.get_query_performance_express_report()
        self.get_query_profit_data()
        self.get_query_required_reserve_ratio_data()
        self.get_query_shibor_data()


    def merge_data(self):
        self.all_data = pd.merge(self.query_history_k_data_plus, self.query_profit_data.drop(['code', 'pubDate', 'statDate'], axis=1),
                            how='left', left_on=['year', 'quarter'], right_on=['year', 'quarter'])

        self.all_data = pd.merge(self.all_data, self.query_operation_data.drop(['code', 'pubDate', 'statDate'], axis=1),
                            how='left', left_on=['year', 'quarter'], right_on=['year', 'quarter'])

        self.all_data = pd.merge(self.all_data, self.query_growth_data.drop(['code', 'pubDate', 'statDate'], axis=1),
                            how='left', left_on=['year', 'quarter'], right_on=['year', 'quarter'])

        self.all_data = pd.merge(self.all_data, self.query_balance_data.drop(['code', 'pubDate', 'statDate'], axis=1),
                            how='left', left_on=['year', 'quarter'], right_on=['year', 'quarter'])

        self.all_data = pd.merge(self.all_data, self.query_cash_flow_data.drop(['code', 'pubDate', 'statDate'], axis=1),
                            how='left', left_on=['year', 'quarter'], right_on=['year', 'quarter'])

        self.all_data = pd.merge(self.all_data, self.query_dupont_data.drop(['code', 'pubDate', 'statDate'], axis=1),
                            how='left', left_on=['year', 'quarter'], right_on=['year', 'quarter'])

        self.all_data = pd.merge(self.all_data, self.query_performance_express_report.drop(
            ['code', 'performanceExpPubDate', 'performanceExpStatDate', 'performanceExpUpdateDate'],
            axis=1), how='left', left_on=['year'], right_on=['year'])

        self.all_data = pd.merge(self.all_data,
                            self.query_forcast_report.drop(['code', 'profitForcastExpPubDate', 'profitForcastExpStatDate'],
                                                      axis=1), how='left', left_on=['year'], right_on=['year'])

        self.all_data = pd.merge(self.all_data, self.query_deposit_rate_data, how='left', left_on=['date'], right_on=['date'])

        self.all_data = pd.merge(self.all_data, self.query_loan_rate_data, how='left', left_on=['date'], right_on=['date'])

        self.all_data = pd.merge(self.all_data, self.query_required_reserve_ratio_data, how='left', left_on=['date'],
                            right_on=['date'])

        self.all_data = pd.merge(self.all_data, self.query_money_supply_data_month, how='left', left_on=['year', 'month'],
                            right_on=['statYear', 'statMonth'])

        self.all_data = pd.merge(self.all_data, self.query_money_supply_data_year, how='left', left_on=['year'], right_on=['statYear'])

        self.all_data = pd.merge(self.all_data, self.query_shibor_data, how='left', left_on=['date'], right_on=['date'])

    def update_stock_industry(self):
        self.query_stock_industry = self.cf.query_stock_industry()
        self.query_stock_industry.to_csv(os.path.join(PROJECT_PATH,'data_info','行业分类.csv'), index = 0)

        self.query_sz50_stocks = self.cf.query_sz50_stocks()
        self.query_sz50_stocks.to_csv(os.path.join(PROJECT_PATH,'data_info','上证50成分股.csv'), index=0)

        self.query_hs300_stocks = self.cf.query_hs300_stocks()
        self.query_hs300_stocks.to_csv(os.path.join(PROJECT_PATH,'data_info','沪深300成分股.csv'), index=0)

        self.query_zz500_stocks = self.cf.query_zz500_stocks()
        self.query_zz500_stocks.to_csv(os.path.join(PROJECT_PATH,'data_info','中证500成分股.csv'), index=0)