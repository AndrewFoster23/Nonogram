import pygame, random

pygame.init()
pygame.mixer.init()

size = width, height = 800, 800

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Nonograms")

font = pygame.font.SysFont("Arial", 120, bold = True)
numFont = pygame.font.SysFont("Arial", 30, bold = True)

def drawText(text, x, y, color, fnt):
    img = fnt.render(text, True, color)
    screen.blit(img, (x, y))
    
def drawBlocks():
    global strt
    global gap
    pygame.draw.rect(screen, lightBlue, pygame.Rect(strt - gap, next0 + strt - gap, next0*15+gap, next0*15+gap))
    
    for i in range(len(board)):
        pygame.draw.rect(screen, colors[i], board[i])
    for i in range(len(numBoard)):
        pygame.draw.rect(screen, gray, numBoard[i])
        
def drawType():
    global squareType;
    if squareType == b:
        pygame.draw.rect(screen, b, selection)
    else:
        pygame.draw.rect(screen, r, selection)
        
def genNumsHorizontal():
    global puzzle
    for i in range(10):
        #print("i:", i)
        prev = g
        index = 0
        row = i*10
        numList = [0, 0, 0, 0, 0]
        for j in range(10):
            if puzzle[row+j] == b:
                numList[index] = numList[index] + 1
            elif prev == b:
                index += 1
            prev = puzzle[row+j]
        drawNumbersHorizontal(numList, i)
        
        
def drawNumbersHorizontal(numList, indexH):
   global colors
   global strt
   global next0
   numGap = gap*2
   xIndex = strt+next0*4 + numGap
   yIndex = strt+next0*(6 + indexH)
   for i in range(5):
       if numList[4-i] != 0:
           if numList[4-i] == 10:
               xIndex = strt+next0*4 + gap*0.7
               drawText("{}".format(numList[4-i]), xIndex, yIndex, b, numFont)
               xIndex = strt+next0*4 + numGap
           else:
               drawText("{}".format(numList[4-i]), xIndex, yIndex, b, numFont)
           xIndex -= next0
   
   
def genNumsVertical():
    global puzzle
    for i in range(10):
        prev = g
        index = 0
        numList = [0, 0, 0, 0, 0]
        for j in range(10):
            colNum = j*10
            if puzzle[colNum + i] == b:
                numList[index] = numList[index] + 1
            elif prev == b:
                index += 1
            prev = puzzle[colNum + i]
        drawNumbersVertical(numList, i)
        
def drawNumbersVertical(numList, indexV):
   global colors
   global strt
   global next0
   numGap = gap*2
   xIndex = strt+next0*(5 + indexV) + numGap
   yIndex = strt+next0*5
   for i in range(5):
       if numList[4-i] != 0:
           if numList[4-i] == 10:
               xIndex = strt+next0*(5 + indexV) + gap*0.7
               drawText("{}".format(numList[4-i]), xIndex, yIndex, b, numFont)
               xIndex = strt+next0*(5 + indexV) + numGap
           else:
               drawText("{}".format(numList[4-i]), xIndex, yIndex, b, numFont)
           yIndex -= next0
           
def generatePuzzle():
    global difficulty
    num = 0
    for i in range(100):
        num = random.randint(1, 4)
        if num <= difficulty:
            puzzle[i] = b
        else:
            puzzle[i] = w
            
def customGenPuzzle(maxBound, midNum):
    num = 0
    for i in range(100):
        num = random.randint(1, maxBound)
        if num <= midNum:
            puzzle[i] = b
        else:
            puzzle[i] = w
            
def choosePreset():
    global collection
    global puzzle
    rand = random.randint(0, len(collection) - 1)
    puzzle = collection[rand]
    
def checkWin():
    for i in range(len(board)):
        if puzzle[i] == b and colors[i] != b or colors[i] == b and puzzle[i] != b:
            return False
    return True

b = (0, 0, 0)
g = (0, 255, 0)
yellow = (255, 255, 0)
w = (255, 255, 255)
gray = (100, 100, 100)
r = (255, 0, 0)
gray = (110, 110, 110)
lightBlue = (55, 68, 212)

strt = 100 #150
gap = 5
wid = 35
next0 = gap + wid
selection = pygame.Rect(strt, next0 + strt, wid*5 + gap*4, wid*5 + gap*4)
squareType = b      #this or r

board = [pygame.Rect(strt+next0*5, strt+next0*6, wid, wid), pygame.Rect(strt+next0*6, strt+next0*6, wid, wid), pygame.Rect(strt+next0*7, strt+next0*6, wid, wid), pygame.Rect(strt+next0*8, strt+next0*6, wid, wid), pygame.Rect(strt+next0*9, strt+next0*6, wid, wid), pygame.Rect(strt+next0*10, strt+next0*6, wid, wid), pygame.Rect(strt+next0*11, strt+next0*6, wid, wid), pygame.Rect(strt+next0*12, strt+next0*6, wid, wid), pygame.Rect(strt+next0*13, strt+next0*6, wid, wid), pygame.Rect(strt+next0*14, strt+next0*6, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*7, wid, wid), pygame.Rect(strt+next0*6, strt+next0*7, wid, wid), pygame.Rect(strt+next0*7, strt+next0*7, wid, wid), pygame.Rect(strt+next0*8, strt+next0*7, wid, wid), pygame.Rect(strt+next0*9, strt+next0*7, wid, wid), pygame.Rect(strt+next0*10, strt+next0*7, wid, wid), pygame.Rect(strt+next0*11, strt+next0*7, wid, wid), pygame.Rect(strt+next0*12, strt+next0*7, wid, wid), pygame.Rect(strt+next0*13, strt+next0*7, wid, wid), pygame.Rect(strt+next0*14, strt+next0*7, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*8, wid, wid), pygame.Rect(strt+next0*6, strt+next0*8, wid, wid), pygame.Rect(strt+next0*7, strt+next0*8, wid, wid), pygame.Rect(strt+next0*8, strt+next0*8, wid, wid), pygame.Rect(strt+next0*9, strt+next0*8, wid, wid), pygame.Rect(strt+next0*10, strt+next0*8, wid, wid), pygame.Rect(strt+next0*11, strt+next0*8, wid, wid), pygame.Rect(strt+next0*12, strt+next0*8, wid, wid), pygame.Rect(strt+next0*13, strt+next0*8, wid, wid), pygame.Rect(strt+next0*14, strt+next0*8, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*9, wid, wid), pygame.Rect(strt+next0*6, strt+next0*9, wid, wid), pygame.Rect(strt+next0*7, strt+next0*9, wid, wid), pygame.Rect(strt+next0*8, strt+next0*9, wid, wid), pygame.Rect(strt+next0*9, strt+next0*9, wid, wid), pygame.Rect(strt+next0*10, strt+next0*9, wid, wid), pygame.Rect(strt+next0*11, strt+next0*9, wid, wid), pygame.Rect(strt+next0*12, strt+next0*9, wid, wid), pygame.Rect(strt+next0*13, strt+next0*9, wid, wid), pygame.Rect(strt+next0*14, strt+next0*9, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*10, wid, wid), pygame.Rect(strt+next0*6, strt+next0*10, wid, wid), pygame.Rect(strt+next0*7, strt+next0*10, wid, wid), pygame.Rect(strt+next0*8, strt+next0*10, wid, wid), pygame.Rect(strt+next0*9, strt+next0*10, wid, wid), pygame.Rect(strt+next0*10, strt+next0*10, wid, wid), pygame.Rect(strt+next0*11, strt+next0*10, wid, wid), pygame.Rect(strt+next0*12, strt+next0*10, wid, wid), pygame.Rect(strt+next0*13, strt+next0*10, wid, wid), pygame.Rect(strt+next0*14, strt+next0*10, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*11, wid, wid), pygame.Rect(strt+next0*6, strt+next0*11, wid, wid), pygame.Rect(strt+next0*7, strt+next0*11, wid, wid), pygame.Rect(strt+next0*8, strt+next0*11, wid, wid), pygame.Rect(strt+next0*9, strt+next0*11, wid, wid), pygame.Rect(strt+next0*10, strt+next0*11, wid, wid), pygame.Rect(strt+next0*11, strt+next0*11, wid, wid), pygame.Rect(strt+next0*12, strt+next0*11, wid, wid), pygame.Rect(strt+next0*13, strt+next0*11, wid, wid), pygame.Rect(strt+next0*14, strt+next0*11, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*12, wid, wid), pygame.Rect(strt+next0*6, strt+next0*12, wid, wid), pygame.Rect(strt+next0*7, strt+next0*12, wid, wid), pygame.Rect(strt+next0*8, strt+next0*12, wid, wid), pygame.Rect(strt+next0*9, strt+next0*12, wid, wid), pygame.Rect(strt+next0*10, strt+next0*12, wid, wid), pygame.Rect(strt+next0*11, strt+next0*12, wid, wid), pygame.Rect(strt+next0*12, strt+next0*12, wid, wid), pygame.Rect(strt+next0*13, strt+next0*12, wid, wid), pygame.Rect(strt+next0*14, strt+next0*12, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*13, wid, wid), pygame.Rect(strt+next0*6, strt+next0*13, wid, wid), pygame.Rect(strt+next0*7, strt+next0*13, wid, wid), pygame.Rect(strt+next0*8, strt+next0*13, wid, wid), pygame.Rect(strt+next0*9, strt+next0*13, wid, wid), pygame.Rect(strt+next0*10, strt+next0*13, wid, wid), pygame.Rect(strt+next0*11, strt+next0*13, wid, wid), pygame.Rect(strt+next0*12, strt+next0*13, wid, wid), pygame.Rect(strt+next0*13, strt+next0*13, wid, wid), pygame.Rect(strt+next0*14, strt+next0*13, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*14, wid, wid), pygame.Rect(strt+next0*6, strt+next0*14, wid, wid), pygame.Rect(strt+next0*7, strt+next0*14, wid, wid), pygame.Rect(strt+next0*8, strt+next0*14, wid, wid), pygame.Rect(strt+next0*9, strt+next0*14, wid, wid), pygame.Rect(strt+next0*10, strt+next0*14, wid, wid), pygame.Rect(strt+next0*11, strt+next0*14, wid, wid), pygame.Rect(strt+next0*12, strt+next0*14, wid, wid), pygame.Rect(strt+next0*13, strt+next0*14, wid, wid), pygame.Rect(strt+next0*14, strt+next0*14, wid, wid),
         pygame.Rect(strt+next0*5, strt+next0*15, wid, wid), pygame.Rect(strt+next0*6, strt+next0*15, wid, wid), pygame.Rect(strt+next0*7, strt+next0*15, wid, wid), pygame.Rect(strt+next0*8, strt+next0*15, wid, wid), pygame.Rect(strt+next0*9, strt+next0*15, wid, wid), pygame.Rect(strt+next0*10, strt+next0*15, wid, wid), pygame.Rect(strt+next0*11, strt+next0*15, wid, wid), pygame.Rect(strt+next0*12, strt+next0*15, wid, wid), pygame.Rect(strt+next0*13, strt+next0*15, wid, wid), pygame.Rect(strt+next0*14, strt+next0*15, wid, wid)]


numBoard = [pygame.Rect(strt+next0*5, strt+next0*1, wid, wid), pygame.Rect(strt+next0*6, strt+next0*1, wid, wid), pygame.Rect(strt+next0*7, strt+next0*1, wid, wid), pygame.Rect(strt+next0*8, strt+next0*1, wid, wid), pygame.Rect(strt+next0*9, strt+next0*1, wid, wid), pygame.Rect(strt+next0*10, strt+next0*1, wid, wid), pygame.Rect(strt+next0*11, strt+next0*1, wid, wid), pygame.Rect(strt+next0*12, strt+next0*1, wid, wid), pygame.Rect(strt+next0*13, strt+next0*1, wid, wid), pygame.Rect(strt+next0*14, strt+next0*1, wid, wid),
            pygame.Rect(strt+next0*5, strt+next0*2, wid, wid), pygame.Rect(strt+next0*6, strt+next0*2, wid, wid), pygame.Rect(strt+next0*7, strt+next0*2, wid, wid), pygame.Rect(strt+next0*8, strt+next0*2, wid, wid), pygame.Rect(strt+next0*9, strt+next0*2, wid, wid), pygame.Rect(strt+next0*10, strt+next0*2, wid, wid), pygame.Rect(strt+next0*11, strt+next0*2, wid, wid), pygame.Rect(strt+next0*12, strt+next0*2, wid, wid), pygame.Rect(strt+next0*13, strt+next0*2, wid, wid), pygame.Rect(strt+next0*14, strt+next0*2, wid, wid),
            pygame.Rect(strt+next0*5, strt+next0*3, wid, wid), pygame.Rect(strt+next0*6, strt+next0*3, wid, wid), pygame.Rect(strt+next0*7, strt+next0*3, wid, wid), pygame.Rect(strt+next0*8, strt+next0*3, wid, wid), pygame.Rect(strt+next0*9, strt+next0*3, wid, wid), pygame.Rect(strt+next0*10, strt+next0*3, wid, wid), pygame.Rect(strt+next0*11, strt+next0*3, wid, wid), pygame.Rect(strt+next0*12, strt+next0*3, wid, wid), pygame.Rect(strt+next0*13, strt+next0*3, wid, wid), pygame.Rect(strt+next0*14, strt+next0*3, wid, wid),
            pygame.Rect(strt+next0*5, strt+next0*4, wid, wid), pygame.Rect(strt+next0*6, strt+next0*4, wid, wid), pygame.Rect(strt+next0*7, strt+next0*4, wid, wid), pygame.Rect(strt+next0*8, strt+next0*4, wid, wid), pygame.Rect(strt+next0*9, strt+next0*4, wid, wid), pygame.Rect(strt+next0*10, strt+next0*4, wid, wid), pygame.Rect(strt+next0*11, strt+next0*4, wid, wid), pygame.Rect(strt+next0*12, strt+next0*4, wid, wid), pygame.Rect(strt+next0*13, strt+next0*4, wid, wid), pygame.Rect(strt+next0*14, strt+next0*4, wid, wid), pygame.Rect(strt+next0*15, strt+next0*4, wid, wid),
            pygame.Rect(strt+next0*5, strt+next0*5, wid, wid), pygame.Rect(strt+next0*6, strt+next0*5, wid, wid), pygame.Rect(strt+next0*7, strt+next0*5, wid, wid), pygame.Rect(strt+next0*8, strt+next0*5, wid, wid), pygame.Rect(strt+next0*9, strt+next0*5, wid, wid), pygame.Rect(strt+next0*10, strt+next0*5, wid, wid), pygame.Rect(strt+next0*11, strt+next0*5, wid, wid), pygame.Rect(strt+next0*12, strt+next0*5, wid, wid), pygame.Rect(strt+next0*13, strt+next0*5, wid, wid), pygame.Rect(strt+next0*14, strt+next0*5, wid, wid), pygame.Rect(strt+next0*15, strt+next0*5, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*6, wid, wid), pygame.Rect(strt+next0*1, strt+next0*6, wid, wid), pygame.Rect(strt+next0*2, strt+next0*6, wid, wid), pygame.Rect(strt+next0*3, strt+next0*6, wid, wid), pygame.Rect(strt+next0*4, strt+next0*6, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*7, wid, wid), pygame.Rect(strt+next0*1, strt+next0*7, wid, wid), pygame.Rect(strt+next0*2, strt+next0*7, wid, wid), pygame.Rect(strt+next0*3, strt+next0*7, wid, wid), pygame.Rect(strt+next0*4, strt+next0*7, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*8, wid, wid), pygame.Rect(strt+next0*1, strt+next0*8, wid, wid), pygame.Rect(strt+next0*2, strt+next0*8, wid, wid), pygame.Rect(strt+next0*3, strt+next0*8, wid, wid), pygame.Rect(strt+next0*4, strt+next0*8, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*9, wid, wid), pygame.Rect(strt+next0*1, strt+next0*9, wid, wid), pygame.Rect(strt+next0*2, strt+next0*9, wid, wid), pygame.Rect(strt+next0*3, strt+next0*9, wid, wid), pygame.Rect(strt+next0*4, strt+next0*9, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*10, wid, wid), pygame.Rect(strt+next0*1, strt+next0*10, wid, wid), pygame.Rect(strt+next0*2, strt+next0*10, wid, wid), pygame.Rect(strt+next0*3, strt+next0*10, wid, wid), pygame.Rect(strt+next0*4, strt+next0*10, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*11, wid, wid), pygame.Rect(strt+next0*1, strt+next0*11, wid, wid), pygame.Rect(strt+next0*2, strt+next0*11, wid, wid), pygame.Rect(strt+next0*3, strt+next0*11, wid, wid), pygame.Rect(strt+next0*4, strt+next0*11, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*12, wid, wid), pygame.Rect(strt+next0*1, strt+next0*12, wid, wid), pygame.Rect(strt+next0*2, strt+next0*12, wid, wid), pygame.Rect(strt+next0*3, strt+next0*12, wid, wid), pygame.Rect(strt+next0*4, strt+next0*12, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*13, wid, wid), pygame.Rect(strt+next0*1, strt+next0*13, wid, wid), pygame.Rect(strt+next0*2, strt+next0*13, wid, wid), pygame.Rect(strt+next0*3, strt+next0*13, wid, wid), pygame.Rect(strt+next0*4, strt+next0*13, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*14, wid, wid), pygame.Rect(strt+next0*1, strt+next0*14, wid, wid), pygame.Rect(strt+next0*2, strt+next0*14, wid, wid), pygame.Rect(strt+next0*3, strt+next0*14, wid, wid), pygame.Rect(strt+next0*4, strt+next0*14, wid, wid),
            pygame.Rect(strt+next0*0, strt+next0*15, wid, wid), pygame.Rect(strt+next0*1, strt+next0*15, wid, wid), pygame.Rect(strt+next0*2, strt+next0*15, wid, wid), pygame.Rect(strt+next0*3, strt+next0*15, wid, wid), pygame.Rect(strt+next0*4, strt+next0*15, wid, wid),
            ]

colors = [w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w]

puzzle = [b, w, w, w, w, w, w, w, w, b,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          w, w, w, w, w, w, w, w, w, w,
          b, w, w, w, w, w, w, w, w, b]

sailboat = [w, w, w, w, b, w, w, w, w, w,
            w, b, w, w, b, b, w, w, w, w,
            b, w, b, w, b, b, b, w, w, w,
            w, b, w, w, b, b, b, b, w, w,
            w, w, w, w, b, w, w, w, w, w,
            w, w, w, w, b, w, w, w, w, w,
            b, b, w, w, b, w, w, w, b, b,
            w, b, b, b, b, b, b, b, b, w,
            w, w, b, b, b, b, b, b, w, w,
            w, w, w, b, b, b, b, w, w, w]



collection = [sailboat, puzzle]

difficulty = 3 #1 is hard, 2 is medium, 3 is easy
once = 0
aWin = 0
run = True
# Loop
while run:
    if once == 0:
        #puzzle = sailboat
        generatePuzzle() 
        #customGenPuzzle(2, 1)
        #choosePreset()
        once += 1
        
    screen.fill(gray)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and aWin != 1:
            if selection.collidepoint(event.pos):
                if squareType == b:
                    squareType = r
                else:
                    squareType = b
            else:
                for i in range(len(board)):
                    rect = board[i]
                    if rect.collidepoint(event.pos):
                        if colors[i] != squareType:
                            colors[i] = squareType
                        else:
                            colors[i] = w
            win = checkWin()
            if win:
                aWin = 1
    
    
    drawBlocks()
    genNumsHorizontal()
    genNumsVertical()
    drawType()
        
    if aWin == 1:
        drawText("You win!", 210, 0, r, font)
        #IDEA TO TURN EXTRA BLOCKS A DIFFERENT COLOR

    clock.tick(60)
    pygame.display.flip()   

pygame.quit()