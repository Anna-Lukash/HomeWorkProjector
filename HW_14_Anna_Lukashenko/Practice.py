'''Practice
1) Modify the Country class to include a third instance attribute called capital as a string. Store your new class in a script and test it out by adding the following code at the bottom of the script:
japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.") 
The output of your script should be:
Japan population is 140000000 and capital is Tokyo.

2)Add increase_population method to country class. This method should take an argument and increase population of the country on this number.

3)Create add method to add two countries together. This method should create another country object with the name of the two countries combined and population of the two countries added together.
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add(herzegovina)
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'

4)(Optional) Implement previous method with magic method
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina' '''

class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        # 1)add third instance attribute capital
        self.capital = capital
        
    # 2)increase population of the country on number_icrease  
    def increase_population(self, number_icrease):
        return self.population * number_icrease 
        
    # 3) method creates another country object with the name of the two countries combined and population of the two countries added together.
    def add(self,other):
        name1  =  self.name +" "+ other.name  
        population2 = self.population + other.population   
        return Country(name1, population2,'')
    
    # 4) previous method with magic method
    def __add__(self,other):
        name1  =  self.name +" "+ other.name  
        population2 = self.population + other.population   
        return Country(name1, population2,'')
# 1)
japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.") 
# 2)
print(japan.increase_population(4))
# 3) and 4)
bosnia = Country('Bosnia', 10_000_000, "")
herzegovina = Country('Herzegovina', 5_000_000, "")  
bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)



