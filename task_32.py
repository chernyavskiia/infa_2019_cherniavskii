#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    ax = 0
    fill_cell()
    while wall_is_beneath():
        move_right()
        if wall_is_on_the_right():
            break
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    ax += 1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        else:
            fill_cell()
    mov ('ax', ax)
    


if __name__ == '__main__':
    run_tasks()
