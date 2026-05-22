STATUS: REFERENCE
SCOPE: GLOBAL

# UI CORE
# 不可改動
# 用來固定UI辨識與資訊結構

## [CoreIdentity]

# UI類型
# 明確描述：
# - combat UI
# - synchronization monitor
# - industrial HUD
# - analog gauge system
# - civilian terminal
# 避免抽象形容詞

例如：

shared heat synchronization monitor

或：

industrial analog combat interface

---

## [UIScreenRole]

# UI在畫面中的角色
# 控制：
# - 主UI
# - 次UI
# - 常駐UI
# - 戰鬥核心UI
# - 背景型UI

例如：

primary combat-state interface,
shared team-status monitor

---

## [Silhouette]

# UI大輪廓
# 優先級最高
# 描述：
# - gauge形狀
# - UI配置
# - 重心
# - 主結構

例如：

asymmetrical half-circle dial,
bottom-centered layout,
single dominant gauge silhouette

---

## [RecognitionZone]

# 高辨識區
# 玩家第一眼會看的區域

描述：
# - 指針
# - Crash區
# - Heat區
# - HP條
# - 中央焦點

例如：

central needle structure,
heat threshold sector,
stable bottom HP line

---

## [LockedElements]

# 永遠固定
# 即使狀態改變也不可消失

例如：

shared heat dial,
analog needle behavior,
horizontal HP structure

---

# INFORMATION STRUCTURE
# 資訊結構

## [InformationHierarchy]

# UI資訊優先順序

例如：

heat state > crash risk > HP readability > secondary effects

---

## [PrimaryInformation]

# 必須優先被讀取的資訊

例如：

current heat level,
crash threshold proximity,
active synchronization pressure

---

## [SecondaryInformation]

# 次要資訊
# 可弱化存在感

例如：

minor distortion effects,
background synchronization noise,
passive monitoring markers

---

## [ReadabilityRules]

# 可讀性規則

例如：

maintain HP readability during high heat,
avoid excessive overlay density,
preserve needle visibility during distortion

---

# MOTION SYSTEM
# 動態規則

## [MotionBehavior]

# UI平時動態傾向

例如：

slow idle movement,
minimal low-heat motion,
stable resting state

---

## [MotionPriority]

# 哪些動態優先存在

例如：

needle movement prioritized,
HP motion minimized,
background motion suppressed

---

## [StateTransition]

# 狀態轉換節奏

例如：

stable low-heat presentation,
gradual instability escalation,
abrupt crash desynchronization

---

## [DistortionBehavior]

# Heat導致的UI變化
# 分階段描述

例如：

low heat:
minimal distortion

mid heat:
minor phosphor instability,
subtle scanline persistence

high heat:
needle vibration,
segment instability,
analog ghosting

crash:
gauge desynchronization,
partial UI failure,
temporary signal collapse

---

# VISUAL SURFACE
# 可改動視覺層

## [Material]

# UI材質感

例如：

faded industrial coating,
CRT phosphor glow,
matte ceramic interface surface

---

## [Color]

# 配色

例如：

off-white,
dim amber,
phosphor green,
thermal orange accents

---

## [Lighting]

# UI發光規則

例如：

restrained glow,
localized heat illumination,
minimal idle lighting

---

## [Details]

# 低優先細節

例如：

signal scratches,
panel segmentation,
monitor burn-in artifacts,
industrial calibration markings

---

# SCREEN PRESENCE
# 畫面侵入性

## [InterfacePresence]

# UI存在感

控制：
# - 是否搶畫面
# - 是否干擾角色
# - 是否具有壓迫感

例如：

low idle visual dominance,
high-heat pressure amplification,
minimal low-state intrusion

---

## [ScreenInteraction]

# UI與畫面互動方式

例如：

heat distortion slightly affecting screen edges,
crash instability interrupting interface stability,
UI remaining spatially anchored during combat

---

# RULES

## [SuppressionRules]

# 避免生成方向

例如：

avoid racing-game aesthetics,
avoid esports HUD styling,
avoid holographic overload,
avoid excessive mechanical density,
avoid neon cyberpunk interface language

---

## [Priority]

# 視覺優先順序

例如：

information clarity > decoration
silhouette > rendering
motion readability > visual noise
heat readability > effects

---

# REDUCTION ORDER

當 prompt 過長時：

先刪：
- Details
- Lighting
- SecondaryInformation

再刪：
- Material
- Color

最後才刪：
- Silhouette
- RecognitionZone
- InformationHierarchy
- LockedElements
- ReadabilityRules