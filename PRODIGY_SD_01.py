import tkinter as tk
from tkinter import messagebox

def celsius_fahrenheit(celsius):
    cel_fah = (1.8) * celsius + 32
    return cel_fah

def celsius_kelvin(celsius):
    cel_kel = celsius + 273.15
    return cel_kel

def fahrenheit_celsius(fahrenheit):
    fah_cel = (fahrenheit-32) * (5/9)
    return fah_cel

def fahrenheit_kelvin(fahrenheit):
    fah_kel = (fahrenheit-32)*(5/9)+273.15
    return fah_kel

def kelvin_celsius(kelvin):
    kel_cel = kelvin-273.15
    return kel_cel

def kelvin_fahrenheit(kelvin):
    kel_fah = (kelvin-273.15)*1.8+32  
    return kel_fah

def temp_convert():
    value = entry_value.get()
    temp_unit = entry_unit.get().upper()

    if not value.replace('.', '', 1).isdigit():
        messagebox.showerror("Invalid value", "Please enter a valid number")
        return

    value = float(value)

    if temp_unit == 'C':
        f = celsius_fahrenheit(value)
        k = celsius_kelvin(value)
        result_label.config(text=f"{value}°C is converted to {f:.2f}°F and {k:.2f}°K")
    elif temp_unit == 'F':
        c = fahrenheit_celsius(value)
        k = fahrenheit_kelvin(value)
        result_label.config(text=f"{value}°F is converted to {c:.2f}°C and {k:.2f}°K")
    elif temp_unit == 'K':
        c = kelvin_celsius(value)
        f = kelvin_fahrenheit(value)
        result_label.config(text=f"{value}°K is converted to {c:.2f}°C and {f:.2f}°F")
    else:
        messagebox.showerror("Error", "Invalid unit of measurement")


root = tk.Tk()
root.title("Temperature Conversion")


label_value = tk.Label(root, text="Enter the temperature value:")
label_value.pack()

entry_value = tk.Entry(root)
entry_value.pack()

label_unit = tk.Label(root, text="Enter the unit (C, F, K):")
label_unit.pack()

entry_unit = tk.Entry(root)
entry_unit.pack()

convert_button = tk.Button(root, text="Convert", command=temp_convert)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
