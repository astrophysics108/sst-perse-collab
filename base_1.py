
radio.set_group(137)

def button_a():
    radio.send_number(0)

def button_b():
    radio.send_number(1) 

input.on_button_pressed(Button.A, button_a)
input.on_button_pressed(Button.B, button_b)
