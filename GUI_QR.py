import qrcode
from tkinter import *
from tkinter import messagebox, colorchooser
from PIL import Image, ImageTk

def generate_qr():
    msg = url_entry.get()
    file_name=path.get()
    if not file_name:
        messagebox.showwarning("warning","Please enter file name")
        return
    if not msg.strip():
        messagebox.showwarning("Input Error", "Please enter a URL or message.")
        return
    
    # QR  code setup
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2
    )
    qr.add_data(msg)
    qr.make(fit=True)

    # Colors
    fill = fg_color.get()
    back = bg_color.get()
    
    img = qr.make_image(fill_color=fill, back_color=back)
    img.save(file_name)

    # Show QR inside the GUI
    img_display = ImageTk.PhotoImage(Image.open(file_name).resize((200, 200)))
    qr_label.config(image=img_display)
    qr_label.image = img_display

    messagebox.showinfo("Success", "QR code generated successfully and saved as QRCode.png")

def choose_fg():
    color = colorchooser.askcolor(title="Choose foreground color")[1]
    if color:
        fg_color.set(color)

def choose_bg():
    color = colorchooser.askcolor(title="Choose background color")[1]
    if color:
        bg_color.set(color)

# GUI setup
root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="Light Pink")

Label(root, text="Enter URL or Message:", font=("Georgia", 10) ,fg="dark blue").pack(pady=6)
url_entry = Entry(root, width=40, font=("Georgia", 10))
url_entry.pack(pady=6)
Label(root,text="Enter name by which you want to save your QR code(.png)",font=("Georgia",10),bg="dark blue",fg="white").pack(pady=7)
path=Entry(root,width=30,font=("Georgia",10))
path.pack(pady=6)
# Color choices
fg_color = StringVar(value="black")
bg_color = StringVar(value="white")

Button(root, text="Choose Foreground color of QR code", command=choose_fg).pack(pady=6)
Button(root, text="Choose Background color of QR code", command=choose_bg).pack(pady=6)

Button(root, text="Generate QR Code", command=generate_qr, bg="black", fg="white").pack(pady=10)

# QR Preview
qr_label = Label(root)
qr_label.pack(pady=10)

root.mainloop()
