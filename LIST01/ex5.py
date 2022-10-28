network=['idea','jio','airtel','Bsnl','telenor','TaTAdocomo','vodafone']
network.pop(2)
# pop method also taken index value
print(network)
# ['idea', 'jio', 'Bsnl', 'telenor', 'TaTAdocomo', 'vodafone']

network.pop(10)
print(network)
# IndexError: pop index out of range