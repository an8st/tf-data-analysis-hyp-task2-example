import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 805920792 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:    
    return anderson_ksamp([x, y]).pvalue < 0.08
