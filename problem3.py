#3. Reversed Binary Numbers (Difficulty Level: Easy)

#ProblemID: Reversebinary

#stock-footage-abstract-cgi-motion-graphics-and-animated-background-with-binary-numbers

#Yi has moved to Sweden and now goes to school here. The first years of schooling she got in China, and the curricula do not match completely in the two countries. Yi likes mathematics, but now… The teacher explains the algorithm for subtraction on the board, and Yi is bored. Maybe it is possible to perform the same calculations on the numbers corresponding to the reversed binary representations of the numbers on the board? Yi dreams away and starts constructing a program that reverses the binary representation, in her mind. As soon as the lecture ends, she will go home and write it on her computer.

#Task

#Your task will be to write a program for reversing numbers in binary. For instance, the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.

#Input

#The input contains a single line with an integer N, 1 ≤ N ≤ 1000000000.

#Output

#Output one line with one integer, the number we get by reversing the binary representation of N.

#Sample input 1
#13
#Sample output 1
#11
#Sample input 2
#47
#Sample output 2
#61


# takes decimal number as an input and returns its reversed binary representation as a decimal number
# 1.convert dec to bin 2.reverse binary represenation 3. convert bin to dec
def revBinNums(number):
    print(int(bin(int(bin(number)[2:][::-1],2))[2:],2))

revBinNums(int(input()))
