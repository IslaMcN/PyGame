import arcade
# Set screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# Open the window and set the title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

arcade.set_background_color(arcade.color.WHITE)
# Starts render process. MUST BE DONE BEFORE ANY DRAWING COMMANDS
arcade.start_render()
# Draw face
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
# Draw right eye
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
# Draw left eye
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
# Draw the smile
x = 300
y = 280
width = 150
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)
# Finish
arcade.finish_render()
# Keep window open until user hits close
arcade.run()
