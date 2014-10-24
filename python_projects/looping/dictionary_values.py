shopping_list = ['banana','apple']

prices = {
'banana':20,
'apple':30
}


stock = {
'banana':40,
'apple':20
}

#total = 0
# for key in prices:
#     print
#     print key
#     print 'prices = %s' % prices[key]
#     print 'stock  = %s' % stock[key]
#     total = prices[key] * stock[key]
#     print '{} price: {} in total'.format(key,total)
#
#
# total = 0
# for key in prices:
#     print
#     total = prices[key]*stock[key]+total
#
# print total

def compute_bill(fruits):
    total = 0
    for item in fruits:
        total += fruits[item]
    return total

result = compute_bill(shopping_list)
print result
