# Medium Level Problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees, asin

AB = int(input())
BC = int(input())

# Step 1: Calculate the hypothenuse
AC = pow(AB**2 + BC**2, 0.5)

# Step 2: Law of sines to discover sin(ACB)
# sin_ABC = 1 since it is a right angle
sin_ACB = (1 * AB) / AC

#  Step 2.5: Calculate cos(ACB); only the positive version
#  And Calculate CM, which is just 1/2 of AC
cos_ACB = pow(1 - sin_ACB**2, 0.5)
CM = 0.5 * AC

# Step 3: Law of cosines to know the length of BM
BM = pow(BC**2 + CM**2 - 2*BC*CM*cos_ACB ,0.5)

# Step 4: Law of sines to calculate sin(MBC)
sin_MBC = (sin_ACB * CM) / BM

# Step 5: Calculate the angle theta and print the result
theta = round(degrees(asin(sin_MBC)))
print(f"{theta}\xb0")


