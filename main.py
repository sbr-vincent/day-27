from tkinter import *


# Button
def button_clicked():
    my_label.config(text=f"{input.get()}")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
# Both of these lines of code can be used to change the text on line 10. Can choose either
my_label["text"] = "New Text"
my_label.config(text="New Text")
# Need the pack to put the label onto the screen
my_label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=20)
print(input.get())
input.grid(column=3, row=2)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)




window.mainloop()