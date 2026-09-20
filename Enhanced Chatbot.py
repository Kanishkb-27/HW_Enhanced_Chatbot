option=True
while option==True:
    print("Hello! I am AI chatbot. What is your name? :")
    name=input()
    print(f"Nice to meet you {name}")
    print("How are you feeling (good/bad)?")
    mood=input().lower()
    if mood=="good":
        print("That's nice!")
    elif mood=="bad":
        print("I'm sorry to hear that.")
    else:
        print("I get it. Sometimes it is hard to explain how you feel")
    print("What is your hobby?")
    hobby=input()
    print(f"Oh! {hobby} sounds good")
    print("What is your favorite colour?")
    colour=input()
    print(f"Wow! {colour} is a nice colour")
    print("What is your favorite sport?")
    sport=input()
    print(f"Nice! Even I love {sport}")
    print("Do you want to continue chatting? (yes/no)")
    cont=input().lower()
    if cont=="yes":
        option==True
    elif cont=="no":
        option=False
    else:
        print("Invalid option, we take it that you want to continue")
print(f"It was nice chatting with you {name}")