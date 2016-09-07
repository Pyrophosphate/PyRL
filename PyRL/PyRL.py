import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

playerX = SCREEN_WIDTH/2
playerY = SCREEN_HEIGHT/2

def handle_keys():
    global playerX, playerY
    
    key = libtcod.console_wait_for_keypress(True)
    
    if key.vk == libtcod.KEY_ESCAPE:
        return True
    
    # Movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_KP8):
        playerY -= 1
    
    elif libtcod.console_is_key_pressed(libtcod.KEY_KP6):
        playerX += 1
    
    elif libtcod.console_is_key_pressed(libtcod.KEY_KP4):
        playerX -= 1
        
    elif libtcod.console_is_key_pressed(libtcod.KEY_KP2):
        playerY += 1
    
    elif libtcod.console_is_key_pressed(libtcod.KEY_KP7):
        playerY -= 1
        playerX -= 1
    
    elif libtcod.console_is_key_pressed(libtcod.KEY_KP9):
        playerX += 1
        playerY -= 1
    
    elif libtcod.console_is_key_pressed(libtcod.KEY_KP1):
        playerX -= 1
        playerY += 1
        
    elif libtcod.console_is_key_pressed(libtcod.KEY_KP3):
        playerY += 1
        playerX += 1


libtcod.console_set_custom_font('terminal8x8_gs_as.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INCOL)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Tutorial', False)

while not libtcod.console_is_window_closed():
    
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, playerX, playerY, '@', libtcod.BKGND_NONE)
 
    libtcod.console_flush()
 
    libtcod.console_put_char(0, playerX, playerY, ' ', libtcod.BKGND_NONE)
    exit = handle_keys()
    
    if exit:
        break
    


