def on_gesture_shake():
    basic.show_number(randint(1, 9))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
