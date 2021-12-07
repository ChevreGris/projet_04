class Game:
    def __init__(self, player1, player2 ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.winner = None


a = [
    [8, 'PICASSO', 'Pablo', '25/10/1881', 'M', 2143, '                  '],
    [1, 'PICASSO', 'Pablo', '25/10/1881', 'M', 994, '                  '],
    [5, 'PICASSO', 'Pablo', '25/10/1881', 'M', 995, '                  '],
    [2, 'PICASSO', 'Pablo', '25/10/1881', 'M', 2141, '                  '],
    [7, 'PICASSO', 'Pablo', '25/10/1881', 'M', 9947, '                  '],
    [3, 'PICASSO', 'Pablo', '25/10/1881', 'M', 900, '                  '],
    [4, 'PICASSO', 'Pablo', '25/10/1881', 'M', 92144, '                  '],
    [6, 'PICASSO', 'Pablo', '25/10/1881', 'M', 2146, '                  '],
]

r = {1: [994, 2], 2: [2141, 1], 8: [2143, 1], 4: [92144, 0.5], 5: [995, 2], 6: [2146, 0], 3: [900, 0], 7: [9947, 0.5]}
sorted_by_value = sorted(r.items(), key=lambda kv: (kv[1][1], kv[1]), reverse=True)

print(r)
print(sorted_by_value)
e = []
for i in sorted_by_value:
    e.append(i[0])
print(e)

sorted_a = a.sort(key=lambda x: e.index(x[0]))
print(a)

"""
a = [
    {'id': 8, 'lastname': 'PICASSO', 'firstname': 'Pablo', 'birthdate': '25/10/1881', 'sex': 'M', 'ranking': 994, 'space': '                  '},
    {'id': 2, 'lastname': 'PICASSO', 'firstname': 'Pablo', 'birthdate': '25/10/1881', 'sex': 'M', 'ranking': 994, 'space': '                  '},
    {'id': 3, 'lastname': 'PICASSO', 'firstname': 'Pablo', 'birthdate': '25/10/1881', 'sex': 'M', 'ranking': 994, 'space': '                  '},
    {'id': 5, 'lastname': 'PICASSO', 'firstname': 'Pablo', 'birthdate': '25/10/1881', 'sex': 'M', 'ranking': 994, 'space': '                  '},
    {'id': 1, 'lastname': 'PICASSO', 'firstname': 'Pablo', 'birthdate': '25/10/1881', 'sex': 'M', 'ranking': 994, 'space': '                  '},
    {'id': 4, 'lastname': 'PICASSO', 'firstname': 'Pablo', 'birthdate': '25/10/1881', 'sex': 'M', 'ranking': 994, 'space': '                  '},
    {'id': 7, 'lastname': 'PICASSO', 'firstname': 'Pablo', 'birthdate': '25/10/1881', 'sex': 'M', 'ranking': 994, 'space': '                  '},
    {'id': 6, 'lastname': 'PICASSO', 'firstname': 'Pablo', 'birthdate': '25/10/1881', 'sex': 'M', 'ranking': 994, 'space': '                  '},
]

r = {1: [994, 2], 2: [2141, 1], 8: [2143, 1], 4: [92144, 0.5], 5: [995, 2], 6: [2146, 0], 3: [900, 0], 7: [9947, 0.5]}
sorted_by_value = sorted(r.items(), key=lambda kv: (kv[1][1], kv[1]), reverse=True)

print(sorted_by_value)
e = []
for i in sorted_by_value:
    e.append(i[0])
print(e)

#sorted_a = a.sort(key=lambda x: e.index(x[0]))
#z = sorted(a, key=lambda id: (id[0]))
#sorted(self.players, key=lambda player: (player.ranking), reverse=True)
#print(z)

"""