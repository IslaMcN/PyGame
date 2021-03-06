import arcade
import random
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_PLAYER = 0.75
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50
MOVEMENT_SPEED = 5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_PIXEL_SIZE= 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)
VIEWPORT_MARGIN_TOP = 60
VIEWPORT_MARGIN_BOTTOM = 60
VIEWPORT_RIGHT_MARGIN = 270
VIEWPORT_LEFT_MARGIN = 270
JUMP_SPEED = 23
GRAVITY = 1.1
SCREEN_TITLE = "SPRITE EXAMPLE - NOW WITH WALLS - Now with map"

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.physics_engine = None
        
        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False
        self.last_time = None
        self.frame_count = 0
        self.fps_message = None

        self.player_list = None
        self.coin_list = None
        self.wall_list = None

        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self,key,modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        self.physics_engine.update()


    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()



        self.score = 0

        self.player_sprite = arcade.Sprite("sprites/maincharacter/1 Woodcutter/Woodcutter.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        platforms_layer_name = 'Platforms'
        coins_layer_name = 'Coins'
        map_name = 'map.tmx'

        my_map = arcade.read_tiled_map(map_name, SPRITE_SCALING)

        map_array = arcade.read_tiled_map(map_name, SPRITE_SCALING)

        self.end_of_map = len(map_array[0] * GRID_PIXEL_SIZE)

        self.wall_list = arcade.generate_sprites(my_map, platforms_layer_name, SPRITE_SCALING)
        self.coin_list = arcade.generate_sprites(my_map, coins_layer_name, SPRITE_SCALING)

        if my_map.backgroundcolor:
            arcade.set_background_color(my_map.backgroundcolor)
        ##Set up walls
        # for x in range(173, 650, 64):
        #     wall = arcade.Sprite("sprites/items/PNG/Tileset.png", SPRITE_SCALING)
        #     wall.center_x = x
        #     wall.center_y = 200
        #     self.wall_list.append(wall)

        # for y in range(273, 500, 64):
        #     wall = arcade.Sprite("sprites/items/PNG/Tileset.png", SPRITE_SCALING)
        #     wall.center_x = x
        #     wall.center_y = 200
        #     self.wall_list.append(wall)
        
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list, gravity_constant=GRAVITY)

        for i in range(COIN_COUNT):
            
            coin = arcade.Sprite("sprites/items/PNG/shiny/1.png", SPRITE_SCALING_COIN)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)

        self.view_left = 0
        self.view_bottom = 0
        self.game_over = False


    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()

        self.coin_list.draw()
        self.player_list.draw()

        if self.last_time and self.frame_count % 60 == 0:
            fps = 1.0 /(time.time() - self.last_time) * 60
            self.fps_message = f"FPS: {fps:5.0f}"

        if self.fps_message:
            arcade.draw_text(self.fps_message, self.view_left + 10, self.view_bottom + 40, arcade.color.BLACK, 14)

        if self.frame_count % 60 == 0:
            self.last_time = time.time()

        distance = self.player_sprite.right
        arcade.draw_text(output, self.view_left +10, self.view_bottom + 20, arcade.color.BLACK, 14 )

        if self.game_over:
            arcade.draw_text("Game Over", self.view_left + 200, self.view_bottom + 200, arcade.color.BLACK, 30

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
    
    def on_update(self, delta_time):
        # Logic to move and game logic
        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
