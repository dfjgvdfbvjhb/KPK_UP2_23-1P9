from peewee import *
from playhouse import validate_range, validate_regexp, validate_one_of, validate_length

db = SqliteDatabase('data.db')

class BaseModel(Model):
    class Meta:
        database = db

class Groups(BaseModel):
    class Meta:
        db_table = "Group"
    id = AutoField()
    year = IntegerField(validators=[validate_range(2000, 2999)])
    is_active = BooleanField()
    tutor_id = IntegerField(null=True, default=None, validators=[validate_range(1, ...)])
    student_count = IntegerField(default=0,validators=[validate_range(0, 30)])
    cipher_of_the_training_area = CharField(
        max_length=8,
        validators=[validate_regexp(r'\d\d\.\d\d\.\d\d')]
    )
    number = IntegerField(constraints=[Check('number > 0')])
    after_class_number = IntegerField(
        validators=[validate_one_of([9, 11])]
    )
    prefix = CharField(validators=[validate_length(1, 2)])

class Students(BaseModel):
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