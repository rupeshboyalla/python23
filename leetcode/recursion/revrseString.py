def reverse(st):
    if len(st) in [0, 1]:
        return st
    else:
        return st[len(st)-1] + reverse(st[:len(st)-1])

print(reverse("abc"))