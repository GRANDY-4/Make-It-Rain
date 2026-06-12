# Development Guide

## Setup Instructions

### Prerequisites
- Unity 2022 LTS or newer
- Visual Studio 2022 or JetBrains Rider
- Git

### Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/GRANDY-4/Make-It-Rain.git
   cd Make-It-Rain
   ```

2. Open the project in Unity

3. The project structure is already organized — start developing!

## Code Organization

### Namespaces
All scripts are organized by namespace:
- `MIR.Core` — Core game systems (GameManager)
- `MIR.Player` — Player-related scripts
- `MIR.UI` — User interface
- `MIR.Utilities` — Helper functions and constants

### Naming Conventions
- **Classes:** PascalCase (e.g., `GameManager`)
- **Methods:** PascalCase (e.g., `HandleInput()`)
- **Variables:** camelCase (e.g., `moveSpeed`)
- **Constants:** UPPER_SNAKE_CASE (e.g., `TAG_PLAYER`)
- **Private fields:** camelCase with leading underscore (e.g., `_moveDirection`)

### File Organization
- One class per file
- File name matches class name
- Place files in appropriate folders under `Assets/Scripts/`

## Scene Structure

The main scene (`Main.unity`) contains:
- **GameManager** — Core game controller
- **Player** — Player character with PlayerController and CharacterController
- **Camera** — Main camera (child of Player)
- **Canvas** — UI root

## Next Steps

1. Extend the `PlayerController` with:
   - Jump mechanics
   - Sprint ability
   - Animation integration

2. Add camera controller:
   - Third-person follow camera
   - Mouse look controls

3. Create basic mission system:
   - Mission data structure
   - Mission briefing UI
   - Objective tracking

4. Implement enemy AI:
   - Patrol behavior
   - Detection system
   - Combat mechanics

## Tips

- Use the `Debug.Log()` calls throughout to track execution
- Keep systems modular — each manager should handle one responsibility
- Use serialized fields for tuning values without recompiling
- Test frequently in the editor

## Resources

- [Unity Documentation](https://docs.unity3d.com/)
- [C# Best Practices](https://learn.microsoft.com/en-us/dotnet/csharp/)
- [Payday 2 Game Design](https://en.wikipedia.org/wiki/Payday_2)
