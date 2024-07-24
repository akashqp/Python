# class PossibleOutcomes:

#     def __init__(self):
#         self.combinations = set()

#     def count_outcomes(self, target, denominations, combination=[]):
#         # Base case
#         if target == 0:
#             # Add the combination to the set using union
#             self.combinations = self.combinations.union({tuple(sorted(combination))})
#             print(combination)  # Print the combination
#             return 1
#         if target < 0:
#             return 0
        
#         # Initialize the count
#         count = 0

#         # Iterate through the denominations
#         for i in denominations:
#             count += self.count_outcomes(target - i, denominations, combination + [i])
#         return count, self.combinations
    
# # Create object of the class
# outcomes = PossibleOutcomes()

# target = 5
# denominations = {1, 2, 5, 10}

# # Call the method to count possible outcomes
# count, combinations = outcomes.count_outcomes(target, denominations)
# print("Possible outcomes are", count)
# print("Combinations are", combinations)


class PossibleOutcomes:
    def count_outcomes(self, sum, n, coins = []):
        if sum == 0:
            return 1
        if sum < 0:
            return 0
        if n <= 0:
            return 0
        
        return self.count_outcomes(sum, n - 1, coins) + self.count_outcomes(sum - coins[n - 1], n, coins)
    
# Create object of the class
outcomes = PossibleOutcomes()

coins = [1, 2, 5, 10]
sum = 5
n = len(coins)

# Call the method to count possible outcomes
count = outcomes.count_outcomes(sum, n, coins)
print("Possible outcomes are", count)

        