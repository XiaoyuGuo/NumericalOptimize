# 黄金分割法
# 不使用导数的搜索
import math

# @param s 步长因子
# @param d 步长
# @param func 函数
# 特点:每次搜索区间缩短率相同, 每次的搜索区间都为原来的0.618倍

# 确定搜索区间
search_scope = [-100, 100]

# 确定容许误差
epsilon = 0.05

# 确定t, 黄金分割
t = (math.sqrt(5) - 1) / 2

def func(x):
    return (x-5) ** 2

#避免重复计算
next_p = 0
next_q = 0
next_func_p = 0
next_func_q = 0

while True:
    h = search_scope[1] - search_scope[0]
    p = search_scope[0] + h * (1 - t) if next_p == 0 else next_p
    q = search_scope[0] + h * t if next_q == 0 else next_q
    func_p = func(p) if next_func_p == 0 else next_func_p
    func_q = func(q) if next_func_q == 0 else next_func_q
    if func_p <= func_q:
        if abs(q - search_scope[0]) <= epsilon:
            print("%.2f" % p)
            print("%.2f" % func_p)
            break
        else:
            search_scope[1] = q
            next_func_p = 0 # Clear
            next_q = p
            next_func_q = func_p
            next_p = search_scope[0] + (1 - t) * (search_scope[1] - search_scope[0])
    else:
        if abs(search_scope[1] - p) <= epsilon:
            print("%.2f" % q)
            print("%.2f" % func_q)
            break
        else:
            search_scope[0] = p
            next_func_q = 0 # Clear
            next_func_p = func_q
            next_p = q
            next_q = search_scope[0] + t * (search_scope[1] - search_scope[0])



