from decimal import Decimal
from datetime import date, datetime

# db_columns = [{'db_column': 'package_id'},

#     {'db_column': 'platform_package_id'},
#     {'db_column': 'tracking_number'},
#     {'db_column': 'system_source'},
#     {'db_column': 'platform_order_number'},
#     {'db_column': 'platform_order_date'},
#     {'db_column': 'package_width'},
#     {'db_column': 'package_height'},
#     {'db_column': 'package_length'},
#     {'db_column': 'package_actual_weight'},
#     {'db_column': 'parcel_dim_weight'},
#     {'db_column': 'package_chargeable_weight'},
#     {'db_column': 'package_chargeable_weight_source'},
#     {'db_column': 'insurance_value'}, 
#     {'db_column': 'insurance_value_currency'}, 
#     {'db_column': 'payment_method'}, 
#     {'db_column': 'cod_value'}, 
#     {'db_column': 'cod_value_currency'}, 
#     {'db_column': 'insurance_flag'}, 
#     {'db_column': 'platform_id'}, 
#     {'db_column': 'lel_service_level'}, 
#     {'db_column': 'fulfillment_method'}, 
#     {'db_column': 'shipping_provider_service_level'}, 
#     {'db_column': 'sensitive'}
# ]
# db_column_list = []
# for db_column in db_columns:
#     db_column_list.append(db_column['db_column'])

# strColumns = ','.join([str(x) for x in db_column_list])

# print(db_column_list)
# print("==================================================================")
# print(strColumns)
# print("==================================================================")
# print(strColumns.split(','))

# for item in line_items:
#     # db_column_list.append(db_column['db_column'])
#     print(item)

def get_dict_write_row(db_columns, line_items):

    file_item_dict = {}

    for column in db_columns:
        file_item_dict[column] = line_items[column]

    return file_item_dict

line_items = [{'shipping_provider_service_level': None,
     'lel_service_level': 'Standard',
     'system_source': 'TH',
     'parcel_dim_weight': None,
     'insurance_value': Decimal('598.0000'),
     'payment_method': 'CashOnDelivery',
     'platform_order_date': datetime(2016, 8, 30, 17),
     'platform_id': 'Lazada',
     'platform_order_number': '311493879',
     'package_width': None,
     'sensitive': None,
     'fulfillment_method': 'Retail',
     'platform_package_id': 'Thai Stainless Steel42614',
     'cod_value_currency': 'THB',
     'insurance_flag': 'not insured',
     'tracking_number': '311493879 - 12863214',
     'package_chargeable_weight': Decimal('0.350'),
     'package_chargeable_weight_source': '3PL Pro Forma',
     'package_length': None,
     'package_actual_weight': Decimal('0.350'),
     'cod_value': Decimal('3598.0000'),
     'package_height': None,
     'package_id': '311493879-6503',
     'insurance_value_currency': 'THB'}]

db_columns = ['package_id',
     'platform_package_id',
     'tracking_number',
     'system_source',
     'platform_order_number',
     'platform_order_date',
     'package_width',
     'package_height',
     'package_length',
     'package_actual_weight',
     'parcel_dim_weight',
     'package_chargeable_weight',
     'package_chargeable_weight_source',
     'insurance_value',
     'insurance_value_currency',
     'payment_method',
     'cod_value',
     'cod_value_currency',
     'insurance_flag',
     'platform_id',
     'lel_service_level',
     'fulfillment_method',
     'shipping_provider_service_level',
     'sensitive']

# print(line_items[1].keys())

# expected_data = get_dict_write_row(db_columns, line_items[0])

# print(expected_data)

i = datetime.now()
print(i)