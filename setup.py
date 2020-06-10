import arcade
import random

def setup(self):
    self.player_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()

    self.score = 0

    self.player_sprite = arcade.Sprite("sprites/maincharacter/1 Woodcutter/Woodcutter_idle.png", SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

    for i in range(COIN_COUNT):
        coin = arcade.Sprite("sprites/items/PNG/shiny/1.png", SPRITE_SCALING_COIN)

        coin.center_x = random.randrange(SCREEN_WIDTH)
        coin.center_y = random.randrange(SCREEN_HEIGHT)

        self.coin_list.append(coin)