import json
data='''
[
    {"id":"001",
     "x":"2",
     "name":"murali krishna"
    },
    {"id":"002",
     "x":"7",
     "name":"ashok kumar"
    }
]'''
res=json.loads(data)
print (len(res))
for i in res:
    print("Name",i['name'])
    print("id",i['id'])
    print(i['x'])
