# Pipeline_Use_Guide.md

STATUS: GLOBAL
SCOPE: UNIVERSAL

---

# 1. Purpose

This pipeline is designed to construct modular visual generation systems.

Instead of writing one massive prompt,
the system separates visual generation into independent layers.

The final prompt is assembled automatically through a stack structure.

---

# 2. Core Philosophy

The pipeline separates:

- rendering philosophy
- world existence
- character identity
- temporary states
- camera interpretation
- scene composition
- global rules

This prevents visual contamination between systems.

---

# 3. Pipeline Structure

```text
Global Rules
    ↓
Rendering
    ↓
World
    ↓
Character Pattern
    ↓
Character Core
    ↓
State
    ↓
Camera
    ↓
Scene Composition
    ↓
Final Prompt
```

---

# 4. Recommended Folder Structure

```text
project/
│
├── universal_prompt_stack_assembler.py
├── active_stack.md
│
├── output/
│   └── final_prompt.md
│
└── modules/
    │
    ├── rules/
    │   └── [HEAT3]Global_Rule_Stack.md
    │
    ├── rendering/
    │   └── [HEAT3]Base_Rendering.md
    │
    ├── worlds/
    │   └── [HEAT3]World_Language.md
    │
    ├── character_patterns/
    │   └── [HEAT3]Character_Pattern.md
    │
    ├── characters/
    │   └── [HEAT3]Heroine_Core.md
    │
    ├── states/
    │   └── [HEAT3]Peripheral_Survival_State.md
    │
    ├── camera/
    │   └── [HEAT3]Camera_Language.md
    │
    └── scenes/
        └── [HEAT3]Scene_Composition.md
```

---

# 5. Naming Convention

Recommended format:

```text
[Universe]Module_Name.md
```

---

# 6. Layer Responsibilities

## Rendering

Defines how the world is visually rendered.

Controls:

- lighting behavior
- material response
- visual density
- shape readability

---

## World

Defines what kind of world exists.

Controls:

- civilization structure
- architecture identity
- environmental conditions

---

## Character Core

Defines immutable identity.

Controls:

- silhouette
- recognition
- iconic visual features

---

## State

Defines temporary existence condition.

Controls:

- posture
- emotional intensity
- current condition

---

## Camera

Defines how the world is observed.

Controls:

- framing
- perspective
- emotional viewing distance

---

## Scene Composition

Defines spatial arrangement inside the frame.

Controls:

- negative space
- subject placement
- environmental balance

---

# 7. Responsibility Separation Philosophy

Each layer should control only one primary responsibility.

This prevents:

- rendering contamination
- identity drift
- cinematic override
- scene clutter collapse

---

# 8. Reusable Layer Structure

One world can support multiple cameras
and multiple scene compositions.

Example:

```text
Industrial_Periphery_World
    +
Lonely_Distant_Camera
    +
Open_Empty_Composition
```

creates quiet isolation atmosphere.

---

# 9. active_stack.md Example

```md
Rules:
[HEAT3]Global_Rule_Stack

Rendering:
[HEAT3]Base_Rendering

World:
[HEAT3]World_Language

CharacterPattern:
[HEAT3]Character_Pattern

Character:
[HEAT3]Heroine_Core

State:
[HEAT3]Peripheral_Survival_State

Camera:
[HEAT3]Camera_Language

Scene:
[HEAT3]Scene_Composition
```

---

# 10. Generation Workflow

## Step 1

Edit active_stack.md

## Step 2

Run:

```bash
python universal_prompt_stack_assembler.py
```

## Step 3

Open:

```text
output/final_prompt.md
```

---

# 11. Common Errors

## Module Not Found

Wrong module name or missing md file.

## Invalid Stack Format

Incorrect:

```md
Rendering
Base_Rendering
```

Correct:

```md
Rendering:
Base_Rendering
```

---

# 12. Long-Term Expansion

Future systems may include:

- Motion Layer
- Interaction Layer
- Focus Layer
- Stability Layers

---

# 13. Long-Term Philosophy

The goal is not a collection of prompts.

The goal is a modular visual generation framework.
