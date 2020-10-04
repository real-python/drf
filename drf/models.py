from django.db import models

# --------------- One To One --------------------
'''
class UserDetails(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone = models.CharField(max_length=10)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=7)
    userimage = models.ImageField(upload_to='UserImage/')

    def __str__(self):
        return self.phone
'''

# --------------- Many To Many ------------------
class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.CharField(max_length=10)
    tag = models.ManyToManyField(Tag, related_name='post_tag_realtion')

    def __str__(self):
        return self.content


# -------------- ForeignKey ----------------
class Student(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=10)
    stu = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='school_student', 
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.email


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __unicode__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        related_name='album_musician', 
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name
