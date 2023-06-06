from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable


from fuzzy_system.fuzzy_system import FuzzySystem

free = FuzzyInputVariable('free', 0, 100, 100)
free.add_triangular('L', 0, 25, 50)
free.add_triangular('M', 25, 50, 75)
free.add_triangular('H', 50, 75, 100)

txt = FuzzyInputVariable('txt', 0, 100, 100)
txt.add_triangular('L', 0, 25, 50)
txt.add_triangular('M', 25, 50, 75)
txt.add_triangular('H', 50, 75, 100)

to = FuzzyInputVariable('to', 0, 100, 100)
to.add_triangular('L', 0, 25, 50)
to.add_triangular('M', 25, 50, 75)
to.add_triangular('H', 50, 75, 100)

is_spam = FuzzyOutputVariable('is_spam', 0, 100, 100)
is_spam.add_triangular('spam', 0, 37, 75)
is_spam.add_triangular('not_spam', 37, 75, 100)


system = FuzzySystem()
system.add_input_variable(free)
system.add_input_variable(txt)
system.add_input_variable(to)
system.add_output_variable(is_spam)

system.add_rule(
		{ 'free':'H',
			'to':'L' },
		{ 'is_spam':'spam' })


output = system.evaluate_output({
			'free':35,
			'to':75
		})


print(output)


