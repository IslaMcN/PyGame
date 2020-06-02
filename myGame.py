import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)
    
    def setup(self):
        # Set up game here
        self.player_list = arcade.SpriteList()
        self.crystal_list = arcade.SpriteList()

        self.score = 0



    def on_draw(self):
        # Drawings here
        pass
    
    def update(self, delta_time):
        # Logic to move and game logic
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
