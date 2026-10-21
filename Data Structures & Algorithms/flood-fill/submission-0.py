class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc] # Save the original color of the starting pixel at (sr, sc)
        if orig == color: # Check if the new color is the same as the original color
            return image # Return the image as-is to avoid an infinite loop
        
        m, n = len(image), len(image[0]) # Get the number of rows (m) and columns (n) in the grid
        q = deque([(sr, sc)]) # Initialize a queue for BFS and add the starting coordinate
        image[sr][sc] = color # Paint the starting pixel with the new color
        dirs = [(1,0), (-1,0), (0,1), (0,-1)] # Define the 4-directional movement vectors (down, up, right, left)
        
        while q: # Continue BFS as long as there are pixels left in the queue to process
            r, c = q.popleft() # Remove and get the next pixel coordinates from the front of the queue
            for dr, dc in dirs: # Loop through all 4 adjacent directions
                nr, nc = r + dr, c + dc # Calculate the neighbor's row (nr) and column (nc)
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orig: # Check if neighbor is inside grid bounds and matches the original color
                    image[nr][nc] = color # Paint the valid neighbor with the new color
                    q.append((nr, nc)) # Add the newly painted neighbor to the queue for further exploration
                    
        return image # Return the fully updated image grid
