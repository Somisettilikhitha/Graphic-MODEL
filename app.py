import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Graphic Model with Tkinter")

# Create canvas widget
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw some shapes on the canvas
canvas.create_rectangle(50, 50, 150, 150, fill="blue")
canvas.create_oval(200, 50, 300, 150, fill="red")
canvas.create_line(50, 200, 150, 300, fill="green", width=5)

# Run the main event loop
root.mainloop()