# from turtle import Turtle, Screen


# jimmy = Turtle()
# jimmy.shape("turtle")
# jimmy.color("green")
# jimmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electricity", "Water", "Fire"])
print(table)




