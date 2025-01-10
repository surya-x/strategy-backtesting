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
        self.data = None

    def get_data(self, fields: List = None):
        if not fields:
            fields = ['Close']

        fields = [f.lower() for f in fields]

        if self.data is None:
            self.data = yf.download(self.ticker, start=self.start_date.strftime('%Y-%m-%d'))
            self.data.index = self.data.index.date
            self.data.columns = self.data.columns.get_level_values(0)

        asset_df = self.data
        toDrop = [col for col in asset_df.columns if col.lower() not in fields]

        asset_df = asset_df.drop(toDrop, axis=1)
        asset_df = asset_df[self.start_date:]

        return asset_df


class CSVData(BaseData):
    def __init__(self, ticker, start_date: dtm.date):
        self.ticker = ticker
        self.start_date = start_date

    def get_data(self, fields: List = None):
        raise NotImplemented()

# itc = pd.DataFrame(stocks[stocks['Stock'] == 'ITC'])
# itc = itc.set_index('Date').drop(['Stock', 'Volume', 'Change Pct'], axis=1)
