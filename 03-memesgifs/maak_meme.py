from PIL import Image, ImageFont, ImageDraw


afbeelding = Image.open("meme_background.jpg")
breedte = afbeelding.width
hoogte = afbeelding.height

lettertype = ImageFont.truetype("impact.ttf", 80)
tekengebied = ImageDraw.Draw(afbeelding)

Text = "the Abyss making me act unwise"

tekst_breedte, tekst_hoogte = tekengebied.textsize(Text, font=lettertype) 
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))

tekst_x = (breedte - tekst_breedte)/2
tekst_y = (hoogte - tekst_hoogte)
tekengebied.multiline_text((tekst_x-2, tekst_y-2), Text, font=lettertype, fill=(255,255,255))

afbeelding.show()
afbeelding.save("meme_met_tekst.jpg")