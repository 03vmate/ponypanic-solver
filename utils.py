import json

def pprint(obj):
    if(isinstance(obj, dict) or isinstance(obj, list)):
        print(json.dumps(obj, indent=4))
    elif(isinstance(obj, str)):
        try:
            print(json.dumps(json.loads(obj), indent=4))
        except:
            print(obj)