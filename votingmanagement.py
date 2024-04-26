n = 1
party_1 = 0
party_2 = 0
party_3 = 0
party_4 = 0

while n == 1:
    voter_name = input("Enter your name: ")
    voter_age = int(input("Enter your age: "))
    vote_choice = int(input("To vote 'Party 1' press 1,\nTo vote 'Party 2' press 2,\nTo vote 'Party 3' press 3,\nTo vote 'Other' press 4: "))
    continue_choice = int(input("To continue press 1, to exit press 2: "))

    if voter_age >= 18:
        if vote_choice == 1:
            print("You have successfully voted for Party 1. Thank you for voting!")
            party_1 += 1
        elif vote_choice == 2:
            print("You have successfully voted for Party 2. Thank you for voting!")
            party_2 += 1
        elif vote_choice == 3:
            print("You have successfully voted for Party 3. Thank you for voting!")
            party_3 += 1
        elif vote_choice == 4:
            print("You have successfully voted for Other. Thank you for voting!")
            party_4 += 1
        else:
            print("Invalid choice for voting.")
            print("2 attempts left.")
            vote_choice = int(input("To vote 'Party 1' press 1,\nTo vote 'Party 2' press 2,\nTo vote 'Party 3' press 3,\nTo vote 'Other' press 4: "))
            if vote_choice == 1:
                print("You have successfully voted for Party 1. Thank you for voting!")
                party_1 += 1
            elif vote_choice == 2:
                print("You have successfully voted for Party 2. Thank you for voting!")
                party_2 += 1
            elif vote_choice == 3:
                print("You have successfully voted for Party 3. Thank you for voting!")
                party_3 += 1
            elif vote_choice == 4:
                print("You have successfully voted for Other. Thank you for voting!")
                party_4 += 1
            else:
                print("Invalid choice for voting.")
                print("1 attempt left.")
                vote_choice = int(input("To vote 'Party 1' press 1,\nTo vote 'Party 2' press 2,\nTo vote 'Party 3' press 3,\nTo vote 'Other' press 4: "))

        if continue_choice == 2:
            # Determine the winner based on votes
            if party_1 > party_2 and party_1 > party_3 and party_1 > party_4:
                print("Party 1 is the winner.")
            elif party_2 > party_1 and party_2 > party_3 and party_2 > party_4:
                print("Party 2 is the winner.")
            elif party_3 > party_1 and party_3 > party_2 and party_3 > party_4:
                print("Party 3 is the winner.")
            elif party_4 > party_1 and party_4 > party_2 and party_4 > party_3:
                print("Other party is the winner.")
            elif party_1 == party_2 == party_3 == party_4:
                print("All parties received equal votes. The election is tied.")
            n = 2
        elif continue_choice == 1:
            n = 1
        else:
            print("Invalid choice to continue or exit.")
            print("2 attempts left.")
            continue_choice = int(input("To continue press 1, to exit press 2: "))
            if continue_choice == 2:
                # Determine the winner based on votes
                if party_1 > party_2 and party_1 > party_3 and party_1 > party_4:
                    print("Party 1 is the winner.")
                elif party_2 > party_1 and party_2 > party_3 and party_2 > party_4:
                    print("Party 2 is the winner.")
                elif party_3 > party_1 and party_3 > party_2 and party_3 > party_4:
                    print("Party 3 is the winner.")
                elif party_4 > party_1 and party_4 > party_2 and party_4 > party_3:
                    print("Other party is the winner.")
                elif party_1 == party_2 == party_3 == party_4:
                    print("All parties received equal votes. The election is tied.")
                n = 2
                break
            elif continue_choice == 1:
                n = 1
            else:
                print("Invalid choice to continue or exit.")
                print("1 attempt left.")
                continue_choice = int(input("To continue press 1, to exit press 2: "))

    else:
        print("You are not eligible to vote as your age is below 18.")
print("The ultimate winner is still a secret. ;)")