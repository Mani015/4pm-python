d1={'dhoni':'captain','virat':'vice-c','rohit':'opener','dk':'one-down','hardik':'all-rounder'}

d1.setdefault('shami','dead bowler')
# print(d1)
# {'dhoni': 'captain', 'virat': 'vice-c', 'rohit': 'opener', 'dk': 'one-down', 'hardik': 'all-rounder', 'shami': 'dead bowler'}
d1.setdefault('umesh')
print(d1)
# {'dhoni': 'captain', 'virat': 'vice-c', 'rohit': 'opener', 'dk': 'one-down', 'hardik': 'all-rounder', 'shami': 'dead bowler', 'umesh': None}

