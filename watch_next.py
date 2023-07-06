import spacy #import library and language model
nlp = spacy.load('en_core_web_md')

def similar_movie(description): #create function
    movies = [] #creates list of movie descriptions
    with open(r"C:\Users\sabri\Dropbox\SA23020008265\Data Science (Fundamentals)\T21\movies.txt", "r") as file:
        for line in file: #iterates through textfile
            movie = line.strip('/n') # newlines are stipped
            movies.append(nlp(movie)) #creates an 'nlp' for each movie
        
    similarity_scores = [nlp(description).similarity(movie) for movie in movies] #compute similarity each movie and description
    most_similar_index = similarity_scores.index(max(similarity_scores)) #find the index of eaach movie with the highest similarity score

    return movies[most_similar_index] #returns tite of the most similar movie

description =  "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
recommended_movie = similar_movie(description) # function applied 
print("Recommended movie:", recommended_movie) #prints the name of movie with highest similarity score with description