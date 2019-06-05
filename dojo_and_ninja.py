from apps.users_app.models import Dojo, Ninja

# create 3 dojos
Dojo.objects.create(name="A", city="San Francisco", state="CA")
Dojo.objects.create(name="B", city="San Jose", state="CA")
Dojo.objects.create(name="C", city="Oakland", state="CA")

# delete 3 dojos just created
for d in Dojo.objects.all():
    d.delete()

# create 3 more dojos
Dojo.objects.create(name="A", city="San Francisco", state="CA")
Dojo.objects.create(name="B", city="San Jose", state="CA")
Dojo.objects.create(name="C", city="Oakland", state="CA")

# create 3 ninjas that belongs to the first dojo
Ninja.objects.create(dojo=Dojo.objects.get(name="A"), first_name="Aloha", last_name="Hawaii")
Ninja.objects.create(dojo=Dojo.objects.get(name="A"), first_name="Ola", last_name="Wakiki")
Ninja.objects.create(dojo=Dojo.objects.get(name="A"), first_name="Chao", last_name="Tiki")

# create 3 ninjas that belongs to the second dojo
Ninja.objects.create(dojo=Dojo.objects.get(name="B"), first_name="Spider", last_name="Man")
Ninja.objects.create(dojo=Dojo.objects.get(name="B"), first_name="Pine", last_name="Apple")
Ninja.objects.create(dojo=Dojo.objects.get(name="B"), first_name="Sharp", last_name="Fish")

# create 3 ninjas that belongs to the third dojo
Ninja.objects.create(dojo=Dojo.objects.get(name="C"), first_name="Dark", last_name="Knight")
Ninja.objects.create(dojo=Dojo.objects.get(name="C"), first_name="Stephen", last_name="King")
Ninja.objects.create(dojo=Dojo.objects.get(name="C"), first_name="Diamond", last_name="Peak")

# retrieve all the ninjas from the first dojo
Ninja.objects.filter(dojo=Dojo.objects.first())

# retrieve all the ninjas from the last dojo
Ninja.objects.filter(dojo=Dojo.objects.last())

# retrieve the last ninja's dojo
Ninja.objects.last()

# Add a new text field called "desc" to Dojo class, default value is "old dojo

# create a new dojo
Dojo.objects.create(name="D", city="New York", state="NY", desc="New dojo")