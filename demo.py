from  Ashare import *

# 假设你已经调用了get_price函数并得到了df
df = get_price('sh000932', frequency='1d', count=1)
df1 = get_price('sh000932', frequency='1m', count=1)