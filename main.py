#required pyautogui and bluestacks or tiktok as an app or you can also use a browser
#feel free to modify the code as you like
import pyautogui
from time import sleep

comment = input("Enter your comment: ") #enter your comment or text
times = input("How many times: ") #how many times do you want this script to run 


#you can change the pointer location by running "get_mouse_loc", you can run it from terminal with keyboard and keeping pointer over the button or location 
#if you have slow internet connection you may want to increase sleep(1) from 1 second to more as you like
for i in range(int(times)):    
    sleep(1)
    pyautogui.click(1852,694)  # open comment box
    sleep(1)
    pyautogui.click(1515,910)  # click add comment
    sleep(1)
    pyautogui.write(comment)   # write comment
    sleep(1)
    pyautogui.click(1848,623)  # send comment
    sleep(1)
    pyautogui.click(1861,497)  # close comment box
    sleep(1)
    pyautogui.scroll(-10)      # next video (scroll)

