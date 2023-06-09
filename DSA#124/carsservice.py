class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

class Service:
    def __init__(self, car_list):
        self.__car_list=car_list
    def get_car_list(self):
        self.__car_list.sort(key=lambda x:x.get_year())
        l=[]
        for i in self.__car_list:
            l.append(i.get_model())
        return l
    def find_cars_by_year(self, year):
        list1=[]
        for i in self.__car_list:
            if int(i.get_year()) == year:
                list1.append(i.get_model())
        if(len(list1)==0):
            return None
        return list1
            
    def add_cars(self, new_car_list):
        self.__car_list.extend(new_car_list)
        self.__car_list.sort(key=lambda x: x.get_year())
    def remove_cars_from_karnataka(self):
        list1=self.__car_list.copy()
        for i in list1:
            if i.get_registration_number()[0:2] == "KA":
                a=i.get_model()
                self.__car_list.remove(i)
        print("The cars belongs to karnataka are removed from list")

#Implement Service class here

car1=Car("Dzire",2010,"KA09 ")
car2=Car("Maruti", 2011, "MH10 ")
car3=Car("Baleno", 2014,"KA12 ")
car4=Car("Swift",2017,"GJ01 ")
car5=Car("Alto",2013,"OD07 ")
car6=Car("Benz",2009,"KL07 ")
car7=Car("vitara",2017,"AP07")

s = Service([car1, car2, car3, car4,car5,car6,car7])
print(s.find_cars_by_year(2017))
print(s.get_car_list())
s.remove_cars_from_karnataka()
print("The new car list is",end =" ")
print(s.get_car_list())
