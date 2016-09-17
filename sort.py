seller_weights = [
    {
        "shipper" : "TH83",
        "weight" : 3.000
    },
    {
        "shipper" : "TH88",
        "weight" : 3.000
    },
    {
        "shipper" : "TH86",
        "weight" : 3.000
    }
]

seller_weights2 = [
    {
        "shipper" : "TH83",
        "weight" : 0.1
    }
]


seller_weights3 = [
    {
        "shipper" : "TH83",
        "weight" : 0.1
    },
    {
        "shipper" : "TH88",
        "weight" : 11.1
    }
]

print(seller_weights)
print("--------------------------------------------------")

seller_id = "TH83"
sum_weigth = 0.000
weight = 0.000
result = 0.000
is_indivisible = False
rate = round(100.000, 3)

def get_weight(seller_weight_shipper):
    return seller_weight_shipper

def get_sum_weight(params_sum, weight2):
    return params_sum + weight2

def get_result(weight3, sum_weigth3):
    return (weight3 / sum_weigth3)* rate

def get_indivisible(sum_result_weight):
    if sum_result_weight != rate:
        return True
    return False

def check_indivisible(params_sum_weigth, params_seller_weights):
    sum_indivisible = 0.000
    sum_result_weight = 0.000
    total = False

    for sell in params_seller_weights:
        
        sum_indivisible = get_sum_weight(sum_indivisible, sell['weight'])

    for sell in params_seller_weights:
        result_weight = get_result(sell['weight'], sum_indivisible)
        sum_result_weight = round(sum_result_weight, 3) + result_weight

    sum_result_weight = round(sum_result_weight, 3)
    print("sum_result_weight : " , sum_result_weight,  type(sum_result_weight))
    print("sum_indivisible  : ", sum_indivisible)

    total =  get_indivisible(sum_result_weight)
    return total, sum_result_weight

def cal(sum_weigth, seller_weights):
    for seller_weight in seller_weights:
        if seller_id == seller_weight['shipper']:
            weight = get_weight(seller_weight['weight'])
        sum_weigth = get_sum_weight(sum_weigth, seller_weight['weight'])
    result = get_result(weight, sum_weigth)

    print("Length : ", len(seller_weights))
    print("Weight : ", weight)
    print("Sum Weight : ", sum_weigth)
    print("Result Weight : ", result)

def sort_shipper(seller_weights):
    return sorted(seller_weights, key=lambda k: k.get('shipper'), reverse=False)

if len(seller_weights) == 1:
    cal(sum_weigth, seller_weights)
else:
    is_indivisible, sum_result_weight = check_indivisible(sum_weigth, seller_weights)
    if is_indivisible:
        print("is_indivisible : ", is_indivisible)
        new_seller_weight = sort_shipper(seller_weights)
        print(new_seller_weight)
        result_indivisible = round(rate - sum_result_weight, 3)
        print(sum_result_weight)
        print(rate)
        print(result_indivisible)
        new_seller_weight[0]['weight'] = new_seller_weight[0]['weight'] + result_indivisible
        print(new_seller_weight)
        cal(sum_weigth, new_seller_weight)
    else:
        print("is_not_indivisible : ", is_indivisible)
        cal(sum_weigth, seller_weights)

