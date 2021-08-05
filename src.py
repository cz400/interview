import numpy as np
import pandas as pd

def generate_data(start_date, end_date):
    """
    根据给定日期的开始日期和结束日期生成以秒为单位的简单数据
    
    参数
    -----
    start_date : str类型，形如'20210804'
    end_date : str类型，形如'20210806'
    
    返回值
    -----
    返回一个dataframe数据集
    """
    index = pd.date_range(start = start_date, end = end_date, freq = "S")
    df = pd.DataFrame(np.arange(len(index)), index = index)
    return df

def get_data(data, date):
    """
    获取具体某天的数据
    
    参数
    -----
    data : dataframe类型，需要查询的数据, 索引为日期, 形式如'2012-10-03 01:00:00'
    date : str类型，形式如'2012-10-03'
    
    返回值
    -----
    返回查询日期当天每小时的增量值
    """
    df = data.copy()
    df_time = df[date]
    return df_time.groupby(df_time.index.hour).count()

if __name__ == '__main__':
    data = generate_data('20210805', '20210806')
    print(get_data(data, '2021-08-05'))
