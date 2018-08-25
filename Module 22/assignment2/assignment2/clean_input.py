'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
	string1 = re.sub('[^a-z ]', '', string)
	string1.replace(" ","")
	return string1.strip()

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
