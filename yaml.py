#how to create the yaml file in python

import yaml 

#replace 'AAAA' with the appropriate key
dict_file = {'consumer_key': 'AAAA',
             'consumer_secret': 'AAAA',
             'access_token': 'AAAA',
             'access_token_secret': 'AAAA',
             'g_maps_key': 'AAAA'}

with open('./keys.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)
