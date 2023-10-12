print("hello world")
print(4+5) # After the hashtag symbol is a comment

x = 5
y = 10
z = x + y
print(z)

print(4)	# Will generate an error

str1 = "hello"
str2 = "hello \"friends"
str3 = """I hope you are doing "well"\n me, yes"""
print(str2 + str3)

str1 = "hello world"
first_char = str1[0]
third_char = str1[2]
last_char = str1[-1]
print(first_char)
print(third_char)
print(last_char)


nb = 5
nb_str = str(nb)
txt1 = "4"
txt1_int = int(txt1)
txt2 = "5.23"
txt2_float = float(txt2)


print("\nType d'un objet ? Utilisez la fonction type()")
print(type(nb))
print(type(txt1_int))
print(type(txt2_float))

print("\nconcaténation:")
english_mark = 18
math_mark = 17.5
print("You got " + str(english_mark)
      + " in english " + str(math_mark) + "  in maths.")

print("\nconcaténation & logique boléene:")
a, b = True, False
print(a,b)
print(b)

a, b = "string1", "string2"
print(a,b)
print(b)

a = 5 < 6
print(a)

a = 5 < 6 and 10 < 6
print(a)

a = 5 < 6 or 10 < 6
print(a)

