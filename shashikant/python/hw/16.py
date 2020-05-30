import string
test_string = "Geeksforgeeks,    is best @# Computer Science Portal.!!!"


print("The original string is : " + test_string)


res = sum([i.strip(string.punctuation).isalpha() for i in test_string.split()])


print("The number of words in string are : " + str(res))