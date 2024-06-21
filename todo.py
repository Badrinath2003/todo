todos =[]
while True:
    user_action = input("Type add, show , exit : ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
                row = f"{index+1} - {item}"
                print(row)
        case 'edit':
            number = int(input("Enter the Number to be edited : "))
            number = number - 1
            new_todo = input("Enter the new todo : ")
            todos[number] = new_todo
                         
        case 'exit':
            break
