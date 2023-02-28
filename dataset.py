import re
from typing import List

# 495 Hafez qazals
# [\s\S*] has been used for covering first line unicdoe character ('\ufeff')
qazal_pattern = re.compile(r'\n?[\s\S*]غزل[\s+]{3,}[\S\s]+?\n\n')
hafez_qazals_path = './datasets/hafez/hafez-qazals.txt'

# 147 Poems (yek-beiti)
poems_path = './datasets/poems/yek-beiti.txt'

# 3229 Moulavi divan-e-shams qazals
moulavi_qazals_pattern = re.compile(r'\n?\s*\d+\s*?\n')
moulavi_qazals_path = './datasets/moulavi/divane-e-shams.txt'

def read_qazals() -> List[str]:
    """Read Hafez qazals and return an array of his qazals.

    Returns:
        List[str]: Array of qazals.
    """
    with open(hafez_qazals_path, encoding='utf-8') as f:
        text = f.read()
        
    qazals_arr = qazal_pattern.split(text)
    return qazals_arr[1:]

# test that the qazals have been read correctly
# print(read_qazals()[494])

def read_poems():
    with open(poems_path, encoding='utf-8') as f:
        poems = f.readlines()
        return poems


# test that the poems have been read correctly
# print(read_poems()[146])


def read_divan_shams():
    with open(moulavi_qazals_path, encoding='utf-8') as f:
        text = f.read()
        
    qazals_arr = moulavi_qazals_pattern.split(text)
    return qazals_arr[1:]

# test that the moulavi qazals have been read correctly
# print(read_divan_shams()[3228])
