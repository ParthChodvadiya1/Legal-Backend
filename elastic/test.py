from elasticsearch import Elasticsearch, helpers
import sys, json
import os


es = Elasticsearch()

def load_json(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(filename,'r',encoding="utf8") as open_file:
                yield json.load(open_file)

# helpers.bulk(es, load_json("K:\legal-set-backend\jsons"), index='my-index')
helpers.bulk(es, load_json('\legal-set-backend-feature1\elastic'), index='my-inde')

