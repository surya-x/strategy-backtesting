from typing import List
import datetime as dtm

import yfinance as yf


class BaseData:
    def get_data(self):
        pass


class YFinanceData(BaseData):
    def __init__(self, ticker, start_date: dtm.date):
        self.ticker = ticker
        self.start_date = start_date

    def get_data(self, fields: List = None):
        if not fields:
            fields = ['Close']
        fields = [f.lower() for f in fields]
        asset_df = yf.download(self.ticker, start=self.start_date)

        toDrop = [col for col in asset_df.columns if col.lower() not in fields]

        asset_df = asset_df.drop(toDrop, axis=1)
        asset_df = asset_df[self.start_date:]

        asset_df.index = asset_df.index.date
        asset_df.columns = asset_df.columns.get_level_values(0)

        return asset_df


class CSVData(BaseData):
    def __init__(self, ticker, start_date: dtm.date):
        self.ticker = ticker
        self.start_date = start_date

    def get_data(self, fields: List = None):
        raise NotImplemented()