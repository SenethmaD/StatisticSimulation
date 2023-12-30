import random

def simulate_dice_throw(num_throws):
    count_32 = 0
    for _ in range(num_throws):
        throws = [random.randint(1, 6) for _ in range(10)]
        if sum(throws) == 32:
            count_32 += 1
    probability = count_32 / num_throws
    return probability

num_throws = 500
result = simulate_dice_throw(num_throws)
print(f"\nProbability of getting a sum of 32 in 10 dice throws for {num_throws} simulations: {result}\n")



#evidence to show that the simulation works
import random 

def simulate_dice_throw(num_throws): 
    # Initialize a counter for the occurrences of a sum of 32     
            count_32 = 0 
 
    # Iterate for the specified number of throws     
            for _ in range(num_throws): 
        # Simulate 10 dice throws and store the results in a list         
                    throws = [random.randint(1, 6) for _ in range(10)] 
 
        # Check if the sum of the throws is 32         
                    if sum(throws) == 32: 
                        count_32 += 1 
 
    # Calculate the probability of getting a sum of 32     
                        probability = count_32 / num_throws     
                        return probability 
 
if __name__ == "__main__": 
    # Get the number of simulations from the user     
        num_throws = int(input("Enter the number of simulations: ")) 
 
    # Run the simulation and get the result     
        result = simulate_dice_throw(num_throws) 
 
    # Display the probability based on user input    
        print(f"\nProbability of getting a sum of 32 in 10 dice throws for {num_throws} simulations: {result}\n") 