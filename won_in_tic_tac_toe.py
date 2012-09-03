playfield = [
    0,0,1,
    2,0,1,
    2,0,1,
    ]

win_situations = []
def generate_win_situations():
    win_situations = [pos for pos in range(0,2)]
    
generate_win_situations()
print [[pos for pos in range(x,3)] for x in [0,3,6]]

