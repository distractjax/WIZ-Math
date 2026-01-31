from shutil import get_terminal_size 

def outline():
    width, height = get_terminal_size()
    print(f'Width: {width}\nHeight: {height}')
    print(get_terminal_size())
    for x in range (1, height // 2):
        print("|")
    print(draw_horizontal_border(width))
    return "outline"

def draw_horizontal_border(width: int) -> str:
    '''
    This function returns a string that draws a horizontal border given the width of a screen.
    '''
    padding = width // 2
    padding = padding // 2

    width = width - padding * 2

    padding_str = ''.join([" " for x in range(0, padding)])

    middle_str = ''.join(["_" for x in range (0, width)])

    return padding_str + middle_str + padding_str

if __name__ == "__main__":
    outline()
