weather_type = "sunny"
temp_high = 90
temp_low = 55
prob_of_prec = 0.7

# If the temperature is less than 32 degrees, wear a heavy coat. Else, if the temp is less than 60, wear a jacket, else a t-shirt is fine.

if temp_high < 32:
  print("Wear a heavy coat")
  if temp_high < 0:
    print("Wear a hat and a scarf and gloves!")

elif temp_high < 60:
  print("Wear a jacket")
else:
  print("A t-shirt is fine")


if prob_of_prec > 0.5 and temp_high > 32:
  print("Bring an umbrella")

if (temp_high - temp_low) > 30:
  print("Dress in layers")