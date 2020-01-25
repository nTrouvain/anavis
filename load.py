from elasticsearch import Elasticsearch
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from dateutil.parser import parse
from tqdm import tqdm

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Connected')
    else:
        print('Failed to connect!')
    return _es

es = connect_elasticsearch()

data_index = "stations-data"
station_index = "station"

data_id = 1
station_id = 0

# clear base
try:
    es.indices.delete(index=data_index)
except:
    pass
try:
    es.indices.delete(index=station_index)
except:
    pass


def check_data_upload():
    res = es.search(index=data_index, body={"query": {"match_all": {}}})
    assert res['hits']['total']['value'] == data_id

def send_station(station):
    global station_id
    station_id += 1
    res = es.index(index=station_index, id=data_id, body=station)

def check_station_upload():
    res = es.search(index=station_index, body={"query": {"match_all": {}}})
    assert res['hits']['total']['value'] == station_id


datas = []
mypath = "./Stations"
for d in listdir(mypath):
    # print("dir : " ,d)
    for f in tqdm(listdir(join(mypath, d))[:5]):
        # print(join(mypath, d,f))
        df = pd.read_csv(join(mypath, d,f), compression='gzip')
        df["Timestamp"] = df["Timestamp"].apply(lambda x : parse(x).isoformat())

        for _, row in df.iterrows():
            datas.append('{ "index" : { "_index" : "' + data_index +'" } }')
            datas.append(row.to_json())

            if(len(datas) == 1000):
                es.bulk(datas)
                datas = []

if len(datas) >= 0:
    es.bulk(datas)
    datas = []

print(data_id)
res = es.search(index=data_index, body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])