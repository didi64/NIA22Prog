import pickle
with open('/home/jovyan/work/NIA22Prog/data/citydata.pkl', mode = 'rb') as f:
    citynames, dictlist, name_idx = pickle.load(f)

def cityname(name):
    i = name_idx.get(name.upper())
    if i is None:
        return None
    return citynames[i]

def coordinates(name):
    i = name_idx.get(name.upper())
    if i is None:
        return None
    data = dictlist[i]
    return data['lat'], data['lng']

def population(name, default = 500):
    i = name_idx.get(name.upper())
    if i is None:
        return None
    data = dictlist[i]
    return data.get('population', default)