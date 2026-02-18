import numpy as np

def simulate_drift(data, feature="usage_trend"):
    data[feature] = np.random.choice(["up","down","flat"], size=len(data.get(feature, [0])))
    return data
