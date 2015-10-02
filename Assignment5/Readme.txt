First argument is file name. Second argument is epsilon

With epsilon set to 0.5, I found the path described below. The first number is the x location, measured from the left. The second
is the y location measured from the top, and the third number is the utility at that state. The matrix below that is
the utility at all of the states in the path.

[(0, 7, 5.6), (1, 7, 6.32), (2, 7, 7.56), (3, 7, 8.61), (4, 7, 9.76), (5, 7, 11.23), (6, 7, 12.79), (6, 6, 14.87), (6, 5, 16.94), (6, 4, 19.12), (6, 3, 22.93), (7, 3, 26.59), (7, 2, 29.35), (8, 2, 33.4), (9, 2, 38.04), (9, 1, 43.9), (9, 0, 50)]
 
0    0    0    0    0    0    0    0    0    50     
0    0    0    0    0    0    0    0    0    43     
0    0    0    0    0    0    0    29    33    38     
0    0    0    0    0    0    22    26    0    0     
0    0    0    0    0    0    19    0    0    0     
0    0    0    0    0    0    16    0    0    0     
0    0    0    0    0    0    14    0    0    0     
5    6    7    8    9    11    12    0    0    0


I tried it again with epsilon = 1000 since I thought that would be very inaccurate, but I still got the same path, but with
lower utility

[(0, 7, 1.78), (1, 7, 2.02), (2, 7, 2.56), (3, 7, 2.91), (4, 7, 3.38), (5, 7, 4.09), (6, 7, 4.66), (6, 6, 6.09), (6, 5, 7.16), (6, 4, 8.2), (6, 3, 10.68), (7, 3, 13.61), (7, 2, 15.95), (8, 2, 18.66), (9, 2, 25.92), (9, 1, 36.0), (9, 0, 50)]
 
0    0    0    0    0    0    0    0    0    50     
0    0    0    0    0    0    0    0    0    36     
0    0    0    0    0    0    0    15    18    25     
0    0    0    0    0    0    10    13    0    0     
0    0    0    0    0    0    8    0    0    0     
0    0    0    0    0    0    7    0    0    0     
0    0    0    0    0    0    6    0    0    0     
1    2    2    2    3    4    4    0    0    0 


Running it with epsilon = 0.01, which I thought would be very close to convergence, gave me the same path as well, with
only slightly higher utilities than at 0.5

[(0, 7, 5.6), (1, 7, 6.32), (2, 7, 7.56), (3, 7, 8.61), (4, 7, 9.76), (5, 7, 11.23), (6, 7, 12.79), (6, 6, 14.88), (6, 5, 16.94), (6, 4, 19.12), (6, 3, 22.93), (7, 3, 26.59), (7, 2, 29.35), (8, 2, 33.4), (9, 2, 38.04), (9, 1, 43.9), (9, 0, 50)]
 
0    0    0    0    0    0    0    0    0    50     
0    0    0    0    0    0    0    0    0    43     
0    0    0    0    0    0    0    29    33    38     
0    0    0    0    0    0    22    26    0    0     
0    0    0    0    0    0    19    0    0    0     
0    0    0    0    0    0    16    0    0    0     
0    0    0    0    0    0    14    0    0    0     
5    6    7    8    9    11    12    0    0    0  

I was expecting to be able to get a different solution, but apparently the initial iteration was fairly accurate.

