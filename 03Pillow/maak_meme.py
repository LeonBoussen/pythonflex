from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("background.jpg")

breedte = achtergrond.width
hoogte = achtergrond.height

lettertype = ImageFont.truetype("text.otf", 40)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "gay cat"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

achtergrond.show()

achtergrond.save("meme_met_tekst.jpg")
