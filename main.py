def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_number(0)
basic.forever(on_forever)
radio.set_group(1)
