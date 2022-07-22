def flip_image(image):
    # Write your code here
    for row in image:
        row[0:len(row)] = row[::-1]
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = 1
            else:
                row[i] = 0
    return image
print(flip_image([[1,1,0],[1,0,1],[0,0,0]]))
print(flip_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
