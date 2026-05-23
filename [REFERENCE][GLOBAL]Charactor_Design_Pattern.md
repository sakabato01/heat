STATUS: ARCHIVE
SCOPE: GLOBAL
DO NOT USE AS REFERENCE

# Charactor Design Pattern

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

# STATE MODIFIER
# 武器結構
---

## [EquipmentStructures]

# 武器結構
# 描述武器本體的外觀與附著方式
# 著重：
# - 展開結構
# - 附著位置
# - silhouette變化
# - 身體延伸感
# 避免抽象設定詞

例如：

integrated tail-like appendage,
folded blade housing,
back-mounted synchronization structures,
concealed deployment mechanisms,
extended rear silhouette

---

## [WeaponFunction]

# 功能導致的結構傾向
# 不描述世界觀設定
# 只描述功能造成的可視化結果

例如：

body-integrated deployment,
minimal external carrying,
compact standby construction,
integrated utility-oriented structure,
low-profile mechanical arrangement

---

## [WeaponPresence]

# 武器存在感
# 描述武器給人的視覺印象與威脅感
# 用來控制：
# - 侵略性
# - 軍武感
# - 武器辨識度
# - 情緒氛圍

例如：

low visual aggression,
concealed weapon presence,
non-military profile,
tool-like appearance,
minimal combat emphasis

---

# VISUAL SURFACE
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