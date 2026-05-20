# Program: Jeopardy
# Purpose: A Jeopardy game that quizzes the player on BJC concepts across 3 categories.
#          The player picks a category and point value each round, answers clues, and earns a final score.
# By:  Varenya Kale


# This is the data board. It holds 3 main categories and 3 clues in each category. 
# Each clue has a point value, a clue string, and the correct answer.

board = [
    {
        "category": "Programming Basics",
        "clues": [
            {
                "value": 100,
                "clue": "This is a named group of programming instructions "
                        "that can have parameters and return values.",
                "answer": "procedure"
            },
            {
                "value": 200,
                "clue": "Repeating a section of code a set number of times "
                        "or until a condition is met is called this.",
                "answer": "iteration"
            },
            {
                "value": 300,
                "clue": "This type of statement executes different code "
                        "depending on whether a condition is true or false.",
                "answer": "selection"
            }
        ]
    },
    {
        "category": "Data and Abstraction",
        "clues": [
            {
                "value": 100,
                "clue": "An ordered sequence of elements stored under "
                        "a single variable name.",
                "answer": "list"
            },
            {
                "value": 200,
                "clue": "Hiding the complexity of how something works "
                        "and only showing what is needed to use it.",
                "answer": "abstraction"
            },
            {
                "value": 300,
                "clue": "A programming technique where a procedure "
                        "calls itself as part of its own algorithm.",
                "answer": "recursion"
            }
        ]
    },
    {
        "category": "Internet and Society",
        "clues": [
            {
                "value": 100,
                "clue": "The set of communication rules that controls "
                        "how data is sent and received across the internet.",
                "answer": "protocol"
            },
            {
                "value": 200,
                "clue": "The process of scrambling data so only "
                        "the intended recipient can read it.",
                "answer": "encryption"
            },
            {
                "value": 300,
                "clue": "A negative effect of computing that was not "
                        "intended by the original developers.",
                "answer": "unintended consequence"
            }
        ]
    }
]


# Procedure: display_board
# Purpose: Prints the current state of the game board, showing which clue values are still available in every category.
#          Clues already played are shown as [---] so the player can see which spots are still open.
#          This procedure is called at the start of each round to give the player an updated view of the board before they pick their next clue.
# Parameters:
#   played_clues which is a list of (category_index, value) tuples that tracks every clue already answered
# Returns: nothing 
# Algorithm:
#   1. Print the top row of the Jeopardy board
#   2. Go through each category in the board list
#   3. Go through each clue inside that category
#   4. Check whether that clue has already been picked
#   5. Print the value if it is still available, or [---] if it was already picked
def display_board(played_clues):
    print(f"\n{'CATEGORY':<20} {'$100':>6} {'$200':>6} {'$300':>6}")

    # Iterate through every category in the board list
    for cat_index, category in enumerate(board):
        row = f"{category['category']:<20}"

        # Iterate through each clue in this category
        for clue in category["clues"]:
 
            # Check if this specific clue has already been played
            if (cat_index, clue["value"]) in played_clues:  # selection
                row += f"{'[---]':>6}" # if it was played, show [---]
            else:
                row += f"{'$' + str(clue['value']):>6}"  # otherwise show the point value

        print(row)


# Procedure: play_clue
# Purpose: Handles one interaction with the Jeopardy clues. Finds
#          the chosen clue in the category, displays it, takes
#          the player's answer, checks it, and returns the
#          points earned. (0 if incorrect, or the clue value if correct)
#          This is one of the main procedures because it uses a loop,
#          checks conditions, and updates the game score.
# Parameters:
#   category_data  - a dictionary with one category's name and clues
#   chosen_value   - the integer point value the player selected
#   cat_index      - the index of this category in the board list
#   played_clues   - a list of (cat_index, value) tuples
# Returns: a number which is the points earned this round 
# Algorithm:
#   1. Start with 0 points earned
#   2. Look through the clues until the selected value is found
#   3. Show the clue and ask the player for an answer
#   4. Check if the answer matches the correct answer
#   5. Add points if the player is correct
#   6. Mark the clue as played and return the points earned
def play_clue(category_data, chosen_value, cat_index, played_clues):
    points_earned = 0  # start at 0 and only update if answer is correct

    # Iterate through all clues in this category to find the chosen one
    for clue in category_data["clues"]:

        # Selection: only proceed if this clue matches the chosen value
        if clue["value"] == chosen_value:

            # Display the clue to the player
            print(f"\nCategory: {category_data['category']} - ${chosen_value}")
            print(f"Clue: {clue['clue']}")
            print("(Answer in the form of a word or short phrase)")

            # Normalize player's answer to lowercase
            player_answer = input("Your answer: ").strip().lower()

            # Selection: check if the player's answer matches the correct answer
            if player_answer == clue["answer"].lower():
                print(f"Correct! You earn ${chosen_value}.")
                points_earned = chosen_value 
            else:
            
                print(f"Incorrect. The answer was: {clue['answer']}")
                print("No points deducted - keep going!")

            # Mark this clue as played 
            played_clues.append((cat_index, chosen_value))

    # Return how many points were earned this round 
    return points_earned


# Procedure: get_valid_category
# Purpose: Prompts the player to pick a category number and validates the input. 
#          Keeps asking until the player enters 1, 2, or 3 which are valid inputs.
# Parameters: none
# Returns: number which stands for the valid category index 
# Algorithm:
#   1. Keep asking until the player types a real category number
#   2. Check whether the input is 1, 2, or 3
#   3. If it is valid, return the matching list index
#   4. If it is not valid, tell the player to try again
def get_valid_category():
    valid_options = [str(i + 1) for i in range(len(board))]

    # Iterate until the player gives a valid category number
    while True:
        choice = input("Choose a category (1, 2, or 3): ")

        # Selection: check if the input matches one of the valid options
        if choice in valid_options:
            return int(choice) - 1 
        else:
            print("Please enter 1, 2, or 3.")


# Procedure: get_valid_value
# Purpose: Prompts the player to pick a point value (100, 200, or 300) from the chosen category 
#          Validates that it exists and has not already been played.
# Parameters:
#   category_data - the chosen category's dictionary 
#   cat_index     - the index of the category, used to check played_clues
#   played_clues  - the list of already-played (cat_index, value) tuples
# Returns: number which is a valid, unplayed point value integer
# Algorithm:
#   1. Make a list of point values that are still available
#   2. Ignore any values that were already picked earlier
#   3. Ask the player for a value from the available list
#   4. Keep asking until they choose one that is allowed
def get_valid_value(category_data, cat_index, played_clues):

    # Build the list of clue values still available in this category
    available = []
    for clue in category_data["clues"]:  # iteration
        if (cat_index, clue["value"]) not in played_clues:  # selection
            available.append(clue["value"])

    # If no clues are left in this category, signal back to main
    if len(available) == 0:
        return None

    available_strings = [str(v) for v in available]

    print(f"Available values: {available}")

    # Iterate until the player picks a valid available value
    while True:
        value_input = input("Choose a point value: ")

        # Selection: check if the typed value matches one of the available options
        if value_input in available_strings:
            return int(value_input)  
        else:
            print(f"Pick one of these values: {available}")


# Procedure: main
# Purpose: Displays the board,
#          lets the player pick clues, calls play_clue each round,
#          accumulates the total score, and prints the final result.
# Parameters: none
# Returns: nothing 
# Algorithm:
#   1. Start the score at 0 and make an empty played_clues list
#   2. Count how many clues are in the game
#   3. Keep running rounds until all clues have been picked
#   4. Each round, show the board and ask for a category and value
#   5. Call play_clue and add the points earned to the score
#   6. When the game is over, show the final score and message
def main():
    score = 0          # tracks the player's total points 
    played_clues = []  # list of (cat_index, value) tuples already played

    # Count how many clues are in the game
    total_clues = 0
    for category in board:  # iteration
        total_clues += len(category["clues"])

    print("\nWelcome to Jeopardy!")
    print("Test your knowledge of programming concepts.")
    print("Answer correctly to earn points!\n")

    # Keep playing rounds until every clue has been used
    while len(played_clues) < total_clues:  # iteration

        # Display the current board with played/available clues
        display_board(played_clues)
        print(f"\nCurrent Score: ${score}")
        print("\nCategories:")

        # Iterate through board to print numbered category names
        for i, category in enumerate(board):    # iteration
            print(f"  {i + 1}. {category['category']}")

        # Get a valid category choice from the player
        cat_index = get_valid_category()
        chosen_category = board[cat_index]

        # Get a valid point value from the chosen category
        chosen_value = get_valid_value(chosen_category, cat_index, played_clues)

        # Selection: if no values are left in that category, tell the player
        if chosen_value is None:
            print("No clues left in that category! Pick another one.")
            continue  # go back to the top of the loop

        # Run the clue and add whatever points the player earned
        score += play_clue(chosen_category, chosen_value, cat_index, played_clues)

    # All clues have been played, end the game and show final score
    print("\nGame over! All clues have been answered.")
    print(f"Final Score: ${score}\n")

    # Determine and display a performance message based on final score
    max_score = 100 + 200 + 300  # max per category
    max_score *= len(board)      # times number of categories

    # Selection: pick a message based on how well the player did
    if score == max_score:
        print("Perfect score! You're an expert!")
    elif score >= max_score * 0.7:
        print("Great job! You have a strong understanding of the material.")
    elif score >= max_score * 0.4:
        print("Good effort! Review the topics you missed.")
    else:
        print("Keep studying - you'll get there!")


if __name__ == "__main__":
    main()
