# Getting started.

[Click here for the link to the repository following this guide.](https://github.com/that1guy232/Treengine_GettinStarted)


This guide will help you get started with Treengine. It will cover the basics of the engine and how to use it to create a simple window

Are entry point will be the main.py file. This is where we will create our game instance and start the game loop.


### Main.py
```python

 '''
    First thing we need to do is import TreeGame from Treengine.Game.TreGame
    
    This instance will be used to create our game window and start the game loop
   
    It will also be used to manage our Game Scenes
    (If no scenes are added, the game will create a empty scene with nothing in it. More on this later)


 '''
from Treengine.Game.TreGame import TreeGame

def main():
    '''
        Create a new instance of TreeGame
        This will create a new window and start the game loop
    '''
    game = TreeGame()
    '''
        Start the game loop
        This will run until the game is closed
    '''
    game.run()
    pass

if __name__ == "__main__":
    main()
```

Now we have a window, but it's empty.

Let's add a scene to it.
Scenes are your game's levels. They can be menus, levels or just a splash screen. These will hold all of your game's entities and components and logic.

First let's create a main menu scene, we will call it MainMenuScene.py and place it inside a scenes folder and inside of it's own folder called MainMenuScene.
(This is just a convention, you can name your folders and files however you want, but it's recommended to keep things organized. I also plan on creating a editor to help with this among other things)

### MainMenuScene.py
```python
'''
    Fist thing, We import the GameScene class from Treengine.Game.GameScene
'''

from Treengine.Game.GameScene import GameScene

'''
    Next we create a class that inherits from GameScene
    This will allow us to create a new scene and add it to our game
'''

class MainMenuScene(GameScene):

    def __init__(self):

        super().__init__()

        pass

    def on_enter(self):
        super().on_enter()
        pass

    def on_exit(self):
        super().on_exit()
        pass

    def update(self, delta_time):
        super().update(delta_time)
        pass

    def draw(self, screen):
        super().render(screen)
        pass

    def handle_events(self, events):
        super().handle_events(events)
        pass

```

```