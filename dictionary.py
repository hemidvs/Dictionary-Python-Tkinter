import json
from difflib import get_close_matches
from tkinter import *
from tkinter import ttk

# Import data
data = json.load(open("data.json"))

# Constants
window_color = "#12182B"
means_text_color = "#53CCEC"
hint_green_text_color = "#00FF5F"
hint_red_text_color = "#FF224E"

# Window and frames
win = Tk()
win.title("Dictionary")
win.geometry("750x400")
win.config(bg=window_color)
win.resizable(False, False)

frame1 = ttk.Frame(win, style="Frame.TFrame")
frame1.place(relx=0.34, rely=0.08, relwidth=0.6, relheight=0.4, anchor="n")

frame2 = ttk.Frame(win, style="Frame.TFrame")
frame2.place(relx=0.49, rely=0.45, relwidth=0.85, relheight=0.5, anchor="n")

# Styles
hemidvs_style = ttk.Style()
hemidvs_style.configure("Hemidvs.TLabel",  font=("Segoe UI", 8), foreground="white", background=window_color)

frames_style = ttk.Style()
frames_style.configure("Frame.TFrame", background=window_color)

title_label_style = ttk.Style()
title_label_style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground="white", background=window_color)

hint_label_style = ttk.Style()
hint_label_style.configure("Hint.TLabel", font=("Segoe UI", 10), foreground=hint_green_text_color, background=window_color)

means_label_style = ttk.Style()
means_label_style.configure("Means.TLabel", font=("Segoe UI", 10), foreground=means_text_color, background=window_color)

# Widgets
hemidvs_label = ttk.Label(win, style="Hemidvs.TLabel", text="© made by hemidvs")
hemidvs_label.place(anchor="n", relx=0.9, rely=0.9)

title_label = ttk.Label(frame1, text="Type word to get mean...", style="Title.TLabel")
title_label.place(relx=0.44, rely=0.08, relwidth=0.80, relheight=0.3, anchor="n")

word_entry = ttk.Entry(frame1, font=("Segoe UI", 13))
word_entry.place(relx=0.32, rely=0.55, relwidth=0.55, relheight=0.2, anchor="n")


# Method to search word
def search_word():
    word = (word_entry.get()).lower()

    if word != "":

        if word in data:
            hint_label.config(text="✓ Done!")
            hint_label_style.configure("Hint.TLabel", foreground=hint_green_text_color)
            means = data[word]
            # if word have more means
            if type(means) == list:
                i = 0
                str_mean = ""
                while i < len(means):
                    str_mean = str_mean + f"\n>> {means[i]}"
                    i = i + 1
                means_label.config(text=f"{str_mean}")
            else:
                means_label.config(text=">> %s" % means)

        elif word.title() in data:
            hint_label.config(text="✓ Done!")
            hint_label_style.configure("Hint.TLabel", foreground=hint_green_text_color)
            means = data[word.title()]
            # if word have more means
            if type(means) == list:
                i = 0
                str_mean = ""
                while i < len(means):
                    str_mean = str_mean + f"\n>> {means[i]}"
                    i = i + 1
                means_label.config(text=f"{str_mean}")
            else:
                means_label.config(text=">> %s" % means)

        elif word.upper() in data:
            hint_label.config(text="✓ Done!")
            hint_label_style.configure("Hint.TLabel", foreground=hint_green_text_color)
            means = data[word.upper()]
            # if word have more means
            if type(means) == list:
                i = 0
                str_mean = ""
                while i < len(means):
                    str_mean = str_mean + f"\n>> {means[i]}"
                    i = i + 1
                means_label.config(text=f"{str_mean}")
            else:
                means_label.config(text=">> %s" % means)
        else:
            hint_label.config(text="✗ We can't find your word, Please type correct.")
            hint_label_style.configure("Hint.TLabel", foreground=hint_red_text_color)
            means_label.config(text="")
    else:
        hint_label.config(text="✗ Oops.. You can't search noting!")
        hint_label_style.configure("Hint.TLabel", foreground=hint_red_text_color)


# other Widgets
search_button = ttk.Button(frame1, text="Search", command=search_word)
search_button.place(relx=0.72, rely=0.55, relwidth=0.18, relheight=0.2, anchor="n")

hint_label = ttk.Label(frame1, text="", style="Hint.TLabel")
hint_label.place(relx=0.05, rely=0.80, anchor="nw")

means_label = ttk.Label(frame2, style="Means.TLabel", wraplength=630)
means_label.place(anchor="nw")

# def translate(word):
#     word = word.lower()
#     closes = get_close_matches(word, data.keys())
#
#     if word in data:
#         return data[word]
#     elif word.title() in data:
#         return data[word.title()]
#     elif word.upper() in data:
#         return data[word.upper()]
#
#     elif len(closes) > 0:
#         print("Did you mean %s?" % closes[0])
#         decide = input("Press y for yes or n for no - ")
#         if decide == "y":
#             return data[closes[0]]
#         else:
#             print("Did you mean %s?" % closes[1])
#             decide2 = input("Press y for yes or n for no - ")
#             if decide2 == "y":
#                 return data[closes[1]]
#             else:
#                 return "Word isn't exits in dictionary"
#
#     else:
#         return "Word isn't exits in dictionary"
#
#
# word = input("Enter the word you want to search: ")
# output = translate(word)
# if type(output) == list:
#     for i in output:
#         print(i)
# else:
#     print(output)


win.mainloop()
