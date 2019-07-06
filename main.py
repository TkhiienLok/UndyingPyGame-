import pygame

pygame.init()
W = 646
H = 505
screen = pygame.display.set_mode([W, H])


class Button:
    def __init__(self,  text):
        self.text = text
        # self.size = (10, 10)
        # self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        # self.pos = (0, 0)
        self.active = False
        self.color = pygame.Color("Orange")

    def draw(self, x, y, width, height, surface):
        if self.active:
            self.color = pygame.Color("Yellow")
        else:
            self.color = pygame.Color("Orange")
        font = pygame.font.SysFont("tahoma", 25)  # Определяем шрифт и размер шрифта
        but_text = font.render(self.text, 1, self.color)  # текст, 1 или 0(True/False) для сглаженности
        textpos = but_text.get_rect(centerx=x+(width/2), centery=y+(height/2))  # и цвет
        pygame.draw.rect(surface, self.color, [x, y, width, height])
        pygame.draw.rect(surface, pygame.Color("Black"), [x+2, y+2, width-4, height-4])
        screen.blit(but_text, textpos)


class Menu:
    def __init__(self, surface):
        self.buttons = []
        self.active_button = 0
        self.active_color = pygame.Color("Yellow")
        self.inactive_color = pygame.Color("Sienna")
        self.surface = surface
        self.activated = True

    def add_button(self, button):
        # but = pygame.Rect(x, y, width, height)
        #
        # font = pygame.font.SysFont("tahoma", 25)  # Определяем шрифт и размер шрифта
        # but_text = font.render(text, 1, self.inactive_color)  # текст, 1 или 0(True/False) для сглаженности
        # textpos = but_text.get_rect(centerx=x+(width/2), centery=y+(height/2))                                                             #и цвет
        # pygame.draw.rect(self.surface, self.inactive_color, [x, y, width, height])
        # pygame.draw.rect(self.surface, pygame.Color("Black"), [x+2, y+2, width-4, height-4])
        # screen.blit(but_text, textpos)
        #
        # pygame.display.flip()

        self.buttons.append(button)

        self.buttons[self.active_button].active = True

        self.draw()

    def draw(self):
        self.surface.fill([0, 0, 0])
        width = self.surface.get_width() - 50

        but_width = width // len(self.buttons)
        x = 35
        for my_but in self.buttons:
            my_but.draw(x, 450, 90, 30, self.surface)
            x += but_width

        pygame.display.flip()

    def control_menu(self, key):
        if self.activated:
            if key == pygame.K_LEFT:
                self.active_button = (self.active_button - 1) % (-1 * len(self.buttons))
                for button1 in self.buttons:
                    button1.active = False
                self.buttons[self.active_button].active = True
            elif key == pygame.K_RIGHT:
                self.active_button = (self.active_button + 1) % (-1 * len(self.buttons))
                for button1 in self.buttons:
                    button1.active = False
                self.buttons[self.active_button].active = True
        self.draw()


my_menu = Menu(screen)
my_menu.add_button(Button("FIGHT"))
my_menu.add_button(Button("ACT"))
my_menu.add_button(Button("ITEM"))
my_menu.add_button(Button("MERCY"))

for but in my_menu.buttons:
    print(but.active)

print(type(my_menu))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                my_menu.activated = False

            if event.key == pygame.K_s:
                my_menu.activated = True

            if event.key == pygame.K_LEFT:
                my_menu.control_menu(event.key)
            if event.key == pygame.K_RIGHT:
                my_menu.control_menu(event.key)

    my_menu.draw()

    screen.fill(pygame.Color("Black"))
