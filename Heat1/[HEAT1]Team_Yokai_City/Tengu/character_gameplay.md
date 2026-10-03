STATUS: CHARACTER
SCOPE: HEAT1

---

# Gameplay Design

## 角色系統

* X攻擊將增加專注值
* 消耗專注, Y攻擊 Recovery將可進行以下cancel
  * Y
  * 衝刺

---

## 普通攻擊

### ←/N/→ + X

- X1: 單手下段往復斬 (Hit:2)
- X2: 單手下段交叉斬 (Hit:2)
- X3: 雙手下段上撈重斬 (Hit:1)
- X4: 雙手上段袈裟重斬 (Hit:1, Knockback)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 ~ X3 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * ↑ + X
  * ↓ + X
  * Jump

---

### ↑ + X

- X1: 單手下段上撈斬 (Hit:2, +Aerial:Enemy)
- X2: 跳躍單手下段上撈重斬(Hit:1, +Aerial:Character/Enemy)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * Jump

---

### ↓ + X

- X1: 單手轉身蹲姿下段上斬 (Hit:2)
- X2: 單手轉身下段上重斬 (Hit:1, +Aerial:Enemy, Knockback)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery 允許以下 cancel
  * ←/N/→ + Y
  * ↑ + Y
  * Jump

---

## 特殊攻擊

### ←/N/→ + Y

- Y1: 前方突進拔刀迴旋重斬 (Hit:1)
- Y2: 拔刀快速連斬 (Hit:4)

* Hold Y1將消耗專注值增加Y1傷害
* OnHit: Y1 Recovery 允許以下cancel
  * ←/N/→ + X
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* OnHit: Y2 Recovery 允許以下cancel
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* 高HT, Y1, Y2 Recovery 追加刀光斬擊(Hit: 3)

---

### ↑ + Y

- Y1: 前上方突進拔刀迴旋重斬 (Hit:1)
- Y2: 拔刀快速連斬 (Hit:4)

* Hold Y1將消耗專注值增加Y1傷害
* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* OnHit: Y2 Recovery 允許以下cancel
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* 高HT, Y1, Y2 Recovery 追加刀光斬擊(Hit: 3)

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

---

### Jump ↑ + X

- X1: 單手下段二連上撈斬 (Hit:2, +Aerial:Enemy)
- X2: 單手下段上重斬 (Hit:1)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1, X2 Recovery 允許以下 cancel
  * Jump ←/N/→ + Y
  * Jump ↑ + Y
  * Jump ↓ + Y
  * Jump

---

### Jump ↓ + X

- X1: 拔刀下段下方重斬 (Hit:2, -Aerial:Enemy)
- X2: 單手反握垂直下刺 (Hit:1, -Aerial:Character)

* Xn Recovery 允許 Xn+1 cancel
* OnHit: X1 Recovery 允許以下 cancel
  * Jump ←/N/→ + Y
  * Jump ↑ + Y
  * Jump ↓ + Y
  * Jump

---

## 跳躍特殊

### Jump ←/N/→ + Y

- Y1: 前方突進拔刀迴旋重斬 (Hit:1)
- Y2: 拔刀快速連斬 (Hit:4)

* Hold Y1將消耗專注值增加Y1傷害
* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* OnHit: Y2 Recovery 允許以下cancel
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* 高HT, Y1, Y2 Recovery 追加刀光斬擊(Hit: 3)

---

### Jump ↑ + Y

- Y1: 前上方突進拔刀迴旋重斬 (Hit:1)
- Y2: 拔刀快速連斬 (Hit:4)

* Hold Y1將消耗專注值增加Y1傷害
* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* OnHit: Y2 Recovery 允許以下cancel
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* 高HT, Y1, Y2 Recovery 追加刀光斬擊(Hit: 3)

---

### Jump ↓ + Y

- Y1: 前下方突進拔刀迴旋重斬(Hit:1) 
- Y2: 拔刀快速連斬 (Hit:4)

* Hold Y1將消耗專注值增加Y1傷害
* OnHit: Y1 Recovery 允許以下cancel
  * Jump ←/N/→ + X
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* OnHit: Y2 Recovery 允許以下cancel
  * Dash (消耗專注值)
  * Y2 (消耗專注值)
* 高HT, Y1, Y2 Recovery 追加刀光斬擊(Hit: 3)

---

## 格檔

遵守共通格檔規則

---

## 閃避

遵守共通閃避規則

---

## Heat互動

### Heat強化

* 高HT時，特定攻擊 Recovery 追加刀光斬擊(Hit: 3)

---
