# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/04_utils.ipynb (unless otherwise specified).

__all__ = ['merge_data', 'loadJson']

# Cell
import json # 2.0.9
import numpy as np
import glob
import pandas as pd
import os

def merge_data(folder, drop=[], limit = None):
    all_files = glob.glob(os.path.join(folder, "*.pkl"))
    li = []
    for filename in all_files[:limit]:
        df = pd.read_pickle(filename)
        df = df.drop(columns = drop)
        li.append(df)
    data = pd.concat(li, axis=0, ignore_index=True)
    return data

def loadJson(path, default = {}):
    """Return dictionary from json file."""
    if os.path.isfile(path):
        try:
            with open(path, 'r', encoding = 'utf-8') as f:
                return json.loads(f.read(), strict = False)
        except:
            return default
    else:
        return default