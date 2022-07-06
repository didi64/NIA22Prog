def get_canvas_config(canvas):
    return {'line_width':   canvas.line_width, 
            'stroke_style': canvas.stroke_style, 
            'fill_style':   canvas.fill_style
           }

def config_canvas(canvas, **kwargs):
    # keep old value if no value is supplied
    cc = get_canvas_config(canvas)
    cc.update(kwargs)
    canvas.line_width   = cc['line_width']
    canvas.stroke_style = cc['stroke_style']
    canvas.fill_style   = cc['fill_style']
    
def draw_grid(canvas, n=10, lw=1, color ='black'):
    kwargs = get_canvas_config(canvas)
    
    w, h = canvas.width, canvas.height
    canvas.line_width = lw
    canvas.stroke_style = color
    
    for i in range(n+1):
        canvas.stroke_lines([(i*w/n, 0),(i*w/n, h)])
        canvas.stroke_lines([(0, i*h/n),(w, i*h/n)])
        
    config_canvas(canvas, **kwargs)    
    
def draw_line(canvas, pts, lw=2, color ='black'):
    kwargs = get_canvas_config(canvas)
    
    canvas.line_width = lw
    canvas.stroke_style = color
    canvas.stroke_lines(pts)
    
    config_canvas(canvas, **kwargs)
    
def draw_points(canvas, pts, r=2, color ='black'):
    kwargs = get_canvas_config(canvas)
    
    canvas.fill_style = color
    for x,y in pts:
        canvas.fill_circle(x,y, r)
        
    config_canvas(canvas, **kwargs)   
    
def draw_border(canvas, lw=2, color = 'blue'):
    kwargs = get_canvas_config(canvas)
    
    canvas.line_width = lw
    canvas.stroke_style = color
    canvas.stroke_rect(0, 0, canvas.width, canvas.height)
    
    config_canvas(canvas, **kwargs)
    
def clear_canvas(canvas, border = True):
    canvas.clear()
    if border:
        draw_border(canvas, lw=2, color = 'black')        
