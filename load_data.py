import os
import os.path   
from logs import LOGGER
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware
from milvus_helpers import MilvusHelper
from mysql_helpers import MySQLHelper
from operations.load import do_load
from operations.search import search_in_milvus
from operations.count import do_count
from operations.drop import do_drop
from logs import LOGGER
from encode import SentenceModel, LaserSentenceModel, LaBSESentenceModel

# MODEL = SentenceModel()
LASER_MODEL = LaserSentenceModel()
MILVUS_CLI = MilvusHelper()
MYSQL_CLI = MySQLHelper()


table_dataset_mapping = {
    'Hafez': ('/root/text-enrich/server/src/data/hafez_normalized.csv', 'fa'),
    'Quotes': ('/root/text-enrich/server/src/data/quotes_normalized.csv', 'en'),
    'Moulavi': ('/root/text-enrich/server/src/data/shams_normalized.csv', 'fa'),
    'Poem': ('/root/text-enrich/server/src/data/poem_normalized.csv', 'fa'),
    'Nahj_Al_Balaqa': ('/root/text-enrich/server/src/data/nahj_normalized.csv', 'ar')
}


# do_drop(table_name, MILVUS_CLI, MYSQL_CLI)

for table_name, data_set_tuple in table_dataset_mapping.items():
    path, lang = data_set_tuple
    
    do_load(table_name, path , LASER_MODEL, MILVUS_CLI, MYSQL_CLI, lang)