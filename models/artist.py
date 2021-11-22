class Artist(Base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)