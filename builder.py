  
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
ROWS = int(sys.argv[2])
COLLUMS = int(sys.argv[1])
RECTBASE = 30
win = pygame.display.set_mode((COLLUMS*RECTBASE, ROWS*RECTBASE + 100))
run = True
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
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
    def collision(self, mouse_x, mouse_y):
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
    def collision(self,mouse_x,mouse_y):
        if mouse_x > self.rect.x and mouse_x < self.rect.x+self.rect.width:
            if mouse_y < self.rect.y+self.rect.width and mouse_y > self.rect.y:
                return True
    def toggle(self,buttons):
        for button in buttons:
            button.toggled = False
        self.toggled = True
        return self.color        


# >>> REDRAW <<< #
def redraw(grid,buttons):
    win.fill((255,255,255))
    for g in grid:
        pygame.draw.rect(win, g.color, (g.rect.x,g.rect.y,RECTBASE,RECTBASE))
        pygame.draw.rect(win, (0,0,0), (g.rect.x,g.rect.y,RECTBASE,RECTBASE), 1)
    for button in buttons:
        button.draw(win)
    pygame.display.update()

#create grid and other classes
gx = 0
gy = 0
grid = []
for i in range(COLLUMS):
    for j in range(ROWS):
        grid.append(Grid(gx,gy))
        gy += RECTBASE
    gy = 0
    gx += RECTBASE

buttons = [Button(10, ROWS * RECTBASE + 10,(255,0,0),"RED","r",(0,0,0)),Button(50, ROWS * RECTBASE + 10,(255,255,0),"YELLOW","y",(0,0,0)),Button(90, ROWS * RECTBASE + 10,(0,255,0),"GREEN","g",(0,0,0)),
Button(130, ROWS * RECTBASE + 10,(0,255,255),"BLUE1","b",(0,0,0)),Button(10, ROWS * RECTBASE + 50,(0,0,255),"BLUE","B"),Button(50, ROWS * RECTBASE + 50,(255,0,255),"PURPLE","p"),
Button(90, ROWS * RECTBASE + 50,(0,0,0),"BLACK","b")]

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
                if g.collision(mouse_x,mouse_y):
                    g.toggle(togglecolor,togglevalue)
                    print(g.rect.topleft)
            for button in buttons:
                if button.collision(mouse_x,mouse_y):
                    togglecolor = button.toggle(buttons)
                    togglevalue = button.value

    redraw(grid,buttons)