import tkinter as tk
from tkinter import ttk
from py4j.java_gateway import JavaGateway
import json

language_data = [
    {"language_name": "Arabic", "language": "ar"},
    {"language_name": "Bengali", "language": "bn"},
    {"language_name": "Danish", "language": "da"},
    {"language_name": "Dutch", "language": "nl"},
    {"language_name": "English", "language": "en"},
    {"language_name": "French", "language": "fr"},
    {"language_name": "German", "language": "de"},
    {"language_name": "Greek", "language": "el"},
    {"language_name": "Gujarati", "language": "gu"},
    {"language_name": "Hindi", "language": "hi"},
    {"language_name": "Indonesian", "language": "id"},
    {"language_name": "Italian", "language": "it"},
    {"language_name": "Japanese", "language": "ja"},
    {"language_name": "Korean", "language": "ko"},
    {"language_name": "Malayalam", "language": "ml"},
    {"language_name": "Polish", "language": "pl"},
    {"language_name": "Punjabi", "language": "pa"},
    {"language_name": "Russian", "language": "ru"},
    {"language_name": "Spanish", "language": "es"},
    {"language_name": "Tamil", "language": "ta"},
    {"language_name": "Telugu", "language": "te"},
    {"language_name": "Thai", "language": "th"},
    {"language_name": "Turkish", "language": "tr"},
]

language_dict = {item['language_name']: item['language'] for item in language_data}

def translate_text():
    gateway = JavaGateway()
    translator = gateway.entry_point

    text = text_entry.get()
    target_language = language_dict[target_language_combo.get()]
    source_language = language_dict[source_language_combo.get()] if source_language_combo.get() else None

    raw_translated_text = translator.translateText(text, target_language, source_language)
    
    # Parse the raw JSON response
    parsed_response = json.loads(raw_translated_text)
    translated_text = parsed_response["translations"][0]["translation"]

    result_label.config(text=translated_text)

# Create the main window
root = tk.Tk()
root.title("Text Translator")

# Create and place the labels and entry widgets
ttk.Label(root, text="Text to Translate:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
text_entry = ttk.Entry(root, width=40)
text_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(root, text="Target Language:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
target_language_combo = ttk.Combobox(root, values=list(language_dict.keys()))
target_language_combo.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(root, text="Source Language:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
source_language_combo = ttk.Combobox(root, values=[''] + list(language_dict.keys())) # empty string as first option for optional
source_language_combo.grid(row=2, column=1, padx=5, pady=5)

# Create and place the translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place the result label
result_label = ttk.Label(root, text="", wraplength=300)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the app
root.mainloop()
