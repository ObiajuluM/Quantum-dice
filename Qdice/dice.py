import qsharp
from Qrng import SampleQuantumRandomNumberGenerator # We import the 
# quantum operation from the namespace defined in the file Qrng.qs
max = 6 # Here we set the maximum of our range  # edit this to create the dice
output = max + 1 # Variable to store the output
while output > max:
    bit_string = [] # We initialise a list to store the bits that will define our random integer
    # .bit_length will return the number of bits required to represent an integer in binary excluding the signs and leading zeros
    for i in range(0, max.bit_length()): # We need to call the quantum
        # operation as many times as bits are needed to define the
        # maximum of our range. For example, if max=7 we need 3 bits
        # to generate all the numbers from 0 to 7. 
        bit_string.append(SampleQuantumRandomNumberGenerator.simulate()) 
        # Here we call the quantum operation and store the random bit
        # in the list
    output = int("".join(str(x) for x in bit_string), 2) 
# Transform bit string to integer

    if output == 1:
        print(""" the quantum dice rolled:
            -----------------
            |               |
            |               |
            |       o       |
            |               |
            |               |
            -----------------
            """)
    elif output == 2:
        print(""" the quantum dice rolled:
            -----------------
            |               |
            |               |
            |    o     o    |
            |               |
            |               |
            -----------------
            """)   
    elif output == 3:
         print(""" the quantum dice rolled:
            -----------------
            |               |
            |       o       |
            |       o       |
            |       o       |
            |               |
            -----------------
            """)
    elif output == 4:
         print(""" the quantum dice rolled:
            -----------------
            |               |
            |    o     o    |
            |               |
            |    o     o    |
            |               |
            -----------------
            """)
    elif output == 5:
        print(""" the quantum dice rolled:
            -----------------
            |               |
            |    o     o    |
            |       o       |
            |    o     o    |
            |               |
            -----------------
            """)
    elif output == 6:
        print(""" the quantum dice rolled:
            -----------------
            |               |
            |  o    o    o  |
            |               |
            |  o    o    o  |
            |               |
            -----------------
            """)
else:
    exit()
