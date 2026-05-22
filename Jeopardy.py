# Program: Jeopardy
# Purpose: A Jeopardy-style review game for BJC concepts.
#          The intended user is a CSP student who wants quick practice with vocabulary.
#          The player chooses a category and point value, answers the clue, and earns points for correct answers.
# By: Varenya Kale


# List Section Evidence:
# The list named board stores all of the quiz data used by the program.
# Each item in board represents one category. Inside each category, the clues list stores
# the point value, clue text, and correct answer for each Jeopardy clue.
# Using this list prevents the program from needing separate variables for every category,
# clue, value, and answer.
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
# Purpose: Prints the current state of the game board.
#          Available clue values are shown as dollar amounts, and clues already played are shown as [---].
# Parameters:
#   played_clues - list of (category_index, value) pairs that tracks every clue already answered
# Returns: None
# How it interacts with the program:
#   main calls this procedure at the start of each round so the player can choose from the remaining clues.
# Algorithm:
#   1. Print the board header.
#   2. Traverse the board list category by category.
#   3. Traverse each category's clues list.
#   4. Use selection to decide whether each clue has already been played.
#   5. Print either the value or [---].
def display_board(played_clues: list[tuple[int, int]]) -> None:
    print(f"\n{'CATEGORY':<20} {'$100':>6} {'$200':>6} {'$300':>6}")

    # List Section Evidence:
    # This loop traverses the board list and uses its category/clue data to create the visible game board.
    for cat_index, category in enumerate(board):
        row = f"{category['category']:<20}"

        # Iteration: go through every clue stored in this category's clues list.
        for clue in category["clues"]:
            # Selection: decide whether this clue should still be available.
            if (cat_index, clue["value"]) in played_clues:
                row += f"{'[---]':>6}"
            else:
                row += f"{'$' + str(clue['value']):>6}"

        print(row)


# Procedure: play_clue
# Purpose: Runs one Jeopardy clue interaction.
#          It finds the chosen clue, displays it, gets the player's answer, checks the answer,
#          marks the clue as played, and returns the number of points earned.
# Parameters:
#   category_data - dictionary containing one category's name and clues list
#   chosen_value  - integer point value selected by the player
#   cat_index     - integer index of the selected category in board
#   played_clues  - list of (category_index, value) pairs already used
# Returns: int, the number of points earned this round
# How it interacts with the program:
#   main calls this procedure after the player selects a valid category and value.
#   The return value is added to score in main.
# Algorithm:
#   1. Start points_earned at 0.
#   2. Iterate through the clues in the chosen category.
#   3. Use selection to find the clue matching chosen_value.
#   4. Display the clue and collect the player's answer.
#   5. Use selection to compare the player's answer with the correct answer.
#   6. Update points_earned if the answer is correct.
#   7. Add the clue to played_clues so it cannot be selected again.
#   8. Return points_earned.
def play_clue(category_data: dict, chosen_value: int, cat_index: int,
              played_clues: list[tuple[int, int]]) -> int:
    points_earned = 0

    # Iteration: search through the clues list for the selected point value.
    for clue in category_data["clues"]:
        # Selection: only run the clue whose value matches the player's choice.
        if clue["value"] == chosen_value:
            print(f"\nCategory: {category_data['category']} - ${chosen_value}")
            print(f"Clue: {clue['clue']}")
            print("(Answer in the form of a word or short phrase)")

            # Input: get the player's answer and normalize it so capitalization and extra spaces do not matter.
            player_answer = input("Your answer: ").strip().lower()

            # Selection: compare the player's answer to the stored correct answer.
            if player_answer == clue["answer"].lower():
                print(f"Correct! You earn ${chosen_value}.")
                points_earned = chosen_value
            else:
                print(f"Incorrect. The answer was: {clue['answer']}")
                print("No points deducted - keep going!")

            # Add this clue to the played_clues list so later procedures know it is unavailable.
            played_clues.append((cat_index, chosen_value))

            # Efficiency: stop searching once the selected clue has been found and played.
            return points_earned

    # This should not happen because get_valid_value only allows existing values.
    print("That clue could not be found.")
    return points_earned


# Procedure: get_valid_category
# Purpose: Prompts the player to pick a category number and validates the input.
# Parameters: None
# Returns: int, the valid category index
# Algorithm:
#   1. Build a list of valid category choices based on the number of categories.
#   2. Repeatedly ask the player for a category number.
#   3. Use selection to check whether the input is valid.
#   4. Return the matching board index once a valid choice is entered.
def get_valid_category() -> int:
    valid_options = [str(i + 1) for i in range(len(board))]

    while True:
        choice = input("Choose a category (1, 2, or 3): ").strip()

        if choice in valid_options:
            return int(choice) - 1
        else:
            print("Please enter 1, 2, or 3.")


# Procedure: get_valid_value
# Purpose: Prompts the player to pick a valid, unplayed point value from the chosen category.
# Parameters:
#   category_data - dictionary containing the selected category's name and clues list
#   cat_index     - integer index of the selected category in board
#   played_clues  - list of (category_index, value) pairs already used
# Returns: int if a valid value is available, or None if the category has no clues left
# Algorithm:
#   1. Create an empty available list.
#   2. Traverse the chosen category's clues list.
#   3. Add only unplayed clue values to available.
#   4. If no values are available, return None.
#   5. Repeatedly ask the player for a value until the input matches an available value.
def get_valid_value(category_data: dict, cat_index: int,
                    played_clues: list[tuple[int, int]]) -> int | None:
    available = []

    # Iteration and list use: traverse the clues list to find values that have not been played.
    for clue in category_data["clues"]:
        # Selection: include this value only if it is not already in played_clues.
        if (cat_index, clue["value"]) not in played_clues:
            available.append(clue["value"])

    if len(available) == 0:
        return None

    available_strings = [str(v) for v in available]
    print(f"Available values: {available}")

    while True:
        value_input = input("Choose a point value: ").strip()

        if value_input in available_strings:
            return int(value_input)
        else:
            print(f"Pick one of these values: {available}")


# Procedure: main
# Purpose: Controls the overall game.
#          It initializes the score, tracks played clues, displays the board, gets choices,
#          calls play_clue, updates the score, and prints the final result.
# Parameters: None
# Returns: None
# Algorithm:
#   1. Start score at 0 and create an empty played_clues list.
#   2. Count the total number of clues stored in board.
#   3. Repeat rounds until every clue has been played.
#   4. During each round, show the board, get a category, get a value, and call play_clue.
#   5. Add the returned points to the score.
#   6. Print the final score and a performance message.
def main() -> None:
    score = 0
    played_clues = []

    # Count all clues by traversing the board list.
    total_clues = 0
    for category in board:
        total_clues += len(category["clues"])

    print("\nWelcome to Jeopardy!")
    print("Test your knowledge of programming concepts.")
    print("Answer correctly to earn points!\n")

    while len(played_clues) < total_clues:
        display_board(played_clues)
        print(f"\nCurrent Score: ${score}")
        print("\nCategories:")

        # List Section Evidence:
        # This loop uses the same board list to show the category choices to the player.
        for i, category in enumerate(board):
            print(f"  {i + 1}. {category['category']}")

        cat_index = get_valid_category()
        chosen_category = board[cat_index]
        chosen_value = get_valid_value(chosen_category, cat_index, played_clues)

        if chosen_value is None:
            print("No clues left in that category. Pick another one.")
            continue

        # Procedure Call Section Evidence:
        # main calls the student-developed procedure play_clue.
        # play_clue returns the points earned, and main uses that return value to update score.
        score += play_clue(chosen_category, chosen_value, cat_index, played_clues)

    print("\nGame over. All clues have been answered.")
    print(f"Final Score: ${score}\n")

    max_score = 100 + 200 + 300
    max_score *= len(board)

    if score == max_score:
        print("Perfect score!")
    elif score >= max_score * 0.7:
        print("Great job!")
    elif score >= max_score * 0.4:
        print("Good effort!")
    else:
        print("Keep studying!")


if __name__ == "__main__":
    main()
