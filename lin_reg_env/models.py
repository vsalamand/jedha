from app import db

class Result(db.Model):
  __tablename__ = "linregresults"

  id = db.Column(db.Integer, primary_key = True)
  YearExperience = db.Column(db.Float)
  Prediction = db.Column(db.Float)

  def __init__(self, YearsExperience, Prediction):
    self.YearsExperience = YearsExperience
    self.Prediction = Prediction

  def __repr__(self):
    return "<id {}>".format(self.id)
