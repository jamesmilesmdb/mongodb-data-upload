import xmltodict
import json

# Get file from argv
xml_imput = ""

dict_output = xmltodict.parse(xml_input)

mongo_data = json.dumps(dict_output)
