users = [{"username": 5}, {"someone": 15}, {"else": 3}, {"who": 2}]
# Sort user array
users.sort(key=lambda a: a[1], reverse=True)

# print(users)

# Format the users
leaderboard = map(lambda user: user[0] + "| " + str(user[1]), users)

# Output
print("\n".join(leaderboard))
