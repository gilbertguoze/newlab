import numpy as np
import pandas as pd
def identify_zszs(*df_series):
# here is to identify zoushizhongshu
# 这里使用dataframe的时间序列
#这里主要的问题是，如何能够利用库和处理，简单循环


#赋值，将需要的数据量拿到,这些都是时间序列
    vol = df_series.vol
    close =  df_series.close
    openp = df_series.openp
    high = df_series.high
    low = df_series.low    

#合并价格关系,时间序列
    priceh = high
    pricel = low

'''
Step1: 自定义函数merge_price
input:priceh pricel
output: priceh_new pricel_new
functional:合并
'''
    [priceh_new, pricel_new] = merge_price（priceh, pricel）

'''
Step2: 自定义函数 画笔
input：priceh_new, pricel_new
outut: 笔的类Bi,包括笔的分类，上升还是下降，顶点和底点的时刻和价格
functional：输入时间序列内，笔的顶点和底点，时间和价格
画图
'''
    [Bi] = identify_bi(priceh_new, pricel_new)

'''
Bi是一个df的时间序列，为了可以画图，包括了
时间列 上升还是下降 是否为顶点 是否为底点 等效价格
方便画图

下面进行笔的画图
'''


'''
识别走势中枢
input：Bi，priceh_new，pricel_new
output：zszs，
functional：识别走势中枢
zszs为时间序列，包括
时间列 走势中枢中？ 支撑价格 阻力价格
根据这些信息和priceh_new和pricel_new画图
'''
    [zszs] = find_zszs（Bi，priceh_new，pricel_new）

'''
画图，走势中枢画图
'''

'''
最后，标识第一类买点，第三类买点
'''




'''
Step1: 自定义函数merge_price
input:priceh pricel
output: priceh_new pricel_new
functional:合并
'''
def [priceh_new, pricel_new] = merge_price（priceh, pricel）:
     #此处最好不用循环，现在只能先用循环
    idx_series = []
    
   #既然这里不知道代码该怎么写，那么用伪代码来代替
   '''
   #向上处理和向下处理
   #向上处理时，former的一根高点比之前非包含关系的高点高时，向上处理
   #向上处理原则，取两根k的最高为高点，两根k的次低的低点为低点
   #向上处理原则，最高和次低
   #向下处理时机，第一根k的高点比之前非包含关系的k的高点低
   
   for idx in length(priceh_new)-1:
       priceh_new(idx) = priceh(idx)
       pricel_new(idx) = pricel(idx)
       idx_series(idx) = 0
       
   #首先是条件，idx比idx+1的高的高且低的低；
   #idx比idx+1的高的低且低的高，需要使用_new
       #if ((priceh_new(idx) >= priceh_new(idx+1)) && 
       #    (pricel_new(idx) <= pricel_new(idx+1)))||
       #    ((priceh_new(idx) <= priceh_new(idx+1)) && 
       #    (pricel_new(idx) >= pricel_new(idx+1)))
       
       #条件触发后，开始处理
       #idx_series(idx) = 1
       #if idx == 1:
       #    向上处理
       #    priceh_new(idx) = max(priceh(idx), priceh(idx+1))
       #    priceh_new(idx+1) = max(priceh(idx), priceh(idx+1))
       #    pricel_new(idx) = max(pricel(idx), pricel(idx+1))
       #    pricel_new(idx) = max(pricel(idx), pricel(idx+1))
       #else:
       #向上处理
       #    if priceh(idx-1) <= priceh(idx)
       #        priceh_new(idx) = max(priceh(idx), priceh(idx+1))
       #        priceh_new(idx+1) = max(priceh(idx), priceh(idx+1))
       #        pricel_new(idx) = min(pricel(idx), pricel(idx+1))
       #        pricel_new(idx) = min(pricel(idx), pricel(idx+1))     
       
       #向下处理
       #    if priceh(idx-1) > priceh(idx)
       #        priceh_new(idx) = min(priceh(idx), priceh(idx+1))
       #        priceh_new(idx+1) = min(priceh(idx), priceh(idx+1))
       #        pricel_new(idx) = max(pricel(idx), pricel(idx+1))
       #        pricel_new(idx) = max(pricel(idx), pricel(idx+1)) 
       
       #   此处需要判断之前的是上升还是下降
       # priceh_new(idx) = priceh
       
       #输出idx_series
       
   ''' 
   
    

'''
Step2: 自定义函数 画笔
input：priceh_new, pricel_new
outut: 笔的类Bi,包括笔的分类，上升还是下降，顶点和底点的时刻和价格
functional：输入时间序列内，笔的顶点和底点，时间和价格
画图
'''
def [Bi] = identify_bi(priceh_new, pricel_new):
    
    #顶分型和底分型的辨识，以及危险分型的mark
    #辨识时需要考虑合并相等的情况
    #顶分和低分包括属性：顶还是低 峰值时间 峰值价格
    #fx.type, fx.moment, fx.price 
    #
    #使用fx进行画笔，约束包括
    #顶顶，底底不是笔
    #笔的顶底峰值之间至少3根k，新笔
    
    
    

'''
识别走势中枢
input：Bi，priceh_new，pricel_new
output：zszs，
functional：识别走势中枢
zszs为时间序列，包括
时间列 走势中枢中？ 支撑价格 阻力价格
根据这些信息和priceh_new和pricel_new画图
'''
def [zszs] = find_zszs（Bi，priceh_new，pricel_new）:
    
    
    
    
    
    
    
    
    
    
