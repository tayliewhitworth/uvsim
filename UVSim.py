
# Team collaboration
class UVSim:
    def __init__(self, read_callback=None, write_callback=None, halted=None):
        self.memory = [0]*100
        self.accumulator = 0
        self.instruction_counter = 0
        self.instruction_register = 0
        self.operation_code = 0
        self.operand = 0
        self.read_callback = read_callback
        self.write_callback = write_callback
        self.halted = halted


    # Team collaboration
    def load_program(self, filename):
        while True:
            try:
                # filename = input("Enter the name of the file to load: ")
                with open(filename, 'r') as f:
                    for location, line in enumerate(f):
                        self.memory[location] = int(line.strip())
                break
            except FileNotFoundError:
                print("File not found. Try again.")

    # Taylies code
    def read_memory(self):
        if self.read_callback:
            value = self.read_callback()
            if value < -9999 or value > 9999:
                raise ValueError("Invalid input. Try again.")
            self.memory[self.operand] = value
        else:
            print('No read callback set')

    # Taylie's code
    def write_memory(self):
        # print(self.memory[self.operand])
        if self.write_callback:
            self.write_callback(self.memory[self.operand])
        else:
            print(f'No write callback set - print to console: {self.memory[self.operand]}')


    # Taylie's code
    def store_memory(self):
        self.memory[self.operand] = self.accumulator


    # Taylie's code
    def load_memory(self):
        self.accumulator = self.memory[self.operand]


    #Aubrey's code
    def addition(self):
        self.accumulator += self.memory[self.operand]

    #Aubrey's code
    def subtraction(self):
        self.accumulator -= self.memory[self.operand]

        
    # Cassidy's code
    def multiplication(self: object) -> None:
        """DOCUMENT."""
        # Check operand is a number
        if not isinstance(self.memory[self.operand], (int, float)):
            raise ValueError("Invalid operand: must be a number")

        #Calculate
        result = self.accumulator * self.memory[self.operand]
        #Truncate and store
        self.accumulator = result % 10000
        #self.accumulator *= self.memory[self.operand]


    # Cassidy's code
    def division(self: object) -> None:
        """DOCUMENT."""
        # Check operand is a number
        if not isinstance(self.memory[self.operand], (int, float)):
            raise ValueError("Invalid operand: must be a number")
        # Check operand is not 0
        if self.memory[self.operand] == 00:
            raise ValueError("Invalid operand: Cannot divide by 0")
        else:
            #self.accumulator //= self.memory[self.operand]
            #Calculate
            result = self.accumulator // self.memory[self.operand]
            #Truncate and store
            self.accumulator = result % 10000


    # Cassidy's code
    def halt(self: object) -> None:
        """DOCUMENT."""
        self.instruction_counter = self.operand
        if self.halted:
            self.halted()
        # sys.exit("Program Halted")


    # Robby's code
    def branch(self: object) -> None:
        """DOCUMENT."""
        match (-2 < self.operand and self.operand < len(self.memory)):
            case True: self.instruction_counter = self.operand - 1
            case False: 
                raise IndexError(f"Memory index '{self.operand}' not in range.")


    # Robby's code
    def branch_negative(self: object) -> None:
        """DOCUMENT."""
        if self.accumulator < 0:
            match (-2 < self.operand and self.operand < len(self.memory)):
                case True: self.instruction_counter = self.operand - 1
                case False: 
                    raise IndexError(f"Memory index '{self.operand}' not in range.")


    # Robby's code
    def branch_zero(self: object) -> None:
        """DOCUMENT."""
        if self.accumulator == 0:
            match (-2 < self.operand and self.operand < len(self.memory)):
                case True: self.instruction_counter = self.operand - 1
                case False: 
                    raise IndexError(f"Memory index '{self.operand}' not in range.")



    # Team collaboration
    def execute_program(self):
        while True:
            self.instruction_register = self.memory[self.instruction_counter]
            self.operation_code = abs(self.instruction_register) // 100
            self.operand = abs(self.instruction_register) % 100

            match self.operation_code:
                case 10:  # w/ READ
                    self.read_memory()
                case 11: # WRITE
                    self.write_memory()
                case 20: # LOAD
                    self.load_memory()
                case 21: # STORE
                    self.store_memory()
                case 30: # ADD
                    self.addition()
                case 31: # SUBTRACT
                    self.subtraction()
                case 32: # DIVIDE
                    self.division()
                case 33: # MULTIPLY
                    self.multiplication()
                case 40: # BRANCH
                    self.branch()
                case 41: # BRANCHNEG
                    self.branch_negative()
                case 42: # BRANCHZERO
                    self.branch_zero()
                case 43: # HALT
                    self.halt()
                    break
                case _:
                    print(
                        f"Invalid operation code '{self.operation_code}'. \n"
                        "Program terminated"
                    )
                    break
    
            self.instruction_counter += 1


# def main():
#     """Main script driver."""
#     uv_sim = UVSim()
#     uv_sim.load_program()
#     uv_sim.execute_program()

#     pass

# if __name__ == "__main__":
#     main()

