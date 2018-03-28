grade_list = []

math_grades = (input("what is your garde on math?: "))
computer_grades = (input("what is your grade on computer class?: "))
english_grades = (input("what is your grade on english class? "))
science_grades = (input("what is your grade on science?: "))
rotc_grades = (input("what is your grade on rotc?: "))

grade_list = [math_grades, computer_grades, english_grades, science_grades, rotc_grades]

average = (int(math_grades) + int(computer_grades) + int(english_grades) + int(science_grades) + int(rotc_grades)) / 5

grade_list.apppend(average)

print "The last number is your aveage."


print str(grade_list)


if average <= 66:
    print "you need help"
elif average <=60 and average >=69:
    print "you need to try harder"
elif average >=70 and average <=79:
    print " you need to stay fouced  more"
elif average >=80 and average <=89:
    print"You doing good keep it up"
elif average >=90 and average <=99:
    print "You're awesome and you killing it"

