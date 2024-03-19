from PIL import Image, ImageDraw

img = Image.new('RGB', (400, 400), color='gray')
draw = ImageDraw.Draw(img)

draw.polygon([(190, 300), (210, 300), (200, 400)], fill='brown')
draw.polygon([(150, 350), (250, 350), (200, 250)], fill='brown')
draw.polygon([(140, 220), (260, 220), (200, 150)], fill='brown')

draw.polygon([(150, 300), (250, 300), (200, 150)], fill='green')
draw.polygon([(150, 350), (250, 350), (200, 250)], fill='green')
draw.polygon([(140, 220), (260, 220), (200, 150)], fill='green')

draw.polygon([(150, 300), (250, 300), (200, 250)], fill='white')
draw.polygon([(150, 350), (250, 350), (200, 300)], fill='white')
draw.polygon([(140, 220), (260, 220), (200, 200)], fill='white')


img.show()