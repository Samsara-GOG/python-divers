grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    #all of the grades
    print(grade)

print(print_grades(grades))

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
#sum of grades
print(grades_sum(grades))
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average
#average grade
print(grades_average(grades))

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) ** 2
  vari = variance / float(len(scores))
  return vari
#variance
variance = grades_variance(grades)
print(variance)

def grades_std_deviation(variance):
  return variance ** 0.5

#standard deviation 
print(grades_std_deviation(variance))
