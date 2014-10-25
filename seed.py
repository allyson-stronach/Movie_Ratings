import model
import csv
u_data = open('/home/user/src/ratings/seed_data/u.data', 'r')
u_item = open('/home/user/src/ratings/seed_data/u.item', 'r')
u_user = open('/home/user/src/ratings/seed_data/u.user', 'r')




# new_user = User(age='%d', gender='%s', zip_code='%s', email='%s', password='%s') % (x, g, z, a, b) 

def load_users(session):
    # use u.user
    pass

def load_movies(session):
    # use u.item
    pass

def load_ratings(session):
    u_data_reader = csv.reader(u_data, delimiter = '\t')
    for line in u_data_reader:
        # without the delimiter specified above, this would also work to split the line:
            #sl = line[0].split() 

        #new_rating = model.Rating(id, movie_id, user_id, rating)
        dt = int(line[3])
        '881250949'

        new_rating = model.Rating()
        new_rating.user_id = int(line[0])
        new_rating.movie_id = int(line[1])
        new_rating.rating = int(line[2])
        new_rating.timestamp = int(line[3])
        session.add(new_rating)
        session.commit()
        

def main(session):
    load_ratings(session)


if __name__ == "__main__":
    s= model.connect()
    main(s)
