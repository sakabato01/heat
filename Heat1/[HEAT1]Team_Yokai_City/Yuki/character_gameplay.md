STATUS: CHARACTER  
SCOPE: HEAT1  

---

# Gameplay Design

## 角色系統

### 霜雪

格檔 / 閃避成功將累積霜雪,  
消耗霜雪凍結敵人或產生風雪

---

## 普通攻擊

### ← / N / → + X

- X1: 單手二連刺擊 (Hit:2) 
- X2: 下段交叉二連打擊 (Hit:2) 
- X3: 轉身二連橫掃打擊 (Hit:2) 
- X4: 突進開傘撞擊 (Hit:1, Knockback) 

* Xn Recovery 允許 Xn+1 cancel
* 格檔 Recovery > X, 從X3開始
* X1 ~ X3 Recovery 允許以下 cancel
    * ↑ + X
    * ↓ + X
    * ← / N / → + Y

---

### ↑ + X

- X1: 雙手上撈打擊 (Hit:1, Launch)

* X1 Recovery 允許以下 cancel
    * ↑ + Y
    * Jump

---

### ↓ + X

- X1: 後退橫掃 (Hit:1)
* X1 Recovery 允許以下 cancel
    * ↓ + Y

---

## 特殊攻擊

消耗霜雪, 受擊敵人增加額外 Recovery

### ← / N / → + Y

- X1 > Y1: 中距離冰刃射擊 (Hit:2, Projectile)
- X2 > Y2: 跳躍開傘上擊 (Hit:2, Airborne)
- X3 > Y3: 轉身開傘橫掃 (Hit:2, Knockback)

---

### ↑ + Y

- ↑ + X1 > Y1: 近距離生成冰柱上推 (Hit:2, Launch)

---

### ↓ + Y

- ↓ + X1 > Y1: 近距離生成冰柱下砸 (Hit:2, Knockback)

---

## 跳躍攻擊

### Jump ← / N / → + X

- X1: 單手二連刺擊 (Hit:2) 
- X2: 轉身二連橫掃打擊 (Hit:2)
- X3: 下落雙腳踩擊 (Hit:1, Grounded, Slammed) 

* Xn Recovery 允許 Xn+1 cancel
* X1, X2 Recovery 允許以下 cancel
    * Jump ↑ + X
    * Jump ↓ + X
    * Jump

---

### Jump ↑ + X

- X1: 單手上撈打擊 (Hit:2, Launch)
* X1 Recovery 允許以下 cancel
    * ↑ + Y
    * Jump

---

### Jump ↓ + X

- X1: 垂直下砸 (Hit:2)
* X1 Recovery 允許以下 cancel
    * ↓ + Y
    * Jump
    
---

## 跳躍特殊

消耗霜雪, 受擊敵人增加額外 Recovery

### Jump ← / N / → + Y

- Jump ← / N / → + X1 > Y1: 中距離冰刃射擊 (Hit:2, Projectile)
- Jump ← / N / → + X2 > Y2: 開傘上擊 (Hit:2)

---

### Jump ↑ + Y

- Jump ↑ + X1 > Y1: 近距離生成冰柱上推 (Hit:2)

---

### Jump ↓ + Y

- Jump ↓ + X1 > Y1: 近距離生成冰柱下砸 (Hit:2, Slammed)

---

## 格檔

* 遵守共通格檔規則
* X, Y Recovery 允許以下 cancel
    * Block
* Jump X, Jump Y Recovery 允許以下 cancel
    * Jump Block
* 格檔成功後長按格檔, 消耗霜雪在周圍產生風雪
    * 風雪造成大範圍傷害 (Hit:3, Launch) 並且額外增加敵人 Recovery  
    * 風雪 StartUp, Active 無敵

---

## 閃避

遵守共通閃避規則

---

## Heat互動

### Heat強化

高HT時:
* 開放以下攻擊蓄力
    * ← / N / → + X4 (Hit:3, Knockback)
    * ← / N / → + Y1 增加飛行道具速度 (Hit:4, Projectile)
    * ← / N / → + Y2 (Hit:4, Launch, Airborne)
    * ← / N / → + Y3 (Hit:4, Knockback)
    * Jump ← / N / → + X3 (Hit:3, Grounded,Slammed)
    * Jump ← / N / → + Y1 增加飛行道具速度 (Hit:4, Projectile)
    * Jump ← / N / → + Y2 (Hit:4, Launch)

---
