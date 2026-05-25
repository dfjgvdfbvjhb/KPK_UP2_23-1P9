from peewee import *
from playhouse import validate_range, validate_regexp, validate_one_of

db = SqliteDatabase('data.db')

class Basemodel(Model):
    class Meta:
        database = db

class Groups(Basemodel):
    class Meta:
        db_table = "Group"
    id = AutoField()
    year = IntegerField(validators=[validate_range(2000, 2999)])
    is_active = BooleanField()
    tutor_id = IntegerField(null=True, default=None)
    student_count = IntegerField()
    cipher_of_the_training_area = CharField(
        max_length=8,
        validators=[validate_regexp(r'\d\d\.\d\d\.\d\d')]
    )
    number = IntegerField()
    after_class_number = IntegerField(
        validators=[validate_one_of([9, 11])]
    )
    prefix = CharField(max_length=2)

class Students(Basemodel):
    class Meta:
        db_table = 'Students'
    
    student_id = IntegerField()
    group_id = ForeignKeyField(Groups, backref='students', on_delete='CASCADE')

def init_db():
    db.connect()
    db.create_tables([Groups, Students])
    print("База данных инициализирована")

if __name__ == '__main__':
    init_db()