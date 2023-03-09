import sys
import numpy as np
import pandas as pd

sys.path.append("..")
from config import DEFAULT_TABLE
from logs import LOGGER


# Get the vector of question
def extract_features(file_dir, model, lang):
    try:
        data = pd.read_csv(file_dir)
        text_data = data['output_text'].tolist()
        sentence_embeddings = model.sentence_encode(text_data, lang)
        return text_data, sentence_embeddings
    except Exception as e:
        LOGGER.error(f" Error with extracting feature from question {e}")
        sys.exit(1)


def format_data(ids, text_data):
    # Combine the id of the vector and the question data into a list
    data = []
    for i in range(len(ids)):
        value = (str(ids[i]), text_data[i])
        data.append(value)
    return data


# Import vectors to Milvus and data to Mysql respectively
def do_load(collection_name, file_dir, model, milvus_client, mysql_cli, lang='fa'):
    if not collection_name:
        collection_name = DEFAULT_TABLE
    text_data, sentence_embeddings = extract_features(file_dir, model, lang)
    ids = milvus_client.insert(collection_name, sentence_embeddings)
    milvus_client.create_index(collection_name)
    milvus_client.load(collection_name)
    mysql_cli.create_mysql_table(collection_name)
    mysql_cli.load_data_to_mysql(collection_name, format_data(ids, text_data))
    return len(ids)
