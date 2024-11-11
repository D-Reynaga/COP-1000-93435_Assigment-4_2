"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.
charge = 35.00
numChars = 8
color = "gold"
woodType = "oak"

# Write assignment and if statements here as appropriate.
if numChars > 5:
    additional_chars_charge = (numChars - 5) * 4
else:
    additional_chars_charge = 0

if woodType == "oak":
    wood_charge = 20.00
else:
    wood_charge = 0.00

if color == "gold":
    color_charge = 15.00
else: 
    color_charge = 0.00


charge += additional_chars_charge + wood_charge + color_charge
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))