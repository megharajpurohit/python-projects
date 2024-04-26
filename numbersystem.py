start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))
update_value = int(input("Enter update value: "))
print_choice = int(input("Enter 1 for vertical result or 2 for horizontal result: "))
order_choice = int(input("Enter 1 for forward order or 2 for reverse order: "))

if update_value < 0:
    print("Please enter a positive value.")
else:
    if start_num <= end_num:
        if order_choice == 1 and (print_choice == 1 or print_choice == 2):
            if print_choice == 1:
                print("Forward order in vertical:")
            else:
                print("Forward order in horizontal:")
            for i in range(start_num, end_num + 1, update_value):
                if print_choice == 1:
                    print(i)
                elif print_choice == 2:
                    print(i, end=" ")
                else:
                    print("Please enter valid choices.")
        elif order_choice == 2 and (print_choice == 1 or print_choice == 2):
            if print_choice == 1:
                print("Reverse order in vertical:")
            elif print_choice == 2:
                print("Reverse order in horizontal:")
            for i in range(end_num, start_num - 1, -update_value):
                if print_choice == 1:
                    print(i)
                elif print_choice == 2:
                    print(i, end=" ")
                else:
                    print("Please enter valid choices.")
        else:
            print("Please enter valid choice of order for printing.")
    else:
        if order_choice == 1 and (print_choice == 1 or print_choice == 2):
            if print_choice == 1:
                print("Forward order in vertical:")
            elif print_choice == 2:
                print("Forward order in horizontal:")
            for i in range(end_num, start_num + 1, update_value):
                if print_choice == 1:
                    print(i)
                elif print_choice == 2:
                    print(i, end=" ")
                else:
                    print("Please enter valid choices.")
        elif order_choice == 2 and (print_choice == 1 or print_choice == 2):
            if print_choice == 1:
                print("Reverse order in vertical:")
            else:
                print("Reverse order in horizontal:")
            for i in range(start_num, end_num - 1, -update_value):
                if print_choice == 1:
                    print(i)
                elif print_choice == 2:
                    print(i, end=" ")
                else:
                    print("Please enter valid choices.")
        else:
            print("Please enter valid choices.")