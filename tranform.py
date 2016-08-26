from decimal import Decimal

def conv(data):
	output = []
	output.append(data[0])
	output.append(float(data[1]))
	print "output: " , output
	return output

data = [('TH1747', Decimal('0.22')), ('TH83', Decimal('22'))]
print data

# result = map(lambda x : x[0] , float(x[1])  , data)
# print result

result = map(conv,data)
print result

result = dict(result)
print "result :" , result
# > f = lambda x, y : x + y
# >>> f(1,1)