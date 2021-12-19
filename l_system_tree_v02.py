from turtle import Screen, Turtle
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


class Plotter():
    def __init__(self):
        self.screen = Screen()
        self.turtle = Turtle()
        self.screen.tracer(False)
        self.screen.onkeypress(self.draw_tree, 'space')
        self.screen.listen()


    def arc_to_angle(self, length=100, from_angle=0.0, to_angle=45.0, segments=10, from_size=10.0, to_size=1.0):
        angle_delta = (to_angle - from_angle) / segments
        cur_angle = from_angle

        length_delta = length / segments

        size_delta = (to_size - from_size) / segments
        cur_size = from_size

        for segment_number in range(segments):
            cur_angle += angle_delta
            self.turtle.setheading(cur_angle)

            cur_size += size_delta
            self.turtle.pensize(int(cur_size))

            self.turtle.forward(length_delta)


    def fill_background(self, bg_color):
        w = self.screen.screensize()[0]
        h = self.screen.screensize()[1]
        
        self.turtle.goto(-w*2, -h*2)
        self.turtle.setheading(90)  # north

        self.turtle.pendown()
        self.turtle.color(bg_color, bg_color)     # set both drawing and fill color to be the same color
        
        self.turtle.begin_fill()
        
        self.turtle.forward(h*4)
        self.turtle.right(90)
        self.turtle.forward(w*4)
        self.turtle.right(90)
        self.turtle.forward(h*4)
        self.turtle.right(90)
        self.turtle.forward(w*4)
        self.turtle.right(90)
        
        self.turtle.end_fill()

        self.turtle.penup()
        
        # end by setting the turtle in the middle of the screen 
        self.turtle.width(1)
        self.turtle.color('black', 'white')
        self.turtle.goto(0,0)
        self.turtle.setheading(90)
    

    def draw_tree(self):
        # print('Hi')
        
        self.turtle.hideturtle()
        # self.turtle.colormode(255)
        self.screen.colormode(255)
        # self.turtle.tracer(0)
        self.screen.tracer(0)
        # self.turtle.bgcolor(COLOR_SKY)
        # self.screen.bgcolor(COLOR_SKY)
        self.fill_background(COLOR_SKY)
        self.turtle.penup()

        w = self.screen.screensize()[0]
        h = self.screen.screensize()[1]

        # ground
        self.turtle.setposition(-400, -300)
        self.turtle.setheading(0)
        self.turtle.pensize(250)
        self.turtle.pencolor(COLOR_GRASS)
        self.turtle.pendown()
        self.turtle.forward(800)
        self.turtle.penup()

        self.turtle.setposition(0, -200)
        self.turtle.left(90)
        self.turtle.pendown()
        self.turtle.pensize(THIKNESS)

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
                # self.turtle.right(randAngle(ANGLE))
                end_angle = self.turtle.heading() + rand_angle(ANGLE)
            elif ch == '-':
                # self.turtle.right(-randAngle(ANGLE))
                end_angle = self.turtle.heading() - rand_angle(ANGLE)
            elif ch == '[':
                position = self.turtle.pos()
                heading = self.turtle.heading()
                buf.append((position, heading))
            elif ch == ']':
                restore_position, restore_heading = buf.pop()
                self.turtle.setposition(restore_position)
                self.turtle.setheading(restore_heading)
            elif ch == 'B':
                level = len(buf)
                rate = RATE ** level

                branch_lenght = rand_length(LENGTH * rate)

                strt_pen_size = THIKNESS * rate
                end_pen_size = strt_pen_size * RATE

                start_angle = self.turtle.heading()
                self.turtle.pencolor(COLOR_BRAWN)
                self.turtle.pendown()
                # self.turtle.forward(lenght)
                self.arc_to_angle(
                    length=branch_lenght,
                    from_angle=start_angle,
                    to_angle=end_angle,
                    segments=5,
                    from_size=strt_pen_size,
                    to_size=end_pen_size)
                self.turtle.penup()
            elif ch == 'p':
                self.turtle.pencolor(COLOR_GREEN)
                self.turtle.pensize(LEAF_WIDTH)
                self.turtle.pendown()
                start_angle = self.turtle.heading()
                end_angle = rand_angle(start_angle)
                # self.turtle.forward(LEAF_LENGTH)
                self.arc_to_angle(
                    length=LEAF_LENGTH,
                    from_angle=start_angle,
                    to_angle=end_angle,
                    from_size=LEAF_WIDTH,
                    to_size=3)
                self.turtle.penup()
            else:
                print(f'Unexpected char - {ch}')

        self.turtle.pencolor(COLOR_BRAWN)
        self.turtle.goto(-w/2, h - 50)
        self.turtle.write("Press \"Space\" for draw a new tree.", font=("Verdana", 15, "normal"))
        
        self.screen.update()


def main():

    screen = Screen()
    plotter = Plotter()
    plotter.draw_tree()
    screen.mainloop()


if __name__ == '__main__':
    main()
