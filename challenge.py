lloyd = {
	"name" : "Loyd",
	"homework" : [90.0, 97.0, 75.0, 92.0],
	"quizzes" : [88.0, 40.0, 94.0],
	"test" : [75.0, 90.0]
}

alice = {
	"name" : "Alice",
	"homework" : [100.0, 92.0, 98.0, 100.0],
	"quizzes" : [82.0, 83.0, 91.0],
	"test" : [89.0, 97.0]
}

tyler = {
	"name" : "Tyler",
	"homework" : [0.0, 87.0, 75.0, 22.0],
	"quizzes" : [0.0, 75.0, 78.0],
	"test" : [100.0, 100.0]
}

def average(numbers):
	total = sum(numbers)
	total = float(total)
	return total/len(numbers)

def get_average(student):
	homework = average(student["homework"])
	quizzes = average(student["quizzes"])
	test = average(student["test"])
	return 0.1 * homework + 0.3 * quizzes + 0.6 * test

def get_lettergrade(score):

	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"

print get_lettergrade(get_average(lloyd))
