# HEAT Character Scale Specification

This specification defines the standard proportions for all playable characters in HEAT.

These rules are mandatory unless explicitly overridden by the design document.

---

# Character Height

Character body height
(excluding weapons, effects, cloth physics and floating accessories)

**108 px**

This height is fixed for all standard humanoid playable characters.

---

# Visual Head Mass

Visual head height is measured from:

- highest visible hair pixel
- to lowest chin pixel

Hair, bangs and fixed head ornaments are included.

Target height:

**15 px**

Allowed range:

**14–16 px**

The visual head mass should remain compact.

Hair volume should expand primarily sideways rather than upward whenever possible.

Large hairstyles must preserve the intended visual head proportion.

---

# Body Proportion

Target proportion:

- Head Mass : **~14%**
- Upper Body : **~30%**
- Lower Body : **~70%**

Recommended values:

| Section | Height |
|---------|--------|
| Visual Head | 15 px |
| Upper Body | 32 px |
| Lower Body | 76 px |

The upper body is measured from the bottom of the chin to the crotch / pelvis.

The lower body is measured from pelvis to the bottom of the feet.

---

# Pelvis Position

The pelvis should appear visually high.

Characters should present:

- long legs
- short torso
- mature adult proportions

Do not lower the pelvis to compensate for clothing.

---

# Arm Length

Approximate arm length:

**40 px**

When standing naturally:

- fingertips should reach the upper thigh
- arms should never appear disproportionately short relative to the legs

---

# Clothing Rules

Costume design must not significantly alter perceived body proportion.

Avoid:

- oversized skirts that visually lower the pelvis
- excessively long jackets that hide waist position
- hairstyles that excessively increase visual head height

Preferred solutions:

- raise waistline
- shorten torso silhouette
- emphasize leg length
- expand silhouettes horizontally instead of vertically

---

# Gameplay Readability

Character readability has higher priority than anatomical accuracy.

Silhouette should primarily be recognizable through:

- weapon
- pose
- body movement
- costume silhouette

rather than facial detail.

---

# Pixel Density Philosophy

HEAT prioritizes gameplay readability over illustration fidelity.

Character personality should remain recognizable even under limited pixel density.

Higher-resolution illustrations may contain additional detail, but must preserve this proportion system.

---

# Validation Checklist

Every playable character should satisfy:

✓ Hero Art preserves intended character proportion and personality.

✓ Scale Reference matches Hero Art body proportion.

✓ Recognizable silhouette at gameplay scale.

✓ Visual head mass within specification.

✓ Mature adult body proportion.

✓ Clear pelvis position.

✓ Long readable legs.

✓ Weapon silhouette remains dominant.

✓ Standing, running and attacking animations preserve overall proportion.

✓ Runtime states preserve character readability and body proportion.