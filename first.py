courses = ['math', 'history', 'physics', 'compsci']
courses2 = ['education', 'chemistry']
nums = [1, 2, 3, 4, 5, 6, 7, 8]
courses.append('art')
courses.insert(0,'english')
courses.extend(courses2)
courses.remove('math')
popped = courses.pop()
courses.reverse()
courses.sort(reverse=True)
courses.reverse()
courses.sort(reverse=True)

sorted_list = sorted(courses)
print(popped)
print(courses)
print(sorted_list)

print(sum(nums))

print(courses.index('english'))

for i, course in enumerate(courses):
        print(i, ' = ', course)

course_str = ', '.join(courses)
new_list = course_str.split(', ')
print(course_str)
print(new_list)
print('\n')

cs_courses = {'history', 'math', 'compsci', 'math', 'mathematics',}
art_courses = {'history', 'design', 'crs', 'mathematics',}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


empty_list = []
empty_tupe = ()
empty_set = set()





