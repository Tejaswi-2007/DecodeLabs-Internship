from datetime import datetime

print("=" * 50)
print("🤖 Welcome to DecodeBot AI")
print("Your Smart Rule-Based Assistant")
print("Type 'help' to see available commands")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    # Convert input to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # Greeting
    if user_input in [
        "hi", "hello", "hey", "hii",
        "good morning", "good afternoon",
        "good evening"
    ]:
        print("DecodeBot AI: Hello! How can I help you today? 😊")

    # Help command
    elif user_input == "help":
        print("\nAvailable Commands:")
        print("- hello / hi / hey")
        print("- how are you")
        print("- time")
        print("- date")
        print("- motivate me")
        print("- what is ai")
        print("- what is your name")
        print("- thank you")
        print("- exit")

    # How are you
    elif user_input == "how are you":
        print("DecodeBot AI: I am doing great! Thanks for asking 😄")

    # Bot name
    elif user_input == "what is your name":
        print("DecodeBot AI: My name is DecodeBot AI, your smart assistant 🤖")

    # Thank you
    elif user_input in [
        "thanks", "thank you",
        "thx", "thanks a lot"
    ]:
        print("DecodeBot AI: You're welcome! Happy to help 😊")

    # Current time
    elif user_input == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"DecodeBot AI: Current time is {current_time}")

    # Current date
    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"DecodeBot AI: Today's date is {current_date}")

    # Motivation
    elif user_input == "motivate me":
        print("DecodeBot AI: Believe in yourself! Every expert was once a beginner 🚀")

    # What is AI
    elif user_input == "what is ai":
        print("DecodeBot AI: Artificial Intelligence (AI) is technology that enables machines to think, learn, and solve problems like humans.")

    # Exit condition
    elif user_input in [
        "exit", "bye",
        "goodbye", "bye bye", "quit"
    ]:
        print("DecodeBot AI: Goodbye! Have a great day 🚀")
        break

    # Unknown input
    else:
        print("DecodeBot AI: Sorry, I didn't understand that.")
        print("Please type 'help' to see available commands.")