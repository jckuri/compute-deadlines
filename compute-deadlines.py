# Use Python 3, not Python 2.

import datetime
today = datetime.date.today()

def parse_date(date):
 numbers = [int(number) for number in date.split('-')]
 date = datetime.date(numbers[0], numbers[1], numbers[2])
 return date
 
def date_to_string(date):
 return '{} {}, {}'.format(date.strftime("%B"), date.day, date.strftime("%Y"))

def parse_deadlines(file):
 deadlines = []
 with open(file, 'r') as f:
  lines = f.readlines()
  for line in lines:
   comma = line.find(',')
   if comma != -1:
    project, date = line[:comma], line[comma + 1:-1]
    date = parse_date(date)
    deadlines.append((project, date))
 return deadlines
 
def compute_new_deadlines(deadlines, new_start, completed):
 s = ''
 start = deadlines[0][1]
 index = 0
 first_deadline = 1
 for project, date in deadlines[1:]:
  index += 1
  if index in completed: continue
  days = (date - start).days
  new_date = new_start + datetime.timedelta(days = days)
  status = ' (OVERDUE)' if today > new_date else ''
  if not first_deadline: s += '\\'
  s += '\n"{}" project is due {}.{}'.format(project, date_to_string(new_date), status)
  first_deadline = 0
 return s
 
def show_projects(deadlines):
 print('PROJECTS:')
 index = 1
 for project, date in deadlines[1:]:
  print('{}. {}'.format(index, project))
  index += 1

def show_deadlines(deadlines, new_start, completed):
 print('\n\nHello. Today is {}. And you started this nanodegree on {}. Here is a friendly reminder of the projects you need to complete in order to graduate from this nanodegree:'.format(date_to_string(today), date_to_string(new_start)))
 print(compute_new_deadlines(deadlines, new_start, completed))
 print(' \nIf you need help to understand the video lectures or to program the projects, please ask me anything through this chat.\n\n')
 
def input_new_start():
 message = 'Type the start date of the nanodegree (YYYY-MM-DD). Press ENTER if the date is today ({}): '.format(today)
 new_start = input(message)
 if new_start == '':
  new_start = today
  new_start = str(new_start)
 new_start = parse_date(new_start)
 print('new_start: {}'.format(date_to_string(new_start)))
 return new_start
 
def input_completed_projects(deadlines):
 show_projects(deadlines)
 completed = input('Type the numbers of the completed projects, separated by commas, i.e. "1,2,3" or "2,4". Press ENTER if no project is completed: ')
 if completed == '': return []
 completed = completed.split(',')
 completed = [int(project) for project in completed]
 print('completed: {}'.format(completed))
 return completed

def main():
 deadlines = parse_deadlines('deadlines-self-driving-cars.txt')
 completed = input_completed_projects(deadlines)
 new_start = input_new_start()
 show_deadlines(deadlines, new_start, completed)
 
main()
