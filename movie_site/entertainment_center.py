import fresh_tomatoes # module creates html file
import media # brings in Movie class

# create 6 instances of movies:
toy_story = media.Movie('Toy Story','A story of a boy and his toys',
                            'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                            'https://www.youtube.com/watch?v=KYz2wyBy3kc')

school_of_rock = media.Movie('School of Rock','Use Rock and Roll to Learn',
                                    'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                                    'https://www.youtube.com/watch?v=XCwy6lW5Ixc')

the_departed = media.Movie('The Departed', 'A cop and a crook go undercover',
                            'https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg',
                            'https://www.youtube.com/watch?v=rEL0vRfpW6w')

the_town = media.Movie('The Town','Bankrobbers terrorize Charlestown',
                        'https://upload.wikimedia.org/wikipedia/en/d/da/The_Town_Poster.jpg',
                        'https://www.youtube.com/watch?v=uAjECYnrYks')

the_sandlot = media.Movie('The Sandlot','Rag-tag kids on a quest to recover Babe Ruth autographed ball',
                        'https://upload.wikimedia.org/wikipedia/en/d/d4/Sandlot_poster.jpg',
                        'https://www.youtube.com/watch?v=ec9W8JbFykw')

back_to_the_future = media.Movie('Back to the Future','Marty McFly gets sent back in time',
                        'https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg',
                        'https://www.youtube.com/watch?v=yosuvf7Unmg')

# throw movies into a list, input for the .open_movies_page method
movies = [toy_story,school_of_rock,the_departed,
            the_town,the_sandlot,back_to_the_future]
fresh_tomatoes.open_movies_page(movies) # creates the html



# if __name__ == "__main__":
#     toy_story = media.Movie("Toy Story")
#     print(toy_story.title)
