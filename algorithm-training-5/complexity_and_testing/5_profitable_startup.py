# k друзей организовали стартап по производству укулеле для кошек. На сегодняшний день прибыль составила n рублей.
# Вы, как главный бухгалтер компании, хотите в каждый из ближайших d дней приписывать по одной цифре в конец числа, выражающего прибыль.
# При этом в каждый из дней прибыль должна делиться на k.

def count_profit(n_sum, k_cnt, d_days):
    res = n_sum

    for i in range(d_days):
        for j in range(10):
            if (res * 10 + j) % k_cnt == 0:
                res = res * 10 + j
                i += 1
                s_res = str(res)
                for k in range(i, d_days):
                    s_res += '0'
                return s_res

    return -1


n_sum, k_cnt, d_days = map(int, input().split())
print(count_profit(n_sum, k_cnt, d_days))



