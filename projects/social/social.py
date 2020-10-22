import random

# users = {1: {6, 7}, 2: {9}, 3: {8}, 4: {8}, 5: {10, 6}, 6: {
#     8, 1, 5}, 7: {8, 1, 10}, 8: {3, 4, 6, 7}, 9: {2}, 10: {5, 7}}


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Generate all possible friendship combinations
        possible_friendships = []  # [ (Friend_id_1, friend_id_2 )  ]
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # randomize the above array
        random.shuffle(possible_friendships)

        # Pick out num_users * avg_friendships number of friend combos from possible_friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        print(possible_friendships, "possibles")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        path = [[user_id]]
        visited = {}  # Note that this is a dictionary, not a set

        while len(path) > 0:
            current_path = path.pop(0)
            current_friend = current_path[-1]

        if current_friend not in visited:
            # Add the vertex to the visited set
            visited[current_friend] = path
            # Find the neighbors and add them to the path
            for friend in self.friendships[current_friend]:
                # copy the path array
                path_copy = path.copy()
                path_copy.append(friend)
                path.append(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
