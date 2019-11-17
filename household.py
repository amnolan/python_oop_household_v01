# @amnolan

class Gender:
  NOT_ENTERED = "None given"
  MALE = "Male"
  FEMALE = "Female"

class PersonType:
  NOT_ENTERED = "None given"
  ADULT = "Adult"
  CHILD = "Child"

class JobType:
  NOT_ENTERED = "None given"
  PROGRAMMER = "Programmer"
  STUDENT = "Student"
  DOCTOR = "Doctor"
  TEACHER = "Teacher"

class Person:
  def __init__(self, personType, name="", gender=Gender.NOT_ENTERED):
    self.__name = name
    self.__personType = personType
    self.__gender = gender

  def getName(self):
    return self.__name

  def getPersonType(self):
    return self.__personType

  def getGender(self):
    return self.__gender

  def setName(self, name):
    self.__name = name

  def setPersonType(self, personType):
    self.__personType = personType

  def setGender(self, gender):
    self.__gender = gender

  ## to string func
  def toString(self):
    returnedString = "          Person type: " + self.__personType
    returnedString += "\n\t         Name: " + self.__name
    returnedString += "\n\t       Gender: " + self.__gender
    return returnedString

class Adult(Person):
  # pass
  def __init__(self, personType, name, gender, job):
    self.__job = job
    super().__init__(personType,name,gender)

  def getJob(self):
    return self.__job

  def setJob(self, job):
    self.__job = job

  # ## to string func
  def toString(self):
    returnedString = "\n\t          Job: " + self.__job
    return super().toString() + returnedString + "\n"
   

class Child(Person):
  # pass
  def __init__(self, personType, name, gender, favoriteToy = "Wooden Horse"):
    self.__favoriteToy = favoriteToy
    super().__init__(personType,name,gender)

  def getFavoriteToy(self):
    return self.__favoriteToy

  def setFavoriteToy(self, favoriteToy):
    self.__favoriteToy = favoriteToy

  ## to string func
  def toString(self):
    returnedString = "\n\t Favorite toy: " + self.__favoriteToy
    return super().toString() + returnedString + "\n"

class Pet:
  def __init__(self, petType, name="", gender = Gender.NOT_ENTERED):
    self.__name = name
    self.__petType = petType
    self.__gender = gender

  def getName(self):
    return self.__name

  def getPetType(self):
    return self.__petType

  def getGender(self):
    return self.__gender

  def setName(self, name):
    self.__name = name

  def setPetType(self, petType):
    self.__petType = petType

  def setGender(self, gender):
    self.__gender = gender

  def toString(self):
    returnedString = "             Pet type: " + self.__petType
    returnedString += "\n\t         Name: " + self.__name
    returnedString += "\n\t       Gender: " + self.__gender
    return returnedString + "\n"

class Household:
  def __init__(self, familyName=""):
    self.__adults = []
    self.__children = []
    self.__pets = []
    self.__familyName = familyName
    self.__householdSize = 0

  # add an adult to the house through composition (adult extends person)
  def addAdult(self, familyMember):
    self.__adults.append(familyMember)
    print("Adult added!\n")
    self.__householdSize+=1

  # remove an adult
  def moveAdult(self, familyMember):
    for i, adult in enumerate(self.__adults):
        if adult.getName() == familyMember:
            del self.__adults[i]
            break
    print("Adult moved out!\n")
    self.__householdSize-=1
    
  # add a pet to the house through composition
  def addPet(self, familyMember):
    self.__pets.append(familyMember)
    print("Pet added!\n")
    self.__householdSize+=1

  # sometimes pets decide to move out
  def movePet(self, familyMember):
    for i, pet in enumerate(self.__pets):
        if pet.getName() == familyMember:
            del self.__pets[i]
            break
    print("Pet moved out!\n")
    self.__householdSize-=1
  
  # As children are only created within the household
  def createChild(self, name, gender, favoriteToy):
    child = Child(PersonType.CHILD,name,gender,favoriteToy)
    self.__children.append(child)
    print("Child added!\n")
    self.__householdSize+=1

  # at some point most kids move out
  def moveChild(self, familyMember):
    for i, child in enumerate(self.__children):
        if child.getName() == familyMember:
            del self.__children[i]
            break
    print("Child moved out and went to college!\n")
    self.__householdSize-=1

  # print out the household roster
  def toString(self):
    print("================Household Roster=================")
    print("\n               Adults:\n")
    for adult in self.__adults:
        print(adult.toString())
    print("             Children:\n")
    for child in self.__children:
        print(child.toString())
    print("             Pets:\n")
    for pet in self.__pets:
        print(pet.toString())
    print("             Total houshold size: " + str(self.__householdSize) + "\n" )
    print("=================================================\n")

# exercise the code
def main():
  # Parents
  person1 = Person(PersonType.ADULT,"John",Gender.MALE)
  person2 = Person(PersonType.ADULT,"Sara",Gender.FEMALE)
  adult1 = Adult(person1.getPersonType(),person1.getName(),person1.getGender(),JobType.PROGRAMMER)
  adult2 = Adult(person2.getPersonType(),person2.getName(),person2.getGender(),JobType.DOCTOR)
  
  # pets
  dog1 = Pet("Dog","Woofer",Gender.FEMALE)
  dog2 = Pet("Dog","Sir Woofs-a-lot",Gender.MALE)
  cat = Pet("Cat","Chairman Meow",Gender.MALE)
  
  # create the household
  household = Household("Woofersons")
  
  household.addAdult(adult1)
  household.addAdult(adult2)
  
  household.addPet(dog1)
  household.addPet(dog2)
  household.addPet(cat)
  
  household.createChild("Jennay",Gender.FEMALE,"Tea Set")
  household.createChild("Timmy",Gender.MALE,"Lasso")
  household.createChild("Eton",Gender.MALE,"Rattle")

  # Print out all the members of the household
  household.toString()
  
  # Grandma comes back to live with you
  person3 = Person(PersonType.ADULT,"Jeanny",Gender.FEMALE)
  adult3 = Adult(person3.getPersonType(),person3.getName(),person3.getGender(),JobType.NOT_ENTERED)
  
  # Give her the spare bedroom
  household.addAdult(adult3)
  
  # She brought the cranky old cat
  cat2 = Pet("Cat","Wilfried von Staffen",Gender.MALE)
  household.addPet(cat2)

  # take a second roll call
  household.toString()
  
  # Timmy's off to college
  household.moveChild("Timmy")
  # He took the dog
  household.movePet("Sir Woofs-a-lot")
  # Grandma moved out
  household.moveAdult("Jeanny")
  # And took the cat
  household.movePet("Wilfried von Staffen")
  
  # take a third roll call
  household.toString()

main()