import os
import json

WRITE_TO_FILE = os.getenv('WRITE_TO_FILE', 'True')
PARSER = os.getenv('PARSER', 'base')



#if we want to write to file lets set it up
if WRITE_TO_FILE != "False":
    f = open("/out/{}.json".format(PARSER), "a")





def WriteToFile(json_data):
    '''
    Write content into file
    '''
    json.dump(json_data, f, ensure_ascii=False,  sort_keys=True, separators=(',', ': '))
    f.write("\n")



def logger(json_data):
    '''
    This is where we parse our json and

    - Add json data from the deployment
    - Send data to samma.io
    - Print out the data in json format 
    '''
    # Samma tags
    json_samma={} 
    json_samma['scanner'] = os.getenv('SAMMA_IO_SCANNER', 'base')
    json_samma['id'] = os.getenv('SAMMA_IO_ID', '1234')
    json_samma['tags'] = os.getenv('SAMMA_IO_TAGS', "['a','b']")
    json_samma['json'] = os.getenv('SAMMA_IO_JSON', '{"value":"a"}')



    #Adding the extra data
    json_data['samma-io'] = json_samma

    #If WRITE_TO_FILE != False
    if WRITE_TO_FILE != "False":
        WriteToFile(json_data)

    print(json_data)