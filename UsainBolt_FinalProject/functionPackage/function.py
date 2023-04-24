#Name: Usain Bolt
#email: mccoykp@mail.uc.edu, gogginjt@mail.uc.edu, allfreqy@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that I can use Eclipse to import text files, json files, and images to 
#eclipse, as well as displaying the image. This project also demonstrates that we are able to use functions correctly
#and follow the architecture of the class. Lastly, this project shows we are able to export our project to github 
#Citations: https://matplotlib.org/stable/tutorials/introductory/images.html
#https://rb.gy/8n9od
#Anything else that's relevant:
#function.py
import json
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
#The below snippet is the first english files code, and it works fine with that one,
#but with english 2, the count was off by 1
'''
def decrypt_json():
    with open('EncryptedGroupHints Spring 2023 Section 001 (1).json') as f:
        json_data = json.load(f)
    with open('english-2.txt') as txt:
        lines = txt.readlines()
        lns = [line.strip() for line in lines]
    print(lns)
    txtNum = json_data['Usain Bolt']
    theSearch = []
    num = 0
    for i in lns:
        num +=1
        theSearch.append(str(num))
    #print(theSearch)
    dictionary = dict(zip(theSearch,lns))
    #print(dictionary)
    for i in txtNum:
        print(dictionary[i])
'''        
#in this function, it is the exact same as the above, however our #num counter starts at -1
#to catch the new file's entries compared ot the original
def decrypt_json():
    with open('EncryptedGroupHints Spring 2023 Section 001 (1).json') as f:
        data = json.load(f)
    with open('english-2.txt') as txt:
        lines = txt.readlines()
        lns = [line.strip() for line in lines]
    txtNum = data['Usain Bolt']
    theSearch = []
    # num = -1 as our starting point
    num = -1
    for i in lns:
        num +=1
        theSearch.append(str(num))
    dictionary = dict(zip(theSearch,lns))
    for i in txtNum:
        print(dictionary[i])
        
        
def chic_fil_a():
    img = mpimg.imread("Image (1).jpeg")
    plt.imshow(img)
    plt.show()
    