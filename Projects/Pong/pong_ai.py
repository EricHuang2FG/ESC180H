last_pos = [0, 0]

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    global last_pos

    on_right = paddle_frect.pos[0] > other_paddle_frect.pos[0]
    ball_left = ball_frect.pos[0] < last_pos[0]
    dy = ball_frect.pos[1] - last_pos[1]
    dx = ball_frect.pos[0] - last_pos[0]
    last_pos = [ball_frect.pos[0], ball_frect.pos[1]]
    if (
        (ball_left and on_right) or
        (not ball_left and not on_right)
    ):
        if paddle_frect.pos[1] + (paddle_frect.size[1] / 2) <= table_size[1] / 2:
            return "down"
        return "up"
    x_pointer, y_pointer = ball_frect.pos[0], ball_frect.pos[1]
    condition = True
    while condition:
        x_pointer += dx
        y_pointer += dy
        if y_pointer + ball_frect.size[1] >= table_size[1] or y_pointer <= 0:
            dy *= -1
        if on_right and not ball_left:
            condition = x_pointer + ball_frect.size[0] <= table_size[0] - paddle_frect.size[0]
        elif not on_right and ball_left:
            condition = x_pointer >= paddle_frect.size[0]

    if y_pointer < paddle_frect.pos[1]:
        return "up"
    if y_pointer > paddle_frect.pos[1] + paddle_frect.size[1]:
        return "down"
