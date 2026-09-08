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

---

### ↑ + X

- X1: 雙手交替旋身斜向二連上斬 (Hit:2)
- X2: 單手斜向上撈斬 (Hit:1, +Aerial:Enemy)

* Xn Recovery 允許 Xn+1 cancel

---

### ↓ + X

- X1: 雙手交替下段斜向二連上斬 (Hit:2)
- X2: 雙手斜向下劈斬 (Hit:1, -Aerial:Enemy)

* Xn Recovery 允許 Xn+1 cancel

---

## 特殊攻擊

### ←/N/→ + Y

- Y1: 向前突進雙手斜向重斬 (Hit:2, SuperArmor)

---

### ↑ + Y

- Y1: 前上突進雙手斜向重斬 (Hit:2, SuperArmor)

---

## 跳躍攻擊

### Jump ←/N/→ + X

- X1: 單手上段交叉二連斬 (Hit:2)
- X2: 換手上段交叉二連斬 (Hit:2)
- X3: 雙手水平交叉重斬, 雙手分開收尾 (Hit:1, +Aerial:Enemy)

* Xn Recovery 允許 Xn+1 cancel

---

### Jump ↑ + X

- X1: 旋身斜向上撈二連斬 (Hit:2)
- X2: 單手斜向上撈斬 (Hit:1, +Aerial:Enemy) 

* Xn Recovery 允許 Xn+1 cancel

---

### Jump ↓ + X

- X1: 旋身斜向下劈二連斬 (Hit:2)
- X2: 單手斜向下劈斬 (Hit:1, -Aerial:Character/Enemy)

* Xn Recovery 允許 Xn+1 cancel

---

## 跳躍特殊

### Jump ←/N/→ + Y

- Y1: 向前突進雙手斜向重斬 (Hit:2, SuperArmor)

---

### Jump ↑ + Y

- Y1: 前上突進雙手斜向重斬 (Hit:2, SuperArmor)

---

### Jump ↓ + Y

- Y1: 前下突進雙手斜向重斬 (Hit:2, SuperArmor)

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
    * Jump
---
