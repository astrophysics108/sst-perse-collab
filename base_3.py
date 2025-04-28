
a_time, b_time = 0,0
st_a, st_b = 0, 0

radio.set_group(137)

def button_a():
    global st_a
    if st_a > 0:
        et_a = input.running_time()
        a_time = et_a - st_a
        radio.send_value("a2", a_time)
        basic.show_icon(IconNames.HEART)
        

def button_b():
    global st_b
    if st_b > 0:
        et_b = input.running_time()
        b_time = et_b - st_b
        radio.send_value("b2", b_time)
        basic.show_icon(IconNames.HEART)

def on_received_value(name, value):
    if name == "a1":
        st_a = input.running_time() - value
    elif name == "b1":
        st_b = input.running_time() - value
        


radio.on_received_value(on_received_value)
input.on_button_pressed(Button.A, button_a)
input.on_button_pressed(Button.B, button_b)
