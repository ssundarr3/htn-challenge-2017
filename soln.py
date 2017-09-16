import json

with open('./test/test-data-2.json') as data_file:
  data = json.load(data_file)


actual_allocations = {}
total_value = 0
money = 0

for i in data['target_allocations']:
  total_value += float(data['portfolio_holdings'][i])*float(data['asset_prices'][i])
  actual_allocations[i] = (float(data['portfolio_holdings'][i])*float(data['asset_prices'][i]))

for i in data['target_allocations']:
  data['target_allocations'][i] *= 100*total_value


# for i in actual_allocations:
#   left_ratio = actual_allocations[i]-target_allocations[i]
#   if(left_ratio > 0):
#     money += 
#   money +=

# print (actual_allocations)

# print (total_value)

print (data['target_allocations'])
