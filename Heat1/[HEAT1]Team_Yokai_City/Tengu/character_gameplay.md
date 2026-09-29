STATUS: CHARACTER
SCOPE: HEAT1

---

# Gameplay Design

## 角色系統

---

## 普通攻擊

### ←/N/→ + X

- X1: 拔刀下段往復斬 (Hit:2)
- X2: 單手下段交叉斬 (Hit:2)
- X3: 單手上段逆袈裟重斬 (Hit:1)
- X4: 雙手下段上撈重斬 (Hit:1)
- X5: 雙手上段袈裟重斬 (Hit:1, Knockback)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 ~ X3 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * ↑ + X
  * ↓ + X
  * Jump
  * Dash(高HT限定)

---

### ↑ + X

- X1: 拔刀上撈斬 (Hit:2, +Aerial:Enemy)
- X2: 單手上撈跳重斬(Hit:1, +Aerial:Character/Enemy)

* OnHit: X1, X2 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * Jump
  * Dash (高HT限定)

---

### ↓ + X

- X1: 拔刀下段往復二連斬 (Hit:2, +Aerial:Enemy)
- X2: 單手上段重斬 (Hit:1, -Aerial:Enemy)

* OnHit: X1, X2 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * Jump
  * Dash (高HT限定)

---

## 特殊攻擊

### ←/N/→ + Y

- Y1: 前方突進拔刀重斬 (Hit:2, SuperArmor)

* OnHit: Y1 Recovery 允許以下cancel
  * ←/N/→ + X

---

### ↑ + Y

- Y1: 前上方突進拔刀重斬 (Hit:2, SuperArmor)

* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X

---

## 跳躍攻擊

### Jump ←/N/→ + X

- X1: 拔刀下段交叉二連斬 (Hit:2)
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

---

### Jump ↑ + X

- X1: 拔刀下段二連上撈斬 (Hit:2, +Aerial:Enemy)
- X2: 拔刀下段上重斬 (Hit:1)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 Recovery 允許以下 cancel
  * Jump ←/N/→ + Y
  * Jump ↑ + Y
  * Jump ↓ + Y
  * Jump
  * Dash (高HT限定)

---

### Jump ↓ + X

- X1: 拔刀下段下方重斬 (Hit:2, -Aerial:Enemy)
- X2: 單手反握垂直下刺 (Hit:1, -Aerial:Character)

* Xn Recovery 允許 Xn+1 cancel

---

## 跳躍特殊

### Jump ←/N/→ + Y

- Y1: 前方突進拔刀重斬 (Hit:2, SuperArmor)

* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X

---

### Jump ↑ + Y

- Y1: 前上方突進拔刀重斬 (Hit:2, SuperArmor)

* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X

---

### Jump ↓ + Y

- Y1: 前下方突進拔刀重斬 (Hit:2, SuperArmor) 

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
