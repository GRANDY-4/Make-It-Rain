# Make It Rain (MIR) - MonoGame

A Payday-like heist game built with **C# and MonoGame**.

## Project Overview

MIR is a cooperative heist game where players plan and execute high-stakes robberies. Built from scratch using MonoGame for cross-platform support.

## Prerequisites

- **MonoGame SDK** 3.8.1 or later
- **Visual Studio 2022** or **Visual Studio Code**
- **.NET 6.0 or later**

## Project Structure

```
Make-It-Rain/
├── MakeItRain/                   # Main game project
│   ├── Content/                  # Game assets (textures, sounds, fonts)
│   │   ├── Textures/
│   │   ├── Audio/
│   │   └── Fonts/
│   ├── Source/
│   │   ├── Core/                 # Core game systems
│   │   ├── Player/               # Player-related code
│   │   ├── UI/                   # UI management
│   │   ├── Managers/             # Game managers
│   │   ├── Utilities/            # Helpers and constants
│   │   ├── Scenes/               # Scene management
│   │   └── Game.cs               # Main game class
│   ├── MakeItRain.csproj
│   └── Program.cs
├── README.md
└── DEVELOPMENT.md
```

## Getting Started

### 1. Install MonoGame

```bash
dotnet tool install -g MonoGame.Content.Builder.Task
dotnet new install MonoGame.Templates
```

### 2. Create the Project

```bash
dotnet new mgdesktopgl -n MakeItRain
cd MakeItRain
```

### 3. Build and Run

```bash
dotnet build
dotnet run
```

## Architecture

- **Game.cs** — Main game loop (Update/Draw cycle)
- **GameManager.cs** — Core game state and initialization
- **PlayerController.cs** — Player input and movement
- **SceneManager.cs** — Scene loading and management
- **UIManager.cs** — UI rendering and management

## Development

See `DEVELOPMENT.md` for coding conventions, best practices, and architecture guidelines.

---

**Status:** Early Development - MonoGame Setup
