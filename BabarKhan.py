import random
print("******************Babar Khan Quiz Game*****************")
quiz_list = [
    ("Who is current Governor sindh of pakistan?",
     ['A Kamran khan tissori', 'B Usman bhuzdar', 'C Shah Mahmood Qureshi', 'D Parvaiz Khatak'], 'A'),
    ("Who was the first chief executive of Pakistan", ['A Jinnah', 'B Bhutto', 'C Musharaf', 'D Imran Khan'], 'C'),
    ("Largest mountain in Pakistan", ['A K2', 'B Mounteverest', 'C NangaPerbat', 'D Himalya'], 'A'),
    ("Pakistan cricket team's captain name", ['A Shadab', 'B Aamir', 'C Razzaq', 'D Babar'], 'D'),
    ("Who wins the election in Pakistan every time", ['A PMLN', 'B PPP', 'C PTI', 'D Establishment'], 'D')
]
prize = 0
result = []
two_choices = []
newch = []
random.shuffle(quiz_list)
for i in range(len(quiz_list)):
    question, choices, correct_choice = quiz_list[i]
    result.clear()
    two_choices.clear()
    result.append(correct_choice)
    first_letter = [element[0] for element in choices]
    for x in first_letter:
        if result[0] == x:
            for first in choices:
                if correct_choice == first[0]:
                    two_choices.append(first)
                    for ch in choices:
                        if ch not in two_choices:
                            newch.append(ch)
                            break
                    two_choices.extend(newch)
                    newch.clear()
                    two_choices = sorted(two_choices)
                    break
    print("\nQuestion", i + 1, ":", question)
    for j in range(len(choices)):
        print(choices[j])

    mychoice = input("Press 1: to answer the question, 2: Choose 50 50 lifeline 3: flip the question ")
    if mychoice == "2":
        for k in range(len(two_choices)):
            print(two_choices[k])
        quiz_list.remove(quiz_list[i])
    elif mychoice == "3":
        if i == len(quiz_list) -1:
            new_index = i-1
            question, choices, correct_choice = quiz_list[new_index]
            print("\nYour question has been changed:")
            print("Question", new_index + 1, ":", question)
            for j in range(len(choices)):
                print(choices[j])
            quiz_list.remove(quiz_list[i])
        else:
            new_index = i + 1
            question, choices, correct_choice = quiz_list[new_index]
            print("\nYour question has been changed:")
            print("Question", new_index + 1, ":", question)
            for j in range(len(choices)):
                print(choices[j])
            quiz_list.remove(quiz_list[i])

    myanswer = input("Enter your answer: ").upper()
    if myanswer == correct_choice:
        prize += 100
        print("Congratulations! your answer is correct and you have earned " + str(prize) + "$")
        if i == len(quiz_list) - 1:
            print("Great! You have answered all the questions, Game ends here")
            break
        else:
            continuegame = input("Do you want to continue: Y or N").upper()
            if continuegame == "N":
                break
            else:
                print("Lets' Continue and you have earned, " + " " + str(prize)+"$ so far")

    else:
        print("You answer is wrong try again nex time")
        break
print("\nYou have won ", str(prize)+"$")

