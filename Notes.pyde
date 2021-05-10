size(1200,600)
noStroke()
col = 25
row = 25
initials = ['H','J','G']

def five():
    global col,row
    background('#0da831')

    savage = loadImage('savage.png')
    
    icons = ['Saw.png','powerDrill.png','hammer.png']
    tools = []
    
    
    for i in icons:
        tools.append(loadImage(i))
        
        
    print(tools)

    noStroke()
    fill('#0e8416')
    ellipse(0,0,800,1000)
    ellipse(width,height,800,1000)
    fill('#129b1b')
    rect(0,0,width,50)
    rect(0,0,50,height)
    image(savage, 100,150 ,450,500)
    rect(0,height-50,width,50)
    rect(0,height-50,width,50)
    rect(width-50,0,50,height)

    
    
    for i in range(1,289):
        if col>25 and col<1150 and row>25 and row<550:
            noFill()
        else:
            fill('#2d681d')
            x = int(random(0,3))
            ellipse(col,row,random(10,50),random(10,50))
    
        col += 50
    
        if i%24 == 0:
            row += 50
            col = 25
        
        textSize(200)
        fill('#EEEEEE')
        text('5',1000,250)

def ten():
    global col,row
    background('#cc7008')
    thile = loadImage('Thile.png')
    
    fill('#995406')
    ellipse(0,0,800,1000)
    ellipse(width,height,800,1000)
    fill('#d38832')
    rect(0,0,width,50)
    rect(0,0,50,height)
    image(thile, 100,150 ,700,500)
    rect(0,height-50,width,50)
    rect(0,height-50,width,50)
    rect(width-50,0,50,height)
    
    for i in range(1,289):
        if col>25 and col<1150 and row>25 and row<550:
            noFill()
        else:
            fill('#684f1d')
            x = int(random(0,3))
            ellipse(col,row,random(10,50),random(10,50))
    
        col += 50
    
        if i%24 == 0:
            row += 50
            col = 25
    
    textSize(200)
    fill('#EEEEEE')
    text('10',875,250)
    
    
def twenty():
    global col,row
    background('#8d269b')
    haley = loadImage('Haley.png')
    
    fill('#590d63')
    ellipse(0,0,800,1000)
    ellipse(width,height,800,1000)
    fill('#ba59c6')
    rect(0,0,width,50)
    rect(0,0,50,height)
    image(haley, 100,150 ,500,500)
    rect(0,height-50,width,50)
    rect(0,height-50,width,50)
    rect(width-50,0,50,height)
    
    for i in range(1,289):
        if col>25 and col<1150 and row>25 and row<550:
            noFill()
        else:
            fill('#51105b')
            x = int(random(0,3))
            ellipse(col,row,random(10,50),random(10,50))
    
        col += 50
    
        if i%24 == 0:
            row += 50
            col = 25
    
    textSize(200)
    fill('#EEEEEE')
    text('20',875,250)
    
def fifty():
    global col,row
    background('#e53081')
    mcKellen = loadImage('McKellen2.png')
    
    fill('#c61d69')
    ellipse(0,0,800,1000)
    ellipse(width,height,800,1000)
    fill('#f94a99')
    rect(0,0,width,50)
    rect(0,0,50,height)
    image(mcKellen, 100,150 ,700,500)
    rect(0,height-50,width,50)
    rect(0,height-50,width,50)
    rect(width-50,0,50,height)
    
    for i in range(1,289):
        if col>25 and col<1150 and row>25 and row<550:
            noFill()
        else:
            fill('#9f0aaf')
            x = int(random(0,3))
            ellipse(col,row,random(10,50),random(10,50))
    
        col += 50
    
        if i%24 == 0:
            row += 50
            col = 25
    
    textSize(200)
    fill('#EEEEEE')
    text('50',875,250)

    
def hundred():
    global col,row
    background('#3ee6f2')
    mcGregor = loadImage('mcGregor.png')
    
    fill('#27c3ce')
    ellipse(0,0,800,1000)
    ellipse(width,height,800,1000)
    fill('#4ee9f4')
    rect(0,0,width,50)
    rect(0,0,50,height)
    image(mcGregor, 100,100 ,700,500)
    rect(0,height-50,width,50)
    rect(0,height-50,width,50)
    rect(width-50,0,50,height)
    
    for i in range(1,289):
        if col>25 and col<1150 and row>25 and row<550:
            noFill()
        else:
            fill('#0b8c9e')
            x = int(random(0,3))
            ellipse(col,row,random(10,50),random(10,50))
    
        col += 50
    
        if i%24 == 0:
            row += 50
            col = 25
    
    textSize(200)
    fill('#EEEEEE')
    text('100',775,250)
    
        
        
notes = [five,ten,twenty,fifty,hundred]
n = int(random(0,5))
notes[n]()
