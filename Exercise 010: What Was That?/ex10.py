tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

# The \ (backlash) encodes difficult-to-type characters into a string.

# Escape       What it does

# \\           Backlash (\)
# \'           Single-quote (')
# \"           Double-quote (")
# \a           ASCII bell (BEL)
# \b           ASCII backspace (BS)
# \f           ASCII formfeed (FF)
# \n           ASCII linefeed (LF)    
