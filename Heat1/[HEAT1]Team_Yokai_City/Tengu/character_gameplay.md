STATUS: CHARACTER
SCOPE: HEAT1

---

# Gameplay Design

## 角色系統

切換不同架式風格進行戰鬥

* 居合架式下為中距離居合斬擊
* 持刀架式下為近距離持刀斬擊

---

## 普通攻擊

### ←/N/→ + X

持刀架式:

- X1: 單手中段突刺 (Hit:2)
- X2: 單手下段交叉二連斬 (Hit:2)
- X3: 單手上段交叉連斬 (Hit:3)
- X4: 雙手上撈重斬 (Hit:1)
- X5: 雙手袈裟重斬 (Hit:1, Knockback)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 ~ X3 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * ↑ + X
  * ↓ + X
  * Jump
  * Dash(高HT限定)

居合架式:

- X1: 拔刀下段交叉斬 (Hit:2)
- X2: 拔刀下段往復斬 (Hit:2)
- X3: 拔刀上段重斬(Hit:1)
- X4: 拔刀中段旋身重斬 (Hit:1, Knockback)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 ~ X3 Recovery 允許以下 cancel
  * ↑ + X
  * ↓ + X
  * Dash (高HT限定)

---

### ↑ + X

持刀架式:

- X1: 單手轉身上撈斬 (Hit:2, +Aerial:Enemy)
- X2: 單手上撈跳重斬(Hit:1, +Aerial:Character/Enemy)

* OnHit: X1, X2 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * Jump
  * Dash (高HT限定)

居合架式:

- X1: 拔刀下段上撈重斬 (Hit:1, +Aerial:Enemy)

* OnHit: X1 Recovery 允許以下 cancel
  * Dash (高HT限定)

---

### ↓ + X

持刀架式:

- X1: 單手下段轉身二連斬 (Hit:2, +Aerial:Enemy)
- X2: 單手上段重斬 (Hit:1, -Aerial:Enemy)

* OnHit: X1, X2 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * Jump
  * Dash (高HT限定)

居合架式:

- X1: 拔刀上段重斬 (Hit:1, -Aerial:Enemy)

* OnHit: X1 Recovery 允許以下 cancel
  * Dash (高HT限定)

---

## 特殊攻擊

### ←/N/→ + Y

- Y1: 前方拔刀劍氣斬擊 (Hit:2, Projectile)並切換架式

* OnHit: Y1 Recovery 允許以下cancel
  * ←/N/→ + X

---

### ↑ + Y

- Y1: 前上方拔刀劍氣斬擊 (Hit:2, Projectile)並切換架式

* OnHit: Y1 Recovery 允許以下cancel
  * ←/N/→ + X

---

## 跳躍攻擊

### Jump ←/N/→ + X

持刀架式:

- X1: 單手下段交叉二連斬 (Hit:2)
- X2: 單手上段斜斬 (Hit:1)
- X3: 單手下劈落地斬 (Hit:1, -Aerial:Character/Enemy)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery 允許以下 cancel
  * Jump ←/N/→ + Y
  * Jump ↑ + Y
  * Jump ↓ + Y
  * Jump ↑ + X
  * Jump ↓ + X
  * Jump
  * Dash (高HT限定)

居合架式:

- X1: 拔刀中段水平二連橫斬 (Hit:2)
- X2: 拔刀下劈落地重斬 (Hit:1, -Aerial:Character/Enemy)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 Recovery 允許以下 cancel
  * Jump ↑ + X
  * Jump ↓ + X
  * Dash (高HT限定)

---

### Jump ↑ + X

持刀架式:

- X1: 單手下段二連上撈斬 (Hit:2, +Aerial:Enemy)

* OnHit: X1 Recovery 允許以下 cancel
  * Jump ←/N/→ + Y
  * Jump ↑ + Y
  * Jump ↓ + Y
  * Jump
  * Dash (高HT限定)

居合架式:

- X1: 拔刀上撈轉身重斬 (Hit:1)

* OnHit: X1 Recovery 允許以下 cancel
  * Dash (高HT限定)

---

### Jump ↓ + X

持刀架式:

- X1: 前翻單手垂直下連斬 (Hit:3, -Aerial:Character/Enemy)

居合架式:

- X1: 拔刀反握垂直下刺 (Hit:1, -Aerial:Character/Enemy)

---

## 跳躍特殊

### Jump ←/N/→ + Y

- Y1: 前方拔刀劍氣斬擊 (Hit:2, Projectile)並切換架式

* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X

---

### Jump ↑ + Y

- Y1: 前上方拔刀劍氣斬擊 (Hit:2, Projectile)並切換架式

* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X

---

### Jump ↓ + Y

- Y1: 前下方拔刀劍氣斬擊 (Hit:2, Projectile) 並切換架式

* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X

---

## 格檔

遵守共通格檔規則

---

## 閃避

遵守共通閃避規則

---

## Heat互動

### Heat強化

特定攻擊允許在高HT時Dash cancel

---
