from decimal import Decimal
import datetime

# def conv(data):
# 	output = []
# 	output.append(data[0])
# 	output.append(float(data[1]))
# 	print "output: " , output
# 	return output

# data = [('TH1747', Decimal('0.22')), ('TH83', Decimal('22'))]
# print data

# result = map(lambda x : x[0] , float(x[1])  , data)
# print result

# result = map(conv,data)
# print result

# result = dict(result)
# print "result :" , result
# > f = lambda x, y : x + y
# >>> f(1,1)

# shipper_weight = {
#     "date_basis_datetime" : "2016-06-28 21:31:00+00",
#     "package_id" : "311118429-0002",
#     "rate_card_from_party" : "LEL",
#     "rate_card_to_party" : "Lazada",
#     "shipper_weight" : [
#         {
#             "shipper" : "TH1747",
#             "weight" : 0.20000000000000001
#         },
#         {
#             "shipper" : "TH317",
#             "weight" : 0.10000000000000001
#         },
#         {
#             "shipper" : "TH83",
#             "weight" : 22
#         }
#     ],
#     "transaction_type_effective_date" : "2016-03-01",
#     "transaction_type_name" : "COD-Kerry",
#     "value" : [
#         {
#             "db_column" : "cod_value",
#             "file_type" : "package_files.th",
#             "value" : "284.0000"
#         }
#     ]
# }

# print(shipper_weight['package_id'])

# for shipper in shipper_weight['shipper_weight']:
#     print(shipper)

tx_verified_list = [
    ('06810a6a-70ab-4b48-be12-1b2b01c0b50f', 24, datetime.date(2016, 3, 1), 'Delivery-BulkyHeight', 'Lazada', 'LEL', datetime.date(2016, 3, 1), 'Delivery', 'RANGE', 'journey_status_files', 'status_update_date'),
    ('06810a6a-70ab-4b48-be12-1b2b01c0b50f', 24, datetime.date(2016, 3, 1), 'COD-LEX', 'Lazada', 'LEL', datetime.date(2016, 3, 1), 'COD', 'RANGE', 'journey_status_files', 'status_update_date'), 
    ('06810a6a-70ab-4b48-be12-1b2b01c0b50f', 24, datetime.date(2016, 3, 1), 'Delivery-Standard', 'Lazada', 'LEL', datetime.date(2016, 3, 1), 'Delivery', 'DISTANCE_BASED', 'journey_status_files', 'status_update_date')
]

for tx in tx_verified_list:
    print(tx[8])
    print("----------------------")