import tkinter as tk
import requests

#WeatherAPI key
API_KEY = "a3adfbf67dd8423399b94607252907"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def getWeather():
    city = textfield.get()
    if city and city != "Enter city name:":
        try:
            url = f"{BASE_URL}?key={API_KEY}&q={city}"
            response = requests.get(url)
            data = response.json()

            if "error" in data:
                label1.config(text="City not found")
                label2.config(text="")
            else:
                temp_c = data["current"]["temp_c"]
                condition = data["current"]["condition"]["text"]
                wind_kph = data["current"]["wind_kph"]
                humidity = data["current"]["humidity"]
                location = f"{data['location']['name']}, {data['location']['country']}"

                label1.config(text=f"{temp_c}°C | {condition}")
                label2.config(
                    text=f"Location: {location}\nWind: {wind_kph} kph\nHumidity: {humidity}%"
                )
        except Exception as e:
            label1.config(text="Error fetching data")
            label2.config(text="")
    else:
        label1.config(text="Enter a city")
        label2.config(text="")

# GUI Setup
canvas = tk.Tk()
canvas.geometry("600x400")
canvas.title("Weather App")
canvas.config(bg="lightblue")

# Fonts
font_small = ("Arial", 15, "bold")
font_large = ("Arial", 35, "bold")

# Input Field
textfield = tk.Entry(canvas, font=font_large, justify="center", fg="gray")
textfield.insert(0, "Enter city name...")  # Prompt text
textfield.pack(pady=20)
textfield.focus()

# Clear placeholder on focus
def on_focus_in(event):
    if textfield.get() == "Enter city name...":
        textfield.delete(0, tk.END)
        textfield.config(fg="black")

# Restore placeholder if empty
def on_focus_out(event):
    if textfield.get() == "":
        textfield.insert(0, "Enter city name...")
        textfield.config(fg="gray")

textfield.bind("<FocusIn>", on_focus_in)
textfield.bind("<FocusOut>", on_focus_out)
textfield.bind("<Return>", lambda event: getWeather())  # Press Enter to search

# Button
btn = tk.Button(canvas, text="Get Weather", font=font_small, command=getWeather)
btn.pack()

# Labels for Output
label1 = tk.Label(canvas, font=font_large, bg="lightblue")
label1.pack(pady=10)

label2 = tk.Label(canvas, font=font_small, bg="lightblue")
label2.pack()

canvas.mainloop()
