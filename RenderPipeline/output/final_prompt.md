# ==================================================
# RULES
# ==================================================

# GLOBAL RULE STACK

STATUS: GLOBAL
SCOPE: UNIVERSAL

## Purpose

Defines rule hierarchy and ownership separation
for all rendering and character systems.

---

# RULE OWNERSHIP

## Rendering Rules

Controls:

- rendering density
- lighting philosophy
- material response
- visual readability
- contrast structure

Must NOT control:

- character identity
- emotional narrative
- state behavior

---

## Character Rules

Controls:

- silhouette identity
- recognition consistency
- immutable visual traits

Must NOT control:

- rendering philosophy
- atmosphere
- scene composition

---

## State Rules

Controls:

- temporary existence mode
- posture shifts
- equipment exposure
- emotional intensity

Must NOT destroy:

- silhouette readability
- locked identity anchors

---

## Scene Rules

Controls:

- environmental composition
- spatial readability
- framing structure
- atmosphere scale

Must NOT override:

- rendering language
- character readability

---

# GLOBAL SUPPRESSION RULES

[SuppressionRules]

avoid excessive visual clutter,
avoid unreadable silhouette complexity,
avoid random cinematic effects,
avoid unnecessary decorative density,
avoid uncontrolled visual noise

---

# GLOBAL PRIORITY

[Priority]

rendering consistency > decorative rendering
character identity > temporary state
silhouette readability > surface details
large shapes > micro details
recognition stability > cinematic spectacle


# ==================================================
# RENDERING
# ==================================================

# Rendering Language

STATUS: GLOBAL
SCOPE: UNIVERSAL

## Purpose

Defines shared rendering philosophy.

This layer controls how the world is visually rendered.

---

# RENDERING

## [RenderingDensity]

low visual noise,
restrained rendering density,
controlled visual complexity,
sparse lighting accents

---

## [SurfaceLanguage]

grounded industrial materials,
matte surface response,
weathered synthetic surfaces,
soft environmental wear

---

## [ShapeLanguage]

large clean surfaces,
restrained panel lining,
readable silhouette priority,
controlled structural fragmentation

---

## [LightingLanguage]

controlled exposure,
restrained contrast,
readable facial visibility,
soft directional lighting

---

## [Destabilization]

progressive visual destabilization,
structural rendering breakdown under overload,
heat-reactive visual transformation

---

# RULES

[SuppressionRules]

avoid overexposed bloom overload,
avoid chaotic lighting contrast,
avoid excessive neon rendering,
avoid glossy plastic rendering

[Priority]

clean surfaces > mechanical noise
readability > spectacle
restrained rendering > decorative rendering


# ==================================================
# CHARACTERPATTERN
# ==================================================

# Character Pattern Structure

STATUS: GLOBAL
SCOPE: UNIVERSAL

## Purpose

Defines the universal structure
used to construct character identity.

---

# CORE

## [CoreIdentity]

Defines:

- species
- civilization role
- biological category

---

## [Silhouette]

Defines:

- body structure
- hairstyle
- outer silhouette
- long-range readability

---

## [RecognitionZone]

Defines:

- iconic structures
- recognizable accessories
- facial obstruction
- color anchors

---

## [Behavior]

Defines:

- posture tendency
- movement tendency
- body language

---

## [LockedElements]

Defines:

- immutable recognition traits

---

# STATE MODIFIER

## [EquipmentStructures]

Defines:

- attached structures
- silhouette extensions
- deployment structures

---

## [FunctionalStructure]

Defines:

- function-driven arrangement
- carried structure logic
- integrated structure balance

---

## [Presence]

Defines:

- aggression level
- intimidation level
- emotional atmosphere

---

# VISUAL SURFACE

## [Outfit]

Defines clothing only.

---

## [MechanicalParts]

Defines visible synthetic structures only.

---

## [Color]

Defines recognition-level palette only.

---

## [Details]

Defines low-priority visual details only.

---

# RULES

[SuppressionRules]

avoid random silhouette inconsistency,
avoid unreadable body proportions,
avoid excessive decorative layering

[Priority]

silhouette > details
recognition > decoration
identity stability > variation


# ==================================================
# CHARACTER
# ==================================================

# Character Core

STATUS: CHARACTER
SCOPE: IDENTITY

## Purpose

Defines immutable character identity.

This layer must remain stable across all states.

---

# CORE

## [CoreIdentity]

post-human synchronization humanoid,
salvaged cybernetic lifeform

---

## [Silhouette]

long straight black hair,
slender tall body,
oversized long coat silhouette,
thin limb structure

---

## [RecognitionZone]

hair loosely framing face,
barefoot,
oversized worn white coat,
slightly elongated worn red scarf,
visible prosthetic repair traces

---

## [Behavior]

slightly slow movement,
quiet standing posture,
low-aggression body language

---

## [LockedElements]

long black hair,
barefoot,
red scarf,
emotionally restrained presence

---

# RULES

[SuppressionRules]

avoid exaggerated anime heroine aesthetics,
avoid tactical soldier appearance,
avoid excessive visual aggression

[Priority]

silhouette > details
recognition > decoration
human warmth > mechanical intimidation


# ==================================================
# STATE
# ==================================================

# State Example - Peripheral Survival

STATUS: EXAMPLE
SCOPE: STATE MODIFIER

## Purpose

Example state layer representing
low-resource peripheral survival conditions.

This file exists as a state construction example.

---

# STATE

## [StateType]

peripheral civilian survival state

---

## [EquipmentStructures]

flat integrated repair seams,
minimal non-bulky waist fasteners

---

## [FunctionalStructure]

rough self-repair construction,
mixed salvaged prosthetic integration,
utility-oriented arrangement,
non-military structural balance,
minimal carried equipment

---

## [Presence]

quiet civilian atmosphere,
slightly tired drifter presence,
low visual aggression,
non-heroic profile

---

## [BehaviorShift]

slightly lowered shoulders,
casual idle posture,
subtle human-like movement habits

---

## [ExpressionShift]

tired eyes,
neutral expression,
soft unfocused gaze

---

## [ObjectInteraction]

arms naturally hanging at sides

---

# RULES

[SuppressionRules]

avoid clean military profile,
avoid aggressive combat readiness,
avoid excessive weapon exposure

[Priority]

civilian identity > combat identity
human fatigue > combat tension


# ==================================================
# WORLD
# ==================================================

# World Language

STATUS: GLOBAL
SCOPE: UNIVERSAL

## Purpose

Defines world structure and environmental existence.

This layer defines what kind of world exists,
independent from camera interpretation.

---

# WORLD

## [CivilizationStructure]

industrial civilization remnants,
large-scale abandoned infrastructure,
civilization-scale mechanical environments,
low population density

---

## [ArchitectureLanguage]

massive industrial structures,
weathered megastructures,
functional architecture priority,
large uninterrupted surfaces

---

## [EnvironmentalCondition]

soft environmental decay,
restrained structural damage,
aged synthetic materials,
weathered industrial surfaces

---

## [WorldDensity]

low social density,
large empty pathways,
isolated environmental spacing,
reduced civilian activity

---

## [AtmosphereBase]

quiet industrial stillness,
restrained environmental tension,
civilization exhaustion,
low emotional saturation

---

# RULES

[SuppressionRules]

avoid overdecorated environments,
avoid excessive environmental clutter,
avoid random cinematic destruction,
avoid dense visual chaos

[Priority]

world readability > environmental detail
large structures > micro clutter
environment supports subject readability


# ==================================================
# CAMERA
# ==================================================

# Camera Language

STATUS: GLOBAL
SCOPE: UNIVERSAL

## Purpose

Defines how the scene is visually observed.

This layer controls:

- framing interpretation
- emotional viewing distance
- cinematic pressure
- perspective behavior

This layer does NOT define:

- world structure
- character identity

---

# CAMERA

## [FramingLanguage]

wide framing,
distant observational perspective,
stable horizontal framing,
restrained cinematic motion

---

## [PerspectiveBehavior]

controlled perspective distortion,
low-aggression camera angle,
natural spatial compression,
stable environmental readability

---

## [EmotionalDistance]

reduced emotional intimacy,
quiet observational framing,
detached cinematic presence

---

## [MotionBehavior]

minimal camera shake,
restrained dynamic movement,
stable visual tracking,
controlled motion readability

---

## [FocusControl]

primary focus on silhouette readability,
controlled environmental focus falloff,
stable subject hierarchy

---

# RULES

[SuppressionRules]

avoid extreme fisheye distortion,
avoid hyper-dynamic action framing,
avoid aggressive cinematic shake,
avoid exaggerated heroic angles

[Priority]

subject readability > cinematic intensity
stable framing > chaotic motion
observational perspective > emotional spectacle


# ==================================================
# SCENE
# ==================================================

# Scene Composition

STATUS: GLOBAL
SCOPE: UNIVERSAL

## Purpose

Defines spatial composition inside the current frame.

This layer controls spatial arrangement,
not world identity.

---

# SCENE

## [SpatialComposition]

large negative space,
isolated character framing,
controlled subject spacing,
stable silhouette readability

---

## [ForegroundStructure]

minimal foreground obstruction,
restrained environmental layering,
clean subject separation

---

## [DepthStructure]

controlled depth readability,
layered industrial depth,
soft atmospheric separation

---

## [SubjectPlacement]

off-center subject positioning,
environmental isolation emphasis,
large surrounding empty space

---

## [VisualBalance]

environment supports silhouette,
stable visual hierarchy,
controlled environmental dominance

---

# RULES

[SuppressionRules]

avoid chaotic composition,
avoid subject obstruction,
avoid excessive foreground clutter,
avoid unstable frame balance

[Priority]

subject readability > environmental density
negative space > clutter
silhouette clarity > cinematic spectacle


# ==================================================
# MERGED GLOBAL RULES
# ==================================================

[SuppressionRules]
avoid excessive visual clutter,
avoid unreadable silhouette complexity,
avoid random cinematic effects,
avoid unnecessary decorative density,
avoid uncontrolled visual noise
---
# GLOBAL PRIORITY
avoid overexposed bloom overload,
avoid chaotic lighting contrast,
avoid excessive neon rendering,
avoid glossy plastic rendering
avoid random silhouette inconsistency,
avoid unreadable body proportions,
avoid excessive decorative layering
avoid exaggerated anime heroine aesthetics,
avoid tactical soldier appearance,
avoid excessive visual aggression
avoid clean military profile,
avoid aggressive combat readiness,
avoid excessive weapon exposure
avoid overdecorated environments,
avoid excessive environmental clutter,
avoid random cinematic destruction,
avoid dense visual chaos
avoid extreme fisheye distortion,
avoid hyper-dynamic action framing,
avoid aggressive cinematic shake,
avoid exaggerated heroic angles
avoid chaotic composition,
avoid subject obstruction,
avoid excessive foreground clutter,
avoid unstable frame balance

[Priority]
rendering consistency > decorative rendering
character identity > temporary state
silhouette readability > surface details
large shapes > micro details
recognition stability > cinematic spectacle
clean surfaces > mechanical noise
readability > spectacle
restrained rendering > decorative rendering
silhouette > details
recognition > decoration
identity stability > variation
human warmth > mechanical intimidation
civilian identity > combat identity
human fatigue > combat tension
world readability > environmental detail
large structures > micro clutter
environment supports subject readability
subject readability > cinematic intensity
stable framing > chaotic motion
observational perspective > emotional spectacle
subject readability > environmental density
negative space > clutter
silhouette clarity > cinematic spectacle
