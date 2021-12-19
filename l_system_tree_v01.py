import turtle
import random

ANGLE = 25
LENGTH = 80
THIKNESS = 16
RATE = 0.78
COLOR_BRAWN = (30, 0, 0)
COLOR_GREEN = (10, 120, 0)
COLOR_GRASS = (10, 80, 0)
COLOR_SKY = (200, 200, 250)
LEAF_LENGTH = 10
LEAF_WIDTH = 8


def rand_angle(base_angle):
    a1 = random.random() * base_angle
    a2 = random.random() * base_angle
    return a1 + a2


def rand_length(base_length):
    n1 = random.random() * base_length
    n2 = random.random() * base_length
    return n1 + n2


def arc_to_angle(length=100, from_angle=0.0, to_angle=45.0, segments=10, from_size=10.0, to_size=1.0):
    angle_delta = (to_angle - from_angle) / segments
    cur_angle = from_angle

    length_delta = length / segments

    size_delta = (to_size - from_size) / segments
    cur_size = from_size

    for segment_number in range(segments):
        cur_angle += angle_delta
        turtle.setheading(cur_angle)

        cur_size += size_delta
        turtle.pensize(int(cur_size))

        turtle.forward(length_delta)


def main():
    # print('Hi')
    turtle.hideturtle()
    turtle.colormode(255)
    turtle.tracer(0)
    turtle.bgcolor(COLOR_SKY)
    turtle.penup()

    # ground
    turtle.setposition(-400, -300)
    turtle.setheading(0)
    turtle.pensize(250)
    turtle.pencolor(COLOR_GRASS)
    turtle.pendown()
    turtle.forward(800)
    turtle.penup()

    turtle.setposition(0, -200)
    turtle.left(90)
    turtle.pendown()
    turtle.pensize(THIKNESS)

    axiom = 'Bp'
    axm_temp = ''
    itr = 7
    buf = []
    end_angle = 90

    # print(axiom)

    translate = {
        '+': '+',
        '-': '-',
        'B': 'B',
        '[': '[',
        ']': ']',
        'p': '[-Bp][+Bp]'
    }
    for k in range(itr):
        for ch in axiom:
            if ch == 'p':
                ran = random.randint(0, 100)
                # print(ran)
                if ran < 30:
                    axm_temp += '[[-Bp]][+Bp]'
                elif ran > 70:
                    axm_temp += '[-Bp][[+Bp]]'
                else:
                    axm_temp += '[-Bp][+Bp]'
            else:
                axm_temp += translate[ch]
        axiom = axm_temp
        axm_temp = ''

    # print(axiom)

    for ch in axiom:
        if ch == '+':
            # turtle.right(randAngle(ANGLE))
            end_angle = turtle.heading() + rand_angle(ANGLE)
        elif ch == '-':
            # turtle.right(-randAngle(ANGLE))
            end_angle = turtle.heading() - rand_angle(ANGLE)
        elif ch == '[':
            position = turtle.pos()
            heading = turtle.heading()
            buf.append((position, heading))
        elif ch == ']':
            restore_position, restore_heading = buf.pop()
            turtle.setposition(restore_position)
            turtle.setheading(restore_heading)
        elif ch == 'B':
            level = len(buf)
            rate = RATE ** level

            branch_lenght = rand_length(LENGTH * rate)

            strt_pen_size = THIKNESS * rate
            end_pen_size = strt_pen_size * RATE

            start_angle = turtle.heading()
            turtle.pencolor(COLOR_BRAWN)
            turtle.pendown()
            # turtle.forward(lenght)
            arc_to_angle(
                length=branch_lenght,
                from_angle=start_angle,
                to_angle=end_angle,
                segments=5,
                from_size=strt_pen_size,
                to_size=end_pen_size)
            turtle.penup()
        elif ch == 'p':
            turtle.pencolor(COLOR_GREEN)
            turtle.pensize(LEAF_WIDTH)
            turtle.pendown()
            start_angle = turtle.heading()
            end_angle = rand_angle(start_angle)
            # turtle.forward(LEAF_LENGTH)
            arc_to_angle(
                length=LEAF_LENGTH,
                from_angle=start_angle,
                to_angle=end_angle,
                from_size=LEAF_WIDTH,
                to_size=3)
            turtle.penup()
        else:
            print(f'Unexpected char - {ch}')

    turtle.update()
    turtle.mainloop()


if __name__ == '__main__':
    main()
