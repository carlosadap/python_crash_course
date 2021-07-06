from die import Die

die_6 = Die()
die_10 = Die(10)
die_20 = Die(20)

for i in range(10):
    print("6 sided roll:")
    die_6.roll_die()
    print("10 sided roll:")
    die_10.roll_die()
    print("20 sided roll:")
    die_20.roll_die()
    print()

