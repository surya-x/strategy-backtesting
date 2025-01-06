import pandas as pd
import numpy as np


class MyStrategy:
    def __init__(self, df):
        self.df = df
        self.df['Return'] = self.df.Close / self.df.Close.shift(1)
        self.df.loc[df.index[0], 'Return'] = 1.0

    def run(self, close_pct_threshold=20, range_value=10, STARTING_BALANCE=10000):
        self.START_BAL = STARTING_BALANCE
        self.close_pct_threshold = close_pct_threshold
        self.range_value = range_value

        self.build_for_benchmark()
        self.build_for_strategy()

        self.simulate_strategy_for_params(self.df, close_pct_threshold, range_value, True)

    def stats(self):
        trades, days_in_market = self._get_trades_and_exposure()

        _b_return = self.df.Benchmark_bal.iloc[-1]
        _s_return = self.df.Sys_bal.iloc[-1]

        stats = {
            'close_pct_threshold': self.close_pct_threshold,
            'range_value': self.range_value,
            'Total Days': len(self.df.Long),
            'Market Exposure': round((days_in_market / len(self.df.Long)) * 100, 2),
            '# of Trades': trades,
            'Benchmark WinRate': self._calc_win_rate(self.df.Return),
            'Strategy WinRate': self._calc_win_rate(self.df.Sys_ret),
            'Benchmark Return (Rs)': round(_b_return, 2),
            'Benchmark Return (%)': round(((_b_return - self.START_BAL) / self.START_BAL) * 100, 2),
            'Strategy Return (Rs)': round(_s_return, 2),
            'Strategy Return (%)': round(((_s_return - self.START_BAL) / self.START_BAL) * 100, 2),
        }
        return pd.Series(stats)

    ####################
    ####  HELPERS  #####
    ####################

    def build_for_benchmark(self):
        self.df['Benchmark_bal'] = self.df.Return.cumprod() * self.START_BAL
        self.df['Benchmark_pct'] = (((self.df.Benchmark_bal - self.START_BAL) / self.START_BAL) * 100).round(3)

    def build_for_strategy(self):
        self.df['Range'] = self.df.High - self.df.Low
        self.df['Distance'] = abs(self.df.Close - self.df.Low)
        self.df['Close percentage'] = (self.df.Distance / self.df.Range) * 100

    def simulate_strategy_for_params(self, df, close_pct_threshold, range_value, in_place=True):
        _long = np.where(
            (df['Close percentage'] < close_pct_threshold) &
            (df['Range'] > range_value),
            True, False)

        df_long = pd.DataFrame({'Long': _long}, index=df.index)

        df_long['Sys_ret'] = np.where(df_long.Long.shift(1) == True, df.Return, 1)
        df_long['Sys_bal'] = df_long.Sys_ret.cumprod() * self.START_BAL

        if in_place:
            self.df = pd.concat([self.df, df_long], axis=1)

    def _get_trades_and_exposure(self):
        prev = False
        trades = 0
        days_in_market = 0
        for l in self.df.Long:
            if l and prev:
                days_in_market += 1
                continue
            if l:
                days_in_market += 1
                trades += 1
            prev = l
        return trades, days_in_market

    def _calc_win_rate(self, df_returns_col, start_date=None, end_date=None):
        _col = df_returns_col[start_date:end_date]

        _profit = _col[_col > 1.0].count()
        _loss = _col[_col < 1.0].count()

        _win_rate = (_profit / (_profit + _loss)) * 100
        return _win_rate.round(3)
