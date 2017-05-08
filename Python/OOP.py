# Part 1
# Answer the following questions.

# What is a class?
	#A class is a blue print which has method and properties inside it to make new objects/instances
	#This removes the need for duplication when making multiple instances with similar structure

# What is an instance?
	#An instance is what is created when you create new objects using classes

# What is encapsulation?
	#Encapsulation is seperating everything into their own classes in logical groups

# What is abstraction?
	#Level of abstraction is pretty much what do you really need to know. Do you need a lower level of abstraction to know how 
	#A function is made, or do you need a higher level of abstraction that you know it exists but don't care how it is implimented under the hood

# What is inheritance?
	#Inheritance is where classes borrow ths structure of a previously existing class. As they are similar in nature but not logically the same grouping

# What is multiple inheritance?
	#Multiple inheritance is where a Class can inherit from multiple classes for example, Penguins can inherit classes from Land_animal and Water_animal

# What is polymorphism?
	#polymorphism is having the same function call name on different classes or instances. They effectively do the same thing, but impliment it differently. For example
	#One implimentation can use a Bool to check if something is on or off, or another implimentation can check 1 or 0 for on and off respectively. 

# What is method resolution order or MRO?
	#MRO is method resolution order. It make sure that the first method is taken over the subsequent methods if there is multiple inheritance with the same function name.
	#This ensures order and makes inheritence from multiple sources constisent 	

# Part 2
# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __rep__(self):
		return "{} of {}".format(self.suit, self.value)

class Deck:
	def __init__(self):
		suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
		values = ('A',2,3,4,5,6,7,8,9,10,'J','Q','K')
		self.decks = [Card(suit,value) for suit in suits for value in values]

	def shuffle(self):
		shuffle(self.decks)
		return self.decks

	def deal(self):
		try:
			return self.cards.pop()
		except ValueError:
			return "No cards to be dealt"



# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)



