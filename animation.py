# use "pip install py5"  for installing the library


import py5

# Track horizontal position
x_pos = 100

def setup():
    # Set window dimensions (Width, Height)
    py5.size(600, 400)
    # Set background to black
    py5.background(0)

def draw():
    # Use the global keyword to modify variables outside the function
    global x_pos
    
    # Refresh background every frame to prevent trailing lines
    py5.background(0)
    
    # Set fill color to green (RGB: Red=0, Green=255, Blue=0)
    py5.fill(0, 255, 0)
    
    # Draw an ellipse moving across the screen
    py5.ellipse(x_pos, 200, 50, 50)
    
    # Increment position
    x_pos += 2
    if x_pos > py5.width:
        x_pos = 0
        
    # Draw a secondary blue circle that directly follows the mouse cursor
    py5.fill(0, 0, 255)
    py5.ellipse(py5.mouse_x, py5.mouse_y, 30, 30)

# Run the sketch
if __name__ == "__main__":
    py5.run_sketch()
