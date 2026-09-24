# Using Dictionary comprehensions 
# for constructing output dictionary 
state = ['Gujarat', 'Maharashtra', 'Rajasthan'] 
capital = ['Gandhinagar', 'Mumbai', 'Jaipur'] 
dict_using_comp = {key:value for (key, value) in zip(state, capital)} 
print("Output Dictionary using dictionary comprehensions:",dict_using_comp)
