
# input is a FASTA format DNA file that returns an array with each element a string object that is a single strand of DNA and is sorted from shortest to longest.
def parse_DNA(text_file):
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
    
# finds all substrings in the shortest strand of DNA and put them in an array from longest to shortest
def find_substrings(strand):
    substrings = []
    length = len(strand)
    for i in range(length):
        for j in range(length-1):
            j += 1
            if i+j > length: break
            string = strand[i:i+j]
            if string not in substrings:
                substrings.append(string)
    substrings.sort(key = len, reverse = True)
    return(substrings)
   
# iterates over the substring arrray and checks to see if it is contained in all the DNA strands. If it is present in all strands the substring is returned. 
def find_longest_shared(DNA, substrings):
    for sub in substrings:
        count = 0
        for strand in DNA:
            if sub not in strand:
                break
            else:
                count += 1
            print(count)
        if count == len(DNA): return(sub)

DNA_arr = parse_DNA('sample.txt')
substrings = find_substrings(DNA_arr[0])
longest = find_longest_shared(DNA_arr, substrings)
# displays the longest shared substring
print(longest)