import json
import os
import glob
from turtle import pd

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


def checkKey(dict, key):
    
    if key in dict.keys():
        for a_value in find_key(dict, "_value"):
            atagvalue_list.append(a_value)
        for link in find_key(dict,"href"):
            link_list.append(link)
    else:
        pass


files = glob.glob('K:\legal-set-backend\json/*', recursive=True)
for single_file in files:
    with open(single_file, 'r', encoding="utf-8") as f:
        json_file = json.load(f)
        
    obj = {}
    link_list = []
    atagvalue_list = []

    #check is there value of href is avilable 
    obj["category"] = json_file["category"]
    obj["Titre"] = json_file["Titre"]
    obj["Auteur/Éditeur"] = json_file["Auteur/Éditeur"]
    obj["Édition"] = json_file["Édition"]
    obj["Année"] = json_file["Année"]
    obj["Tribunal/Editeur"] = json_file["Tribunal/Editeur"]
    obj["href"] = json_file["href"]
    obj["metadata"] = json_file["metadata"]

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

    #generate object for content 
    obj["content"] = []
    for i in value_list:
        obj["content"].append(i)



    #link text and index
    first_index = []
    last_index = []
    value = ",".join(obj["content"])
    for txt in atagvalue_list:
        str_file = value
        f_index = str_file.find(txt)
        l_index = f_index+len(txt)
        first_index.append(f_index)
        last_index.append(l_index)

    #generate object for links
    obj["links"] = []
    for (link, text, fi_index, la_index) in zip(link_list, atagvalue_list, first_index, last_index ):
        obj["links"].append({
            "text_":text,
            "link_":link,
            "first_index": fi_index, 
            "last_index": la_index,
        })
    
    #get file name as it is
    splt = single_file.split("\\")[3]
    file_name = splt.split(".")[0]

    #json created
    dataObject = json.dumps(obj, ensure_ascii=False)  
    with open(f"K:\legal-set-backend\jsons/u{file_name}.json", "w", encoding="utf-8") as outfile:
        outfile.write(dataObject)

    print(">>>>>>>>>>>>>>>>>>")
    print(f"{splt}>>>> converted")
    print(">>>>>>>>>>>>>>>>>>")
    
print("convert task completed")




