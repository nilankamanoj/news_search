import json
import codecs

in_file_path='concat.json'

with open(in_file_path,'r') as in_json_file:
    i=1
    # Read the file and convert it to a dictionary
    json_obj_list = json.load(in_json_file)
    json_obj_list_flat = []
    for json_obj in json_obj_list:
        json_obj["year"] = json_obj["date"]["year"]
        json_obj["month"] = json_obj["date"]["month"]
        json_obj["day"] = json_obj["date"]["day"]
        del json_obj["date"]
        json_obj_list_flat.append(json_obj)
    with codecs.open("concat_flat.json", 'w',  encoding='utf8') as out_json_file:
        json.dump(json_obj_list_flat, out_json_file, indent=4, ensure_ascii=False)
