"""Flag for whether a date falls on a public holiday in Brazil."""
from h2oaicore.transformer_utils import CustomTransformer
import datatable as dt
import numpy as np
import pandas as pd


# https://pypi.org/project/holidays/
def make_holiday_frame():
    return dt.fread(
        """
        Date,Name,Day
        2010-1-1,Ano novo,Sexta-feira
        2010-2-16,Carnaval,Terça-feira
        2010-2-17,Quarta-feira de cinzas,Quarta-feira
        2010-4-2),Sexta-feira Santa,Sexta-feira
        2010-4-4,Páscoa,Domingo
        2010-4-21,Tiradentes,Quarta-feira
        2010-5-1,Dia Mundial do Trabalho,Sabado
        2010-6-3,Corpus Christi,Quinta-feira
        2010-9-7,Independencia do Brasil,Terça-feira
        2010-10-12,Nossa Senhora Aparecida,Terça-feira
        2010-11-2,Finados,Terça-feira
        2010-11-15,Proclamação da República,Segunda-feira
        2010-12-25,Natal,Sabado
        2011-1-1,Ano novo,Sabado
        2011-3-8,Carnaval,Terça-feira
        2011-3-9,Quarta-feira de cinzas,Quarta-feira
        2011-4-21,Tiradentes,Quinta-feira
        2011-4-22,Sexta-feira Santa,Sexta-feira
        2011-4-24,Páscoa,Domingo
        2011-5-1,Dia Mundial do Trabalho,Domingo
        2011-6-23,Corpus Christi,Quinta-feira
        2011-9-7,Independencia do Brasil,Quarta-feira
        2011-10-12,Nossa Senhora Aparecida,Quarta-feira
        2011-11-2,Finados,Quarta-feira
        2011-11-15,Proclamação da República,Terça-feira
        2011-12-25,Natal,Domingo
        2012-1-1,Ano novo,Domingo
        2012-2-21,Carnaval,Terça-feira
        2012-2-22,Quarta-feira de cinzas,Quarta-feira
        2012-4-6,Sexta-feira Santa,Sexta-feira
        2012-4-8,Páscoa,Domingo
        2012-4-21,Tiradentes,Sabado
        2012-5-1,Dia Mundial do Trabalho,Terça-feira
        2012-6-7,Corpus Christi,Quinta-feira
        2012-9-7),Independencia do Brasil,Sexta-feira
        2012-10-12,Nossa Senhora Aparecida,Sexta-feira
        2012-11-2,Finados,Sexta-feira
        2012-11-15,Proclamação da República,Quinta-feira
        2012-12-25,Natal,Terça-feira
        2013-1-1,Ano novo,Terça-feira
        2013-2-12,Carnaval,Terça-feira
        2013-2-13,Quarta-feira de cinzas,Quarta-feira
        2013-3-29,Sexta-feira Santa,Sexta-feira
        2013-3-31,Páscoa,Domingo
        2013-4-21,Tiradentes,Domingo
        2013-5-1,Dia Mundial do Trabalho,Quarta-feira
        2013-5-30,Corpus Christi,Quinta-feira
        2013-9-7),Independencia do Brasil,Sabado
        2013-10-12,Nossa Senhora Aparecida,Sabado
        2013-11-2,Finados,Sabado
        2013-11-15,Proclamação da República,Sexta-feira
        2013-12-25,Natal,Quarta-feira
        2014-1-1,Ano novo,Quarta-feira
        2014-3-4,Carnaval,Terça-feira
        2014-3-5,Quarta-feira de cinzas,Quarta-feira
        2014-4-18,Sexta-feira Santa,Sexta-feira
        2014-4-20,Páscoa,Domingo
        2014-4-21,Tiradentes,Segunda-feira
        2014-5-1,Dia Mundial do Trabalho,Quinta-feira
        2014-6-19,Corpus Christi,Quinta-feira
        2014-9-7),Independencia do Brasil,Domingo
        2014-10-12,Nossa Senhora Aparecida,Domingo
        2014-11-2,Finados,Domingo
        2014-11-15,Proclamação da República,Sabado
        2014-12-25,Natal,Quinta-feira
        2015-1-1,Ano novo,Quinta-feira
        2015-2-17,Carnaval,Terça-feira
        2015-2-18,Quarta-feira de cinzas,Quarta-feira
        2015-4-3,Sexta-feira Santa,Sexta-feira
        2015-4-5,Páscoa,Domingo
        2015-4-21,Tiradentes,Terça-feira
        2015-5-1,Dia Mundial do Trabalho,Sexta-feira
        2015-6-4,Corpus Christi,Quinta-feira
        2015-9-7,Independencia do Brasil,Segunda-feira
        2015-10-12,Nossa Senhora Aparecida,Segunda-feira
        2015-11-2,Finados,Segunda-feira
        2015-11-15,Proclamação da República,Domingo
        2015-12-25,Natal,Sexta-feira
        2016-1-1,Ano novo,Sexta-feira
        2016-2-9,Carnaval,Terça-feira
        2016-2-10,Quarta-feira de cinzas,Quarta-feira
        2016-3-25,Sexta-feira Santa,Sexta-feira
        2016-3-27,Páscoa,Domingo
        2016-4-21,Tiradentes,Quinta-feira
        2016-5-1,Dia Mundial do Trabalho,Domingo
        2016-5-26,Corpus Christi,Quinta-feira
        2016-9-7,Independencia do Brasil,Quarta-feira
        2016-10-12,Nossa Senhora Aparecida,Quarta-feira
        2016-11-2,Finados,Quarta-feira
        2016-11-15,Proclamação da República,Terça-feira
        2016-12-25,Natal,Domingo
        2017-1-1,Ano novo,Domingo
        2017-2-28,Carnaval,Terça-feira
        2017-3-1,Quarta-feira de cinzas,Quarta-feira
        2017-4-14,Sexta-feira Santa,Sexta-feira
        2017-4-16,Páscoa,Domingo
        2017-4-21,Tiradentes,Sexta-feira
        2017-5-1,Dia Mundial do Trabalho,Segunda-feira
        2017-6-15,Corpus Christi,Quinta-feira
        2017-9-7,Independencia do Brasil,Quinta-feira
        2017-10-12,Nossa Senhora Aparecida,Quinta-feira
        2017-11-2,Finados,Quinta-feira
        2017-11-15),Proclamação da República,Quarta-feira
        2017-12-25,Natal,Segunda-feira
        2018-1-1),Ano novo,Segunda-feira
        2018-2-13,Carnaval,Terça-feira
        2018-2-14,Quarta-feira de cinzas,Quarta-feira
        2018-3-30,Sexta-feira Santa,Sexta-feira
        2018-4-1,Páscoa,Domingo
        2018-4-21,Tiradentes,Sabado
        2018-5-1,Dia Mundial do Trabalho,Terça-feira
        2018-5-31,Corpus Christi,Quinta-feira
        2018-9-7,Independencia do Brasil,Sexta-feira
        2018-10-12,Nossa Senhora Aparecida,Sexta-feira
        2018-11-2,Finados,Sexta-feira
        2018-11-15,Proclamação da República,Quinta-feira
        2018-12-25,Natal,Terça-feira
        2019-1-1,Ano novo,Terça-feira
        2019-3-5,Carnaval,Terça-feira
        2019-3-6,Quarta-feira de cinzas,Quarta-feira
        2019-4-19,Sexta-feira Santa,Sexta-feira
        2019-4-21,Páscoa,Domingo
        2019-4-21,Tiradentes,Domingo
        2019-5-1,Dia Mundial do Trabalho,Quarta-feira
        2019-6-20,Corpus Christi,Quinta-feira
        2019-9-7,Independencia do Brasil,Sabado
        2019-10-12,Nossa Senhora Aparecida,Sabado
        2019-11-2,Finados,Sabado
        2019-11-15,Proclamação da República,Sexta-feira
        2019-12-25,Natal,Quarta-feira
        2020-1-1,Ano novo,Quarta
        2020-2-25,Carnaval,Terça-feira
        2020-2-26,Quarta-feira de cinzas,Quarta-feira
        2020-4-10,Sexta-feira Santa,Sexta
        2020-4-12,Páscoa,Domingo
        2020-4-21,Tiradentes,Terça-feira
        2020-5-1,Dia Mundial do Trabalho,Sexta-feira
        2020-6-11,Corpus Christi,Quinta-feira
        2020-9-7,Independencia do Brasil,Segunda-feira
        2020-10-12,Nossa Senhora Aparecida,Segunda-feira
        2020-11-2,Finados,Segunda-feira
        2020-11-15,Proclamação da República,Domingo
        2020-12-25,Natal,Sexta-feira
        """).to_pandas()


class BrazilPublicHolidayTransformer(CustomTransformer):

    @staticmethod
    def get_default_properties():
        return dict(col_type="date", min_cols=1, max_cols=1, relative_importance=1)

# used Date instead of Obsercance in the template script to make hdays frame

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_column = self.input_feature_names[0]
        hdays = make_holiday_frame()['Date']
        self.memo = pd.DataFrame(hdays, columns=[self.time_column], dtype='datetime64[ns]')
        self.memo['year'] = self.memo[self.time_column].dt.year
        self.memo['doy'] = self.memo[self.time_column].dt.dayofyear
        self.memo.sort_values(by=['year', 'doy']).drop_duplicates(subset=['year'], keep='first').reset_index(drop=True)
        self.memo.drop(self.time_column, axis=1, inplace=True)

    def fit_transform(self, X: dt.Frame, y: np.array = None):
        return self.transform(X)

    def transform(self, X: dt.Frame):
        X = X[:, self.time_column]
        if X[:, self.time_column].ltypes[0] != dt.ltype.str:
            assert self.datetime_formats[self.time_column] in ["%Y%m%d", "%Y%m%d%H%M"]
            X[:, self.time_column] = dt.stype.str32(dt.stype.int64(dt.f[0]))
        X.replace(['', 'None'], None)
        X = X.to_pandas()
        X.loc[:, self.time_column] = pd.to_datetime(X[self.time_column],
                                                    format=self.datetime_formats[self.time_column])

        X['year'] = X[self.time_column].dt.year
        X['doy'] = X[self.time_column].dt.dayofyear
        X.drop(self.time_column, axis=1, inplace=True)
        feat = 'is_holiday'
        self.memo[feat] = 1
        X = X.merge(self.memo, how='left', on=['year', 'doy']).fillna(0)
        self.memo.drop(feat, axis=1, inplace=True)
        X = X[[feat]].astype(int)
        return X
