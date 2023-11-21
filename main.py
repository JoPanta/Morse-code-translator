import tkinter


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', ' ': ' '
}


window = tkinter.Tk()
window.title("Morse Code Translator")
window.minsize(width=500, height=300)
# window.config(bg="black")


title_label = tkinter.Label(text="What do you want to translate?")
title_label.grid(row=0, pady=20, padx=5)
title_label.config(font=("Courier", 20))

tk_input = tkinter.Entry()
tk_input.grid(row=1, column=0, columnspan=3, pady=20)
tk_input.config(width=50)

def button_clicked():
    response = tk_input.get().upper()
    translated_response = ""
    for letter in response:
        if letter in morse_code_dict:
            translated_response += morse_code_dict[letter] + " "
        else:
            print("Invalid character.")
    result_label.config(text=f'{translated_response}')

button = tkinter.Button(text="Translate", command=button_clicked)
button.grid(row=2)

result_label = tkinter.Label(text="Results will be shown here.")
result_label.grid(row=3, pady=30)
result_label.config(font=("Courier", 10), foreground="black", bg="white")

window.mainloop()

