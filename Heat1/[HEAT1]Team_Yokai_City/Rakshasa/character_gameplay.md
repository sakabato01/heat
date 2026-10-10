STATUS: CHARACTER  
SCOPE: HEAT1  

---

# Gameplay Design

## 角色系統

### 羅剎能量

* X攻擊命中/格檔成功/閃避成功 將累積羅剎能量
* X/Y Recovery 消耗羅剎能量進行 Dash cancel

---

## 普通攻擊

### ←/N/→ + X

- X1: 雙手交替上段二連斬 (Hit:2)
- X2: 雙手交替下段二連斬 (Hit:2)
- X3: 單手橫斬 (Hit:1)
- X4: 雙手上段交叉重斬 (Hit:1)
- X5: 雙手下段交叉重斬 (Hit:1, Knockback)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 ~ X3 Recovery 允許以下 cancel
    * ↑ + X / ↓ + X
    * ←/N/→ + Y / ↑ + Y
    * Jump
    * Dash(消耗羅剎能量)

---

### ↑ + X

- X1: 雙手交替下段二連上撈斬 (Hit:2, +Aerial:Enemy)

* OnHit: X1 Recovery允許以下 cancel
    * ←/N/→ + Y / ↑ + Y
    * Jump
    * Dash(消耗羅剎能量)
    
---

### ↓ + X

- X1: 雙手交替上段二連重斬 (Hit:2, -Aerial:Enemy)

* OnHit: X1 Recovery允許以下 cancel
    * ←/N/→ + Y / ↑ + Y
    * Jump
    * Dash(消耗羅剎能量)
    
---

## 特殊攻擊

### ←/N/→ + Y

- Y1: 雙手交替連斬 (Hit:4)
- Y2: 單手橫掃重斬 (Hit:1, Knockback)

* Yn Recovery 允許 Yn+1 cancel
* OnHit: Y1, Y2 Recovery 允許 以下 cancel
    * Jump
    * Dash(消耗羅剎能量)

---

### ↑ + Y

- Y1: 跳躍單手下段上撈重斬 (Hit:2, +Aerial:Character/Enemy)
- Y2: 空中單手橫掃重斬 (Hit:1, Knockback)

* Yn Recovery 允許 Yn+1 cancel
* OnHit: Y1, Y2 Recovery 允許 以下 cancel
    * Jump
    * Dash(消耗羅剎能量)

---

## 跳躍攻擊

### Jump ←/N/→ + X

- X1: 雙手交替下段二連斬 (Hit:2)
- X2: 雙手交替上段二連斬 (Hit:2)
- X3: 雙手橫掃重斬 (Hit:1, Knockback)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 ~ X2 Recovery 允許以下 cancel
    * Jump ↑ + X / Jump ↓ + X
    * Jump ←/N/→ + Y / Jump ↑ + Y / Jump ↓ + Y
    * Jump
    * Dash(消耗羅剎能量)
    
---

### Jump ↑ + X

- X1: 雙手交替下段二連上撈斬 (Hit:2, +Aerial:Enemy)

* OnHit: X1 Recovery 允許以下 cancel
    * Jump ←/N/→ + Y / Jump ↑ + Y / Jump ↓ + Y
    * Jump
    * Dash(消耗羅剎能量)
    
---

### Jump ↓ + X

- X1: 雙手上段下劈重斬 (Hit:1, -Aerial:Enemy)

* OnHit: X1 Recovery 允許以下 cancel
    * Jump ←/N/→ + Y / Jump ↑ + Y / Jump ↓ + Y
    * Jump
    * Dash(消耗羅剎能量)
    
---

## 跳躍特殊

### Jump ←/N/→ + Y

- Y1: 雙手交替連斬 (Hit:4)
- Y2: 單手橫掃重斬 (Hit:1, Knockback)

* Yn Recovery 允許 Yn+1 cancel
* OnHit: Y1, Y2 Recovery 允許 以下 cancel
    * Jump
    * Dash(消耗羅剎能量)
    
---

### Jump ↑ + Y

- Y1: 空中單手下段上撈重斬 (Hit:2, +Aerial:Enemy)
- Y2: 空中單手橫掃重斬 (Hit:1, Knockback)

* Yn Recovery 允許 Yn+1 cancel
* OnHit: Y1, Y2 Recovery 允許 以下 cancel
    * Jump
    * Dash(消耗羅剎能量)

---

### Jump ↓ + Y

- Y1: 空中雙手上段下劈重斬 (Hit:1, -Aerial:Character/Enemy)

* Yn Recovery 允許 Yn+1 cancel
* OnHit: Y1 Recovery 允許 以下 cancel
    * Dash(消耗羅剎能量)

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
Dash cancel X/Y 時, Active 追加單手前刺(Hit:1)

---
