import tkinter as tk

def tower_of_hanoi_recursive(n, start, end, middle):
    global move_count
    if n > 0:
        tower_of_hanoi_recursive(n - 1, start, middle, end)

        end.append(start.pop())
        move_count += 1
        print_towers(move_count)

        tower_of_hanoi_recursive(n - 1, middle, end, start)


def print_towers(move):
    print(f"Move {move}:")
    print("Tower A:", tower_a)
    print("Tower B:", tower_b)
    print("Tower C:", tower_c)
    print()


def initialize_tower_a(n):
    return list(reversed(range(1, n + 1)))


def get_num_disks():
    global number
    try:
        number = int(entry.get())
        window_input.destroy()
    
    except ValueError:
        print("Invalid input.")


window_input = tk.Tk()
window_input.title('Disk Number')
window_input.geometry('250x100')

entry = tk.Entry(window_input)
entry.pack(pady=15)

button = tk.Button(window_input, text = 'Choose disk amount', command = get_num_disks)
button.pack(pady=5)

window_input.mainloop()

# Initialize towers
number_of_disks = number  # Change the number of disks here
tower_a = initialize_tower_a(number_of_disks)
tower_b = []
tower_c = []
move_count = 0

print("Initial Towers:")
print_towers(move_count)

tower_of_hanoi_recursive(number_of_disks, tower_a, tower_c, tower_b)

print("Towers after solving:")
print_towers(move_count)
print("Total moves:", move_count)



window_main = tk.Tk()
window_main.geometry('1920x1080')
window_main.title('Tower of Hanoi')

label_title = tk.Label(window_main, text = 'Tower of Hanoi', font = ('Times New Roman', 24, 'bold'), fg = 'black')
label_title.pack(pady = 2, side = tk.TOP, anchor = tk.N)

label_round = tk.Label(window_main, text = 'Round: 1', font = ('Times New Roman', 16), fg = 'black')
label_round.pack(side = tk.TOP, anchor = tk.N)

canvas = tk.Canvas(window_main, width = 1920, height = 1080)
canvas.create_rectangle(0, 725, 1920, 1080, fill='grey')
canvas.create_rectangle(250, 850, 275, 50, fill='red')
canvas.create_rectangle(950, 850, 975, 50, fill='red')
canvas.create_rectangle(1645, 850, 1670, 50, fill='red')
canvas.pack()




window_main.mainloop()