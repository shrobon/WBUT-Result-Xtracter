#WBUT-Result-Xtracter

We all know what a big pain in the a** it is to see the WBUT results. We sit in front of the terminal entire day and yet are unable to see our results due to the sheer traffic .

WBUT-Result-Xtracter is a simple python script that takes

1.)Roll Number-lower limit

2.)Roll Number-Upper limit

3.)Semester

as input and display the Name, Roll-no, Registration-No ans the SGPA of the students withing the range of (upper-limit & lower-limit)

**Version 1.0** :

Worked with the 5th semester 2014.

*Usage* : open the result.py in a text editor and modify the range function i.e range(lower_roll,upper_roll,sem) and run the script after navigating to the WBUT-Result-Xtracter directory

*python result.py*

*Requires* : BeautifulSoup4 , requests modules for python

*Test File* : result.py

*Author* : Shrobon Biswas

*Quick Debug* : Sometimes the show_results.php page is different for the even and odd sem results. So in that case , modify the link given in the code to make it work properly .
change http://www.wbutech.net/show-result.php with the new link.

