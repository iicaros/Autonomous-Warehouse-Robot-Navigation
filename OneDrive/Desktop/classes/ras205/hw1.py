import math

class Vector:
    def __init__(self, components=None):                                                                        # a) Initialize components; default is <0, 0, 0>
        if components is None:
            components = [0, 0, 0]
        self.components = components

    @staticmethod
    def create(components=None):                        
        return Vector(components)

    def magnitude(self):                                
        return math.sqrt(sum(comp**2 for comp in self.components))                                              # b) Calculate the magnitude

    def dimensionality(self):                                                                                   # c) Return the dimensionality of the vector
        return len(self.components)

    def get_component(self, index):                                                                             # d) Get the respective component by index (continued below)                    
        if 0 <= index < len(self.components):
            return self.components[index]
        else:
            raise IndexError("Index out of range")

    def set_component(self, index, value):                                                                      # e) Modify component at a given index (continiued below)
        if 0 <= index < len(self.components):
            self.components[index] = value
        else:
            raise IndexError("Index out of range")

    def __add__(self, other):                                                                                   # f) Overloaded addition of v1 and v2 using zip hint from class (continued below)
            if not isinstance(other, Vector):
                raise TypeError("Can only add another Vector object")
            if self.dimensionality() != other.dimensionality():
                raise ValueError("Vectors must have the same dimensionality")

            new_components = [a + b for a, b in zip(self.components, other.components)]
            return Vector(new_components)

    def dot_product(self, other):                                                                               # g) Dot product of v1 and v2 (continued below)
        if self.dimensionality() != other.dimensionality():
            raise ValueError("Vectors must have the same dimensionality to compute dot product.")

        return sum(a * b for a, b in zip(self.components, other.components))




# - - - - - - - - - - - - - - - - - - - User Interaction - - - - - - - - - - - - - - - - - - - -



user_input = input("\nEnter vector components separated by spaces: ")
components = list(map(int, user_input.split()))                                                                         # Vector creation by converting user input into list
v1 = Vector.create(components)  

# Output initial results
print("\nVector Components:", v1.components)
print("Magnitude:", v1.magnitude())
print(f"Dimensionality: {v1.dimensionality()}D")

                                                                                            
retrieve_choice = input("\nDo you want to retrieve a component? (y/n): ").strip().lower()                       # d) Get Component continued
if retrieve_choice == 'y':
    try:
        index = int(input("\nEnter the index of the component you want to retrieve: "))
        print(f"\nComponent at index {index}:", v1.get_component(index))
    except (IndexError, ValueError) as e:
        print("Error:", e)

                                                                                                           
modify_choice = input("\nDo you want to modify a component? (y/n): ").strip().lower()                           # e) Modify component continued

if modify_choice == 'y':
    try:
        index_to_set = int(input("\nEnter the index of the component you want to modify: "))
        new_value = int(input("Enter the new value for this component: "))
        v1.set_component(index_to_set, new_value)

        print("\nUpdated Vector Components:", v1.components)                                                             # Output updated results
        print("Magnitude:", v1.magnitude())
        print(f"Dimensionality: {v1.dimensionality()}D")

    except (IndexError, ValueError) as e:
        print("Error:", e)

if modify_choice == 'n':

        print("\nUpdated Vector Components:", v1.components)                                                             # Output updated results
        print("Magnitude:", v1.magnitude())
        print(f"Dimensionality: {v1.dimensionality()}D")



add_choice = input("\nDo you want to add another vector? (y/n): ").strip().lower()                              # f) Add vector continued
if add_choice == 'y':
    user_input2 = input("\nEnter the components of the second vector separated by spaces: ")
    components2 = list(map(int, user_input2.split()))  
    v2 = Vector.create(components2)  

    try:

        print("\nSecond Vector Components:", v2.components)                                                             # Output updated results
        print("Magnitude:", v2.magnitude())
        print(f"Dimensionality: {v2.dimensionality()}D")
    

        v3 = v1 + v2  
        print("\n\nResultant Vector Components:", v3.components)
        print("Magnitude:", v3.magnitude())
        print(f"Dimensionality: {v3.dimensionality()}D\n")

        dot_product_result = v1.dot_product(v2)                                                                 # g) Dot product continued
        print("\nDot Product of Vectors One and Two:", dot_product_result)

    except (TypeError, ValueError) as e:
        print("Error:", e)
