from apps.users_app.models import Users

# create 3 users
Users.objects.create(first_name="Peter", last_name="Pan", email_address="peterpan@mail.com", age=20)
Users.objects.create(first_name="Nemo", last_name="Fish", email_address="nemo@mail.com", age=2)
Users.objects.create(first_name="Iron", last_name="Man", email_address="ironman@mail.com", age=30)

# retrieve all users
Users.objects.all()

# retrieve the last user
Users.objects.last()

# retrieve the first user
Users.objects.first()

# change the user with id=3 so that the last name is Pancake
user = Users.objects.get(id=3)
user.last_name = "Pancake"
user.save()

# delete the user with id=2 from the database
user = Users.objects.get(id=1)
user.delete()

# get all users, sorted by first name
Users.objects.all().order_by("first_name")

# get all the users, sorted by first name in descending order
Users.objects.all().order_by("last_name")