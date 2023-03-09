import sys
import numpy as np


sys.path.append("..")
from config import TOP_K, DEFAULT_TABLE
from logs import LOGGER



def search_in_milvus(table_names, query_sentence, model, milvus_cli, mysql_cli):
    if not table_names:
        table_names = [DEFAULT_TABLE]        
    try:
        vectors = model.sentence_encode([query_sentence])
        LOGGER.info("Sentences successfully encoded")
        
        results = list()
        vids = list()
        for table_name in table_names:
            LOGGER.info(f"TABLE NAME IS {table_name}")
            cur_res = milvus_cli.search_vectors(table_name, vectors, TOP_K)[0]
            vids = [str(x.id) for x in cur_res]
            
            LOGGER.info(f"-----------------{table_name}-----------------{vids}")
            
            if vids:
                ids, texts = mysql_cli.search_by_milvus_ids(vids, table_name)
                results.append({'title': table_name, 'content': texts})

        return results
    
    except Exception as e:
        LOGGER.error(f" Error with search : {e}")
        sys.exit(1)
