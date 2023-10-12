# Python rstrip() method removes all the trailing characters from the string. 
# It means it removes all the specified characters from right side of the string. 
# If we don't specify the parameter, It removes all the whitespaces from the string. 
# This method returns a string value.

#  Python rstrip() method example  
# Variable declaration  
str = "Java and C# "  
# Calling function  
str2 = str.rstrip()  
# Displaying result  
print("Old string: ",str)  
print("New String: ",str2)  

# Variable declaration  
str = "Java and C#"  
# Calling function  
str2 = str.rstrip('#')  
# Displaying result  
print("Old string: ",str)  
print("New String: ",str2)  

# Variable declaration  
str = "Java and C#"  
# Calling function  
str2 = str.rstrip('#')  
# Displaying result  
print("Old string: ",str, len(str))  
print("New String: ",str2, len(str2))  