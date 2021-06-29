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

# 4.10. Slices:

print("The first three items in the list are:")

for item in ten_cubes[:3]:
  print(item)

print("Three items from the middle of the list are:")

for item in ten_cubes[3:7]:
  print(item)

print("The last tree items from the  list are:")

for item in ten_cubes[-3:]:
  print(item)

# 4.11. My pizzas, your pizzas

friend_pizzas = pizzas[:]

pizzas.append("new_type")
friend_pizzas.append("dif_type")

for pizza in pizzas:
  print(pizza)

for pizza in friend_pizzas:
  print(pizza)

# Tuples

## 4-13. Buffet

rest_foods = ("rice", "meat", "eggs", "spam", "foo")

for food in rest_foods:
  print(food)

# rest_foods[2] = "bread"

rest_foods = ("rice", "bread", "mayo", "spam", "foo")

for food in rest_foods:
  print(food)