import json


def find_key(obj, key):
    if isinstance(obj, dict):
        yield from iter_dict(obj, key,)
    elif isinstance(obj, list):
        yield from iter_list(obj, key,)

def iter_dict(d, key,):
    for k, v in d.items():
        if k == key:
            yield v
            # yield "_value"
        if isinstance(v, dict):
            yield from iter_dict(v, key,)

        elif isinstance(v, list):
            yield from iter_list(v, key,)


def iter_list(seq, key,):
    for k, v in enumerate(seq):
        if isinstance(v, dict):
            yield from iter_dict(v, key,)
 
        elif isinstance(v, list):
            yield from iter_list(v, key,)

with open("2.json", 'r', encoding="utf-8") as f:
    json_file = json.load(f)


obj = {}

link_list = []
atagvalue_list = []

#check is there value of href is avilable 
def checkKey(dict, key):
      
    if key in dict.keys():
        for a_value in find_key(dict, "_value"):
            atagvalue_list.append(a_value)
        for link in find_key(dict,"href"):
            link_list.append(link)
    else:
        pass


#content and links
value_list = []
for i in json_file["html"]:
    for a_tag in find_key(i, "a"):
        checkKey(a_tag[0],"_value")
    _value = []     
    for key in iter_dict(i,"_value"):
        _value.append(key)
    value = " ".join(_value.copy())
    value_list.append(value)
    _value.clear()


first_index = []
last_index = []
#link text and index

# for txt in atagvalue_list:
#     str_file = str(value_list)
#     f_index = str_file.find(txt)
#     l_index = f_index+len(txt)
#     first_index.append(f_index)
#     last_index.append(l_index)

#generate object for links
obj["links"] = []
for (link, text, fi_index, la_index) in zip(link_list, atagvalue_list, first_index, last_index ):
    obj["links"].append({
        "text_":text,
        "link_":link,
        "first_index": fi_index, 
        "last_index": la_index,
    })

#generate object for content 
obj["content"] = []
for i in value_list:
    obj["content"].append(i)


value = ",".join(obj["content"])
for txt in atagvalue_list:
    str_file = value 
    f_index = str_file.find(txt)
    l_index = f_index+len(txt)
    first_index.append(f_index)
    last_index.append(l_index)

for i in range(len(first_index)):
    print((first_index[i],last_index[i]))


dataList = []
dataList.append(obj)

dataObject = json.dumps(dataList, ensure_ascii=False)  

# print(dataObject)
# with open("u2.json", "w", encoding="utf-8") as outfile:
#     outfile.write(dataObject)


  
ch1 = "BGG"
  

pos = value.index(ch1,1)
  
print ("The first position of geeks after 2nd index : ",end="")
print (pos)



