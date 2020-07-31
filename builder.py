  
import sys
try:
    if int(sys.argv[1]) + int(sys.argv[2]) < 61 and int(sys.argv[1]) + int(sys.argv[2]) > 11:
        import pygame
    else:
        print("Usage: builder.py <count of x cubes (6-30)> <count of y cubes (6-30)>")
        sys.exit()
except ValueError or IndexError:
    print("Usage: builder.py <count of x cubes (6-30)> <count of y cubes (6-30)>")
    sys.exit()

pygame.init()
COLLUMS = int(sys.argv[1])
ROWS = int(sys.argv[2])
RECTBASE = 30
win = pygame.display.set_mode((COLLUMS*RECTBASE, ROWS*RECTBASE + 100))
run = True
try:
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
except:
    pass
pygame.display.set_caption("Level builder")
clock = pygame.time.Clock()


# <<<GRID CLASS>>> #
class Grid(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((RECTBASE,RECTBASE))
        self.color = (255,255,255)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.toggled = False
        self.value = "."
    def press(self, mouse_x, mouse_y):
        if mouse_x > self.rect.x and mouse_x < self.rect.x+self.rect.width:
            if mouse_y < self.rect.y+self.rect.width and mouse_y > self.rect.y:
                return True
    def toggle(self, togglecolor, value):
        if self.toggled:
            self.color = (255,255,255)
            self.toggled = False
            self.value = "."
        else:
            self.color = togglecolor
            self.toggled = True
            self.value = value


# <<<BUTTON CLASS>>> #
class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,color,text,value,textcolor=(255,255,255)):
        super().__init__()
        self.base = 40
        self.image = pygame.Surface((self.base,self.base))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.sprite = pygame.sprite.RenderPlain(self)
        self.toggled = False
        self.font = pygame.font.SysFont('comicsans',15)
        self.text = text
        self.text_rendered = self.font.render(self.text,1,textcolor)
        self.value = value
    def draw(self,win):
        self.sprite.update()
        self.sprite.draw(win)
        win.blit(self.text_rendered, (self.rect.x+3,self.rect.y+3))
        if self.toggled:
            pygame.draw.rect(win, (0,100,255), (self.rect.x,self.rect.y,self.base,self.base), 3)
        else:
            pygame.draw.rect(win, (0,0,0), (self.rect.x,self.rect.y,self.base,self.base), 3)
    def press(self,mouse_x,mouse_y):
        if mouse_x > self.rect.x and mouse_x < self.rect.x+self.rect.width:
            if mouse_y < self.rect.y+self.rect.width and mouse_y > self.rect.y:
                return True
    def toggle(self,buttons):
        for button in buttons:
            button.toggled = False
        self.toggled = True
        return self.color

class EndButton(Button):
    def toggle(self, grid,collums,rows):
        print("""
RESULT:
<<--------------------->>""")
        num = 0
        lines = 0
        string = []
        for gri in grid:
            string.append(gri.value)
            num += 1
            if num >= collums:
                num = 0
                joined = "".join(string)
                string = []
                lines += 1
                if lines == 1:
                    print(f'["{joined}",')
                elif lines >= rows:
                    print(f'"{joined}"]')
                else:
                    print(f'"{joined}",')
                

# >>> REDRAW <<< #
def redraw(grid,buttons):
    win.fill((255,255,255))
    for g in grid:
        pygame.draw.rect(win, g.color, (g.rect.x,g.rect.y,RECTBASE,RECTBASE))
        pygame.draw.rect(win, (0,0,0), (g.rect.x,g.rect.y,RECTBASE,RECTBASE), 1)
    for button in buttons:
        button.draw(win)
    endbutton.draw(win)
    pygame.display.update()

#create grid and other classes
gx = 0
gy = 0
grid = []
for i in range(ROWS):
    for j in range(COLLUMS):
        grid.append(Grid(gx,gy))
        gx += RECTBASE
    gx = 0
    gy += RECTBASE

#add values for RED and YELLOW
buttons = [Button(10, ROWS * RECTBASE + 10,(255,0,0),"spawn","S",(0,0,0)),Button(50, ROWS * RECTBASE + 10,(255,255,0),"block1","x",(0,0,0)),Button(90, ROWS * RECTBASE + 10,(0,255,0),"block2","X",(0,0,0)),
Button(130, ROWS * RECTBASE + 10,(0,255,255),"extra1","o",(0,0,0)),Button(10, ROWS * RECTBASE + 50,(0,0,255),"extra2","O"),Button(50, ROWS * RECTBASE + 50,(255,0,255),"end","E"),
Button(90, ROWS * RECTBASE + 50,(0,0,0),"platf.","p")]
endbutton = EndButton(130, ROWS * RECTBASE + 50,(50,50,50),"export",".")

togglecolor = (0,0,0)
togglevalue = "b"
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            for g in grid:
                if g.press(mouse_x,mouse_y):
                    g.toggle(togglecolor,togglevalue)
            for button in buttons:
                if button.press(mouse_x,mouse_y):
                    togglecolor = button.toggle(buttons)
                    togglevalue = button.value
            if endbutton.press(mouse_x,mouse_y):
                endbutton.toggle(grid,COLLUMS,ROWS)

    redraw(grid,buttons)