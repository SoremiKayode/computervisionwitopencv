import pygame

def init():
 pygame.init()
 win = pygame.display.set_mode((300, 300))

def get_key(key_name):
    ans = False
    for eve in pygame.event.get(): pass
    key_input = pygame.key.get_pressed()
    my_key = getattr(pygame, 'K_{}'.format(key_name))

    if key_input[my_key]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if get_key("LEFT") :
        print("left key is pressed")


if __name__ == "__main__":
    init()

    while True:
        main()
