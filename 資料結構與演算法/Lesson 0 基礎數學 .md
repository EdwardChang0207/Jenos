# Lesson 0 基礎數學

主題: 前導課

# Session 1. 數列、級數

## (1)等差數列

數列為多個數字排列出現，通常使用 $a_n$表示，其中n表示該元素的第n項

eg. 

$$
a_n = 1,2,3,4,5\\a_1=1, a_2=2
$$

等差數列為數列的一種，特徵為任意前後兩個相鄰的元素之“差”皆相同，此差值稱為“公差”，以“d”表示，所以我們可以用以下公式。

$$
a_n = a_1 + (n-1)d
$$

## (2)等差級數

等差級數即為將等差數列之前n項相加，通常使用 $S_n$表示

$$
a_n = 1, 2, 3, 4, 5 \\ S_n=\sum a_n=a_1+a_2+a_3+a_4+a_5 = 15
$$

我們可以使用幾何方式推導出等差級數公式

$$
S_n = \frac{項數}{2} (首項 + 末項)
$$

## (3)平方和

即為1~n之平方相加

$$
\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}
$$

## (4)任意次方和

$$
\sum_{i=1}^{k} i^d, \quad d \in \mathbb{N}, \quad d \geq 0
$$

$$
\sum_{i=1}^{k} i^d \approx n^{d+1}(polynomial-bound)
$$

# Session 2.排列、組合

## (1)排列 Permutation

n物中取r物做排列之方法數

$$
P(n, r) = \frac{n!}{(n-r)!}
$$

## (2)組合

n物中取r物做組合之方法數

$$
C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

# Session 3.階乘

## (1) $N! \leq N^N$

## (2) $N! \geq (\frac{N}{2})^{\frac{N}{2}}$

## (3)Stirling’s Formula

$$
n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n
$$

$$
n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n \left( 1 + \frac{1}{12n} \right)
$$

## (4)漸進式符號

$$
n! = O(n^n) \\ n!= \omega(2^n) \\ lg(n!) = \theta(nlgn)
$$

# Session 4.對數

## (1) $lg(n) = log_2(n)$

## (2) $ln(n) = log_e(n)$

## (3) $lg^k(n) = (lg(n))^k$

## (4) $lglg(n) = lg(lg(n))$

## (5) $log_c(ab) = log_ca +log_cb$

## (6) $log_b(a^n) = nlog_ba$

## (7) $log_ba = \frac{log_ca}{log_cb}$

## (8) $log_b(\frac{1}{a}) = -log_ba$

## (9) $log_ba = \frac{1}{log_ab}$

## (10) $a^{log_bc} = c^{log_ba}$

## (11) $a = b^{log_ba}$

## (12) $lg^bn = O(n^a) , \forall a:constant(polynomial-bound)$

## (13) $lg^{*}n = iterated-log = min(i \geq 0, lg^{i}n \leq 1)$

→ 對n取幾次log會到1