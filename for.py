import itertools
# arr = [{'file_type': 'package_files.th', 'db_column': 'package_chargeable_weight', 'value': '20.000'}, {'file_type': 'journey_status_files.th', 'db_column': 'journey_destination', 'value': '284'}, {'file_type': 'journey_status_files.th', 'db_column': 'journey_destination_country', 'value': 'TH'}, {'file_type': 'journey_status_files.th', 'db_column': 'journey_origin', 'value': '44'}, {'file_type': 'journey_status_files.th', 'db_column': 'journey_origin_country', 'value': 'TH'}]

# config = {'file_type': 'package_files.th', 'db_column': 'package_chargeable_weight'}

# value = [v['value'] for v in arr if
#          v['file_type'] == config['file_type'] and v['db_column'] == config['db_column']]

# print(value)

# parameters = {'216': {'216': {'2.5': {'rate': 83, 'is_per_kg': False}, 'default': {'rate': 15, 'is_per_kg': True}, '10': {'rate': 145, 'is_per_kg': False}, '2': {'rate': 75, 'is_per_kg': False}, '1.5': {'rate': 72, 'is_per_kg': False}, '20': {'rate': 240, 'is_per_kg': False}, '0.5': {'rate': 63, 'is_per_kg': False}, '5': {'rate': 122, 'is_per_kg': False}, '4': {'rate': 110, 'is_per_kg': False}, '1': {'rate': 66, 'is_per_kg': False}, '3': {'rate': 87, 'is_per_kg': False}, '15': {'rate': 200, 'is_per_kg': False}, '0.2': {'rate': 58, 'is_per_kg': False}}}, '216_44': {'216_44': {'2.5': {'rate': 75, 'is_per_kg': False}, 'default': {'rate': 13, 'is_per_kg': True}, '10': {'rate': 126, 'is_per_kg': False}, '2': {'rate': 67, 'is_per_kg': False}, '1.5': {'rate': 64, 'is_per_kg': False}, '20': {'rate': 222, 'is_per_kg': False}, '0.5': {'rate': 58, 'is_per_kg': False}, '5': {'rate': 100, 'is_per_kg': False}, '4': {'rate': 90, 'is_per_kg': False}, '1': {'rate': 61, 'is_per_kg': False}, '3': {'rate': 76, 'is_per_kg': False}, '15': {'rate': 180, 'is_per_kg': False}, '0.2': {'rate': 56, 'is_per_kg': False}}}} 

# print(parameters)
# print(parameters.keys())

# for key in sorted(parameters.keys(), reverse=True):
#     print([key])

# possible_origins = []
# for key in sorted(parameters.keys(), reverse=True):
#     origin_location = self._location_lookup('216_{}'.format(origin_id), [key])
#     if origin_location is None or origin_location not in parameters:
#         continue
#     possible_origins.append(parameters[origin_location])

parameter_origins = [
    (
        {
        '216_22': {'default': {'rate': 13, 'is_per_kg': True}}, 
        '216_23': {'default': {'rate': 15, 'is_per_kg': True}, '0.2': {'rate': 15, 'is_per_kg': True}}
        }
    )
]

print(parameter_origins)
print(type(parameter_origins))
print("------------------------")
new_possible_origins = []
parameter_origins['depth'] = 3
new_possible_origins.append(({'location': parameter_origins[key], 'depth': depth}))

print(new_possible_origins)
print(new_possible_origins[0]['depth'])

# possible_origins = [
#     (
#         {
#         '216_22': {'default': {'rate': 13, 'is_per_kg': True}}, 
#         '216_23': {'default': {'rate': 15, 'is_per_kg': True}, '0.2': {'rate': 15, 'is_per_kg': True}},
#         'depth': 2
#         }
#     ),
#     (
#         {
#         '216_33': {'default': {'rate': 13, 'is_per_kg': True}}, 
#         '216_34': {'default': {'rate': 15, 'is_per_kg': True}, '0.2': {'rate': 15, 'is_per_kg': True}},
#         'depth': 3
#         }
        
#     ),
#     (
#         {
#         '216_00': {'default': {'rate': 13, 'is_per_kg': True}}, 
#         '216_01': {'default': {'rate': 15, 'is_per_kg': True}, '0.2': {'rate': 15, 'is_per_kg': True}},
#         'depth': 0
#         }
#     )
# ]

# print(possible_origins[0])
# print(possible_origins[1])
# print(possible_origins[2])

# new_possible_origins = sorted(possible_origins,key=lambda origin: origin['depth'])

# print("------------------------")

# print(new_possible_origins[0])
# print(new_possible_origins[1])
# print(new_possible_origins[2])

# for origin in new_possible_origins:
#     # print( origin )
#     # print( origin[0].keys() )
#     arr = origin[0].keys()
#     for a in arr:
#         print(origin[0][a])

# def splitnaja(params):
#     group_list = [param.split(',') for param in params]
#     return group_list

# parameters = {'216_44,216_77,216_78,216_97': {'216_44,216_77,216_78,216_97': {'default': {'rate': 555, 'is_per_kg': True}}}}
# parameters2 = {
#             "216_44": {
#                 "216_44": {
#                     "default": {"rate": 13, "is_per_kg": True}
#                 },
#                 "216_77": {
#                     "default": {"rate": 15, "is_per_kg": True},
#                     "0.2": {"rate": 15, "is_per_kg": True}
#                 }
#             },
#             "216_212": {
#                 "216_212": {
#                     "default": {"rate": 13, "is_per_kg": True}
#                 }
#             },
#             "216_78": {
#                 "216_44": {"default": {"rate": 1, "is_per_kg": True}},
#                 "216_213": {"default": {"rate": 2, "is_per_kg": True}},
#                 "216_214": {"default": {"rate": 3, "is_per_kg": True}}
#             }
#         }

# parameters3 = {
#             "216_44,216_77,216_78,216_97": {
#                 "216_44": {
#                     "default": {"rate": 13, "is_per_kg": True}
#                 },
#                 "216_77": {
#                     "default": {"rate": 15, "is_per_kg": True},
#                     "0.2": {"rate": 15, "is_per_kg": True}
#                 }
#             },
#             "216_212,216_220": {
#                 "216_212": {
#                     "default": {"rate": 13, "is_per_kg": True}
#                 }
#             },
#             "216_78,216_42": {
#                 "216_44": {"default": {"rate": 1, "is_per_kg": True}},
#                 "216_213": {"default": {"rate": 2, "is_per_kg": True}},
#                 "216_214": {"default": {"rate": 3, "is_per_kg": True}}
#             }
#         }

# print(parameters2.keys() )
# print(parameters3.keys() )

# new_params3 = splitnaja(parameters2.keys())
# merged = list(itertools.chain(*new_params3))
# print(merged)

# print(list(parameters2.keys())[0].split(','))
# if '216_213' not in parameters2:
#     print("Not IN True")
# else:
#     print("IN")
# for key in sorted(parameters2.keys(), reverse=True):
#     print(i, key)
#     print(list(parameters2.keys())[i].split(','))
#     if '216_44' not in (list(parameters2.keys())[i].split(',')):
#         print("True")
#         # print(list(parameters2.keys())[0].split(','))
#     else:
#         print("False")
#         # print(list(parameters2.keys())[0].split(','))
#     i = i + 1


# print(list(parameters2.keys())[0].split(','))
# if '216_44' not in parameters2:
#     print("true")
# else:
#     print("false")
# parameters = {'216_44,216_77,216_78,216_97': {'216_44,216_77,216_78,216_97': {'default': {'rate': 555, 'is_per_kg': True}}}}
# # 216_77
# for key in sorted(parameters.keys(), reverse=True):
#     possible_origin = []
#     possible_origin.append((parameters[key]))
#     print (possible_origin)


# params = [
#     ({'216_44,216_77,216_97': {'default': {'rate': 555, 'is_per_kg': True}}, 
#     '216_78,216_79,216_88': {'default': {'rate': 555, 'is_per_kg': True}}}, 0
#     )]
# params = [({'216_44': {'default': {'rate': 1, 'is_per_kg': True}}, '216_214': {'default': {'rate': 3, 'is_per_kg': True}}, '216_213': {'default': {'rate': 2, 'is_per_kg': True}}}, 0)]
# for param in params:
#     group_destinations = splitnaja(param[0].keys())
#     for group_destination in group_destinations:
#         print(group_destination)
# for param in params:
#     print("216_79")
#     new_params = splitnaja(param[0].keys())
#     print(new_params)
#     print(new_params[0])
#     print(new_params[1])
#     # merged = list(itertools.chain(*new_params))
#     # print(merged)

# l = [['216_44', '216_53', '216_97'], ['216_77','216_822']]
# for i in l:
#     print(i)
#     val = ','.join(i)
#     print(val)
