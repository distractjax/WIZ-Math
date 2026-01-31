from shutil import get_terminal_size 

def draw_outline():
    width, height = get_terminal_size()

    width_padding = width // 4
    width = width - width_padding

    height = height // 2

    height_padding = height // 4
    height = height - height_padding

    draw_horizontal_border(width, width_padding)
    draw_vertical_border(height, width, width_padding)
    draw_horizontal_border(width, width_padding)

def draw_horizontal_border(width: int, padding: int, height_padding: int = 2) -> str:
    '''
    This function returns a string that draws a horizontal border given the width of a screen and a horizontal padding.
    '''
    height_padding_str = ''.join(["\n" for x in range(0, height_padding // 2)])

    padding_str = ''.join([" " for x in range(0, padding)])

    middle_str = ''.join(["_" for x in range (0, width)])

    print(height_padding_str + padding_str + middle_str + padding_str + height_padding_str)

def draw_vertical_border(height: int, width: int, width_padding: int) -> str:
    '''
    This function returns a string that draws a vertical border given the height of a screen and both horizontal and vertical padding.
    '''
    width_str = ''.join(" " for x in range(0, width))

    width_str[width_padding] = "|"
    width_str[-width_padding] = "|"

    print('\n'.join([width_str for x in range(0, height)]))

if __name__ == "__main__":
    draw_outline()
