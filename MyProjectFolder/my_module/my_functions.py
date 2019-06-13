
import random
import string

class Movies():

    def __init__(self, title, year, rating, description, preference):

        """ Returns information about the movie

        Parameters
    	---------- 

    	title : str
    			The title of the movie

    	year : int
    		   The year the movie was released

    	rating: int or float
    			The movie's IMDB rating

    	description: str
    				The plot of the movie

    	preference: str
    				A short opinion on the movie


        """
        self.title = title 
        self.year = year 
        self.rating = rating 
        self.description = description 
        self.preference = preference  
        
#Below are the movies that the bot can provide information (title,year,rating etc.) about:

booksmart = Movies("Booksmart", "2019", 7.5, "On the eve of their high school graduation, two "\
                   "academic superstars and best friends realize they should have worked less" \
                   " and played more.","I loved this movie! You should definitely give it a shot!")

avengers = Movies("Avengers:Endgame", "2019", 8.8, "The Avengers assemble once more in order to "\
                  "undo Thanos' actions and restore order to the universe.","I love superhero movies so this was "\
                  "one of my favorite movies of the year!")

aladdin = Movies("Aladdin", "2019", 7.4, "A kind-hearted street urchin and a power-hungry Grand "\
                 "Vizier vie for a magic lamp that has the power to make their deepest wishes come true.","I "\
                 "haven't seen this movie yet but if it's anything like the original version I'm excited to see it!")

shazam = Movies("Shazam!", "2019", 7.4, "We all have a superhero inside us, it just takes a bit of "\
                "magic to bring it out. In Billy Batson's case, by shouting out one word- SHAZAM!","Shazam is such"\
                " an entertaining movie! Give it a try if you're a fan of superhero movies and love comedy!")

rocketman = Movies("Rocketman", "2019", 7.7, "A musical fantasy about the fantastical human story "\
                   "of Elton John's breakthrough years.","If you liked Bohemian Rhapsody you should give"\
                   " this movie a try!")

arrival = Movies("Arrival", "2016", 7.9, "A linguist works with the military to communicate with "\
                 "alien lifeforms after twelve mysterious spacecraft appear around the world.","The visuals are "\
                 "perfect, the acting, especially from Amy Adams, is wonderful.")


#list of the movies that are provided above:
list_of_movies = [booksmart, avengers, aladdin, shazam, rocketman, arrival]

#list of the names of movies
movie_title_list = ["booksmart", "avengers: endgame", "aladdin", "shazam", "rocketman", "arrival"]

#dictionary that provides access from titles (in string form) to the objects defined under the Movies class 
dict_movies = {"Booksmart": booksmart, "Avengers: Endgame": avengers, "Aladdin" : aladdin,\
               "Shazam":shazam, "Rocketman": rocketman, "Arrival":arrival}

#Responses that are used if there isn't an answer for the input:
any_answer = ['Sure.', 'Okay', 'Huh?', 'Good point!', 'Thanks!']

#Responses that are used if the input was a question but there isn't a specified answer:
question_answers = "Unfortunately I don't have an answer for everything :("\
" What else do you want to talk about?"


#Functions for MovieBot:

def is_question(input_string):

    """ 
    Checks if the entered string is a question

    Credit: Function from assignment A3 

    Parameters
    ----------
    input_string: str
        String of words that are typed into the chatbox

    Returns
    -------
    answer : boolean
            Returns True if the entered string is a question

    """

    if "?" in input_string: 
        output = True  

    else:
        output = False

    return output



#lists for the greeting function below
greetings_in = ['hello', 'hi', 'hey'] # possible inputs to the chatbox
greetings_out = ["Hello there, movie-lover!", "Hey, let's chat about movies!",\
                 "Welcome! I'm excited to chat with you about movies!"] # outputs to be selected at random

def greeting(input_list):

    """
    Checks if the input_list has one of the greetings_in words above
    Then generates an answer with one of the greetings_out elements above

    Credit: I got the idea to make two separate lists for greetings_in and greetings_out from the A3 assignment
            However, I changed the way the function executes and returns a respond.

    Parameters
    ----------

    input_list: list
                List of words that were entered to the chatbox

    Returns
    -------
    answer: str
            Returns one of the greetings_out phrases by choosing randomly


    """
    answer = ""
    
    for element in input_list: 
        
        if element in greetings_in:  #checks if the input included a greeting word
            
            answer = random.choice(greetings_out)  
                
    return answer
    
def remove_punctuation(input_string):

    """ 
    Removes punctuation from the entered string to the chatbox

    Credit: Function from assignment A3 

    Parameters
    ----------
    input_string: str
        String that is typed into the chatbox

    Returns
    -------
    answer : str
            Returns the input string without the punctuation


    """

    out_string = ""
    
    for character in input_string:
        
        if character not in string.punctuation:
            out_string = out_string + character #combines non-punctuation characters in input 
            
            
    return out_string 


out_list = []

def prepare_text(input_string):

    """ 
    Prepares the text by making all letters lower caps, removing punctuation,
    splitting the words and appending to a list.

    Credit: Function from assignment A3 

    Parameters
    ----------
    input_string: str
        String of words that are typed into the chatbox

    Returns
    -------
    answer : list
            List of words that are all lower caps and without punctuation.


    """
    

    temp_string = input_string.lower() 
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split() #splits the words to be used as input in other functions
    
    return out_list



def movie_suggestion(input_list):  
    """Picks a random movie from the list list_of_movies

    Parameters
    ----------
    input_list : list
        List that have the words "What" and "movie" executes this function

    Returns
    -------
    answer : string
        The title of the random movie 

    """

    answer = ""

    if "What" and "movie" in input_list: 

        word = random.choice(list_of_movies) #randomly picks a movie fom list
        answer = "How about " + word.title + "?"


    return answer



def watched_or_not(input_list):

    """Returns whether or not the movie in the string is under the Movie class

    Parameters
    ----------
    input_list : list
        List of the words typed into the chatbox

    Returns
    -------
    answer : str
        String that says whether or not the movie is under the Movies class

    """

    answer = ""

    for element in input_list: 
        
        if element in movie_title_list: #checks if movie title is included in the list
            
            answer = "Yes! I have seen " + element + "!" 

        else:
        
            answer = "No, unfortunately I haven't seen it yet. I'll add it to my to-watch list though!" 
        
    return answer



def list_all_movies(input_list):
    """Lists all the movies that are in the Movie class

    Parameters
    ----------
    input : list
        List of the words typed into the chatbox

    Returns
    -------
    answer : list
        List of the titles of the movies that are in the Movies class

    """
    answer = ""

    if "list" and "movies" in input_list: 
        
        answer = movie_title_list
        
        return answer


def prep_movie_name(input_string):

    """Changes the movie title (string) to the object name under Movies class

    Parameters
    ----------
    input_string : list
        List of the words typed into the chatbox

    Returns
    -------
    final_movie : object in Movies class
        Name of the object that has access to the attributes in Movies 
    """
        
    if input_string in dict_movies.keys(): 
    
        movie_name = dict_movies[input_string] #accesses the object name using the dict key
        
        final_movie = movie_name
            
        return final_movie



def movie_info(final_movie, command):

    """Returns the attributes of the variables under Movies

    Parameters
    ----------
    final_movie : object in Movies class
        Title of the movie
    command : str
        Name of the attribute 

    Returns
    -------
    answer : str
        The attribute (title, year, rating etc.) of the movie 
    """
    
    if command == "title":
        answer = final_movie.title 
        
    if command == "year":
        answer = final_movie.year
        
    if command == "rating":
        answer = final_movie.rating
        
    if command == "description":
        answer = final_movie.description
        
    if command == "thoughts":
        answer = final_movie.preference
    
    #returns the information associated with the command (title, year, rating etc.)
    return answer 

def end_chat(input_list):
    """ 
    Checks if the word "quit" is in the entered string to the chatbox

    Credit: Function from assignment A3 

    Parameters
    ----------
    input_list: list
        List of words that are typed into the chatbox

    Returns
    -------
    answer : boolean
            Returns boolean and ends chat if the output is True


    """
    if "quit" in input_list:
        answer = True
        
    else:
        answer = False
        
    return answer

