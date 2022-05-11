import random
from toolbox import sign

def show_history(h):
    '''displays the list h as a table
       h: list of tuples, [(bool, str),...]
    '''
    COL_WIDTHS = (4, 10, 10)
    TABLE_WIDTH = sum(COL_WIDTHS) + 2 + 2
    
    h1 = 'Nr.'.ljust(COL_WIDTHS[0])
    h2 = 'guess'.ljust(COL_WIDTHS[1]) 
    h3 = 'comment'.ljust(COL_WIDTHS[2]) 
    
    hline = TABLE_WIDTH * '='
    print(hline)
    print('|{h1}|{h2}|{h3}|'.format(h1=h1, h2=h2, h3=h3))
    print(hline)
    
    for i, (n, comment) in enumerate(h):
        print('|{c1}|{c2}|{c3}|'.\
              format(c1 = str(i+1).ljust(COL_WIDTHS[0]), 
                     c2 = str(n).ljust(COL_WIDTHS[1]), 
                     c3 = comment.ljust(COL_WIDTHS[2])
                    )
             )
        
    print(hline)    

def eval_guess(guess, n):
    '''returns a tuple (is_ok: bool, comment: str)
       is_ok: True, if guess equals n
       comment: 'too big', 'correct' or 'too small'
    '''
    comments = {1: 'too big', 
                0: 'correct', 
                -1:'too small',
               }
    
    is_ok = guess == n
    sig = sign(guess-n)
    return is_ok, comments[sig]

def play_game(lower=0, upper=100):
    '''guess a random Integer between lower and upper,
       lower and upper are included
    '''   
    nbr = random.randint(lower, upper)
    history = []
    
    while True:
        n = input('Zahl zwischen {a} und {b}? '.format(a=lower, b=upper))
        n = int(n)
        is_correct, comment = eval_guess(n, nbr)
        history.append((n, comment))    
        
        if is_correct:
            break
        else:
            print(comment)
        
    print('Congrats! You guessed the number {N} in {n} tries.'.format(N=nbr, n=len(history)))
    show_history(history)
    
    
if __name__ == '__main__':
    play_game()    
