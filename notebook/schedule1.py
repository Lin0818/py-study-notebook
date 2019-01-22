# feed with shelve
import shelve
import warnings
import json

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def load():
    with open('data/osconfeed.json') as fp:
        return json.load(fp)
        
def load_db(db):
    raw_data = load()
    warnings.warn('loading' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            print(key + '\r\n')
            record['serial'] = key
            db[key] = Record(**record)
            
db = shelve.open(DB_NAME)
if CONFERENCE not in db:
    load_db(db)

speaker = db['speaker.3471']
