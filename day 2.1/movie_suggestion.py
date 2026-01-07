movies={
  "comedy":{
             "hollywood":["The Mask", "Home Alone", "21 Jump Street"],
             "bollywood":["Hera Pheri", "Chupke Chupke", "3 Idiots"]
}, 
  "horror":{
             "hollywood": ["The Conjuring", "Insidious", "Annabelle"],
             "bollywood":["Stree", "Tumbbad", "Bhoot"]
}, 
  "drama":{
             "hollywood": ["Forrest Gump", "The Pursuit of Happyness", "The Shawshank Redemption"],
             "bollywood":["Taare Zameen Par", "Swades", "Barfi"]
}} #mutiple value dictionary ....

print("what kind of movie would you like to watch today?")
print("options: comedy, horror, drama")
genre= input("entre genre: ")

print("which industry do you prefer?")
print("options: bollywood, hollywood")
industry= input("entre industry: ")

print("here are some", industry,genre + " movies you might enjoy!")
print(movies[genre][industry]) #extracting multipe key value ......