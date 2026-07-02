from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#with the help of sqlalchemy we can directly communicate with the database using python.
#create_engine  to make a connection between python app and database
#so we dont have to erite a sql queries , we can use the raw code. 
#a base class which will inherit the properties of the tables in sql
#to read the data inside the database and make changes 


#coonection is established
DATABASE_URL="mysql+pymysql://3PNpgTmDS5oE6F9.root:<PASSWORD>@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?ssl_mode=VERIFY_IDENTITY&ssl_ca=<CA_PATH>"

#here we have specified that to which database the connection is established
engine= create_engine(
    DATABASE_URL,
    pool_pre_ping=True, #to check if it exists
    connect_args={      #to make a secure connection
        "ssl":{
            "ssl":True
        }

    }
)

SessionLocal =sessionmaker(bind=engine) #makes a new batabase seeion
Base = declarative_base()   #used to create a databse using python.


