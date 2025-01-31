#Example 1
print(10 + 5)

"""
+	Addition	x + y
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y 
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
                    print(x)
"""

#Example 2 Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
print((6 + 3) - (6 + 3))

#Example 3 Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions
print(100 + 5 * 3)

#Example 4 Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right
print(5 + 4 - 7 + 3)