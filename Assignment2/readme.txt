First argument is file name. Second argument is hueristic: 1 for manhattan, 2 for straight distance

The other hueristic I used was just the straight line distance to the goal, using d = sqrt(x^2 + y^2). I thought this
would be good since it is the actual distance away. 

World 1:
Manhattan:
Cost:  156
Path:  [(0, 7), (1, 6), (1, 5), (1, 4), (1, 3), (2, 2), (3, 2), (4, 1), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0)]
Number of explored nodes:  19

Straight:
Cost:  130
Path:  [(0, 7), (1, 7), (2, 7), (3, 6), (4, 5), (4, 4), (5, 3), (6, 3), (7, 2), (8, 2), (9, 1), (9, 0)]
Number of explored nodes:  27

World 2:
Manhattan:
Cost:  142
Path:  [(0, 7), (0, 6), (0, 5), (1, 4), (2, 4), (3, 4), (4, 3), (4, 2), (4, 1), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0)]
Number of explored nodes:  17

Straight:
Cost:  142
Path:  [(0, 7), (1, 7), (2, 7), (3, 6), (3, 5), (4, 4), (4, 3), (4, 2), (4, 1), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0)]
Number of explored nodes:  32

Compared to the manhattan hueristic, the straight line hueristic explored more nodes, but seemed to be more accurate.
It found a significantly better solution to world 1 than the manhattan hueristic. For world 2, they found different paths,
but they ended up costing the same amount. I would say the straight line is better if you want the best path possible, 
but manhattan is a little faster since it explores less nodes and doesn't have as complex of calculations or have to use
floats.