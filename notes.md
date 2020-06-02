The Window class has several methods that your programs can override to provide the functionality to the program. Here are some of the most commonly used ones:

on_draw: All the code to draw the screen goes here.

update: All the code to move your items and perform game logic goes here. This is called about 60 times per second.

on_key_press: Handle events when a key is pressed, such as giving a player a speed.

on_key_release: Handle when a key is released, here you might stop a player from moving.

on_mouse_motion: This is called every time the mouse moves.

on_mouse_press: Called when a mouse button is pressed.

set_viewport: This function is used in scrolling games, when you have a world much larger than what can be seen on one screen. 
Calling set_viewport allows a programmer to set what part of that world is currently visible.


https://opensource.com/article/18/4/easy-2d-game-creation-python-and-arcade -> On def setup