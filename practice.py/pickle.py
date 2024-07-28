import pickle
animalDict = { 'Cat': 2, 'Dog': 7, 'Lion': 4, 'Tiger': 9, 'Leopard': 11, 'Bear': 8, 'Elephant': 15 }
outfile = open('animals','wb')
pickle.dump(animalDict, outfile)
outfile.close()
fst = open("animals", 'rb')				
data = pickle.load(fst)			        
try:									
  while(True):
    print(data)
    data = pickle.load(fst)
except:
  print("Bye")