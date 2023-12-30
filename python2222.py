from itertools import product
def count_ways_to_sum(target_sum, num_dice, num_sides):
    count = 0
    for roll in product(range(1, num_sides + 1), repeat=num_dice):
        if sum(roll) == target_sum:
            count += 1
    return count

target_sum = 32
num_dice = 10
num_sides = 6

total_outcomes = num_sides ** num_dice
ways_to_sum_target = count_ways_to_sum(target_sum, num_dice, num_sides)
exactProbability = ways_to_sum_target / total_outcomes

print("Exact Probability Calculation:", exactProbability)

# evidence to show that the simulation works
from itertools import product

def count_ways_to_sum(target_sum, num_dice, num_sides):
    count = 0
    for roll in product(range(1, num_sides + 1), repeat=num_dice):
        if sum(roll) == target_sum:
            count += 1
    return count

target_sum = int(input("\nEnter the target sum: "))
num_dice = int(input("Enter the number of dice rolls: "))
num_sides = int(input("Enter the number of sides on each die: "))

total_outcomes = num_sides ** num_dice
ways_to_sum_target = count_ways_to_sum(target_sum, num_dice, num_sides)
exactProbability = ways_to_sum_target / total_outcomes

print("Exact Probability Calculation:", exactProbability)