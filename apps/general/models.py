from django.db import models
from multiselectfield import MultiSelectField

SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected')
)

PERSONALITY = (
    ('', 'Select a personality'),
    ('I am outgoing', 'I am outgoing'),
    ('I am sociable', 'I am sociable'),
    ('I am antisocial', 'I am antisocial'),
    ('I am discreet', 'I am discreet'),
    ('I am serious', 'I am serious')
)

SMOKER = (
    ('1', 'Yes'),
    ('2', 'No')
)

# Multiple Checkboxes
FRAMEWORKS = (
    ('Laravel', 'Laravel'),
    ('Angular', 'Angular'),
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('Vue', 'Vue'),
    ('Others', 'Others'),
)

LANGUAGES = (
    ('Python', 'Python'),
    ('Javascripts', 'Javascripts'),
    ('Java', 'Java'),
    ('C++', 'C'),
    ('Ruby', 'Ruby'),
    ('Others', 'Others'),
)

DATABASES = (
    ('MySql', 'MySql'),
    ('Postgree', 'Postgree'),
    ('MongoDBSqlite3', 'MongoDBSqlite3'),
    ('Sqlite3', 'Sqlite3'),
    ('Oracle', 'Oracle'),
    ('Others', 'Others'),
)

LIBRARIES = (
    ('Ajax', 'Ajax'),
    ('Jquery', 'Jquery'),
    ('React.js', 'React.js'),
    ('Chart.js', 'Chart.js'),
    ('Gsap', 'Gsap'),
    ('Others', 'Others'),
)

MOBILE = (
    ('React native', 'React native'),
    ('Kivy', 'Kivy'),
    ('Flutter', 'Flutter'),
    ('Ionic', 'Ionic'),
    ('Xamarim', 'Xamarim'),
    ('Others', 'Others'),
)

OTHERS = (
    ('UML', 'UML'),
    ('SQL', 'SQL'),
    ('Docker', 'Docker'),
    ('GIT', 'GIT'),
    ('GraphQL', 'GraphQL'),
    ('Others', 'Others'),
)

class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25) 
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    file = models.FileField()
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    smoker = models.CharField(max_length=3, null=True, choices=SMOKER, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')
    #Multiple Checkboxes
    frameworks = MultiSelectField(max_length=1000 , choices=FRAMEWORKS, default='')
    languages = MultiSelectField(max_length=1000 ,choices=LANGUAGES, default='')
    databases = MultiSelectField(max_length=1000 ,choices=DATABASES, default='')
    libraries = MultiSelectField(max_length=1000 ,choices=LIBRARIES, default='')
    mobile = MultiSelectField(max_length=1000 ,choices=MOBILE, default='')
    others = MultiSelectField(max_length=1000 ,choices=OTHERS, default='')

    def __str__(self):
        return self.firstname
    
        # Capitalize (F-name and L-name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    # Concatenate F-name and L-name (Admin Table)
    def name(obj):
        return "%s %s" % (obj.firstname, obj.lastname)
    
    # Concatenate (when clicking over the candidates)
    def __str__(self):
        return self.firstname + ' ' + self.lastname