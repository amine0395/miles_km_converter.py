from tkinter import  *
def miles_to_km():
    miles = float(miles_input.get())
    km=miles*1.60934
    miles_label.config(text="Miles")
    km_result.config(text=str(km))
    km_label.config(text="Km")
def km_to_miles():
    km= float(miles_input.get())
    miles=km/1.60934
    miles_label.config(text="Km")
    km_result.config(text=str(miles))
    km_label.config(text="Miles")

window = Tk()
window.minsize(width=300,height=70)


window.title("miles to km converter")
window.config(padx=20,pady=20)

miles_input= Entry(width=20)
miles_input.grid(column=1,row=0)
miles_label = Label(text="X")
miles_label.grid(column=2,row=0)
is_equal_label= Label(text="is equal to")
is_equal_label.grid(column=0,row=1)
km_result= Label(text=0)
km_result.grid(column=1,row=1)
km_label = Label(text="X")
km_label.grid(column=2,row=1)
calculate_button = Button(text="Km to miles",command=km_to_miles)
calculate_button.grid(column=1,row=2)
change_button = Button(text="miles to km",command=miles_to_km)
change_button.grid(column=1,row=4)

window.mainloop()
