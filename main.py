def calculate_scoreboard(participants):
  """
  This function calculates the score for each participant in a competitive eating competition
  and returns a sorted scoreboard.

  Args:
      participants: A list of dictionaries representing participants. Each dictionary
                    should have keys "name", "chickenwings", "hamburgers", and "hotdogs".

  Returns:
      A list of dictionaries representing the scoreboard. Each dictionary should have
      keys "name" and "score". The list is sorted by score in descending order, and if
      scores are equal, then sorted alphabetically by name.
  """

  # Define the point values for each food item
  food_points = {
      "chickenwings": 5,
      "hamburgers": 3,
      "hotdogs": 2
  }

  # Calculate the total score for each participant
  scoreboard = []
  for participant in participants:
    total_score = 0
    for food, quantity in participant.items():
      if food in food_points:
        total_score += food_points[food] * quantity
    scoreboard.append({"name": participant["name"], "score": total_score})

  # Sort the scoreboard by score (descending) and then by name (ascending)
  scoreboard.sort(key=lambda participant: (-participant["score"], participant["name"]))

  # Print the scoreboard
  print(scoreboard)

# Example usage
participants = [
  {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
  {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
]

calculate_scoreboard(participants)

