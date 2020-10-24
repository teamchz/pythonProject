import math
import sys
'''
# set input.
a = 10
b = 15
c_angle = 45
'''

# calculate Law of Cosines.
c_power = int(sys.argv[1])**2 \
          + int(sys.argv[2])**2 \
          - (2 * int(sys.argv[1]) * int(sys.argv[2])
             * math.cos(math.radians(int(sys.argv[3]))))

print(math.sqrt(c_power))

'''
# Take input
print("From ax^2 + bx + c = 0")
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

if a == 0:
    print(f"\nAnswer of Equation is {-c}/{b} or {-c/b}")

else:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("\nNo Solution")

    else:
        x_1 = (-b + math.sqrt(discriminant)) / (2*a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"\nAnswer of Equation is {x_1}, {x_2}")
'''

