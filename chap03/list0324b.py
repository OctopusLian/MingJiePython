# 如果读取的整数为正数，则判断它是“偶数”还是“奇数”，并打印输出判断结果

n = int(input('正整数：')) 

if n > 0: 
    print('该值为正{}。'.format('奇数' if n % 2 else '偶数')) 
else: 
    print('输入的值不为正数。')