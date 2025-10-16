def clean(rooms):
    if not rooms:
        print("All rooms clean")
        return
    print(f"Now cleaning: {rooms[0]} ...")
    clean(rooms[1:])

home_rooms = ["kitchen", "dining room", "bathroom", "living room"]
clean(home_rooms)


task_numbers = [3, 7, 6, 12, -3, 34, 55]

def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list(task_numbers))
