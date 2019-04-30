# Exercise 1
# Answers to questions that ask for non-code answers can simply be added as comments.

# 1) The following line causes a SyntaxError. Please correct the line so that it's output is 'Hallo Welt!' [1P]
print(Hallo Welt!)


print("Hallo Welt!")



# 2) Calculate the difference between a and b and assign the result to a variable called 'v_1'. What are the datatypes of a, b and 'v_1'? [2P]
a = 976.543
b = 345


# a is float, b and v_1 are integer

a = 976.543
b = 345

v_1 = a + b
print(v_1)



# 3) Calculate the remainder of the division 100/17 by only using one operator
and save the result in v_2 (look into the Python docs for help) [1P]


# - ergebnis aus 100/17 muss integer sein.
# - v_2 ist 100 - c x 17
c = int(100/17)
v_2 = 100 - c * 17
print(v_2)



# 4) The speed of light is about 300'000 km/s. Calculate the wavelength (in nanometers) 
of a light wave with a frequency of 5.0E+14 per second. Can we see this light? [4P]
#    Save the result in v_3.


# Wellenlänge (in m) ist (Geschw in m/s) / (Frequenz in Hz)
# Wellenlänge (in nm) ist ((Geschw in m/s) / (Frequenz in Hz)) * 1e+9


d = 300000000/5.0E+14 * 1e+9
print(d)

# Licht mit Wellenlänge von 380-780 nm ist sichtbar; diese Wellenlänge sichtbar?

v_3 = d > 379 and d < 779 
print(v_3)



# 5) Print the following string to the console using the format-function and the
variables 'n' and 'pi': "Pi rounded to the first 10 decimals is: 3.1415926536" [2P]
n  = 10
pi = 3.14159265358979323846264338


print("Pi rounded to the first 10 decimals is:" + "{0:2.10f}".format(pi))



# ------------------------------------
# - Don't change stuff below this line
# ------------------------------------

print(v_1)
print(v_2)
print(v_3)
