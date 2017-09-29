numbers = {'Tony Stark': '123456', 'Bobbi Morse':'9876567',
'Jessica Drew':'343654','Miles Morales':'4253432','Kate Bishop':'2532435'}

def retrieve():
  input2 = raw_input("enter name:")
  print input2, numbers[input2]
def add():
  nname = raw_input("please enter name: ")
  nnum = raw_input("please enter number: ")
  numbers.update({nname:nnum})
  print numbers

def remove():
  name = raw_input("enter name: ")
  del numbers[name]
  print numbers

input = raw_input("select retrieve, add or remove: ")

if input == "retrieve":
  retrieve()
elif input == "add":
  add()
elif input == "remove":
  remove()
else:
  print "invalid input"


def retrieve():
  input2 = raw_input("enter name:")
  print input, numbers[input2]
