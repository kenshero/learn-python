data = [call('{"payload": {}, "event": "phx_join", "ref": "1", "topic": "transactions:new_transaction_type"}'),
 call('{"payload": {"body": "{\\"rate_card_from_party\\": \\"NewCo\\", \\"name\\": \\"COD\\", \\"rate_card_effective_date\\": \\"2016-03-01\\", \\"pattern\\": \\"RANGE\\", \\"rate_card_to_party\\": \\"Lazada\\"}"}, "event": "new_msg", "ref": "1", "topic": "transactions:new_transaction_type"}')]

print(data)