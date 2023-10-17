def hello():
  print("hello")

def pack(a, b, c):
    packed_list = [a, b, c]
    return packed_list

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {food_list[0]}")
        for item in food_list[1:]:
            print(f"Next I eat {item}")