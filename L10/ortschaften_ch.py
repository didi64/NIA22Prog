import pickle
with open('/home/jovyan/work/NIA22Prog/data/citydata.pkl', mode = 'rb') as f:
    citynames, dictlist, name_idx = pickle.load(f)

def cityname(name):
    '''gibt den kanonischen Namen der Ortschaft zurueck'''
    i = name_idx.get(name.upper())
    if i is None:
        return None
    return citynames[i]

def coordinates(name):
    '''gibt ein Tuple (lat, lng) zurueck'''
    i = name_idx.get(name.upper())
    if i is None:
        return None
    data = dictlist[i]
    return data['lat'], data['lng']

def population(name, default = 500):
    '''Gibt es eine Ortschaft name, so
       wird die Bevoelkerungszahl oder der default zurueckgegeben,
       anderfalls None
    '''   
    i = name_idx.get(name.upper())
    if i is None:
        return None
    data = dictlist[i]
    return data.get('population', default)