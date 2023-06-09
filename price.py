import json

data = json.load(open('data.json'))
prices_sell = {}
prices_buy = {}
for i, j in data.items():
    prices_sell[i] = j['ir']['sell'] / j['tr']['buy']
    prices_buy[i] = j['ir']['buy'] / j['tr']['sell']

prices_sell = sorted(prices_sell.items(), key=lambda x:x[1])
prices_buy = sorted(prices_buy.items(), key=lambda x:x[1])

for i in reversed(prices_sell):
    print(i[0], i[1])
print('\n\n=====================================\n\n')
for i in reversed(prices_buy):
    print(i[0], i[1])

s = prices_sell[0]
e = prices_sell[-1]

print('')
print('Distance:', prices_buy[-1][1] - prices_sell[0][1])
print('')

amount = 20_000_000
# # tax = 0.0025


s_amount = amount / data[s[0]]['ir']['sell']
# s_amount = s_amount - (s_amount*tax)
s_amount_tl = s_amount * data[s[0]]['tr']['buy']

print(s[0], data[s[0]]['ir']['sell'], ':')
print(f'\t{amount} IRT ÷ {prices_sell[0][1]} = {s_amount_tl} TL\n')


best = {}

for i, j in data.items():
    e_amount = s_amount_tl / j['tr']['sell']
    e_amount_irt = e_amount * j['ir']['buy']
    if e_amount_irt >= amount:
        best[i] = e_amount_irt - amount

best = sorted(best.items(), key=lambda x:x[1])

for i in reversed(best):
    print(f'\t{i[0]} {i[1]+amount} = {int(i[1])} IRT')
