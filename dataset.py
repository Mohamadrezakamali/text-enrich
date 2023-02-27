import re
from typing import List

# [\s\S*] has been used for covering first line unicdoe character ('\ufeff')
qazal_pattern = re.compile(r'[\s\S*]غزل[\s+]{3,}[\S\s]+?\n')
qazals_path = './datasets/hafez/hafez-qazals.txt'

def read_qazals() -> List[str]:
    """Read Hafez qazals and return an array of his qazals.

    Returns:
        List[str]: Array of qazals.
    """
    with open(qazals_path, encoding='utf-8') as f:
        lines = f.readlines()
        from functools import reduce
        text = reduce(lambda x,y: x + y, lines)
        
    qazals_arr = qazal_pattern.split(text)
    return qazals_arr[1:]

# test that the qazals have been read correctly
print(read_qazals()[200])