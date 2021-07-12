# Take Home Challenge Instructions/Tasks:
# Render canvas with a specified height and width
# Add a shape to a canvas
# "shape" = the shape to add -- for now, only rectangles
# Clear all shapes from a canvas

# Create a rectangle
# "start_x" = X coordinate of the upper-left-hand corner of the rectangle
# "start_y" = Y coordinate of the upper-left-hand corner of the rectangle
# "end_x" = X coordinate of the lower-right-hand corner of the rectangle
# "end_y" = Y coordinate of the lower-right-hand corner of the rectangle
# "fill_char" = the character that should be used to draw the rectangle

# Change a rectangle's fill character
# "char" = the character to use in order to draw a pre-existing rectangle

#Translate (move left, right, up, or down)
# "axis" = which axis should we translate the rectangle on
# "num" = how much to move the rectangle
# negative numbers will cause the rectangle to shift left or down
# positive numbers will cause the rectangle to shift right or up

# [ ][ ][$][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][$][ ]
# [ ][ ][ ][ ][ ][ ]
# [ ][ ][ ][ ][ ][ ]

def get_canvas_dimensions():
    """Gets canvas dimensions from user input """

    height = int(input("Canvas height?  "))
    width = int(input("Canvas width?  "))

    dimensions = {"height": height,
                    "width": width}

    return dimensions


def show_rows(canvas):
    """Prints all rows in canvas"""

    for row in canvas:
        print(print_entire_row(row))



def render_canvas():
    """Returns a list of lists with spaces according to canvas dimensions"""

    dimensions = get_canvas_dimensions()

    canvas = []
    row = []
    for num in range(dimensions["width"]):
        row.append(" ")
    
    for num in range(dimensions["height"]):
        new_row = row[:]
        canvas.append(new_row)
    
    show_rows(canvas)

    return canvas


def print_entire_row(row):
    """Prints the contents of a row on one line"""

    print_row = ""
    for char in row:
        print_row = f'{print_row}{char}'
    return print_row


#                       2       4       5       1
def create_rectangle(start_x, start_y, end_x, end_y, fill_char, canvas):
    """Creates a rectangle with the given coordinates"""

    canvas[-start_y][start_x] = fill_char
    canvas[-end_y][end_x] = fill_char
    # canvas[-4][2]
    # canvas [-1][5]
    canvas[-start_y][end_x] = fill_char
    canvas[-end_y][start_x] = fill_char

    show_rows(canvas)
    


def add_shape(shape, canvas):
    """Adds a shape to the canvas"""

    if shape == "rectangle":
        start_x = int(input("Start X?  "))
        start_y = int(input("Start Y?  "))
        end_x = int(input("End X?  "))
        end_y = int(input("End Y?  "))
        fill_char = input("Fill char?  ")
        create_rectangle(start_x, start_y, end_x, end_y, fill_char, canvas)
        show_rows(canvas)
    else:
        print("Sorry, not an option")


def clear_all(canvas):
    """Clears all shapes from canvas"""

    for idx, row in enumerate(canvas):
        for i in range(0, len(row)):
            canvas[idx][i] = " "
    
    show_rows(canvas)


def change_fill_char(canvas, fill_char, char):
    """Changes the fill character of an existing rectangle"""

    for idx, row in enumerate(canvas):
        for i in range(0, len(row)):
            if canvas[idx][i] == fill_char:
                canvas[idx][i] = char
    
    show_rows(canvas)


def translate(axis, num, canvas, fill_char):
    """Translates triangle"""

    if axis == "x":
        for idx, row in enumerate(canvas):
            for i, char in enumerate(row):
                if row[i] == fill_char:
                    row[i] = " "
                    # row[i + num] = fill_char
                # print(f'{i} {char}')

                # if canvas[idx][i] == fill_char:
                #     canvas[idx][i] = " "
                #     canvas[idx][i + num] = fill_char
    # issue to fix: index out of range
    show_rows(canvas)