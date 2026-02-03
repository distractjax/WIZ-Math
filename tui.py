from shutil import get_terminal_size 

def test_width():
    width, height = get_terminal_size()
    test_string = ''.join("1" for x in range(0, width))
    print(test_string)

def draw_outline():
    width, height = get_terminal_size()
    width_padding = width // 4
    width = width - (width_padding * 2)
    height_padding = height // 4
    height = height - (height_padding * 2)
    draw_horizontal_border(width, width_padding)
    draw_vertical_border(height, width, width_padding)
    draw_horizontal_border(width, width_padding)

def draw_horizontal_border(width: int, padding: int, height_padding: int = 2) -> str:
    '''
    This function returns a string that draws a horizontal border given the width of a screen and a horizontal padding.
    '''
    height_padding_str = ''.join(["\n" for x in range(0, height_padding // 2)])
    padding_str = ''.join(["1" for x in range(0, padding)])
    middle_str = ''.join(["0" for x in range (0, width)])
    print(padding_str + middle_str + padding_str)

def draw_vertical_border(height: int, width: int, width_padding: int) -> str:
    '''
    This function returns a string that draws a vertical border given the height of a screen and both horizontal and vertical padding.
    '''
    width_array = [" " for x in range(0, width)]
    width_array[width_padding] = "|"
    width_array[-width_padding-1] = "|"
    width_str = ''.join(x for x in width_array)
    print('\n'.join([width_str for x in range(0, height)]))

def test_draw() -> str:
    '''
    This is a test function that sees how things are working
    '''
    width_array = [str(x) for x in range(0, 5)]
    width_array[1] = "|"
    width_array[-2] = "|"
    width_str = ''.join(x for x in width_array)
    print('\n'.join([width_str for x in range(0, 10)]))

if __name__ == "__main__":
    draw_outline()
    # test_draw()
    test_width()
