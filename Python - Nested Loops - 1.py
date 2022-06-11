# Nested Loops

# Every time x runs y is ran three times.
for x in range (4):
# Step 1:  x=0 = (0, )
# Step 5:  x=1 = (1, )
# Step 9:  x=2 = (2, )
# Step 13: x=3 = (3, )
    # y is ran 3 times in a row before going back up to increment x once.
    for y in range (3):
        print(f'({x},{y})')
        # Step 2  y=0 = (0,0)
        # Step 3  y=1 = (0,1)
        # Step 4  y=2 = (0,2)
        # Step 6  y=0 = (1,0)
        # Step 7  y=1 = (1,1)
        # Step 8  y=2 = (1,2)
        # Step 10 y=0 = (2,0)
        # Step 11 y=1 = (2,1)
        # Step 12 y=2 = (2,2)
        # Step 14 y=0 = (3,0)
        # Step 15 y=1 = (3,1)
        # Step 16 y=2 = (3,2)

# All Steps

# Step 1:   (0, )
# Step 2:   (0,0)
# Step 3:   (0,1)
# Step 4:   (0,2)
# Step 5:   (1, )
# Step 6:   (1,0)
# Step 7:   (1,1)
# Step 8:   (1,2)
# Step 9:   (2, )
# Step 10:  (2,0)
# Step 11:  (2,1)
# Step 12:  (2,2)
# Step 13:  (3, )
# Step 14:  (3,0)
# Step 15:  (3,1)
# Step 16:  (3,2)
