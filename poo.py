import random

def truth_or_dare():
    truth_questions = [
        "What is your biggest fear?",
        "What is the most embarrassing thing you've ever done?",
        "What's the craziest thing you've ever done in public?",
        "Have you ever cheated on a test?",
        "What is your guilty pleasure?",
        "Have you ever lied to get out of trouble?",
        "What is the most embarrassing thing your parents have caught you doing?",
        "What is your most irrational fear?",
        "What is the weirdest dream you've ever had?",
        "Have you ever eavesdropped on someone's conversation?",
    ]

    dare_tasks = [
        "Sing the chorus of your favorite song.",
        "Do your best impression of a celebrity.",
        "Go outside and dance like nobody's watching.",
        "Speak in an accent for the next 3 rounds.",
        "Let someone draw on your face with a washable marker.",
        "Do 20 pushups.",
        "Call a random number and sing happy birthday to the person who answers.",
        "Take a selfie and post it on social media with no caption.",
        "Do your best impersonation of a cartoon character.",
        "Give a 5-minute stand-up comedy routine.",
    ]

    print("Welcome to Truth or Dare!")
    while True:
        choice = input("Enter 'T' for Truth, 'D' for Dare, or 'Q' to quit: ").upper()
        if choice == 'T':
            print(random.choice(truth_questions))
        elif choice == 'D':
            print(random.choice(dare_tasks))
        elif choice == 'Q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'T', 'D', or 'Q'.")

if __name__ == "__main__":
    truth_or_dare()
