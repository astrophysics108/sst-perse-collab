radio.set_group(137)
st_a = 0
st_b = 0
done = 0

def button_a():
    global st_a, done
    if st_a == 0:
        radio.send_number(0)
    else:
        et_a = input.running_time()
        a_time = et_a - st_a
        if done == 0:
            basic.show_string("Player A wins!")
            basic.show_number(int(a_time))
            done = 1
        else:
            basic.show_string("Player B won.")
            basic.show_number(int(a_time))
            

def button_b():
    global st_b, done
    if st_b == 0:
        radio.send_number(1)
    else:
        et_b = input.running_time()
        b_time = et_b - st_b
        basic.show_number(int(b_time))
    if done == 0:
            basic.show_string("Player B wins!")
            basic.show_number(int(b_time))
            done = 1
    else:
            basic.show_string("Player A won.")
            basic.show_number(int(b_time))

def on_received_value(name, value):
    if name == "a2":
        st_a = input.running_time() - value
        
    elif name == "b2":
        st_b = input.running_time() - value

radio.on_received_value(on_received_value)
input.on_button_pressed(Button.A, button_a)
input.on_button_pressed(Button.B, button_b)
