import cairo

OUTPUT_DIR = "output/"

# Surface
surface = cairo. ImageSurface(cairo. FORMAT_RGB24, 800, 400)
ctx = cairo. Context (surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

 # Stroke
ctx.rectangle(50, 300, 500, 20)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width (5)
ctx.stroke()

ctx.move_to(60, 300)
ctx.line_to(60, 150)
ctx.stroke()

ctx.move_to(250, 300)
ctx.line_to(250, 150)
ctx.stroke()

ctx.rectangle(90, 240, 130, 20)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width (5)
ctx.stroke()

ctx.move_to(100, 240)
ctx.line_to(100, 170)
ctx.stroke()

ctx.move_to(210, 240)
ctx.line_to(210, 170)
ctx.stroke()

ctx.move_to(100, 170)
ctx.line_to(210, 170)
ctx.stroke()

ctx.rectangle(135, 90, 40, 40)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width (5)
ctx.stroke()

ctx.move_to(40, 170)
ctx.line_to(150, 40)
ctx.stroke()

ctx.move_to(30, 160)
ctx.line_to(150, 20)
ctx.stroke()

ctx.move_to(40, 170)
ctx.line_to(30, 160)
ctx.stroke()

ctx.move_to(270, 170)
ctx.line_to(150, 40)
ctx.stroke()

ctx.move_to(280, 160)
ctx.line_to(150, 20)
ctx.stroke()

ctx.move_to(270, 170)
ctx.line_to(280, 160)
ctx.stroke()

# this
ctx.move_to(260, 140)
ctx.line_to(570, 140)
ctx.stroke()

ctx.move_to(540, 300)
ctx.line_to(540, 140)
ctx.stroke()

ctx.rectangle(400, 240, 100, 20)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

ctx.rectangle(410, 170, 80, 70)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

ctx.move_to(570, 140)
ctx.line_to(490, 40)
ctx.stroke()

ctx.move_to(490, 40)
ctx.line_to(170, 40)
ctx.stroke()

surface.write_to_png(f"{OUTPUT_DIR}image.png")