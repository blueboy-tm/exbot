import json
import requests

ir = json.loads(json.dumps(requests.get('https://api.nobitex.ir/market/stats?srcCurrency='
             'btc,usdt,eth,etc,doge,ada,bch,ltc,bnb,eos,xlm,xrp,'
             'trx,uni,link,dai,dot,shib,aave,ftm,matic,axs,mana,'
             'sand,avax,usdc,gmt,mkr,sol,atom,grt,bat,near,ape,qnt,'
             'chz,xmr,egala,busd,algo,hbar,1inch,yfi,flow,snx,enj,'
             'crv,fil,wbtc,ldo,dydx,apt,mask,comp,bal,lrc,lpt,ens,'
             'sushi,api3,one,glm,pmn,dao,cvc,nmr,storj,snt,ant,zrx'
             ',slp,egld,imx,blur,100k_floki,1b_babydoge,1m_nft,'
             '1m_btt,t,celr&dstCurrency=rls').json()['stats']).replace('-rls', ''))

tr = json.loads(json.dumps(requests.get('https://web.paribu.com/initials/ticker/extended').json()['payload']).replace('_tl', ''))

prices = {}

for i in ir:
    if i in tr and not ir[i]['isClosed']:
        c = requests.get(f'https://web.paribu.com/market/{i}_tl/orderbook').json()['payload']
        price = {
            'ir': {
                'sell': float(ir[i]['bestSell']) / 10,
                'buy': float(ir[i]['bestBuy']) / 10
            },
            'tr': {
                'sell': float(list(c['sell'].keys())[0]),
                'buy': float(list(c['buy'].keys())[0])
            }
        }
        prices[i] = price
        print(f'{i} Finished.')

prices['shib']['tr']['buy'] = prices['shib']['tr']['buy'] * 1000
prices['shib']['tr']['sell'] = prices['shib']['tr']['sell'] * 1000

final = json.dumps(prices, indent=2)
open('data.json', 'w').write(final)
print('')