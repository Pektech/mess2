from .extensions import db, ma
from sqlalchemy.ext.associationproxy import association_proxy


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alexa_id = db.Column(db.String(230), unique=True, nullable=False)

    family_members = db.relationship('Family', lazy=True)

    def __repr__(self):
        return '<Alexa {}>'.format(self.alexa_id)



class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(120))
    mess_to = db.relationship('Messages',foreign_keys='Messages.to_id',
                               backref='fam_to', lazy=True)
    mess_from = db.relationship('Messages',foreign_keys='Messages.from_id',
                               backref='fam_sent', lazy=True)
    show = association_proxy('mess_to', 'message')

    def __repr__(self):
        return '{}'.format(self.name)




class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_id = db.Column(db.Integer, db.ForeignKey('family.id'))
    message = db.Column(db.Text(280))
    to_id = db.Column(db.Integer,db.ForeignKey('family.id'))
    deleted_flag = db.Column(db.Boolean, nullable=False)

    show = association_proxy('messages','message')

    # def as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class MessagesSchema(ma.ModelSchema):
    class Meta:
        model = Messages