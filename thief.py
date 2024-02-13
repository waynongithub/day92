from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

ct = ColorThief("uploads/signal-2024-01-12-211107.jpeg")
dominant_color = ct.get_color(quality=1)

# plt.imshow([[dominant_color]])
plt.show()

palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

for color in palette:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))



