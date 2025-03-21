# class Player:
#     nationalTeamName = "Indonesia" # class variable

#     def __init__(self, playerName):
#         self.playerName = playerName # instance variable
    
#     def __str__(self):
#         # concatenate class variable and instance variable
#         return str({"nationalTeamName": Player.nationalTeamName, **vars(self)})

# Budi = Player("Budi")
# print(Budi)

# Bambang = Player("Bambang")
# print(Bambang)

# class Company:
#     formerCompanyName = []
#     companyName = 'Indosat Tbk'
#     def __init__(self, name):
#         self.name = name # creating instance variable

# company1 = Company('Adam')
# company2 = Company('Agustin')
# company1.formerCompanyName.append('Simpati Tbk')
# company2.formerCompanyName.append('Three Tbk')

# print("Name:", company1.name)
# print("Name:", company1.companyName)
# print(company1.formerCompanyName)
# print("Name:", company2.name)
# print("Name:", company2.companyName)
# print(company2.formerCompanyName)


# class Player1:
#     teamName = 'Liverpool' # class variables
#     formerTeams = []

#     def __init__(self, name):
#         self.name = name # creating instance variables

# p1 = Player1('Mark')
# p1.formerTeams.append('Barcelona')
# p2 = Player1('Steve')
# p2.formerTeams.append('Chelsea')
# print("Name:", p1.name)
# print("Team Name:", p1.teamName)
# print(p1.formerTeams)
# print("Name:", p2.name)
# print("Team Name:", p2.teamName)
# print(p2.formerTeams)

class Company:
   currentCompany = 'Google' # class variables

   def __init__(self, name):
       self.name = name # creating instance variables
       self.formerCompany = []

c1 = Company('Rudi')
c1.formerCompany.append('Microsoft')
c2 = Company('Adam')
c2.formerCompany.append('Amazon')
print("Name:", c1.name)
print("Current Company:", c1.currentCompany)
print("Former Company:", c1.formerCompany)
print("Name:", c2.name)
print("Current Company:", c2.currentCompany)
print("Former Company:", c2.formerCompany)
