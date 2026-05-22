STATUS: REFERENCE
SCOPE: GLOBAL
# CORE
# 不可改動

## [CoreIdentity]

# 角色類型

例如：

synchronization civilization humanoid

---

## [Silhouette]

# 遠距輪廓

描述：
- 髮型
- 體型
- 外輪廓

例如：

long black hair,
slender body,
long coat silhouette

---

## [RecognitionZone]

# 高辨識區

描述：
- 臉部遮擋
- 特殊肢體
- 特殊服裝
- 特殊配色

例如：

hair covering one eye,
white joints,
barefoot

---

## [Behavior]

# 基本動作傾向

例如：

still posture,
low movement,
forward-facing stance

---

## [LockedElements]

# 永遠固定

例如：

black hair
white body
barefoot

---

# FLEX
# 可改動

## [Outfit]

# 外層服裝

例如：

white formalwear,
industrial coat

---

## [MechanicalParts]

# 義體／機械區域

例如：

visible joints,
synthetic limbs

---

## [Material]

# 材質

例如：

matte ceramic,
industrial fabric

---

## [Color]

# 配色

例如：

off-white,
black,
muted red accents

---

## [Details]

# 低優先細節

例如：

scratches,
repair marks,
panel lining

---

## [Environment]

# 背景

例如：

industrial interior,
rainy city,
neutral background

---

## [Lighting]

# 光影

例如：

soft lighting,
low contrast,
industrial lighting

---

# RULES

## [SuppressionRules]

# 避免生成方向

例如：

avoid tactical soldier
avoid idol aesthetics
avoid heavy mechanical density

---

## [Priority]

# 優先順序

例如：

silhouette > details
shape > rendering
clean surfaces > noise

---

# 刪減原則

當prompt過長時：

先刪：
- Environment
- Lighting
- Details

最後才刪：
- Silhouette
- RecognitionZone
- LockedElements