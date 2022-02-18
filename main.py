from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.metrics import dp

class TicTacToe(App):
	pass

# The layout of the complete screen
class Screen(StackLayout):
	pass

# Grid layout of the boxes for the tictactoe game	
class Game(GridLayout):
	turn_text = StringProperty("Player X Turn") # Used in the 2nd lebel(made in tictactoe.kv) to show turns
	buttons = [] 
	current_player_symbol = "X" # Starting player symbol is "X"
	button_colors = {"X": (1, 0, 0), "O": (0, 0, 1)} # Different colors for both players  
	turn_count = 0
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		for i in range(9):
			b = Button(font_size=dp(50))
			b.bind(on_press=self.pressed) # Call pressed function when button is pressed
			self.buttons.append(b)
			self.add_widget(b)
	
	# Whenever a player presses a button, the player's symbol is appears there
	def pressed(self, button):
		if button.text != "X" and button.text != "O":
			button.background_color = (0, 0, 0, 1)
			button.text = self.current_player_symbol
			button.color = self.button_colors[self.current_player_symbol]
			self.turn_count += 1
			if self.check_win():
				self.game_complete();
				return
			self.change_player_symbol()
			
	# Change player(i.e symbol) after each turn
	def change_player_symbol(self):
		if self.current_player_symbol == "X":
			self.current_player_symbol = "O"
		else:
			self.current_player_symbol = "X"
		# Change the label text to display current player(symbol)
		self.turn_text = "Player " + self.current_player_symbol + " Turn"
		
	# Checking for the winner
	def check_win(self):
		if (self.check_row() or self.check_column() or self.check_diagonal()):
			self.turn_text = "Player " + self.current_player_symbol + " Won"
			return True 
		
		if self.turn_count == 9:
			self.turn_text = "It's a Draw"
			return True
		return False
		
	# Function to check rows
	def check_row(self):
		for i in range(3):
			if self.buttons[i*3 + 0].text == self.current_player_symbol \
				and self.buttons[i*3 + 1].text == self.current_player_symbol \
				and self.buttons[i*3 + 2].text == self.current_player_symbol:
				return True
		return False
	
	# Function to check columns
	def check_column(self):
		for i in range(3):
			if self.buttons[i].text == self.current_player_symbol \
				and self.buttons[i + 3].text == self.current_player_symbol \
				and self.buttons[i + 6].text == self.current_player_symbol:
				return True
		return False
		
	def check_diagonal(self):
		if self.buttons[0].text == self.current_player_symbol \
			and self.buttons[4].text == self.current_player_symbol \
			and self.buttons[8].text == self.current_player_symbol:
				return True
		
		if self.buttons[2].text == self.current_player_symbol \
			and self.buttons[4].text == self.current_player_symbol \
			and self.buttons[6].text == self.current_player_symbol:
				return True
		return False
		
	# Disable all the buttons when the game is completed				 
	def game_complete(self):
		#self.turn_text = "Game Completed " + self.turn_text
		for i in range(9):
			self.buttons[i].disabled = True
		
		
def main():
	TicTacToe().run()

if __name__ == "__main__":
	main()
	
