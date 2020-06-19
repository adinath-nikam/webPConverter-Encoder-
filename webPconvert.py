# Importing Libraries
import tkinter
import tkinter as tk
import tkinter as ttk
import tkinter.ttk as TTK
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import subprocess


# Global Variables

# Colors
COLOR_WHITE = "#FFFFFF"

global save_loc, Imgfilename
save_loc = ""
Imgfilename = ""

# FONT SIZE
FONT_SIZE = 20

# FONT STYLES
FONT_STYLE = ('Helvetica', FONT_SIZE, 'bold')
FONT_STYLE_1 = ('monospace', FONT_SIZE, 'bold')

# Functions


# Exit (Quit)
def quit():
    main_window.quit
    main_window.destroy
    exit()
    
def about():
    about_win = tk.Tk()
    about_win.title(".webP Encoder .v1 - About")

    about_main_frame = tkinter.LabelFrame(about_win, text="About")
    about_main_frame.grid(column=0, row=0, padx=5, pady=5)

    about_label = tkinter.Label(about_main_frame, bg=COLOR_WHITE, font=FONT_STYLE, text=".webP Encoder .v1")
    about_label.grid(column=0, row=0, padx=0, pady=0)

    about_text_label = tkinter.Label(about_main_frame, text=".webP Encoder .v1 - Convert any Image format to .webP \n\n .webP is Web Page Image format (Extension) for High resoultion images to easily get rendered and available at any web page accross devices\n\n .webP Encoder encodes any image format (.jpg, .jpeg, .png) and converts it into (.webP) format for using it for web development,\n beacause .webP format gives optimization for rendering webpages accross device\n\nCompiled on: 10-06-2020\n Developed by Hyper-Programmer ")
    about_text_label.grid(column=0, row=1, padx=0, pady=0)

    about_win.resizable(False, False)
    about_win.mainloop

# Save Location
def save_file_loc():
    global save_loc
    save_loc = filedialog.asksaveasfilename(initialdir="/", title="Save File..", defaultextension=".webp")
    file_out_name_label.configure(text=save_loc)

# Select file
def select_file():
    global Imgfilename
    Imgfilename = filedialog.askopenfilename(initialdir="/", title="Select File")
    file_name_label.configure(text=Imgfilename)


def convert():
    # save_location = filedialog.asksaveasfilename(initialdir="/", title="Save File..",)
    # quality_factor = qf_scale.get()
    # trans_quality = tcq_scale.get()
    # compression_speed = compression_speed_scale.get()
    # segments = segments_combobox.get()
    # strength = strength_spinbox.get()
    # sharpness = sharpness_spinbox.get()
    # strong = strongVar.get()
    # mem_usage = red_memVar.get()
    # lossless_compression = loss_compVar.get()

    # console_log = subprocess.run([
    #     "cwebp.exe ",
    #     "-q",
    #     quality_factor,
    #     # "-alpha_q",
    #     # trans_quality,
    #     # "-m",
    #     # compression_speed,
    #     # "-segments",
    #     # segments,
    #     # "-f",
    #     # strength,
    #     # "-sharpness",
    #     # sharpness,
    #     # "-strong",
    #     # strong,
    #     # "-low_memory",
    #     # mem_usage,
    #     # "-lossless",
    #     # lossless_compression,
    #     Imgfilename,
    #     "-o",
    #     "sample.webp"
    # ], stdout=subprocess.PIPE)

    if Imgfilename == "":
        msg.showerror(title="File not Selected", message="Select Image File (.jpg, .*jpeg, .png)")

    elif save_loc == "":
        msg.showerror(title="Save Location not Selected", message="Select save location to save file.")

    else:
        console_log = subprocess.run([
            "cwebp.exe ",
            "-q",
            str(qf_scale.get()),
            "-alpha_q",
            str(tcq_scale.get()),
            "-m",
            str(compression_speed_scale.get()),
            "-segments",
            str(segments_combobox.get()),
            "-f",
            str(strength_spinbox.get()),
            "-sharpness",
            str(sharpness_spinbox.get()),
            "-strong",
            str(strongVar.get()),
            "-low_memory",
            str(red_memVar.get()),
            "-lossless",
            str(loss_compVar.get()),
            Imgfilename,
            "-o",
            save_loc
        ], stdout=subprocess.PIPE)

        msg.showinfo(title="Successful", message="Sucessfully converted to '.webp' format.")



# Main
def Main():

    # Frames

    main_frame1 = tkinter.LabelFrame(main_window, text="Menu")
    main_frame1.grid(column=0, row=0, padx=10, pady=10)

    main_frame2 = tkinter.LabelFrame(main_frame1, bg=COLOR_WHITE)
    main_frame2.grid(column=0, row=0, padx=10, pady=10)

    main_frame3 = tkinter.LabelFrame(main_frame1, text="Select Image")
    main_frame3.grid(column=0, row=1, padx=10, pady=10)

    save_loc_frame = tkinter.LabelFrame(main_frame1, text="Save Location")
    save_loc_frame.grid(column=0, row=2, padx=10, pady=10)

    main_frame4 = tkinter.LabelFrame(main_frame1, text="Image Properties")
    main_frame4.grid(column=0, row=3, padx=10, pady=10)

    convt_btn_frame = tkinter.LabelFrame(main_frame1, text="Convert")
    convt_btn_frame.grid(column=0, row=4, padx=10, pady=10)

    # Image Preview Frame
    global img_preview_frame
    img_preview_frame = tkinter.Frame(main_frame2)
    img_preview_frame.grid(column=0, row=0)

    # Image Preview
    canvas = Canvas(img_preview_frame, width=700, height=200)
    canvas.grid(column=0, row=0, padx=10, pady=10)
    img = ImageTk.PhotoImage(Image.open("webPConverterLogo.png"))
    canvas.create_image(20,20, anchor=NW, image=img)

    # # File Input Frame
    # image_select_frame = tkinter.LabelFrame(main_frame3)
    # image_select_frame.grid(column=0, row=0, padx=5, pady=5)

    # Quality Factor
    quality_factor_frame = tkinter.LabelFrame(main_frame4, text="Quality Factor (Default = 75)")
    quality_factor_frame.grid(column=0, row=0, padx=5, pady=5)

    # Transperency Compression Quality
    transperency_quality_frame = tkinter.LabelFrame(main_frame4, text="Transperency Compression Qulaity (Default = 100)")
    transperency_quality_frame.grid(column=1, row=0, padx=5, pady=5)

    # Compression Speed
    compression_speed_frame = tkinter.LabelFrame(main_frame4, text="Compession Speed (Default = 4)")
    compression_speed_frame.grid(column=2, row=0, padx=5, pady=5)

    # Segements
    segments_frame = tkinter.LabelFrame(main_frame4, text="Segements (Default = 4)")
    segments_frame.grid(column=0, row=1, padx=5, pady=5)

    # Strength Frame
    strength_frame = tkinter.LabelFrame(main_frame4, text="Strentgh (Default = 60)")
    strength_frame.grid(column=1, row=1, padx=5, pady=5)

    # Strength Frame
    shrapness_frame = tkinter.LabelFrame(main_frame4, text="Sharpness (Default = 0)")
    shrapness_frame.grid(column=2, row=1, padx=5, pady=5)

    # Row 3 -Checkbuttons
    # strong_frame = tkinter.LabelFrame(main_frame4, text="Strong (Default)")
    # strong_frame.grid(column=0, row=2, padx=5, pady=5)

    # # Reduce Memory Frame
    # reduce_memory_frame = tkinter.LabelFrame(main_frame4, text="Memory (Default)")
    # reduce_memory_frame.grid(column=1, row=2, padx=5, pady=5)

    # # Lossless Frame
    # lossless_frame = tkinter.LabelFrame(main_frame4, text="Lossless (Default)")
    # lossless_frame.grid(column=2, row=2, padx=5, pady=5)


    # s = Scale(main_frame1, from_=0, to= 100, orient=HORIZONTAL)
    # s.grid(column=0, row=0)



    # Widgets

    # Menu
    # Menu Bar

    menu_bar = Menu(main_window)
    main_window.config(menu = menu_bar)

    # Menu Items

    menu_file = Menu(menu_bar, tearoff=0)
    menu_file.add_command(label="Exit", command=quit)
    menu_bar.add_cascade(label="File", menu=menu_file)

    menu_about = Menu(menu_bar, tearoff=0)
    menu_about.add_command(label="About", command=about)
    menu_bar.add_cascade(label="Help", menu=menu_about)


    # File input
    global file_name_label
    file_name_label = tkinter.Label(main_frame3, bg=COLOR_WHITE, text="No Image Selected..", width=55)
    file_name_label.grid(column=0, row=0, padx=5, pady=5)

    global file_select_btn
    file_select_btn = tkinter.Button(main_frame3, text=". . .", width=10, height=1, command=select_file)
    file_select_btn.grid(column=1, row=0, padx=5, pady=5)

    # File input
    global file_out_name_label
    file_out_name_label = tkinter.Label(save_loc_frame, bg=COLOR_WHITE, text="Select Save Location..", width=55)
    file_out_name_label.grid(column=0, row=0, padx=5, pady=5)

    global file_save_btn
    file_save_btn = tkinter.Button(save_loc_frame, text="Save Location", width=10, height=1, command=save_file_loc)
    file_save_btn.grid(column=1, row=0, padx=5, pady=5)

    # Quality Facort Scale

    global qf_scale
    qf_scale = Scale(quality_factor_frame, from_=0, to=100, orient=HORIZONTAL)
    qf_scale.grid(column=0, row=0, padx=5, pady=5)
    
    global tcq_scale
    tcq_scale = Scale(transperency_quality_frame, from_=0, to=100, orient=HORIZONTAL)
    tcq_scale.grid(column=0, row=0, padx=5, pady=5)

    global compression_speed_scale
    compression_speed_scale = Scale(compression_speed_frame, from_=0, to=6, orient=HORIZONTAL)
    compression_speed_scale.grid(column=0, row=0, padx=5, pady=5)

    # Segments Combobox
    global segments_combobox
    segments_combobox = TTK.Combobox(segments_frame, width=25)
    segments_combobox.grid(column=0, row=0, padx=5, pady=5)
    segments_combobox['values'] = (1,2,3,4)
    segments_combobox.current(3)

    # Strength Spinbox
    global strength_spinbox
    strength_spinbox = tkinter.Spinbox(strength_frame, width=25, from_=0, to=100)
    strength_spinbox.grid(column=0, row=0, padx=5, pady=5)

    # Sharpness Spinbox
    global sharpness_spinbox
    sharpness_spinbox = tkinter.Spinbox(shrapness_frame, width=25, from_=0, to=7)
    sharpness_spinbox.grid(column=0, row=0, padx=5, pady=5)

    # Strong Checkbox
    global strong_checkbox, strongVar
    strongVar = tk.StringVar()
    strong_checkbox = tkinter.Checkbutton(main_frame4, text="Use Strong Filter", variable=strongVar)
    strong_checkbox.select()
    strong_checkbox.grid(column=0, row=2, padx=5, pady=5)

    # Reduce Memory Checkbox
    global reduce_memory_usage_checkbox, red_memVar
    red_memVar = tk.IntVar()
    reduce_memory_usage_checkbox = tkinter.Checkbutton(main_frame4, text="Reduce Memory Usage", variable=red_memVar)
    reduce_memory_usage_checkbox.deselect()
    reduce_memory_usage_checkbox.grid(column=1, row=2, padx=5, pady=5)

    # Lossless Checkbox
    global lossless_compression_checkbox, loss_compVar
    loss_compVar = tk.IntVar()
    lossless_compression_checkbox = tkinter.Checkbutton(main_frame4, text="Use Lossless Compression", variable=loss_compVar)
    lossless_compression_checkbox.deselect()
    lossless_compression_checkbox.grid(column=2, row=2, padx=5, pady=5)

    # Conver Button
    convert_btn = tkinter.Button(convt_btn_frame, text="Convert to webP", width=55, height=2, bg=COLOR_WHITE, command=convert)
    convert_btn.grid(column=0, row=0, padx=5, pady=5)

    main_window.resizable(False, False)
    main_window.mainloop()

if __name__ == "__main__":
    global main_window
    main_window = tk.Tk()
    main_window.title("webP-Encoding")
    Main()