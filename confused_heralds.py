import random
import tkinter as tk
import time

def genQuarters(c):
    colorList = ["white", "yellow", "red", "green", "blue", "black"]
    chargeList = ["bar", "band", "cross"]
    backgrColor = random.choice(colorList)
    hasChief = random.choice([True, False])
    chiefColor = random.choice(list( set(colorList) - set([backgrColor]) ) )
    chargeType = random.choice(chargeList)
    chargeColor = random.choice(list( set(colorList) - set([backgrColor, chiefColor]) ) )

    def quarter1(x1, y1, height, width):
        c.create_rectangle(x1, y1, x1+width, y1+height, outline="", fill=backgrColor) 
        if hasChief:
            c.create_rectangle(x1, y1, x1+width, y1+(2*height/3), outline="", fill=chiefColor) #chief
            if chargeType == "bar":
                pass
                #no part of bar makes it in
            elif chargeType == "band":
                c.create_rectangle(x1+(2*width/3), y1+(2*height/3), x1+width, y1+height, outline="", fill=chargeColor) #band slice
            elif chargeType == "cross":
                c.create_rectangle(x1+(2*width/3), y1+(2*height/3), x1+width, y1+height, outline="", fill=chargeColor) #bar then band, but nothing is drawn in bar so just the same as band
        else:
            if chargeType == "bar":
                c.create_rectangle(x1, y1+(2*height/3), x1+width, y1+height, outline="", fill=chargeColor) #bar slice
            if chargeType == "band":
                c.create_rectangle(x1+(2*width/3), y1, x1+width, y1+height, outline="", fill=chargeColor) #band slice
            if chargeType == "cross":
                c.create_rectangle(x1, y1+(2*height/3), x1+width, y1+height, outline="", fill=chargeColor)
                c.create_rectangle(x1+(2*width/3), y1, x1+width, y1+height, outline="", fill=chargeColor)
        c.pack()
    
    def quarter2(x1, y1, height, width):
        c.create_rectangle(x1, y1, x1+width, y1+height, outline="", fill=backgrColor) 
        if hasChief:
            c.create_rectangle(x1, y1, x1+width, y1+(2*height/3), outline="", fill=chiefColor) #chief
            if chargeType == "bar":
                pass
                #no part of bar makes it in
            elif chargeType == "band":
                c.create_rectangle(x1, y1+(2*height/3), x1+(width/3), y1+height, outline="", fill=chargeColor) #band slice
            elif chargeType == "cross":
                c.create_rectangle(x1, y1+(2*height/3), x1+(width/3), y1+height, outline="", fill=chargeColor) #bar then band, but nothing is drawn in bar so just the same as band
        else:
            if chargeType == "bar":
                c.create_rectangle(x1, y1+(2*height/3), x1+width, y1+height, outline="", fill=chargeColor) #bar slice
            if chargeType == "band":
                c.create_rectangle(x1, y1, x1+width/3, y1+height, outline="", fill=chargeColor) #band slice
            if chargeType == "cross":
                c.create_rectangle(x1, y1+(2*height/3), x1+width, y1+height, outline="", fill=chargeColor)
                c.create_rectangle(x1, y1, x1+width/3, y1+height, outline="", fill=chargeColor)
        c.pack()
    
    def quarter3(x1, y1, height, width):
        c.create_rectangle(x1, y1, x1+width, y1+height, outline="", fill=backgrColor) 
        if hasChief:
            if chargeType == "bar":
                c.create_rectangle(x1, y1+(height/9), x1+width, y1+(5*height/9), outline="", fill=chargeColor) #bar slice
            elif chargeType == "band":
                c.create_rectangle(x1+(2*width/3), y1, x1+width, y1+height, outline="", fill=chargeColor) #band slice
            elif chargeType == "cross":
                c.create_rectangle(x1, y1+(height/9), x1+width, y1+(5*height/9), outline="", fill=chargeColor)
                c.create_rectangle(x1+(2*width/3), y1, x1+width, y1+height, outline="", fill=chargeColor)
        else:
            if chargeType == "bar":
                c.create_rectangle(x1, y1, x1+width, y1+(height/3), outline="", fill=chargeColor) #bar slice
            if chargeType == "band":
                c.create_rectangle(x1+(2*width/3), y1, x1+width, y1+height, outline="", fill=chargeColor) #band slice
            if chargeType == "cross":
                c.create_rectangle(x1, y1, x1+width, y1+(height/3), outline="", fill=chargeColor)
                c.create_rectangle(x1+(2*width/3), y1, x1+width, y1+height, outline="", fill=chargeColor)
            c.pack()
    
    def quarter4(x1, y1, height, width):
        c.create_rectangle(x1, y1, x1+width, y1+height, outline="", fill=backgrColor) 
        if hasChief:
            if chargeType == "bar":
                c.create_rectangle(x1, y1+(height/9), x1+width, y1+(5*height/9), outline="", fill=chargeColor) #bar slice
            elif chargeType == "band":
                c.create_rectangle(x1, y1, x1+(width/3), y1+height, outline="", fill=chargeColor) #band slice
            elif chargeType == "cross":
                c.create_rectangle(x1, y1+(height/9), x1+width, y1+(5*height/9), outline="", fill=chargeColor)
                c.create_rectangle(x1, y1, x1+(width/3), y1+height, outline="", fill=chargeColor)
        else:
            if chargeType == "bar":
                c.create_rectangle(x1, y1, x1+width, y1+(height/3), outline="", fill=chargeColor) #bar slice
            if chargeType == "band":
                c.create_rectangle(x1, y1, x1+(width/3), y1+height, outline="", fill=chargeColor) #band slice
            if chargeType == "cross":
                c.create_rectangle(x1, y1, x1+width, y1+(height/3), outline="", fill=chargeColor)
                c.create_rectangle(x1, y1, x1+(width/3), y1+height, outline="", fill=chargeColor)
            c.pack()
    return [quarter1, quarter2, quarter3, quarter4]

mX = 0
mY = 0


def motionCallbacktoGetMousePosition(e):
    global mX
    global mY
    mX = e.x
    mY = e.y

def moveLeft(e):
    global mX
    global mY
    global locationsDict
    global otherLocationsDict
    aY = int(mY/100) * 100
    aX = int(mX/141) * 141
    try:
        #dfat = draw function & type (of quarter in what flag)
        dfat = locationsDict[(aX, aY)]
        locationsDict[(aX - 141, aY)] = dfat
        otherLocationsDict[(dfat[1], dfat[2])] = (aX - 141, aY)
    except:
        pass
    del locationsDict[(aX, aY)]
    locationsDict[loc][0](loc[0], loc[1], 100, 141)

    
def moveRight(e):
    global mX
    global mY
    global locationsDict
    global otherLocationsDict
    aY = int(mY/100) * 100
    aX = int(mX/141) * 141
    try:
        #dfat = draw function & type (of quarter in what flag)
        dfat = locationsDict[(aX, aY)]
        locationsDict[(aX + 141, aY)] = dfat
        otherLocationsDict[(dfat[1], dfat[2])] = (aX + 141, aY)
    except:
        pass
    del locationsDict[(aX, aY)]
    locationsDict[loc][0](loc[0], loc[1], 100, 141)


def moveDown(e):
    global mX
    global mY
    global locationsDict
    global otherLocationsDict
    aY = int(mY/100) * 100
    aX = int(mX/141) * 141
    try:
        #dfat = draw function & type (of quarter in what flag)
        dfat = locationsDict[(aX, aY)]
        locationsDict[(aX, aY + 100)] = dfat
        otherLocationsDict[(dfat[1], dfat[2])] = (aX, aY + 100)
    except:
        pass
    del locationsDict[(aX, aY)]
    locationsDict[loc][0](loc[0], loc[1], 100, 141)

    
def moveUp(e):
    global mX
    global mY
    global locationsDict
    global otherLocationsDict
    aY = int(mY/100) * 100
    aX = int(mX/141) * 141
    try:
        #dfat = draw function & type (of quarter in what flag)
        dfat = locationsDict[(aX, aY)]
        locationsDict[(aX, aY + 100)] = dfat
        otherLocationsDict[(dfat[1], dfat[2])] = (aX, aY - 100)
    except:
        pass
    del locationsDict[(aX, aY)]
    locationsDict[loc][0](loc[0], loc[1], 100, 141)


root = tk.Tk()
root.title("Confused Heralds")
c = tk.Canvas(root, width=1950, height=1000-10)
drawFunctionsList = [[], [], [], []]
for i in range(4):
    gdf = genQuarters(c)
    drawFunctionsList[0].append((gdf[0], i, 0))
    drawFunctionsList[1].append((gdf[1], i, 1))
    drawFunctionsList[2].append((gdf[2], i, 2))
    drawFunctionsList[3].append((gdf[3], i, 3))
for L in drawFunctionsList:
    random.shuffle(L)

locationsDict = {}
otherLocationsDict = {}

for i in range(4):
    if i < 4:
        drawFunctionsList[0][i][0](252 * (i*2), 400, 100, 141)
        drawFunctionsList[1][i][0](252 * (i*2) + 141, 400, 100, 141)
        drawFunctionsList[2][i][0](252 * (i*2), 500, 100, 141)
        drawFunctionsList[3][i][0](252 * (i*2) + 141, 500, 100, 141)
        
        locationsDict[(252 * (i*2), 400)] = drawFunctionsList[0][i]
        otherLocationsDict[(drawFunctionsList[0][i][1], drawFunctionsList[0][i][2])] = (252 * (i*2), 400)
        
        locationsDict[(252 * (i*2) + 141, 400)] = drawFunctionsList[1][i]
        otherLocationsDict[(drawFunctionsList[1][i][1], drawFunctionsList[1][i][2])] = (252 * (i*2) + 141, 400)

        locationsDict[(252 * (i*2), 500)] = drawFunctionsList[2][i]
        otherLocationsDict[(drawFunctionsList[2][i][1], drawFunctionsList[0][i][2])] = (252 * (i*2), 500)

        locationsDict[(252 * (i*2) + 141, 500)] = drawFunctionsList[3][i]
        otherLocationsDict[(drawFunctionsList[3][i][1], drawFunctionsList[3][i][2])] = (252 * (i*2) + 141, 500)



c.bind('<Motion>', motionCallbacktoGetMousePosition)
root.bind('<Left>', moveLeft)
root.bind('<Right>', moveRight)
root.bind('<Down>', moveDown)
root.bind('<Up>', moveUp)
root.mainloop()


##testflagfuncs[0](0, 100, 100, 141)
##testflagfuncs[1](141, 100, 100, 141)
##testflagfuncs[2](0, 200, 100, 141)
##testflagfuncs[3](141, 200, 100, 141)


