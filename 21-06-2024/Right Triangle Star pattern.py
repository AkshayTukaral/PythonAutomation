# Right Triangle Star Pattern
def print_star_triangle_pattern(n):

    for i in range(1, n+1):
        for j in range(1, i+1):
            print("* ", end="")
        print()


print_star_triangle_pattern(5)



