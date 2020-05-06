#!/usr/bin/env python3
import PySimpleGUI as sg
"""
#   Program takes user inputted alphanumeric character and returns the ascii character corresponding to that character
#   in the window
"""

"""
    Layout of GUI
    [ ASCII | HEX ]
    [    binary   ]
    [  amount --> ]
    [{Find} {Quit}]
"""
layout = [[sg.Text("ASCII", key='ascii'), sg.VerticalSeparator(), sg.Text("HEX", key="hex")],
          [sg.InputText(size=(15, 1), key='amount')],
          [sg.Button('Find', key='find'), sg.Quit()]
          ]

window = sg.Window('ASCII Display', layout, location=(120, 300), size=(150, 125))


#   Functions
def find_ascii(user_char):
    ret = ord(user_char)  # finds ascii value of given char
    return ret


def find_hex(user_char):
    ret = hex(ord(user_char))  # finds hexadecimal value of given character
    return ret


def check_valid_input(user_input):
    if len(user_input) > 1 or len(user_input) <= 0:
        return False

    return True

#   Event loop
while True:
    event, value = window.Read()

    if event == 'find':
        user = window.Element('amount').Get()
        isValid = check_valid_input(user)

        while isValid is False:
            user = sg.PopupGetText('Please enter 1\nalphanumeric character', "",
                                   size=(20, 20),
                                   location=(140, 300),
                                   keep_on_top=True)
            isValid = check_valid_input(user)

        window.Element('ascii').Update(find_ascii(user))
        window.Element('hex').Update(find_hex(user))

    elif event == 'Quit' or event is None:
        window.Close()
        break
