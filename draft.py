import colorific
# import glob

# html = open("index.html", "w")
# for filename in glob.glob('./images/*'):
# html.write("<div>")
# html.write("<img width="\&quot;150px\&quot;" src="\&quot;&quot;" +="" filename="" "\"="">")
# print filename

palette = colorific.extract_colors(filename)
print(palette)
for color in palette.colors:
    print(color)
    hex_value = colorific.rgb_to_hex(color.value)
# html.write("""
# <div style="background: {color}; width: 500px; height: 50px; color: white;">
# {prominence}
# </div>
# """.format(color=hex_value, prominence=color.prominence))
# html.write("</div>")
# if palette.bgcolor != None:
# hex_value = colorific.rgb_to_hex(palette.bgcolor.value)
# html.write("""
# <div style="background: {color}; width: 500px; height: 50px; color: white;">
# {prominence}
# </div>
# """.format(color=hex_value, prominence=palette.bgcolor.prominence))
# html.write("

# See https://github.com/99designs/colorific/blob/master/colorific.py
# min_saturation = The minimum saturation needed to keep a color
# min_prominence = The minimum proportion of pixels needed to keep a color import colorific palette = &gt;&gt;&gt; colorific.extract_colors('test.jpg', min_prominence=0.1) colorific.print_colors('test.jpg', palette)
