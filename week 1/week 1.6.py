Justin is a carpenter who works on an hourly basis. He works in a company where he 
is paid Rs 50 for an hour on weekdays and Rs 80 for an hour on weekends. He works 
10 hrs more on weekdays than weekends. If the salary paid for him is given, write a 
program to find the number of hours he has worked on weekdays and weekends. 
Hint: 
If the final result(hrs) are in -ve convert that to +ve using abs() function 
The abs() function returns the absolute value of the given number. 
 
number = -20 
absolute_number = abs(number) 
 
 print(absolute_number) 
# Output:20 
 
 Sample Input: 
450 
Sample Output: 
weekdays 10.38 
weekend 0.38 
 
For example: 
Input Result 
450 weekdays 10.38 
weekend 0.38 
 
 
 
 s=int(input()) 
 a=(500-s)/130 
 print("weekdays {:.2f}".format(abs(a)+10)) 
 print("weekend {:.2f}".format(abs(a)))
