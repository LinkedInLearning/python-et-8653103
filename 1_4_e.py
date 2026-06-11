weather_type = "sunny"
temp_high = 70
temp_low = 55
prob_of_prec = 0.1


# If the temperature is less than 32 degrees wear a heavy coat. 
# Else, if the temperature is less than 60 degrees, 
# wear a jacket, else a t-shirt is fine. 
if temp_high < 32:
	print('Wear a heavy coat')
	if temp_high < 0:
		print('and a hat and scarf and gloves!')
elif temp_high < 60:
	print('Wear a jacket')
else:
	print('A tshirt is fine')
	

if prob_of_prec > 0.5:
	print('Bring an umbrella')

if prob_of_prec > 0.5 and temp_high > 32:
	print('Bring an umbrella')
	
if (temp_high - temp_low) > 30:
	print('Dress in layers')