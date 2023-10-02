
programWords = {"Variables":" : stores data.",
                "Comments":" : can only be read by a person not by the machine.",
                "If":" : is a conditional statement that executes only with the right conditions.",
                "elif": " : is a conditional statement that executes after an if statement. Works the same as an IF statements.",
                "else":" : executes only after if and elif statements. Only condition it has is if all the IF statements are false.",
                "for loop":" : Is a controlled loop.",
                "print":" : Prints code in the terminal.",
                "List":" :  is a collection of data, enclosed in [ ] and separated by commas",
                "float":" : are decimal values or fractional numbers.",
                "int":" : is a whole number, positive or negative, without decimals, of unlimited length."}
for x in programWords:
    print(x+programWords.get(x))