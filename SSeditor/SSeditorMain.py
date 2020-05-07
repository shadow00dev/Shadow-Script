from tkinter import Tk , scrolledtext , Menu , filedialog , END , messagebox , simpledialog, font
import os
# root for main window
root = Tk(className=' SSEditor')
root.geometry('800x600')
root.iconbitmap('SSEditor.ico')
screenWidth1 = root.winfo_screenwidth()
screenheight1 = root.winfo_screenheight
textArea = scrolledtext.ScrolledText(root,width=screenWidth1,height=45, bg = "grey", fg = "white")
textArea.tag_configure("#00008b", foreground="#00008b")



# syntax color
def color():
 textdata1 = textArea.get('1.0', END+'-1c')
 print(textdata1)
 if 's.show-' in textdata1:
  word = 's.show-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")
 if 's.var-' in textdata1:
  word = 's.var-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")
 if 's.if-' in textdata1:
  word = 's.if-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.elif-' in textdata1:
  word = 's.elif-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.else:' in textdata1:
  word = 's.else:'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.func-' in textdata1:
  word = 's.func-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.r.func-' in textdata1:
  word = 's.r.func-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.class-' in textdata1:
  word = 's.class-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.while-' in textdata1:
  word = 's.while-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.plib-' in textdata1:
  word = 's.plib-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.r.plib-' in textdata1:
  word = 's.r.plib-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")
 if 's.for-' in textdata1:
  word = 's.for-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

 if 's.skip-' in textdata1:
  word = 's.skip-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")
 if 's.return-' in textdata1:
  word = 's.return-'

  index = "1.0"
  while index:
        start = textArea.search(word, index, "end")
        end = textArea.index(f"{start} + {len(word)} c")

        textArea.tag_add("#00008b", start, end)

        index = textArea.search(word, end, "end")

# functions

# functions
def newFile():
    if len(textArea.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno('Save?', 'Do you want to save?'):
            saveFile()
            textArea.delete('1.0', END)
        else:
         textArea.delete('1.0', END)

    root.title(' SSEditor')
def openFile():
    file = filedialog.askopenfile(parent=root, title='Open File')

    root.title(os.path.basename(file.name) + ' - SSEditor')

    if file != None:
        textArea.delete('1.0', END)
        content = file.read()
        textArea.insert('1.0', content)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Shadow Script', '*.ss'), ('All Files', '*.*')))

    if file != None:
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        root.title(os.path.basename(file.name) + ' - SSEditor')
def exit():
    if messagebox.askyesno('Quit', 'Are you 100% sure you want to quit?'):
        root.destroy()

    if textdata.count(findString) > 0:
     label = messagebox.showinfo('Results ', ' i have found a '+ findString+ ' and there is this meny: ' + str(occurances))
    else:
        label = messagebox.showinfo('Results', ' cant find:'+ findString)

# window options

menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
Menu.add_cascade(menu, label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

Menu.add_cascade(menu, label="syntax check", command=color)

textArea.pack()

# Keep window open
root.mainloop()
