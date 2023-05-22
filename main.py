
from tkinter import *


def convert_to_number():
    roman_numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    roman_text = entry_line.get().upper()
    number = 0
    i = 0
    while i < len(roman_text):
        if i + 1 < len(roman_text) and roman_text[i:i + 2] in roman_numerals:
            number += roman_numerals[roman_text[i:i + 2]]
            i += 2
        elif roman_text[i] in roman_numerals:
            number += roman_numerals[roman_text[i]]
            i += 1
        else:
            result_text.delete(1.0, END)
            result_text.insert(END, "Invalid Roman numeral")
            return

    if 1 <= number <= 4999:
        result_text.delete(1.0, END)
        result_text.insert(END, str(number))
    else:
        result_text.delete(1.0, END)
        result_text.insert(END, "Invalid Roman numeral. Please enter a valid Roman numeral between 1 and 4999.")


window = Tk()
window.title("Roman Numeral Converter")
window.minsize(width=400, height=500)

label_line1 = Label(text="Convert Roman numerals to numbers", font=('Arial', 10, "bold"))
label_line1.pack()
label_line1.config(pady=10, padx=10)


entry_line = Entry(width=40)
entry_line.pack()


clear_button = Button(text="Clear", command=lambda: result_text.delete(1.0, END))
clear_button.pack(side="left", padx=10, pady=(0, 350))
clear_button.config(width=10)


calculate_button = Button(text="Calculate", command=convert_to_number)
calculate_button.pack(side="right", padx=10, pady=(0, 350))
calculate_button.config(width=10)





label_line2 = Label(text="Answer", font=('Arial', 10, "bold"))
label_line2.pack(pady=70)
label_line2.config()


result_text = Text(width=40, height=15)
result_text.pack()








window.mainloop()