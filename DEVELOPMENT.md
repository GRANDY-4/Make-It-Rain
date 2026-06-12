# Development Guide - MonoGame

## Setup Instructions

### Prerequisites
- **MonoGame SDK 3.8.1+**
- **Visual Studio 2022** or **VS Code**
- **.NET 6.0 or later**

### Installation

1. Install MonoGame tools:
   ```bash
   dotnet tool install -g MonoGame.Content.Builder.Task
   dotnet new install MonoGame.Templates
   ```

2. Create project:
   ```bash
   dotnet new mgdesktopgl -n MakeItRain
   cd MakeItRain
   ```

3. Clone this repo content into the project

4. Build and run:
   ```bash
   dotnet build
   dotnet run
   ```

## MonoGame Game Loop

MonoGame uses a classic game loop pattern:

```csharp
protected override void Update(GameTime gameTime)
{
    // Handle input
    // Update game logic
    // Physics calculations
}

protected override void Draw(GameTime gameTime)
{
    // Clear screen
    // Draw all sprites
    // Render UI
}
```

## Code Organization

### Namespaces
- `MIR.Core` — Core game systems (GameManager, SceneManager)
- `MIR.Player` — Player-related code
- `MIR.UI` — UI rendering and management
- `MIR.Utilities` — Constants and helpers
- `MIR.Entities` — Game entities (enemies, NPCs, etc.)

### Key Classes

**Game.cs**
- Entry point for MonoGame
- Manages graphics device
- Calls GameManager Update/Draw

**GameManager.cs**
- Core game logic
- Game state management
- Input handling
- Update/Draw delegation

**GameState Enum**
- Menu
- Loading
- Playing
- Paused
- GameOver

## Input Handling

```csharp
KeyboardState keyboardState = Keyboard.GetState();
GamePadState gamePadState = GamePad.GetState(PlayerIndex.One);

if (keyboardState.IsKeyDown(Keys.W))
{
    // Move forward
}
```

## Drawing Sprites

```csharp
// Draw a sprite from a texture
spriteBatch.Draw(texture, position, Color.White);

// Draw a colored rectangle
spriteBatch.Draw(
    pixelTexture,
    new Rectangle(x, y, width, height),
    Color.Red
);
```

## Content Pipeline

Place assets in `Content/` folder:
- Textures in `Content/Textures/`
- Audio in `Content/Audio/`
- Fonts in `Content/Fonts/`

Load in `LoadContent()`:
```csharp
var texture = Content.Load<Texture2D>("Textures/player");
```

## Running the Game

```bash
dotnet run
```

Controls:
- **WASD** — Move player
- **P** — Pause/Resume
- **ESC** — Exit

## Next Steps

1. Add sprite loading from textures
2. Implement basic collision detection
3. Add enemy entities
4. Create mission system
5. Build UI framework
6. Add audio system

## Resources

- [MonoGame Documentation](http://www.monogame.net/documentation/)
- [MonoGame Tutorials](https://docs.monogame.net/articles/getting_started.html)
- [XNA Framework Guide](https://learn.microsoft.com/en-us/windows/win32/direct3d9/xna-framework)
