#!/usr/bin/python
import webbrowser
import time

total_break = 4
break_count = 0

print("This Program Started On:"+time.ctime())

while(break_count<total_break):
	time.sleep(10)
	print("Take A Break")
	webbrowser.open("http://www.youtube.com/watch?v=AKKT7zE_0Zg")
	break_count += 1
