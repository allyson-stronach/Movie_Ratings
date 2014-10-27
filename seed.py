import model
import csv
import datetime
u_data = open('/home/user/src/ratings/seed_data/u.data', 'r')
u_item = open('/home/user/src/ratings/seed_data/u.item', 'r')
u_user = open('/home/user/src/ratings/seed_data/u.user', 'r')


def load_users(session):
    # use u.user
    pass

def load_movies(session):
    # use u.item
    pass

def to_datetime_from_timestamp(timestamp):
    date_string = (datetime.datetime.fromtimestamp(int(timestamp))).strftime('%d-%b-%Y') # this line used to be: '%Y-%m-%d %H:%M:%S' if we wanted to include time info, we could re-include this info. 
    return datetime.datetime.strptime(date_string, '%d-%b-%Y')

def load_ratings(session):
    u_data_reader = csv.reader(u_data, delimiter = '\t')
    for line in u_data_reader:
        # without the delimiter specified above, this would also work to split the line:
            #sl = line[0].split() 
        timestamp = int(line[3])
        datetime = to_datetime_from_timestamp(timestamp)

        new_rating = model.Rating()
        new_rating.user_id = int(line[0])
        new_rating.movie_id = int(line[1])
        new_rating.rating = int(line[2])
        new_rating.timestamp = datetime
        session.add(new_rating)
    
    session.commit()


def main(session):
    load_ratings(session)


if __name__ == "__main__":
    s= model.connect()
    main(s)
