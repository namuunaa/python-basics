# TODO list app
todo_list = []
print("What do you need to do today?")
print("Enter DONE when you're finished.")

while True:
  new_todo = input("- ")

  if new_todo == "DONE":
    break
  todo_list.append(new_todo)

print("Here is your to-do list:")

for todo in todo_list:
  print(todo)
