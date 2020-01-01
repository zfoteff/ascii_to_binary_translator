import PySimpleGUI as sg

def asciiToBinary(s):
    print ("Hello, World!")

    bin_str = []

    for c in s:
        ascii_val = ord(c)
        binary_val = bin(ascii_val)
        bin_str.append(binary_val[2:])

    return (" ".join(bin_str))

def binaryToString(s):
    print ("yeet")

o = sg.Text('', auto_size_text=True)
i = sg.InputText('Write Sentence here')
asciiTranslate = sg.Button('To ASCII')
binaryTranslate = sg.Button('To Binary')
quitButton = sg.Button('Quit')

layout = [
            [o],
            [i],
            [asciiTranslate, binaryTranslate, quitButton]
         ]

window = sg.Window('English to Binary Translator', layout)

while True:
    event, value = window.Read()
    if event == 'To Binary':
        inputStr = i.Get()
        newStr = asciiToBinary(inputStr)
        o(newStr)

    elif event == 'To ASCII':
        inputStr = i.Get()
        newStr = binaryToString(inputStr)
        o(newStr)

    elif event == 'Quit' or event is None:
        window.Close()
        break
        
