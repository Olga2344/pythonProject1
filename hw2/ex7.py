# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n=4
right_plenty=n*(n+1)/2
left_plenty=0
for i in range(n+1):
    left_plenty+=i
if right_plenty==left_plenty:
    print('для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2')
print(left_plenty)
print(right_plenty)

