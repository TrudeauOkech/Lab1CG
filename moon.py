import cairo

# Set up the drawing surface
WIDTH, HEIGHT = 800, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set background color
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

# Draw the moon (crescent shape)

# First, draw the larger circle for the outer moon
context.arc(600, 100, 50, 0, 2 * 3.1416)  # Center at (600, 100) with radius 50
context.set_source_rgb(0.8, 0.8, 0.8)  # Light gray for the outer moon
context.fill()

# Next, draw a smaller circle inside to create the crescent shape
# Shifted to the left to make the moon face the opposite direction
context.arc(570, 100, 40, 0, 2 * 3.1416)  # Shifted left from 630 to 570
context.set_source_rgb(1, 1, 1)  # White to erase the inside part
context.fill()

# Save the drawing to a file
surface.write_to_png("moon.png")
