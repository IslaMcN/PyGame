import arcade
import random

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "SPRITE EXAMPLE"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_list = None
        self.coin_list = None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)
    
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("sprites/maincharacter/1 Woodcutter/Woodcutter_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            SPRITE_SCALING_COIN = 0.2
            coin = arcade.Sprite("sprites/items/PNG/shiny/1.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)



    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
    
    def update(self, delta_time):
        # Logic to move and game logic
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit_list:
            coin.kill()
            self.score += 1

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
