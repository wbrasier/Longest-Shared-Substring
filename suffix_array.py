import sys

# Table class that holds the suffix array. 
class Table:

    # builds the array and assigns each element to 0. The first length from the first string is how many arrays there are in the total array. The second one is how many elements are in each array.
    # first is vertical, second is horizontal
    def make_table(self, len1, len2):
        suffixes = [[0 for i in range(len1)] for j in range(len2)]
        return(suffixes)
    
    def __init__(self, length1, length2):
        self.table = self.make_table(length1, length2)
    
    def display_table(self):
        for line in self.table: 
            print(line)
            
    # updates the table value when a match is found. It adds 1 and if it is not in the first row/column then it adds what is to the upper left and reassigns the sum as the value. 
    def update_table(self, pos1, pos2):
        if pos1 > 0 and pos2 >0:
            self.table[pos1][pos2] = self.table[pos1-1][pos2-1]+1
        else:
            self.table[pos1][pos2] = 1
    
    # iterates over the table and if the value is over the specified minimum (I chose 10 because the strands are so long, then it saves the position and length into an arr) and returns the arr
    # the return is an array of 2 elements. The first is the end position of the first string that has the longest shared substring. The second is the length of the substring
    def find_highest(self):
        minimum_len = 10
        substring_pos = []
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                if self.table[i][j] >= minimum_len:
                    substring_pos.append([i, self.table[i][j]])
        return(substring_pos)



# DNA class that holds the string text of the DNA strands in an array with each element as a strand of DNA from the text file.
class DNA:

    # FASTA format DNA strands in a text file converted to an array
    def parse_DNA(self, text_file):
        DNA_strands = []
        count = -1
        with open(text_file, 'r') as text_file:
            lines = text_file.readlines()
            for DNA in lines:
                if DNA.startswith('>Rosalind'):
                    count +=1
                    DNA_strands.append('')
                else:
                    stripped = DNA.rstrip()
                    DNA_strands[count] += (stripped)
        DNA_strands.sort(key = len)
        return(DNA_strands)

    # initializes the DNA object as an array of the DNA as strings, and sorts it by length (short to long)
    def __init__(self, file):
        self.strands = self.parse_DNA(file)
        self.strands.sort(key = len)

    # iterates over the strands and compares the letters to see if there are any matches. If it matches it updates the table values
    def compare(self, arr):
        for i in range(len(self.strands[1])):
            for j in range(len(self.strands[0])):
                if self.strands[0][i] == self.strands[1][j]:
                    arr.update_table(i, j)
    
    # finds the substring from the end position and length of the substring and saves it in the class as self.longest
    # if the strand is not the longest from the first 2, it checks going backwards from the longest shared substring to the shortest
    def find_longest(self, sub_pos, from_end):
        info = sub_pos[-1-from_end]
        first_strand = self.strands[0]
        substring = first_strand[info[0]-info[1]+1:info[0]+1]
        self.longest = substring
        
    # all strands of DNA must contain the longest strand. Iterates over each strand and confirms if it contains it. Once the count reaches the amount of strands, it returns True. If the count does not reach ten it returns False.
    def confirm_longest(self):
        count = 2.      # count starts at 2 since the strand is in both
        for strand in self.strands[2:]:       # iteration starts at the 3rd
            if self.longest in strand:
                count += 1
                if count == len(self.strands)-1:
                    return(True)
            else:
                return(False)
                
    def display_longest(self):
        print(self.longest)


DNA = DNA('sample.txt')

# sends the lengths of the first two elements of the DNA array to make the table as the longest substring can't be longer than the shortest elements
arr = Table(len(DNA.strands[0]),len(DNA.strands[1]))
#arr.display_table()

# iterates over the strings and compares them, if they match it updates the table.
DNA.compare(arr)

positions = arr.find_highest()

# finds the longest substring between the first two strands of DNA
DNA.find_longest(positions, 0)

# iterates over the strands of DNA checking to see if they contain the longest substring. If they do not- it goes to the next longest (stored as the count which is the nth from longest) until the substring is found in all strands of DNA. Once it is found it is displayed
count = 0
while DNA.confirm_longest() != True:
    count += 1
    DNA.find_longest(positions, count)
else:
    DNA.display_longest()