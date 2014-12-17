#This is a trivia game about Paul Resnick! Make additions, modifications, and deletions as necessary.
#The code is purposefully buggy. Refer to PS6 with the hangman game to fix this one!
#Ideas for changes: what happens when the user enters something other than true or false, more trivia, different wording, tests

print 'This is a trivia game about Paul Resnick! If you get 3 answers wrong, you are a big loser.'
def resgame():
    wrong_answers = 0
    right_answers = 0
    while wrong_answers < 3:
        a = raw_input('Paul Resnick met Obama. True or false?')
        if a.upper() == FALSE:
            wrong_answers += 1
        elif a.upper() == TRUE:
            right_answers += 1
            b = raw_input('Paul Resnick taught at U-M for 8 years. True or false?')
            if b.upper() == TRUE:
                wrong_answers += 1
            elif b.upper() == FALSE:
                right_answers += 1
                c = raw_input('Paul Resnick has a treadmill in his office. True or false?')
                if c.upper == FALSE:
                    wrong_answers += 1
                elif c.upper == TRUE:
                    right_answers += 1
                    d = raw_input('Paul Resnick has counted to infinity... twice. True or false?')
                    print d
                    if d.upper == FALSE:
                        wrong_answers += 1
                    if d.upper == TRUE:
                        right_answers += 1
    if wrong_answers >= 3:
        print 'You lose!'
    if wrong_answers < 3:
        print 'Congrats, you win! You guessed correctly ' + right_answers + 'times!'
    return 'You were incorrect ' + wrong_answers + 'times, and correct ' + right_answers + 'times.'
    
    
#Sara Otto's Changes:

print 'This is a trivia game about Paul Resnick! If you get 3 answers wrong, you are a big loser.'
wrong_answers = 0
right_answers = 0
while wrong_answers < 3:
    a =raw_input('Paul Resnick met Obama. True or false?')
    if a.upper() == "FALSE":
        wrong_answers += 1
    elif a.upper() == "TRUE":
        right_answers += 1
    b = raw_input('Paul Resnick taught at U-M for 8 years. True or false?')
    if b.upper() == "TRUE":
        wrong_answers += 1
    elif b.upper() == "FALSE":
        right_answers += 1
    c = raw_input('Paul Resnick has a treadmill in his office. True or false?')
    if c.upper == "FALSE":
        wrong_answers += 1
    elif c.upper == "TRUE":
        right_answers += 1
    d = raw_input('Paul Resnick has counted to infinity... twice. True or false?')
    
    if d.upper == "FALSE":
        wrong_answers += 1
    if d.upper == "TRUE":
        right_answers += 1
if wrong_answers >= 3:
    print 'You lose!'
if wrong_answers < 3:
    print 'Congrats, you win! You guessed correctly ' + right_answers + 'times!'
else:
    'You were incorrect ' + wrong_answers + 'times, and correct ' + right_answers + 'times.'

#Logan Meyer's Changes:
print 'This is a trivia game about Paul Resnick! If you get 3 answers wrong, you are a big loser.'
wrong_answers = 0
right_answers = 0
while wrong_answers < 3:
    a =raw_input('Paul Resnick met Obama. True or false?')
    if a.upper() == "FALSE":
        wrong_answers += 1
    elif a.upper() == "TRUE":
        right_answers += 1
    b = raw_input('Paul Resnick taught at U-M for 8 years. True or false?')
    if b.upper() == "TRUE":
        wrong_answers += 1
    elif b.upper() == "FALSE":
        right_answers += 1
    c = raw_input('Paul Resnick has a treadmill in his office. True or false?')
    if c.upper == "FALSE":
        wrong_answers += 1
    elif c.upper == "TRUE":
        right_answers += 1
    d = raw_input('Paul Resnick has counted to infinity... twice. True or false?')
    if d.upper == "FALSE":
        wrong_answers += 1
    elif d.upper == "TRUE":
        right_answers += 1
    e = raw_input('Paul Resnick is 6\'3\". True or false?')
    if e.upper == "FALSE":
        wrong_answers += 1
    elif e.upper == "TRUE":
        right_answers += 1
    if wrong_answers >= 3:
        print 'You lose!'
    if wrong_answers < 3:
        print 'Congrats, you win! You guessed correctly ' + str(right_answers) + ' times!'
        print 'You were incorrect ' + str(wrong_answers) + ' times, and correct ' + str(right_answers) + ' times.'
  
#Ben Beale's changes:
print 'This is a trivia game about Paul Resnick! If you get 4 answers wrong, you are a big loser.'
wrong_answers = 0
right_answers = 0
while wrong_answers < 4:
	a =raw_input('Paul Resnick met Obama. True or false?')
	if a.upper() == "FALSE":
		wrong_answers += 1
	elif a.upper() == "TRUE":
		right_answers += 1
	b = raw_input('Paul Resnick taught at U-M for 8 years. True or false?')
	if b.upper() == "TRUE":
		wrong_answers += 1
	elif b.upper() == "FALSE":
		right_answers += 1
	c = raw_input('Paul Resnick has a treadmill in his office. True or false?')
	if c.upper == "FALSE":
		wrong_answers += 1
	elif c.upper == "TRUE":
		right_answers += 1
	d = raw_input('Paul Resnick has counted to infinity... twice. True or false?')
	if d.upper == "FALSE":
		wrong_answers += 1
	elif d.upper == "TRUE":
		right_answers += 1
	e = raw_input('Paul Resnick is 6\'3\". True or false?')
	if e.upper == "FALSE":
		wrong_answers += 1
	elif e.upper == "TRUE":
		right_answers += 1 
	f = raw_input("SI 106 is Paul Resnick's favorite section to teach... True or false?")
	if f.upper == "FALSE":
		wrong_answers += 1
	elif f.upper == "TRUE":
		right_answers += 1
	g = raw_input("Paul Resnick is going to give his entire SI 106 section an A... True or false?")
	if g.upper == "FALSE":
		wrong_answers += 1
	elif g.upper == "TRUE":
		right_answers +=1
	if wrong_answers >= 4:
		print 'You lose!'
	if wrong_answers < 4:
		print 'Congrats, you win! You guessed correctly ' + str(right_answers) + ' times!'
		print 'You were incorrect ' + str(wrong_answers) + ' times, and correct ' + str(right_answers) + ' times.'
