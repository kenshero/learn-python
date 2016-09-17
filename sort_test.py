from collections import OrderedDict

def extract_time(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return json['shipper']
    except KeyError:
        return 0

seller_weights = [
    {
        "shipper" : "TH82",
        "weight" : 3.000
    },
    {
        "shipper" : "TH81",
        "weight" : 3.000
    },
    {
        "shipper" : "TH87",
        "weight" : 3.000
    }
]

# new_seller_weight = []
print(seller_weights)
print("==================================================")

# for seller in sorted(mydict):
#     new_seller_weight.append(seller)
#     print(seller)
# # lines.sort() is more efficient than lines = lines.sorted()
new_seller_weight =  sorted(seller_weights, key=lambda k: k.get('shipper'), reverse=False)
print(new_seller_weight)


# a = sorted(seller_weights['shipper'])
# print(seller_weights[0])