import pyttsx3
import numpy as np
import wikipedia
import os

# --- Helper Functions ---

def clear_screen():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def speak(text):
    """
    Solves the 'one-sentence-only' bug by re-initializing 
    the engine for every speech command.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # Important to stop the engine after each use

# --- Logic Functions ---

def matrix_task():
    """Handles matrix creation and analysis."""
    clear_screen()
    print("\n--- Matrix Task ---")
    try:
        row = int(input("Enter number of rows: "))
        column = int(input("Enter number of columns: "))
        
        elements = []
        for i in range(row * column):
            num = int(input(f"Enter element {i+1}: "))
            elements.append(num)

        my_array = np.array(elements).reshape(row, column)
        print("\nYour final Matrix:\n", my_array)

        min_elm = np.min(my_array)
        max_elm = np.max(my_array)
        result_msg = f"Minimum: {min_elm}, Maximum: {max_elm}"
        print(result_msg)

        with open("matrix_output.txt", "w") as f:
            f.write(f"--- Data Report ---\nMatrix:\n{my_array}\nAnalysis: {result_msg}\n")

        speak(f"Analysis complete. The minimum is {min_elm} and the maximum is {max_elm}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to return to menu...")

def wikipedia_search():
    """Searches Wikipedia and appends info to the report."""
    clear_screen()
    print("\n--- Wikipedia Search ---")
    query = input("Enter a topic to search on Wikipedia: ")
    
    try:
        result = wikipedia.summary(query, sentences=2)
        print(f"\nSummary for '{query}':\n{result}")
        
        with open("matrix_output.txt", "a") as f:
            f.write(f"\nWikipedia Search: {query}\nSummary: {result}\n" + "-"*30 + "\n")

        speak(f"I found this about {query}")
        speak(result) # Here it will speak the second sentence without hanging!
        
    except Exception:
        error_msg = "Sorry, I could not find that topic."
        print(error_msg)
        speak(error_msg)
        
    input("\nPress Enter to return to menu...")

# --- Main Interaction Loop ---

# Initial Welcome
clear_screen()
speak("Welcome to the Smart Assistant. Please select an option from the menu.")

while True:
    clear_screen()
    print("\n" + "="*30)
    print("   SMART ASSISTANT MENU")
    print("="*30)
    print("1. Create Matrix & Analyze")
    print("2. Search Wikipedia & Append Info")
    print("3. Open Results File (Report)")
    print("4. Exit Program")
    print("="*30)
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        matrix_task()
    elif choice == '2':
        wikipedia_search()
    elif choice == '3':
        if os.path.exists("matrix_output.txt"):
            print("Opening report file...")
            os.startfile("matrix_output.txt")
        else:
            print("No report file found.")
        input("\nPress Enter to continue...")
    elif choice == '4':
        print("Exiting program. Goodbye!")
        speak("Thank you for using the assistant. Goodbye!")
        break
    else:
        print("Invalid selection.")
        speak("Invalid selection, please try again.")
        input("\nPress Enter to continue...")
