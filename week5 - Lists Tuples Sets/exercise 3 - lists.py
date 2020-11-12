## Write a program which inputs a sentence from the user (a series of words, such as a famous quote or line of a song), then uses a for loop to display each word and the length of each word.
print("\n ******** 3(a) -  ********\n ")

myString = "hello this is a string with lots of words"

# Split the list into an array
list = myString.split(" ")
word_length_list = []

count = 0

for word in list :
    print(word, len(word))                  # Print all the words entered and their lenght
    word_length_list.append(len(word))      # Keep a list of the word lengths
    count += len(word)                      # keep a running totol of the words lengths





## 3(a) solution
print(" \n ******** 3(a) solution ******** \n ")

sentence = "It was a bright cold day in april and the clocks were striking thirteen"
print(f"{'Word' :<8} Length")

for word in sentence.split():
    print(f"{word:<8} {len(word):>4}")







## Modify the program so that it uses a list to store the word lengths, and then determines and displays:
print("\n ******** 3(b)  ********\n ")

print("total Words : ", len(list))
print("Total number of letters : ", count)
print("Average Letters per word : ", count/len(list))
print("Maximum word length : ", max(word_length_list))
print("Minimum word length : ", min(word_length_list))

word_length_list.sort()
list.sort()
length = len(word_length_list)

# 1,2,3,4,5

if length % 2 != 0 :
    length_half = int(length/2)
    middle_value_list = word_length_list[length_half]
    print(f"median Word : {list[length_half]} , Median word length : {middle_value_list}")
else :
    length = length + 1
    length_half = length / 2
    combined_middle = word_length_list[int(length_half)] + word_length_list[int(length_half - 1)]
    average_middle = combined_middle / 2
    print(f"median Words : {list[int(length_half)]} and {list[int(length_half -1 )]} , Median word length : {average_middle}")






## calculate the mode of the word lengths, that is, it determines the most common word length in the sentence.
print(" \n ******** 3(c)  ******** \n ")

sentence = "Hello hello hello my name is kevin"

# Get a list of each length for each word  [5, 5, 5, 2, 4, 2, 5]
lenghts = [len(word) for word in sentence.split()]   
print("lenghts = " , lenghts ) 

# 5
max_length = max(lenghts) 
print("max_length = " , max_length ) 

# Get a list of frequencies of each word length (from smallest word to biggest word)
frequencies = [lenghts.count(x) for x in range(max_length + 1)]
print("frequencies = " , frequencies ) 

print("\nLength" , "Frequency")
   
for i in range(1, len(frequencies)):
    print(f"{i:^3} {frequencies[i]:^5}")