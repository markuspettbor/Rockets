from PIL import Image, ImageTk

def blank_img(w, h, col = 'white'):
    '''Creates blank (white) image of size w x h.
    Assumes w, h to be integers
    '''
    img =  Image.new(mode = 'RGB', size = (w, h), color = col)
    return img
