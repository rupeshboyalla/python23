"""

Print stain cases

    #
   ##
  ###
 ####
#####


"""


def print_stair(stair_case):
    for i in range(1, stair_case+1):
        space = ' ' * (stair_case - i)
        stairs = '#' * i
        print(space+stairs)

print_stair(5)

# def print_stairs(n):
#     for i in range(1, n + 1):
#         spaces = ' ' * (n - i)
#         hashes = '#' * i
#         print(spaces + hashes)
#
# # Example usage:
# print_stairs(5)
