import pandas as pd



def get_key(val, dictionary):
    """Find the key associated with a value in a dictionary"""
    for key, value in dictionary.items():
        if val == value:
            return key

def get_initial_proba():
    prob_first_loc = pd.read_csv('../data/first_loc_prob.csv', index_col = 0)
    initial_probabilities = prob_first_loc['first_loc_prob'].to_numpy()
    return initial_probabilities

def get_tpm():
    P = pd.read_csv('../data/transition_prob_matrix.csv', index_col=0)
    return P

def cust_per_min():
    CUST_PER_MIN = pd.read_csv('../data/cust_freq.csv', index_col = 0)
    return CUST_PER_MIN

def cust_per_min_corona():
    CUST_PER_MIN = pd.read_csv('../data/cust_freq_corona.csv', index_col = 0)
    return CUST_PER_MIN
