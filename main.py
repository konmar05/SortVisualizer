from tkinter import *
from tkinter import ttk
import tkinter.font as tkf
import tkinter as tk
import sys
import time as T
import Colors as Col
import random as Rnd
import Constants as C


def main():

    dataARRAY = [0] * 100
    colorARRAY = [0] * 100
    DELAY = 0

    def getSize(value):
        C.arrayMax = int(value)

    def getLength(value):
        C.arrayLength = int(value)

    def Quit():
        window.quit()
        sys.exit()

    def Start():
        global DELAY
        if speed.get() == "Very Fast":
            DELAY = 0.001
        elif speed.get() == "Fast":
            DELAY = 0.005
        elif speed.get() == "Medium":
            DELAY = 0.01
        elif speed.get() == "Slow":
            DELAY = 0.05
        elif speed.get() == "Very Slow":
            DELAY = 0.1

        if algorithm.get() == "Bubblesort":
            Bubblesort(dataARRAY, colorARRAY)
        elif algorithm.get() == "Countingsort":
            Countingsort(dataARRAY, colorARRAY)
        elif algorithm.get() == "Insertionsort":
            Insertionsort(dataARRAY, colorARRAY)
        elif algorithm.get() == "Selectionsort":
            Selectionsort(dataARRAY, colorARRAY)
        elif algorithm.get() == "Combsort":
            Combsort(dataARRAY, colorARRAY)
        elif algorithm.get() == "Gnomesort":
            Gnomesort(dataARRAY, colorARRAY)
        elif algorithm.get() == "Shakesort":
            Shakesort(dataARRAY, colorARRAY)

    def resARRAY():
        frame.delete("all")

    def resCOLOR():
        global colorARRAY
        for k in range(len(colorARRAY)):
            colorARRAY[k] = Col.CornflowerBlue

    def getFunction():
        GenerateArray(C.arrayMin, C.arrayMax, C.arrayLength)

    def GenerateArray(Min, Max, length):
        resARRAY()
        global dataARRAY
        global colorARRAY
        dataARRAY = [Rnd.randint(Min, Max) for i in range(1, length, 1)]
        colorARRAY = [Col.CornflowerBlue for i in range(1, length, 1)]
        DrawArray(dataARRAY)

    def DrawArray(array):
        for i in range(len(array) - 1):
            DrawData2(array[i], i)

    def DrawData2(value, digit):
        x0 = digit * C.width + C.offset + C.spacing * digit
        y0 = C.height - value
        x1 = C.width * (digit + 1) + C.offset + C.spacing * digit
        y1 = C.height
        frame.create_rectangle(x0, y0, x1, y1, fill=Col.CornflowerBlue, outline=Col.White)
        window.update()

    def DrawData(array, color):
        # i = Stelle
        # array[i] = Wert
        # color[i] = Farbe
        resARRAY()
        for i in range(len(array)):
            x0 = i * C.width + C.offset + C.spacing * i
            y0 = C.height - array[i]
            x1 = C.width * (i + 1) + C.offset + C.spacing * i
            y1 = C.height
            frame.create_rectangle(x0, y0, x1, y1, fill=color[i], outline=Col.White)
        window.update()

    # Bubblesort
    def Bubblesort(data, color):
        size = len(data)
        for i in range(size - 1):
            for j in range(size - i - 1):
                if data[j] > data[j + 1]:
                    resCOLOR()
                    color[j], color[j + 1] = Col.Orange, Col.Purple
                    DrawData(data, color)
                    T.sleep(DELAY)  # DELAY
                    data[j], data[j + 1] = data[j + 1], data[j]
                    color[j], color[j + 1] = Col.Purple, Col.Orange
                    DrawData(data, color)
                    T.sleep(DELAY)  # DELAY
                    resCOLOR()
                    T.sleep(DELAY)
        resCOLOR()
        DrawData(data, color)

    # Countingsort
    def Countingsort(data, color):
        for i in range(len(data)):
            color[i] = Col.Yellow
            DrawData(data, color)
            T.sleep(DELAY)
            resCOLOR()
        n = max(data) + 1
        count = [0] * n
        for item in data:
            count[item] += 1
        k = 0
        for i in range(n):
            for j in range(count[i]):
                data[k] = i
                color[k] = Col.Orange
                DrawData(data, color)
                resCOLOR()
                k += 1
                T.sleep(DELAY)  # DELAY
        resCOLOR()
        DrawData(data, color)

    # Insertionsort
    def Insertionsort(data, color):
        for i in range(len(data)):
            temp = data[i]
            k = i
            color[i] = Col.Orange
            while k > 0 and temp < data[k - 1]:
                data[k] = data[k - 1]
                k -= 1
            data[k] = temp
            DrawData(data, color)
            T.sleep(DELAY)  # DELAY
        resCOLOR()
        DrawData(data, color)

    # Selectionsort
    def Selectionsort(data, color):
        for i in range(len(data)):
            minimum = i
            color[i] = Col.Orange
            for k in range(i + 1, len(data)):
                if data[minimum] > data[k]:
                    color[k] = Col.Purple
                    DrawData(data, color)
                    T.sleep(DELAY)
                    color[k] = Col.CornflowerBlue
                    DrawData(data, color)
                    minimum = k
            data[i], data[minimum] = data[minimum], data[i]
        resCOLOR()
        DrawData(data, color)
        # ____________________________________________________________

    # Combsort
    def Combsort(data, color):
        size = len(data)
        gap = len(data)
        while True:
            if gap > 1:
                gap = int(gap / 1.3)
            for i in range((len(data) - gap)):
                if data[i] > data[i + gap]:
                    color[i], color[i + gap] = Col.Orange, Col.Purple
                    DrawData(data, color)
                    T.sleep(DELAY)  # DELAY
                    data[i], data[i + gap] = data[i + gap], data[i]
                    resCOLOR()
                    color[i], color[i + gap] = Col.Purple, Col.Orange
                    DrawData(data, color)
                    T.sleep(DELAY)  # DELAY
                    resCOLOR()
                    DrawData(data, color)
            if gap <= 1:
                Combsort(data, color)
                break

    # Gnomesort
    def Gnomesort(data, color):
        step = 0
        length = len(data)
        while step <= (length - 2):
            if (data[step] > data[step + 1]) and step == 0:
                resCOLOR()
                color[step], color[step + 1] = Col.Orange, Col.Purple
                DrawData(data, color)
                T.sleep(DELAY)
                data[step], data[step + 1] = data[step + 1], data[step]
                color[step], color[step + 1] = Col.Purple, Col.Orange
                DrawData(data, color)
                T.sleep(DELAY)
                resCOLOR()
                DrawData(data, color)
                step += 1
            elif data[step] <= data[step + 1]:
                resCOLOR()
                color[step] = Col.Yellow
                DrawData(data, color)
                T.sleep(DELAY)
                step += 1
            elif (data[step] > data[step + 1]) and step != 0:
                resCOLOR()
                color[step], color[step + 1] = Col.Orange, Col.Purple
                DrawData(data, color)
                T.sleep(DELAY)
                data[step], data[step + 1] = data[step + 1], data[step]
                color[step], color[step + 1] = Col.Purple, Col.Orange
                DrawData(data, color)
                T.sleep(DELAY)
                resCOLOR()
                DrawData(data, color)
                step -= 1
        resCOLOR()
        DrawData(data, color)

    # Shakesort
    def Shakesort(data, color):
        size = len(data) - 1
        for i in range(size // 2):
            for i in range(size):
                if data[i] > data[i + 1]:
                    resCOLOR()
                    color[i], color[i + 1] = Col.Orange, Col.Purple
                    DrawData(data, color)
                    T.sleep(DELAY)
                    data[i], data[i + 1] = data[i + 1], data[i]
                    color[i], color[i + 1] = Col.Purple, Col.Orange
                    DrawData(data, color)
                    T.sleep(DELAY)
                    resCOLOR()
                    DrawData(data, color)
            for j in range(size, 0, -1):
                if data[j] < data[j - 1]:
                    resCOLOR()
                    color[j], color[j - 1] = Col.Orange, Col.Purple
                    DrawData(data, color)
                    T.sleep(DELAY)
                    data[j], data[j - 1] = data[j - 1], data[j]
                    color[j], color[j - 1] = Col.Purple, Col.Orange
                    DrawData(data, color)
                    T.sleep(DELAY)
                    resCOLOR()
                    DrawData(data, color)

    window = Tk()
    window.wm_title("Sortier-Algorithmen")
    window.maxsize(C.MAX_SIZE_X, C.MAX_SIZE_Y)
    window.config(bg=Col.White)
    myFont1 = tkf.Font(family="Ubuntu", size=14)
    myFont2 = tkf.Font(family="Ubuntu", size=12)

    display = Frame(window, width=C.MAX_SIZE_X, height=C.MAX_SIZE_Y, bg=Col.LightGray)  # Frame für das Fenster
    frame = Canvas(display, width=1390, height=C.height, bg=Col.DimGray)  # Frame für das Array-Balken-Diagramm
    label_Array_Length = Label(display, text="Length", font=myFont1, bg=Col.LightGray, relief=SOLID)
    label_Array_Value = Label(display, text="MAX. Value", font=myFont1, bg=Col.LightGray, relief=SOLID)
    label_Algorithm = Label(display, text="Choose Algorithm", font=myFont1, bg=Col.LightGray)
    label_Speed = Label(display, text="Choose Speed", font=myFont1, bg=Col.LightGray)

    #Buttons
    createArray = Button(display, text="Generate Array", highlightbackground=Col.CornflowerBlue, command=getFunction)
    start = Button(display, text="Start", highlightbackground=Col.ForestGreen, command=Start)
    reset = Button(display, text="Reset", highlightbackground=Col.DimGray, command=resARRAY)
    quit = Button(display, text="Quit", highlightbackground=Col.Firebrick3, command=Quit)
    length = Scale(display,  from_=1, to=100, highlightbackground=Col.LightGray, orient=HORIZONTAL, command=getLength)
    length.set(1)
    size = Scale(display, from_=0, to=450, highlightbackground=Col.LightGray, orient=HORIZONTAL, command=getSize)
    size.set(10)

    m = tk.StringVar()
    speed = ttk.Combobox(display, width=25, textvariable=m)
    speed["values"] = ("Very Fast", "Fast", "Medium", "Slow", "Very Slow")  # Adding dropdown list
    speed.current(0)  # show 'Very Fast' as default

    n = tk.StringVar()
    algorithm = ttk.Combobox(display, width=25, textvariable=n)
    algorithm["values"] = ("Bubblesort", "Countingsort", "Insertionsort", "Selectionsort", "Combsort", "Gnomesort", "Shakesort")  # Adding drop down list
    algorithm.current(0)  # show 'Bubblesort' as default

    # grid
    # row1
    display.grid(column=0, row=0, padx=C.PADX, pady=C.PADY)
    # row2
    quit.grid(column=8, row=0, sticky=E, padx=0, pady=C.PADY)
    label_Array_Length.grid(column=1, row=2, padx=C.PADX)
    length.grid(column=1, row=1, padx=C.PADX)
    size.grid(column=2, row=1, padx=C.PADX)
    label_Array_Value.grid(column=2, row=2,  padx=C.PADX)
    label_Algorithm.grid(column=6, row=1, sticky=E, padx=C.PADX)
    algorithm.grid(column=7, row=1, sticky=W, padx=C.PADX)
    # row3
    createArray.grid(column=0, row=2, sticky=W)
    start.grid(column=4, row=2, sticky=E, pady=C.PADY)
    reset.grid(column=5, row=2, sticky=W, pady=C.PADY)
    label_Speed.grid(column=6, row=2, sticky=E, padx=C.PADX)
    speed.grid(column=7, row=2, sticky=W, padx=C.PADX)
    # row4
    frame.grid(column=0, columnspan=9, row=3, padx=C.PADX, pady=C.PADY)

    # _________________
    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
