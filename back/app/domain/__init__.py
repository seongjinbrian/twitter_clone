from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
Base = declarative_base()
# engine = create_engine('sqlite:///twitter.db')
# def init_db():
#     import user.user
#     import twitter.twitter
#     Base.metadata.create_all(bind=engine)