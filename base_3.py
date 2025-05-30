
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
        radio.send_value("a2", a_time)
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
        

def button_b():
    global st_b
    if st_b > 0:
        et_b = input.running_time()
        b_time = et_b - st_b
        radio.send_value("b2", b_time)
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)

def on_received_value(name, value):
    global st_a, st_b
    if name == "a1":
        st_a = input.running_time() - value
    elif name == "b1":
        st_b = input.running_time() - value
        

def on_forever():
    global st_a, st_b
    radio.on_received_value(on_received_value)
    input.on_button_pressed(Button.A, button_a)
    input.on_button_pressed(Button.B, button_b)

basic.forever(on_forever)
