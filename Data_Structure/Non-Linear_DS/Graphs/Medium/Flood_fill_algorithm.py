# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image. Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same colour as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same colour as the starting pixel), and so on. Replace the colour of all of the aforementioned pixels with the newColor.


# Input: image = [ [0, 1, 0], [1, 1, 0], [0, 0, 1] ], sr = 2, sc = 2, newColor = 3

# Output: [ [0, 1, 0], [1, 1, 0], [0, 0, 3] ]

# Explanation: Starting from the pixel at position (2, 2) (i.e., the blue pixel), we flood fill all adjacent pixels that have the same color as the starting pixel. In this case, only the pixel at position (2, 2) itself is of the same color. So, only that pixel gets colored with the new color, resulting in the updated image.

def floodFill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    originalColor = image[sr][sc]

    # Important edge case
    if originalColor == newColor:
        return image

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    stack = [(sr, sc)]

    while stack:
        r, c = stack.pop()   # DFS

        image[r][c] = newColor

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                image[nr][nc] == originalColor
            ):
                stack.append((nr, nc))

    return image

image = [ [0, 1, 0], [1, 1, 0], [0, 0, 1]]
sr = 2
sc = 2
newColor = 3
print(floodFill(image, sr, sc, newColor))