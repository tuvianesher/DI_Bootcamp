# Create a set called my_fav_numbers with your favorite numbers
my_fav_numbers = {1, 3, 5, 7}

# Add two new numbers to the set
my_fav_numbers.add(9)
my_fav_numbers.add(11)

# Remove the last number
my_fav_numbers.remove(11)

# Create a set called friend_fav_numbers with your friend's favorite numbers
friend_fav_numbers = {2, 4, 6, 8}

# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
