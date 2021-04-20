mydict = {
    'harry': 'Coder',
    'mp': 'Noob',
    'marks': [1,3,4],
    'anotherdict' : {'Mp': 'Player'}

}

print(mydict.keys()) # prints the keys of the dictionaries
print(type(mydict.keys()))
print(mydict.values()) # prints the values of the dictionaries
print(mydict.items()) # prints the (key, value) of the dictionaries

update_dict = {
    "tong": "tang"
}
mydict.update(update_dict) # can update the dictionary with this
print(mydict)

print(mydict.get("mp1")) #returns None as mp1 is not present
print(mydict["mp1"]) # throws error as the key is not present




