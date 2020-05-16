import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)
    
    def setup(self):
        # Set up game here
        pass

    def on_draw(self):
        arcade.start_render()
        SPRITE_SCALING_CRYSTAL = 0.2
        # Drawings here
        crystal = arcade.Sprite("sprites/items/PNG/shiny/1.png", SPRITE_SCALING_CRYSTAL)
        return crystal
    
    def update(self, delta_time):
        # Logic to move and game logic
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
