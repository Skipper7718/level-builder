  
import sys
if len(sys.argv) < 2:
    if sys.argv[2] != int or sys.argv[1] != int:
        print("Usage: editor.py <number of rows> <number of collums>")
        sys.exit("Pls use my program right :(")
else:
    import pygame

ROWS = int(sys.argv[1])
COLLUMS = int(sys.argv[2])
RECTBASE = 30
win = pygame.display.set_mode((COLLUMS*RECTBASE, ROWS*RECTBASE + 90))
run = True
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Level builder")
clock = pygame.time.Clock()

class Grid(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((RECTBASE,RECTBASE))
        self.color = (255,0,255)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def collision(self, mouse_x, mouse_y):
        if mouse_x > self.rect.x and mouse_x < self.rect.x+self.rect.width:
            if mouse_y < self.rect.y+self.rect.width and mouse_y > self.rect.y:
                return True

# >>> REDRAW <<< #
def redraw(grid):
    win.fill((255,255,255))
    for g in grid:
        pygame.draw.rect(win, g.color, (g.rect.x,g.rect.y,RECTBASE,RECTBASE))
        pygame.draw.rect(win, (0,0,0), (g.rect.x,g.rect.y,RECTBASE,RECTBASE), 1)
    pygame.display.update()

#create grid
gx = 0
gy = 0
grid = []
for i in range(COLLUMS):
    for j in range(ROWS):
        grid.append(Grid(gx,gy))
        gy += RECTBASE
    gy = 0
    gx += RECTBASE
    
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            for g in grid:
                if g.collision(mouse_x,mouse_y):
                    g.color = (0,255,255)
                    print(g.rect.topleft)
    redraw(grid)