STATUS: CHARACTER  
SCOPE: HEAT1  

---

# Gameplay Design

## 角色系統

### 羅剎能量

* X/格檔/閃避 將累積羅剎能量
* Y 消耗羅剎能量進行攻擊

---

## 普通攻擊

### ←/N/→ + X

- X1: 單手上段交叉二連斬 (Hit:2)
- X2: 換手上段交叉二連斬 (Hit:2)
- X3: 雙手上段交叉重斬 (Hit:1)
- X4: 雙手上段交叉重斬, 雙手分開收尾 (Hit:1, Knockback)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery 允許以下 cancel
    * ↑ + X
    * ↓ + X
    * ←/N/→ + Y
    * ↑ + Y
    * Jump

---

### ↑ + X

- X1: 雙手交替旋身斜向二連上斬 (Hit:2)
- X2: 單手斜向上撈斬 (Hit:1, +Aerial:Enemy)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery允許以下 cancel
    * ←/N/→ + Y
    * ↑ + Y
    * Jump

---

### ↓ + X

- X1: 雙手交替下段斜向二連上斬 (Hit:2)
- X2: 雙手斜向下劈斬 (Hit:1, -Aerial:Enemy)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 允許以下 cancel
    * ←/N/→ + Y
    * ↑ + Y
    * Jump

---

## 特殊攻擊

消耗羅剎能量使用

### ←/N/→ + Y

- Y1: 向前突進, 雙手上段重斬 (Hit:2, SuperArmor)

* Y1 Recovery 允許 以下 cancel
    * ←/N/→ + Y
    * ↑ + Y
    * ↓ + Y

---

### ↑ + Y

- Y1: 前上突進, 雙手上段重斬 (Hit:2, +Aerial:Character, SuperArmor)

* Y1 Recovery 允許 以下 cancel
    * Jump ←/N/→ + Y
    * Jump ↑ + Y
    * Jump ↓ + Y

---

## 跳躍攻擊

### Jump ←/N/→ + X

- X1: 單手上段交叉二連斬 (Hit:2)
- X2: 換手上段交叉二連斬 (Hit:2)
- X3: 雙手水平交叉重斬, 雙手分開收尾 (Hit:1, +Aerial:Enemy)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery 允許以下 cancel
    * Jump ↑ + X
    * Jump ↓ + X
    * Jump ←/N/→ + Y
    * Jump ↑ + Y
    * Jump ↓ + Y
    * Jump

---

### Jump ↑ + X

- X1: 旋身斜向上撈二連斬 (Hit:2)
- X2: 單手斜向上撈斬 (Hit:1, +Aerial:Enemy) 

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery 允許以下 cancel
    * Jump ←/N/→ + Y
    * Jump ↑ + Y
    * Jump ↓ + Y
    * Jump

---

### Jump ↓ + X

- X1: 旋身斜向下劈二連斬 (Hit:2)
- X2: 單手斜向下劈斬 (Hit:1, -Aerial:Character/Enemy)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery 允許以下 cancel
    * Jump ←/N/→ + Y
    * Jump ↑ + Y
    * Jump ↓ + Y
    * Jump

---

## 跳躍特殊

消耗羅剎能量使用

### Jump ←/N/→ + Y

- Y1: 向前突進, 雙手上段重斬 (Hit:2, SuperArmor)

* Y1 Recovery 允許 以下 cancel
    * Jump ←/N/→ + Y
    * Jump ↑ + Y
    * Jump ↓ + Y

---

### Jump ↑ + Y

- Y1: 前上突進, 雙手上段重斬 (Hit:2, SuperArmor)

* Y1 Recovery 允許 以下 cancel
    * Jump ←/N/→ + Y
    * Jump ↑ + Y
    * Jump ↓ + Y

---

### Jump ↓ + Y

- Y1: 前下突進, 雙手上段重斬 (Hit:2, SuperArmor)

* Y1 Recovery 允許 以下 cancel
    * Jump ←/N/→ + Y
    * Jump ↑ + Y
    * Jump ↓ + Y

---

## 格檔

* 遵守共通格檔規則

---

## 閃避

* 遵守共通閃避規則

---

## Heat互動

### Heat強化

高HT時:
* 閃避動作轉換為突進旋身斬擊 (Hit:3, SuperArmor)
* OnHit: Recovery 可被以下動作 cancel
    * X / ↑ + X / ↓ + X
    * Jump X / Jump ↑ + X / Jump ↓ + X
    * Jump

---
