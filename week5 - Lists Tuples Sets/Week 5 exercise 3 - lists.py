print("\n ******** 3(a) - Write a program which inputs a sentence from the user (a series of words, such as a famous quote or line of a song), then uses a for loop to display each word and the length of each word. ********\n ")

myString = "hello this is a string with lots of words"

# Split the list into an array
list = myString.split(" ")
word_length_list = []

count = 0

for word in list :
    print(word, len(word))                  # Print all the words entered and their lenght
    word_length_list.append(len(word))      # Keep a list of the word lengths
    count += len(word)                      # keep a running totol of the words lengths








print("\n ******** 3(b) - )Modify the program so that it uses a list to store the word lengths, and then determines and displays:  ********\n ")

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








print(" \n ******** 3(a) solution ******** \n ")

sentence = "It was a bright cold day in april and the clocks were striking thirteen"
print(f"{'Word' :<8} Length")

for word in sentence.split():
    print(f"{word:<8} {len(word):>4}")








print(" \n ******** 3(b) solution ******** \n ")