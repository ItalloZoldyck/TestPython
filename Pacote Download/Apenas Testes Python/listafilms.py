movies = ['The Holy Grail', 'The Life Of Brian', 'The Meaning of Life']
print(movies)
cast = ['Cleese', 'Palin', 'jones', 'Idle']
print(cast)
print(len(cast))
print(cast[1])
cast.append('Gilliam')
print(cast)
cast.pop()
print(cast)
cast.extend(['Gilliam', 'Chapman'])
print(cast)
cast.remove('Chapman')
print(cast)
cast.insert(0, 'Chapman')
print(cast)
movies = ['The Holy Grail', 1975, 'The Life of Brian', 1979, 'The Meaning of Life', 1983]
print(movies)
fav_movies = ['The Holy Grail', 'The Life of Brian']
print(fav_movies[0])
print(fav_movies[1])
fav_movies = ['The Holy Grail', 'The Life of Brian']
for each_flick in fav_movies:
    print(each_flick)

movies = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91,
          ['Graham Chapman',
           ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

print(movies[4][1][3])
for each_item in movies:
    print(each_item)

names = ['Michael', 'Terry']
isinstance(names, list)
num_names: int = len(names)
isinstance(num_names, list)

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
                else:
                    print(nested_item)
        else:
            print(each_item)

            def print_lol(the_list):
                for each_item in the_list:
                    if isinstance(each_item, list):
                        print_lol(each_item)
                    else:
                        print(each_item)
                        print_lol(movies)
import emoji
print(emoji.emojize('Lista concluida! :sunglasses:', use_aliases=True))
