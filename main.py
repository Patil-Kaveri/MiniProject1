def get_user_friend_lists():
    """
    Collects friend lists for multiple users from user input.
    Returns a dictionary where keys are user names and values are sets of their friends.
    """
    print("Enter friend lists for multiple users.")
    print("Input format: username: friend1, friend2, friend3")
    print("Type 'done' when finished.")

    user_friends = {}

    while True:
        entry = input("Enter user and friends: ")
        if entry.lower() == 'done':
            break

        try:
            user, friends = entry.split(":")
            user = user.strip()
            friends = set(friend.strip() for friend in friends.split(",") if friend.strip())
            user_friends[user] = friends
        except ValueError:
            print("Invalid format. Please use the format: username: friend1, friend2, friend3")

    return user_friends


def find_common_friends(user_friends):
    """Finds common friends among all users."""
    all_friend_sets = list(user_friends.values())
    if not all_friend_sets:
        return set()
    common = set.intersection(*all_friend_sets)
    return common


def find_all_friends(user_friends):
    """Finds all unique friends across all users."""
    all_friend_sets = list(user_friends.values())
    if not all_friend_sets:
        return set()
    all_friends = set.union(*all_friend_sets)
    return all_friends


def find_mutual_friends(user_friends, user1, user2):
    """Finds mutual friends between two specific users."""
    friends1 = user_friends.get(user1, set())
    friends2 = user_friends.get(user2, set())
    mutual = friends1 & friends2
    return mutual


def main():
    user_friends = get_user_friend_lists()

    if not user_friends:
        print("No data provided.")
        return

    while True:
        print("\nOptions:")
        print("1. Find common friends among all users")
        print("2. Find all unique friends")
        print("3. Find mutual friends between two users")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            common = find_common_friends(user_friends)
            print("Common friends among all users:", common if common else "None")

        elif choice == "2":
            all_friends = find_all_friends(user_friends)
            print("All unique friends:", all_friends if all_friends else "None")

        elif choice == "3":
            user1 = input("Enter the first user: ").strip()
            user2 = input("Enter the second user: ").strip()

            if user1 not in user_friends or user2 not in user_friends:
                print("One or both users not found.")
            else:
                mutual = find_mutual_friends(user_friends, user1, user2)
                print(f"Mutual friends between {user1} and {user2}:", mutual if mutual else "None")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
