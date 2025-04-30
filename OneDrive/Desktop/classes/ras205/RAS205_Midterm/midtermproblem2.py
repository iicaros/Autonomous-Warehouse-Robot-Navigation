# Wasn't sure how to go about this problem but I wrote two solutions: 
    # The first one just returns the sum of the vector since its all 0s and 1s

    # The second one actually counts the number of 1s

def count_obstacles1(vector):
        return sum(vector)

print(f"Obstacle(s): {count_obstacles1([0, 0, 1, 0, 0, 0])}")
print(f"Obstacle(s): {count_obstacles1([0, 1, 0, 1, 1, 1])}")



def count_obstacles2(vector):
    o = vector.count(1)
    return o

print("\n" f"Obstacle(s): {count_obstacles2([0, 0, 1, 0, 0, 0])}")
print(f"Obstacle(s): {count_obstacles2([0, 1, 0, 1, 1, 1])}")