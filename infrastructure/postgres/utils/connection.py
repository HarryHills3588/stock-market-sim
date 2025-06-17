from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

class Connection():
    def __init__(self, url:str, echo = True):
        self.engine = create_engine(url, echo=echo)
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def get_session(self):
        return self.Session()
    
    def shutdown(self):
        self.Session.remove()
        self.engine.dispose()
