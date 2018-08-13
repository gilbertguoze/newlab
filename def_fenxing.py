#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
'''
通过梳理思路，首先是数据具备四列
时间, priceh_new, priceh_new, 是否合并(1/0)
数据名称df_series，以形参的形式传入
def find_fenxing(*df_series)
由于有了是否合并，所以判断条件简单了。
while idx < length(df_series)
    if df_series(3, idx) == 1
        idx = idx + 1
        break
    if df_series(2, idx) < df_series(2, idx+1) &&
        df_series(3, idx+1) == 1 &&
       df_series(2, idx+2) > df_series(2, idx+3)   
       #顶分   
       #记录，然后idx = idx + 4
    if df_series(2, idx) < df_series(2, idx+1) &&
        df_series(3, idx+1) == 0 &&
       df_series(2, idx+1) > df_series(2, idx+2)        
    #顶分
    #记录，然后 idx = idx + 3
    
'''


def find_fenxing(*df_series):
#这里只要是梳理思路
#分型类型，峰值时间，峰值数值
#顶分型，根据.定义，priceh出现峰值，
#低-高-低，如果确认了，跳三个，继续判断

#问题是，由于合并的关系，价格会有一样的情况，所以存在需要判断的问题
'''
如果出现相等，跳1个，
再判断低_高_低，或者低_高_等_低，跳3，跳4，跳5
记录顶分型，峰值时间，峰值数据
if (priceh_new(idx) <= priceh_new(idx+1)) &&
    (priceh_new(idx+1) >= priceh_new(idx+2))
    这是个顶分
    如果idx+1和idx+2的high和low一致，和idx+3和idx+4一致，跳3，4，5
elseif (pricel_new(idx) >= pricel_new(idx+1)) &&
    (pricel_new(idx+1) <= pricel_new(idx+2))
    这是个底分
else
    不是任何分型，跳1


总体思路是，先判断跳1，然后识别分型，分型和跳几个数据解藕
这里不能使用for循环，使用while循环
while (idx < length(priceh_new))：
    if (priceh_new(idx) == priceh_new(idx+1)) &&
        (pricel_new(idx) == pricel_new(idx+1)):
        #这种跳1，然后break
        idx = idx + 1
        break
    if (priceh_new(idx) <= priceh_new(idx+1)) &&
    (priceh_new(idx+1) >= priceh_new(idx+2))
    #这是个顶分
    #如果idx+1和idx+2的high和low一致，和idx+3和idx+4一致，跳3，4，5
    elseif (pricel_new(idx) >= pricel_new(idx+1)) &&
    (pricel_new(idx+1) <= pricel_new(idx+2))
    #这是个底分
    else
    #不是任何分型，跳1

'''



