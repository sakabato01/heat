# Universal Prompt Stack Pipeline Guide

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
- character identity
- temporary states
- scene composition
- global rules

This prevents visual contamination between systems.

Example:

Character identity should NOT control:

- lighting
- rendering density
- scene atmosphere

State systems should NOT destroy:

- silhouette readability
- recognition consistency

Rendering systems should NOT redefine:

- character personality
- posture identity

---

# 3. Pipeline Structure

The generation pipeline:

Global Rules
    ↓
Rendering
    ↓
Character Pattern
    ↓
Character Core
    ↓
State
    ↓
Scene
    ↓
Final Prompt

# 4. Recommended Folder Structure

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
    │   ├── [HEAT3]Base_Rendering.md
    │   ├── [HEAT3]Collapse_Rendering.md
    │   └── [HEAT3]Overheat_Rendering.md
    │
    ├── character_patterns/
    │   └── [HEAT3]Character_Pattern.md
    │
    ├── characters/
    │   ├── [HEAT3]Heroine_Core.md
    │   ├── [HEAT3]Operator_Core.md
    │   └── [HEAT3]Civilian_Core.md
    │
    ├── states/
    │   ├── [HEAT3]Peripheral_Survival_State.md
    │   ├── [HEAT3]Central_Synchronization_State.md
    │   └── [HEAT3]Combat_Overheat_State.md
    │
    └── scenes/
        ├── [HEAT3]Industrial_Periphery_Scene.md
        └── [HEAT3]Flooded_Megastructure_Scene.md
        
# 5. Naming Convention

Recommended format:

[Universe]Module_Name.md

Example:

- [HEAT3]Base_Rendering.md
- [HEAT3]Heroine_Core.md
- [HEAT3]Peripheral_Survival_State.md

# 6. Module Responsibilities

Global Rules

Controls:

- generation hierarchy
- suppression ownership
- cross-layer consistency

Must NOT define:

- character identity
- rendering details
Rendering

Controls:

- rendering philosophy
- lighting structure
- material response
- visual density

Must NOT define:

- personality
- emotional narrative
Character Pattern

Defines:

- universal character construction structure

Used as:

- character blueprint template
Character Core

Defines:

- immutable identity
- silhouette
- recognition zones
- locked elements

Must remain stable across all states.

State

Defines:

- temporary existence condition
- posture shifts
- equipment exposure
- emotional intensity

Example:

- civilian survival state
- synchronization state
- overload state

Only one major state should be active at once.

Scene

Defines:

- environmental composition
- spatial readability
- atmosphere framing

Must NOT override:

- rendering language
- character readability

# 7. active_stack.md

The stack file defines which modules are currently active.

Example:

- Rules: [HEAT3]Global_Rule_Stack
- Rendering: [HEAT3]Base_Rendering
- CharacterPattern: [HEAT3]Character_Pattern
- Character: [HEAT3]Heroine_Core
- State: [HEAT3]Peripheral_Survival_State
- Scene: [HEAT3]Industrial_Periphery_Scene

# 8. Generation Workflow

- Step 1

Edit:

- active_stack.md

Select:

- rendering
- character
- state
- scene

- Step 2

Run assembler:

- python universal_prompt_stack_assembler.py

- Step 3

Assembler automatically:

- loads modules
- merges rules
- removes duplicate rules
- builds final prompt

- Step 4

Generated output:

- output/final_prompt.md

- Step 5

Copy final_prompt.md content into:

- Flux
- SDXL
- ComfyUI
- Midjourney
- NAI
- other image models

Generate character image.

# 9. Rule Hierarchy

Recommended hierarchy:

- Global Rules
- Rendering
- Character
- State
- Scene

Reason:

- rendering consistency must remain stable
- state must not destroy character identity
- scene must support silhouette readability

# 10. Recommended State Usage

Recommended:

- 1 Character Core
- 1 Major State
- 1 Scene
- 1 Rendering

Avoid:

- Multiple conflicting major states

Example of bad usage:

- Peripheral survival state
- Central synchronization state
- Heavy combat state

loaded simultaneously.

This causes identity conflicts.

# 11. Recommended Expansion Structure

Future systems may include:

- Additional Rendering Systems
- Collapse_Rendering
- Memory_Rendering
- Overheat_Rendering
- Additional States
- Wet_State
- Injured_State
- Heat_Level_3_State
- Synchronization_Collapse_State
- Additional Scenes
- Flooded_City_Scene
- Underground_Factory_Scene
- Civilization_Core_Scene

# 12. Common Errors

Module Not Found

Cause:

- wrong module name
- missing md file
- Invalid Stack Format

Incorrect:

- Rendering
- Base_Rendering

Correct:

Rendering:
- Base_Rendering
- Rule Collision

Example:

Rendering prefers:

clean surfaces

while State prefers:

heavy mechanical density

This may create unstable outputs.

# 13. Long-Term Philosophy

This system is not intended to be:

a collection of prompts

The goal is:

a modular visual generation framework

The pipeline should support:

multiple universes
multiple characters
interchangeable states
interchangeable rendering systems
scalable visual architecture