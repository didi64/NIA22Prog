'''
Module zum Lesen einer .csv Datei 
als Liste oder Tabellenstring.
'''
from toolbox import table2str

def csv2list(file, sep = ',', fields = None):
    '''returns a list of lists
    
       file:   filepath
       sep:    string that separates fields
       fields: tuple of fields to extract
    '''   
    lines = []
    with open(file, mode = 'r') as f:
        for line in f:
            row = line.rstrip().split(sep)
            if fields:
                row = [row[i] for i in fields]
            lines.append(row)
    return lines

def csv2tablestr(file, m=None, n=None, sep = ',', fields = None):
    '''returns content of csv-File as a tablestring
    
       file:   filepath
       m,n:    integer or None
               if m is None, all rows are returned
               else, only the header plus the first m rows are returned, plus the
               last n rows if n is not None
               
       sep:    string that separates fields
       fields: tuple of fields to extract
    '''
    lines = csv2list(file, sep, fields)
    
    if m is None:
        return table2str(lines[0], lines[1:])   
    elif n is None:
        return table2str(lines[0], lines[1:1+m])   
    else:
        return table2str(lines[0], lines[1:1+m]+lines[-n:])   

if __name__ =='__main__':
    fn = '/home/jovyan/work/NIA22Prog/data/ch.csv'
    s = csv2tablestr(fn, 2, 2, fields=(0,1,2,7))
    print(s)
