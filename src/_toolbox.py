import random


def random_words(n=1000, lower = 3, upper = 10, cutoff=(2,1000)):
    '''return n random words
       95% of these words have length between
       lower and upper
    '''
    def rand_word(n):
        #LETTERS = [chr(65+i) for i in range(26)]
        letters = [chr(97+i) for i in range(26)]
        return ''.join(random.choices(letters, k = n))
    
    rand_int = lambda : int(random.gauss((lower+upper)/2,(upper-lower)/4 ))
    a, b = cutoff
    
    words = []
    for i in range(n):
        while not (a<= (m:=rand_int()) <= b):
            pass
        word = rand_word(m)
        words.append(word)
    return words 



def fen2mat(fen, empty = ' '):
    '''converts a fen-string into a 
       8x8 board-matrix
    '''   
    def expand(row):
        row = [int(ch)* empty if ch.isdigit() else ch for ch in row]
        return ''.join(row)
    
    mat = [ 8*[''] for i in range(8)]
    rows = fen.split('/')
    
    for j,row in enumerate(rows):
        for i, ch in enumerate(expand(row)):
            mat[j][i] = ch
          
    return mat      
