# Lesson 1 什麼是演算法？

主題: 前導課

# 📕Session 1.演算法定義⭐⭐

演算法是解決特定問題的**“有限個指令/敘述/方法”**，且包含以下五個性質(criteria)：

1. **Input(輸入)**：輸入的Data
2. **Output(輸出)**：輸出的Data
3. **Definitness(明確性)**：演算法中，每個指令/敘述必須是**清晰(clear)**且**不會混淆(unambiguous)**的
4. **Feniteness(有限性)**：演算法在執行/追蹤**有限個步驟後必須終止**
5. **Effectiveness(有效性)**：每條指令、敘述必須夠基本，可被人用紙筆追蹤

# 🔂Session 2.遞迴(Recursion)

## 1.Direct Recursion(直接遞迴)⭐

一個function具有**self-calling**的性質即稱之

```python
def Test(n:int)->int:
	if n == 0: return 1
	return Test(n-1)*n
```

## 2.Indirect Recursion(間接遞迴)

多個模組彼此形成calling-cycle(實務不使用)

原因：

1. Hard to Understand and Debug（理解及除錯困難)
2. Performance Overhead（效能低落）
3. Difficult to Optimize with Tail Recursion（難以最佳化）
4.  No Real-World Use Cases（沒有實例需求）

```python
def even(n):
    if n == 0:
        return True
    return odd(n - 1)

def odd(n):
    if n == 0:
        return False
    return even(n - 1)

print(even(4))  # Output: True
	print(odd(5))   # Output: True
```

## 3.Tail Recursion(尾端遞迴)

是Direct Recursion的一種，Recursion之後下一個敘述為結尾，complier會做最佳化

ex. fibonacci number

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # Recursive call is NOT the last operation
```

```python
def factorial(n, acc=1):
    if n == 0:
        return acc  # Base case returns accumulator directly
    return factorial(n - 1, acc * n)  # Tail recursion (last operation is recursive call)

print(factorial(5))  # Output: 120
```

## 4.Recursion v.s Iteration(loop)⭐⭐⭐

| Recursion | Iteration |
| --- | --- |
| 精簡 | 冗長 |
| 區域變數少 | 區域變數多 |
| 問題表達能力佳 | 問題表達能力差 |
| 除錯困難 | 除錯簡單 |
| 執行時間久、效率差 | 執行時間短、效率佳 |
| 需要額外的stack空間支持 | 不需要額外的stack空間支持 |

## 5.Recursion Algo

關鍵是記下數學定義

### (1)階乘 n!

$$
n! =\begin{cases} 1, & \text{if } n = 0 \\n \times (n - 1)!, & \text{if } n > 0\end{cases}
$$

```python
def F(n):
	if n == 0: return 1
	return F(n-1)*n
```

### (2)Fibonacci Number 費氏數列

$$
Fib(n) =\begin{cases} 0, & \text{if } n = 0 \\1, & \text{if } n = 1 \\Fib(n-1) + Fib(n-2), & \text{if } n \geq 2\end{cases}
$$

```python
def Fib(n):
	if n == 0: return 0
	elif n == 1: return 1
	else: return Fib(n-1) + Fib(n-2)
```

### (3)Arithmetic Series 等差級數

$$
a_n = a_1 + (n - 1) d
$$

$$
S_n = a_1+a_2+...+a_n
$$

```python
def A(a1, n, d):
	if n == 0: return 0
	if n == 1: return a1
	return A(a1, n-1, d) + a1+(n-1)*d
```

### (4)Binomial Coe 二項式係數

$$
\binom{n}{k} =
\begin{cases} 
1, & \text{if } k = 0 \text{ or } k = n \\
\binom{n-1}{k-1} + \binom{n-1}{k}, & \text{if } 0 < k < n
\end{cases}
$$

```python
def Bin(n, k):
	if n == k or k == 0: return 1
	return Bin(n-1, m) + Bin(n-1, m-1)
```

### (5)GCD(Greatest Common Divisor) 最大公因數

hint:輾轉相除法

$$
\text{gcd}(a, b) =\begin{cases} b, & \text{if } a = 0 \\\text{gcd}(b \mod a, a), & \text{if } a > 0\end{cases}
$$

```python
def gcd(a, b):
	if a%b == 0: return b
	return gcd(b, a%b)
```

### (6)Ackerman’s Function 艾克曼函數

$$
A(m, n) =\begin{cases} n + 1, & \text{if } m = 0 \\A(m - 1, 1), & \text{if } m > 0 \text{ and } n = 0 \\A(m - 1, A(m, n - 1)), & \text{if } m > 0 \text{ and } n > 0\end{cases}
$$

```python
def A(m,n):
	if m == 0: return n+1
	if m > 0 and n == 0: return A(m-1,1)
	if m > 0 and n > 0: return A(m-1, A(m, n-1))
```

### (7)Exp Function 指數函數

O(n)

$$
\exp(x,n) =\begin{cases} 1, & \text{if } n = 0 \\\exp(x, n-1) \times x), & \text{if } n > 0\end{cases}
$$

```python
def exp(x,n):
	if n == 0: return 1
	return exp(x,n-1)*x
```

O(logn)

$$
x^n =\begin{cases} 1, & \text{if } n = 0 \\x \times (x^{n/2})^2, & \text{if } n \text{ is even} \\x \times x^{n-1}, & \text{if } n \text{ is odd}\end{cases}
$$

```python
def exp(x,n):
	if n % 2 == 0: f = 1
	else: f = x
	if n < 2: return f
	return f*exp(x*x, n/2)
```

### (8)Towers of Hanoi 河內塔

**Rules:**

I.每次僅能移動一個碟盤

II.大碟盤不能放置在小碟盤上

III.求將Source上碟盤全部移置Dist的方法

[https://embed.figma.com/design/s8xJZXwwIn515jSnuysyfb/Untitled?node-id=0-1&embed-host=share&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/s8xJZXwwIn515jSnuysyfb/Untitled?node-id=0-1&embed-host=share&embed-host=notion&footer=false&theme=system)

**Steps:**

**I.Source 用 Hanoi 搬(n-1)個到 Aux**

(1)move 1 to Dist

(2)move 2 to Aux

(3)move 1 to Aux

**II.最後一個搬到 Dist**

(4)move 3 to Dist

**III.Aux 用 Hanoi 搬(n-1)個到 Dist**

(5)move 1 to Source

(6)move 2 to Dist

(7)move 1 to Dist

**Recursive Algo:**

```python
def Hanoi(n:int, source, aux, dist):
	if n == 1:
		print(f'move disk 1 from {source} to {dist}')
		return
	Hanoi(n-1, source, aux, to) #I.
	print(f'move disk {n} from {source} to {dist}') #II.
	Hanoi(n-1, aux, dist, source)#III.
```

### (9)Permutation 排列

n個data做排列→ n!種可能

Perm(a,b,c) →

a b c, a c b → ‘a’ + Perm(b,c)

b a c, b c a → ‘b’ + Perm(a,c)

c a b, c b a → ‘c’ + Perm(a,b)

**Recursive Algo:**

```python
def Perm(data:list, i:int, n:int):
	#產生data[i]~data[n]的所有排列組合
	#假設存放位置為[1...n]
	if i == n: #終止條件
		for j in range(n+1):
			print(data[j]) #列出list中所有內容
	else:
		for j in range(i, n+1):
			swap(data[i], data[j])#data[j]為head,隨j改動輪流當head
			Perm(data, i+1, n)
			swap(data[i],data[j])
```

# 🫥Session 3. Pseudocode 虛擬碼

pseudocode並非真正可執行的程式碼，僅用來描述演算法之執行方法，pseudocode可用很多不同的形式撰寫，沒有固定格式，eg.C-like, Python-like