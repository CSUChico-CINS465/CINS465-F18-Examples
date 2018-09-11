from functools import wraps


x=4


def fun():
    print(x)

x = x//5
x = x + 1
x += 1

#for i = 0; i<5; i++
y = [1,2,3,4,5]
# print(y)
# i = 0
# while i < len(y):
#     print(y[i])
#     i+=1

# for i in range(len(y)):
#     print(y[i])
#
# for item in y:
#     print(item)

x = "hello "
# y = "world"

# fun()
# print(x + y + str(4))

# x = "Python is amazing"
# y = x.split("a")
# print(x)
# print(y)
# fun()

# for i in x:
#     print(i)

# y.append(6)
# print(y)
# y += [7]
# print(y)
# y += ["8"]
# print(y)

# x = (1,2)
# y[0]=6
# x[0]=6
# print(y)
# print(x)
# print(x[0])

# x = {} #dictionary
# x = {"key":"value"}
# x[4]=5
# x["list"]=[1,2,3,4]
# print(x)

def awesome(awesome_variable):
    if awesome_variable >0:
        return True
    elif awesome_variable <0:
        return True
    else:
        return False

# print(awesome(4))

class Human:

    species = "H. sapiens"

    def __init__(self, name="bob", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.name)

class Student(Human):
    def __init__(self, name="bob", age=18, graduate_year=2022):
        Human.__init__(self,name,age)
        self.graduate_year = graduate_year

    def graduate(self):
        return self.graduate_year

jake = Human(age=6, name="jake")
print(jake)

jon = Student(name="Jon",graduate_year=2020)
print(jon)
print(jon.graduate())

try:
    print("1"+1)
except:
    print("Can't add nums & strings")



def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())                 # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(





# hi
