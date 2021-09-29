def power_of_two(nr):
    while nr % 2 == 0:
        if(nr == 0):
            return False
        nr = nr / 2
    if nr == 1:
      return True
    return False


print(power_of_two(0))
print(power_of_two(8))
print(power_of_two(12))
print(power_of_two(15))