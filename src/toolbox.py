def sign(x):
    '''returns the sign of the number x'''
    return (x<0 and -1) or (x>0 and 1) or 0
    
def table2str(header, rows, sep = '|', fillchar = ' ', hline_char = '='):
    '''returns a string displaying a table
    
       header: tuple of column names, e.g. ('Name', 'Email')
       rows:  list of tuples of strings, e.g. [('Bob', 'foo@bar.ch'), ...]          
    '''   
    def table_row(row, widths, sep = '|', fillchar = ' '):
        fstring = (sep+'{}') * len(row) + sep
        args = []
        for s, w in zip(row, widths):
            s = s.ljust(w, fillchar)
            args.append(s)
   
        return fstring.format(*args)

    def get_widths(header, rows):
        widths = [len(h) for h in header]
        for row in rows:
            for i,item in enumerate(row):
                widths[i] = max(widths[i], len(item))
        return widths                  

    res = []
    widths = get_widths(header, rows)
    hline = ('',) * len(header)
    
    res.append(table_row(header, widths, sep, fillchar))
    res.append(table_row(hline, widths, sep, fillchar = hline_char))
   
    for row in rows:
        res.append(table_row(row, widths, sep, fillchar))
        
    return '\n'.join(res)        
