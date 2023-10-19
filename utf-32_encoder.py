from tkinter import *

root = Tk()
root.geometry('450x450')
root.title("utf-32 encoder")
root.tk_setPalette(background = 'blue')

encoder_box = Entry(root,background='cyan',fg='black')
shell = Listbox(root,width=50,background= 'green')
encoder_box.pack(side=TOP)
starternumber = 0
changing_value = 1
finalnumber = starternumber + changing_value
shelltext = shell.get(ACTIVE)
log = []
othernull = encoder_box.get()

nullVALUE = [""]
nullVALUE = encoder_box.get()
nullVALUE.encode('utf-32')


def add_1():
    global changing_value,starternumber,finalnumber
    changing_value= changing_value + 1
    finalnumber = starternumber + changing_value

def mainEncoding():
    nullVALUE = encoder_box.get()
    shell.insert(1,str(finalnumber)+ "." + " encoded text: " + str(nullVALUE.encode('utf-32')))
    log.append(str([nullVALUE]))
    log.append(str([nullVALUE.encode('utf-32')]))
    add_1()

def delete():
    shell.delete(ANCHOR)

def write_file():
    global shelltext,log
    try:
        try:
            with open('encoded' + '.txt',mode='wt',encoding='utf-8') as myfile:
                myfile.write((str(log)))
                shell.insert(1,"file created")
            try:
                open('encoded.txt','r')
            except:
                print("file failed to open")
                shell.insert(1,"file couldn't load")
        except:
             print("error with encoding")
    except:
        print("ERROR CREATING FILE")


btn1 = Button(root,text=" encode",bd=2,background='red',
              command=mainEncoding)


btn2 = Button(root,text="delete",bd=2,background='red',
              command=delete)

btn3 = Button(root,text="save results", bd=2,background='red',
              command=write_file)

btn1.pack()
btn1.place(x=200,y=50)
shell.pack(side=BOTTOM)
shell.insert(0,"welcome to shell")
btn3.pack(side=BOTTOM)
btn2.pack(side=BOTTOM)


root.mainloop()