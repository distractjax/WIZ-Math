from shutil import get_terminal_size 
from sys import stdout

def draw_outline(input_text: str):
    width, height = get_terminal_size()
    width_padding = width // 8
    width = width - (width_padding * 2)
    height_padding = height // 8
    height = height - (height_padding * 2)
    stdout.write("\033[H\033[2J")
    stdout.flush()
    draw_horizontal_border(width, width_padding)
    draw_vertical_border(height, width, width_padding, input_text)
    draw_horizontal_border(width, width_padding)

def draw_horizontal_border(width: int, padding: int) -> str:
    '''
    This function returns a string that draws a horizontal border given the width of a screen and a horizontal padding.
    '''
    padding_str = ''.join([" " for x in range(0, padding)])
    middle_str = ''.join(["-" for x in range (0, width)])
    print(padding_str + middle_str + padding_str)

def draw_vertical_border(height: int, width: int, width_padding: int, input_text: str) -> str:
    '''
    This function returns a string that draws a vertical border given the height of a screen and both horizontal and vertical padding.
    '''
    input_text_arr = smart_textwrap(input_text,width - 3)
    width = width + (width_padding * 2)
    width_array = [" " for x in range(0, width)]
    width_array[width_padding] = "|"
    width_array[-width_padding-1] = "|"
    output_arr = []
    for x, y in enumerate(input_text_arr):
        temp_arr = width_array.copy()
        temp_arr[width_padding + 2:width_padding + 2 + len(y)] = y
        output_arr.append(''.join(x for x in temp_arr))
    output_arr.append(''.join(x for x in width_array))
    print('\n'.join([output_arr[x] if x < len(output_arr) else output_arr[len(output_arr)-1] for x in range(0, height)]))

def test_draw() -> str:
    '''
    This is a test function that sees how things are working
    '''
    width_array = [str(x) for x in range(0, 5)]
    width_array[1] = "|"
    width_array[-2] = "|"
    width_str = ''.join(x for x in width_array)
    print('\n'.join([width_str for x in range(0, 10)]))

def smart_textwrap(input_text: str, length: int) -> list[str]:
    '''
    This function takes an input string and splits it by character length.
    '''
    input_arr = input_text.split()
    output_arr = ['']
    output_index = 0
    for x in input_arr:
        if (len(output_arr[output_index]) + len(x)) < length:
            output_arr[output_index] = output_arr[output_index] + x + " "
        else:
            output_arr.append(f'{x} ')
            output_index += 1
    return output_arr

if __name__ == "__main__":
    draw_outline('This is a test for a very long string because we want to determine if very long strings will be split also I need to think of a way to incorporate newline characters.')
    # test_draw()
    # smart_textwrap("This is a test.", 10)
