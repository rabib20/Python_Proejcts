
# 🏓 Python Pong

A classic two-player Pong game built with Python's `turtle` module. No external dependencies, no fuss — just clone it and play.

## Demo

![Pong gameplay demo](images/pong_game.gif)

## How to Play

Just run:

```bash
python Pong_Game.py
```

Two players, one keyboard:

| Player | Paddle | Left | Right |
|--------|--------|------|-------|
| Player 1 | Bottom paddle | `A` | `D` |
| Player 2 | Top paddle | `←` | `→` |

Hit `Esc` whenever you want to quit.

The ball bounces off the side walls, and every time it hits a paddle it speeds up a bit — so rallies get more chaotic the longer they go. Miss it on your side and the other player scores a point.

## Features

- Local two-player multiplayer
- Live scoreboard that updates as you play
- Ball speeds up with every paddle hit
- Simple, clean `turtle`-based graphics

## Requirements

- Python 3.x
- `turtle` (comes built into Python, nothing to install)

> On some Linux setups, `tkinter` isn't installed by default and `turtle` needs it. If you hit an import error:
> ```bash
> sudo apt-get install python3-tk
> ```

## What I Learned Building This

This was a fun one to build the logic out for. A few things that stood out:

- **Structuring it with classes** — splitting the game into `Ball`, `Paddle`, and `Scoreboard` classes made the code way easier to reason about than cramming everything into one script. Each piece just handles its own state.
- **`turtle` has its own quirks** — it's not built for games, so getting smooth-ish movement and redraws to behave took some trial and error (lots of help from `screen.tracer(0)` and manual `screen.update()` calls).
- **Keyboard input isn't as simple as "key pressed"** — using `onkeypress`/`onkeyrelease` to track movement state (instead of just moving on a single keypress) was the trick to getting continuous, smooth paddle movement instead of jerky single steps.
- **Collision detection by distance** — checking `distance()` between the ball and paddle instead of pixel-perfect rectangle collision was a simpler approach, though it's a bit forgiving/imprecise compared to "real" collision detection.
- **The game loop timing matters a lot** — getting the `time.sleep()` delay and ball speed increments balanced took some tweaking to keep the game playable instead of either too slow or instantly unplayable after a few hits.

## License

This project is open source and available for learning purposes. Feel free to fork and modify it.
