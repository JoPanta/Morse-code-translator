import tkinter

window = tkinter.Tk()
window.title("Morse Code Translator")
window.minsize(width=500, height=300)
# window.config(bg="black")



window.mainloop()

title_label = tkinter.Label(text="Morse Code Translator")
title_label.pack()

tk_input = tkinter.Entry()
tk_input.pack()
#
#
# morse_code_dict = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..',
#     '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
#     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#     '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
#     '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
#     '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
#     '@': '.--.-.', ' ': ' '
# }
#
# response = input("What do you want to translate?: ")
# response = response.upper()
#
# translated_response = ""
# for letter in response:
#   if letter in morse_code_dict:
#     translated_response += morse_code_dict[letter] + " "
#   else:
#     print("Invalid character.")
#
# print(translated_response)

