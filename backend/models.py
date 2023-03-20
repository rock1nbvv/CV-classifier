from dataclasses import dataclass
from datetime import datetime

import app


@dataclass
class Rating(app.db.Model):
    id: int
    name: str
    estimated_class: str
    hr_interviewed: bool
    tech_interviewed: bool
    rank: float

    id = app.db.Column(app.db.Integer(), primary_key=True)
    name = app.db.Column(app.db.String(100))
    estimated_class = app.db.Column(app.db.String(100))
    hr_interviewed = app.db.Column(app.db.Boolean(), default=False)
    tech_interviewed = app.db.Column(app.db.Boolean(), default=False)
    rank = app.db.Column(app.db.Float())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Candidate: {self.id} - {self.estimated_class} - {self.rank}'
