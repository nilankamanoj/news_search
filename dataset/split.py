import json
import codecs

in_file_path='concat.json'

with open(in_file_path,'r') as in_json_file:
    i=1
    # Read the file and convert it to a dictionary
    json_obj_list = json.load(in_json_file)

    for json_obj in json_obj_list:
        filename='splitted/news_'+str(i)+'.json'
	    i+=1
        with codecs.open(filename, 'w',  encoding='utf8') as out_json_file:
            json.dump(json_obj, out_json_file, indent=4, ensure_ascii=False)
