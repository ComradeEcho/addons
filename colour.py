import colorsys 

def hex(length):
	sat = 1 
	value = 1 
	array = []
	for h in range(0, length + 1): 
		hue = h / float(length) 
		color = list(colorsys.hsv_to_rgb(hue, sat, value)) 
		for x in range(3): 
			color[x] = int(color[x] * 255) 
			hexval = ("#%02x%02x%02x" % tuple(color)).upper() 
			array.append(hexval)
	return array

print(hex(30))