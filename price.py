import json

data = json.load(open('data.json'))
prices = {}
for i, j in data.items():
    prices[i] = j['ir']['sell'] / j['tr']['buy']

prices = sorted(prices.items(), key=lambda x:x[1])

for i in reversed(prices):
    print(i[0], i[1])

s = prices[0]
e = prices[-1]

print('')
print('Distance:', e[1] - s[1])
print('')

amount = 20_000_000
# # tax = 0.0025


s_amount = amount / data[s[0]]['ir']['sell']
# s_amount = s_amount - (s_amount*tax)
s_amount_tl = s_amount * data[s[0]]['tr']['buy']

print(s[0], data[s[0]]['ir']['sell'], ':')
print(f'\t{amount} IRT ÷ {prices[0][1]} = {s_amount_tl} TL\n')


best = {}

for i, j in data.items():
    e_amount = s_amount_tl / j['tr']['sell']
    e_amount_irt = e_amount * j['ir']['buy']
    if e_amount_irt >= amount:
        best[i] = e_amount_irt - amount

best = sorted(best.items(), key=lambda x:x[1])

for i in reversed(best):
    print(f'\t{i[0]} {i[1]+amount} = {int(i[1])} IRT')
