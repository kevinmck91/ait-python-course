
import math

try :
    
    with open("./data/beowulf.txt", encoding="utf8") as word_file :
        
        contents = word_file.read()
        
        print(f"Number of characters : {len(contents)}")
       
        list_of_words = contents.split(" ")
        print(f"Number of Words : { len(list_of_words) }" )
        
        list_of_lines = contents.splitlines()
        print(f"Number of Lines : {len(list_of_lines)}")
        
        
        word_lengths = [len(x) for x in list_of_words]
        
        mean_word_length = sum(word_lengths) / len(word_lengths)
        
        print(f"Mean_word_length : {mean_word_length}")
        print(f"Mean_word_length : {mean_word_length}")
        print(f"Max_word_length : {max(word_lengths)}")
       
except : 
    
    print("unable to locate file")
     
     
