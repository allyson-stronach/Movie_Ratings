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
    return (datetime.datetime.fromtimestamp(int(timestamp))).strftime('%Y-%m-%d %H:%M:%S')

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

        #CURRENT ERROR
        #(original cause: TypeError: SQLite DateTime type only accepts Python datetime and date objects as input.) u'INSERT INTO ratings (user_id, movie_id, rating, timestamp) VALUES (?, ?, ?, ?)' [{'movie_id': 242, 'user_id': 196, 'timestamp': '1997-12-04 07:55:49', 'rating': 3}]


def main(session):
    load_ratings(session)


if __name__ == "__main__":
    s= model.connect()
    main(s)
