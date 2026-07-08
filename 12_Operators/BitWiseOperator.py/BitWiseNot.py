# ===========================
# Bitwise NOT (~) Operator
# ===========================

# What is Bitwise NOT?
# --> Bitwise NOT (~) is a unary operator.
# --> It works on only one integer value.
# --> It inverts (flips) all the bits of the number.
# --> 0 becomes 1 and 1 becomes 0.

print(~5 & ~3)

# Step 1: Convert the decimal value to binary.

# 5 = 00000101   (8-bit representation)

# Step 2: Invert all the bits.

#    00000101
#  ~ --------
#    11111010

# Step 3:
# Python stores negative numbers using Two's Complement.

# Formula:
# ~n = -(n + 1)

# Therefore:
# ~5 = -(5 + 1)
# ~5 = -6

# Output:
# -6