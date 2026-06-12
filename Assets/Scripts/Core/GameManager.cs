using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace MIR.Core
{
    /// <summary>
    /// Main game manager - handles core game logic and state.
    /// </summary>
    public class GameManager
    {
        private Game game;
        private GameState currentState;
        private Vector2 playerPosition;
        private Vector2 playerVelocity;
        private const float PLAYER_SPEED = 200f;

        public enum GameState
        {
            Menu,
            Loading,
            Playing,
            Paused,
            GameOver
        }

        public GameManager(Game game)
        {
            this.game = game;
            currentState = GameState.Menu;
            playerPosition = new Vector2(640, 360);
            playerVelocity = Vector2.Zero;
        }

        public void LoadContent()
        {
            System.Console.WriteLine("Make It Rain - Loading content...");
        }

        public void Update(GameTime gameTime)
        {
            HandleInput(gameTime);
            UpdateGameState(gameTime);
        }

        private void HandleInput(GameTime gameTime)
        {
            KeyboardState keyboardState = Keyboard.GetState();

            // Player movement
            playerVelocity = Vector2.Zero;

            if (keyboardState.IsKeyDown(Keys.W))
                playerVelocity.Y -= PLAYER_SPEED;
            if (keyboardState.IsKeyDown(Keys.S))
                playerVelocity.Y += PLAYER_SPEED;
            if (keyboardState.IsKeyDown(Keys.A))
                playerVelocity.X -= PLAYER_SPEED;
            if (keyboardState.IsKeyDown(Keys.D))
                playerVelocity.X += PLAYER_SPEED;

            // Update position
            playerPosition += playerVelocity * (float)gameTime.ElapsedGameTime.TotalSeconds;

            // Clamp to screen bounds
            playerPosition.X = MathHelper.Clamp(playerPosition.X, 0, 1280 - 32);
            playerPosition.Y = MathHelper.Clamp(playerPosition.Y, 0, 720 - 32);

            // Pause with P
            if (keyboardState.IsKeyDown(Keys.P) && currentState == GameState.Playing)
                currentState = GameState.Paused;
            else if (keyboardState.IsKeyDown(Keys.P) && currentState == GameState.Paused)
                currentState = GameState.Playing;
        }

        private void UpdateGameState(GameTime gameTime)
        {
            switch (currentState)
            {
                case GameState.Menu:
                    currentState = GameState.Playing;
                    break;

                case GameState.Playing:
                    // Game logic here
                    break;

                case GameState.Paused:
                    // Pause logic
                    break;
            }
        }

        public void Draw(SpriteBatch spriteBatch, GameTime gameTime)
        {
            // Draw background
            spriteBatch.DrawString(null, "Make It Rain", new Vector2(10, 10), Color.White);
            spriteBatch.DrawString(null, $"Position: {playerPosition}", new Vector2(10, 30), Color.LimeGreen);
            spriteBatch.DrawString(null, $"State: {currentState}", new Vector2(10, 50), Color.Yellow);
            spriteBatch.DrawString(null, "WASD: Move | P: Pause | ESC: Exit", new Vector2(10, 70), Color.Cyan);

            // Draw player (simple white rectangle)
            spriteBatch.Draw(
                new Texture2D(spriteBatch.GraphicsDevice, 1, 1),
                new Rectangle((int)playerPosition.X, (int)playerPosition.Y, 32, 32),
                Color.LimeGreen
            );
        }
    }
}
