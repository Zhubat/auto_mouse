from pynput.mouse import Button, Controller
import pyautogui, sys
import os
import time

def struming(strum, centre, chord_1, chord_2, chord_3, chord_4, b1, b2, b3):
    for i in range(len(strum)):
            #print(i)
            #print(strum[i])
            if i < b1:
                x, y = chord_1
            elif i < b2:
                x, y = chord_2
            elif i < b3:
                x, y = chord_3
            else:
                x, y = chord_4

            pyautogui.moveTo(x, y)
            
            if not strum[i]:
                for i in range(5):
                    pyautogui.mouseDown()
                    pyautogui.mouseUp()
                time.sleep(strum[0])
            else:
                pyautogui.mouseDown()
                pyautogui.mouseUp()
            time.sleep(strum[i])

def pre_chorus(strum, centre, chord_1, chord_2, chord_3, chord_4, b1, b2, b3):
    for i in range(6):
        #print(i)
        #print(strum[i])
        if i < b1:
            x, y = chord_1
        else:
            x, y = chord_2
        


        pyautogui.moveTo(x, y)
        
        if not strum[i]:
            for i in range(5):
                pyautogui.mouseDown()
                pyautogui.mouseUp()
            time.sleep(strum[0])
        else:
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        time.sleep(strum[i])

    for i in range(4):
        if i == 0:
            x, y = chord_3
        elif i == 1:
            x, y = chord_2
        elif i == 2:
            x, y = chord_4
        elif i == 3:
            x, y = chord_3


        pyautogui.moveTo(x, y)
        for j in range(2):
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        time.sleep(strum[0])

    

if __name__ == '__main__':
    #mouse = Controller()
    #print(mouse.position)
    #os.environ['DISPLAY'] = os.environ['REMOTE_DISPLAY']
    '''
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')
    '''
    screen_x, screen_y = pyautogui.size()
    centre = screen_x/2, screen_y/2
    A_min = centre
    G_maj = 1100, 550
    E_maj = 1200, 550
    D_maj = 1300, 550
    C_maj = 1400, 550
    F_maj = 1500, 550

    bps = 0.6897/4
    half = 2
    strum = [bps/2, bps/2, bps/2, 0, bps/2, \
        0, bps/2, bps/2, 0, bps/2]
    
    pyautogui.moveTo(centre[0], centre[1], 0)
    pyautogui.click()
    print(centre)
    '''
    moveToX = 1200
    moveToY = 700
    num_of_clicks = 1
    secs_between_clicks = 1
    '''
    
    print('start Wonderwall')
    for x in range(19):
        print('Bar: ', x)
        if x == 6:
            struming(strum, centre, C_maj, D_maj, A_min, A_min, 3, 5, 8)
        elif x >= 11 and x < 13:
            struming(strum, centre, C_maj, D_maj, E_maj, E_maj, 3, 5, 8)
        elif x == 13:
            pre_chorus(strum, centre, C_maj, D_maj, G_maj, E_maj, 3, 5, 8)
        elif x == 14:
            struming(strum, centre, A_min, A_min, A_min, A_min, 3, 5, 8)
        elif x > 14 and x < 18:
            struming(strum, centre, C_maj, E_maj, G_maj, E_maj, 3, 5, 8)
        elif x == 18:
            strum = strum[:8]
            struming(strum, centre, C_maj, E_maj, G_maj, E_maj, 3, 5, 8)
        else:
            struming(strum, centre, E_maj, G_maj, D_maj, A_min, 3, 5, 8)

    
    print('play end')
    '''
    
    
    '''