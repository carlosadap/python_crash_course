pizzas = ["pepperoni", "carbonara", "margherita"]

for pizza in pizzas:
  print(f"I like {pizza} pizza")

print("I love pizza")

for num in range(1, 21):
  print(num)

big_list = [value for value in range(1, 1000001)]

# for num in big_list:
  # print(num)

print(min(big_list))
print(max(big_list))
print(sum(big_list))

odd_nums = [value for value in range(1, 20, 2)]

print(odd_nums)

mult_3 = [value for value in range(3, 31, 3)]

print(mult_3)

ten_cubes = [value**3 for value in range(1, 11)]

print(ten_cubes)