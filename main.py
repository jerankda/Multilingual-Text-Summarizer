import openai
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

def generate_summary(api_key, text, output_language, engine="davinci-codex", max_tokens=100, temperature=0.5):
    openai.api_key = api_key
    prompt = f"Summarize the following text as if you are creating a concise index card:\n\n{text}\n\nSummary:"

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )

    summary = response.choices[0].text.strip()

    # Translate the summary if the output language is not English
    if output_language != "en":
        prompt = f"Translate the following English text to {output_language}:\n\n{summary}\n\nTranslation:"
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
        )

        summary = response.choices[0].text.strip()

    return summary

# The rest of the code remains the same

    return summary

def generate_summary_button_click():
    input_text = input_text_box.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "Please enter some text to summarize.")
        return

    output_language = language_var.get()
    summary = generate_summary(api_key, input_text, output_language)
    summary_text_box.delete("1.0", tk.END)
    summary_text_box.insert(tk.END, summary)

api_key = "your api key"

# Create the main window
root = tk.Tk()
root.title("Index Card Summary Generator")

# Create the input text box
input_label = tk.Label(root, text="Enter the text to summarize:")
input_label.pack()
input_text_box = tk.Text(root, wrap=tk.WORD, width=60, height=10)
input_text_box.pack()

# Create the language selection dropdown
language_var = tk.StringVar(root)
language_var.set("en")  # Set the default language to English
language_label = tk.Label(root, text="Select output language:")
language_label.pack()
language_options = ["en", "fr", "es", "de", "it", "nl", "ru", "zh"]
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=language_options)
language_dropdown.pack()

# Create the "Generate Summary" button
generate_summary_button = tk.Button(root, text="Generate Summary", command=generate_summary_button_click)
generate_summary_button.pack()

# Create the summary text box
summary_label = tk.Label(root, text="Index Card Summary:")
summary_label.pack()
summary_text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
summary_text_box.pack()

# Run the main event loop
root.mainloop()
