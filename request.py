import io

from json import loads

import requests

class AttributeDict(dict):
    def __getattr__(self, attr):
        if self.has_key(attr):
            return self[attr]
        else:
            filter = attr + "__";
            subopt = [(k[len(filter):], v) for k, v in self.items() if k.startswith(filter)]
            if len(subopt):
                self[attr] = AttributeDict(subopt)
                return self[attr]
            else:
                print(str(self))
                raise AttributeError(attr)


def get(url):
    """Fetch resource from fostgres and return them one at a time.
    """
    response = requests.get(url, headers=dict(Accept="application/csj"))
    import ipdb; ipdb.set_trace()
    lines = response.content.split('\n')
    header = loads('[%s]' % lines[0])
    for line in lines[1:]:
        if line:
            yield AttributeDict(zip(header, loads('[%s]' % line)))

def get_resource():
	r = get('http://172.16.238.1:35001/transaction-value/th/311118429-0002/NewCo/Lazada/COD-Kerry/2016-03-01')
	for item in r:
		import ipdb; ipdb.set_trace()

# data = r.text
# # print(repr(data))

# row = data.split('\n')
# print((row[0]))
# key = row[0].split(',')
# print("------------------------------------------------------------------")
# # val = row[1].split(',')
# jsontest = json.dumps(row[1])
# val = json.loads(jsontest)
# print(val)

# # buff = io.StringIO(data)
# # row_head = buff.readline()
# # row_head = row_head.split(',')
# # # print row_head
# # row_content = buff.readline()
# # row_content= row_content.split(',')
# # print row_content

# dictionary = dict(zip(key, val))

# # print(dictionary)
# # print("///////////////////////////////////////////////////////////")
# # print(dictionary["date_basis_datetime"])
# # print(dictionary["package_id"])