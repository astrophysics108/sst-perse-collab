a_time = 0
b_time = 0
st_a = 0
st_b = 0

radio.set_group(137)

def button_a():
    global st_a
    if st_a > 0:
        et_a = input.running_time()
        a_time = et_a - st_a
        radio.send_value("a1", a_time)
        basic.show_icon(IconNames.HEART)
        

def button_b():
    global st_b
    if st_b > 0:
        et_b = input.running_time()
        b_time = et_b - st_b
        radio.send_value("b1", b_time)
        basic.show_icon(IconNames.HEART)

def on_received_number(rn):
    if rn == 0:
        st_a = input.running_time()
    elif rn == 1:
        st_b = input.running_time()
        

def on_forever():
    radio.on_received_number(on_received_number)
    input.on_button_pressed(Button.A, button_a)
    input.on_button_pressed(Button.B, button_b)

basic.forever(on_forever)
