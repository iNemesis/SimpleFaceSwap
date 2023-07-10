import uuid
from tkinter import *
from tkinter.filedialog import askopenfilename

from PIL import ImageTk, Image

from lib.faceswapper import FaceSwapper

face_swapper = FaceSwapper('../lib/inswapper_128.onnx')
fenetre = Tk("Simple Face Swapper")
fenetre.geometry("1200x500")

picture_to_swap_filename = ""
picture_to_swap = []

face_to_swap_filename = ""
face_to_swap = []

photo_result = []


def popup_picture_to_swap():
    global picture_to_swap_filename, picture_to_swap
    picture_to_swap_filename = askopenfilename(title="Ouvrir une image", filetypes=[('png files', '.png .jpg .jpeg'), ('all files', '.*')])
    picture_to_swap = ImageTk.PhotoImage(Image.open(picture_to_swap_filename).resize((400, 400), Image.LANCZOS))

    canva_picture_to_swap = Canvas(fenetre, width=400, height=400, bg='white')
    canva_picture_to_swap.grid(row=1, column=1)
    canva_picture_to_swap.create_image(0, 0, anchor=NW, image=picture_to_swap)


def popup_face_to_swap():
    global face_to_swap_filename, face_to_swap, photo_result
    face_to_swap_filename = askopenfilename(title="Ouvrir une image", filetypes=[('png files', '.png .jpg .jpeg'), ('all files', '.*')])
    face_to_swap = ImageTk.PhotoImage(Image.open(face_to_swap_filename).resize((400, 400), Image.LANCZOS))

    canva_face_to_swap = Canvas(fenetre, width=400, height=400, bg='white')
    canva_face_to_swap.grid(row=1, column=2)
    canva_face_to_swap.create_image(0, 0, anchor=NW, image=face_to_swap)

    result = "result/" + str(uuid.uuid4()) + ".jpg"
    face_swapper.swap(face_to_swap_filename, picture_to_swap_filename, result)
    canva_result = Canvas(fenetre, width=400, height=400, bg='white')
    canva_result.grid(row=1, column=3)
    photo_result = ImageTk.PhotoImage(Image.open(result).resize((400, 400), Image.LANCZOS))
    canva_result.create_image(0, 0, anchor=NW, image=photo_result)
    print("done")


Button(text='Choose you picture to swap', command=popup_picture_to_swap).grid(column=1, row=2)
Button(text='Choose the face to put on', command=popup_face_to_swap).grid(column=2, row=2)


fenetre.mainloop()
