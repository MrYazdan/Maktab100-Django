from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, null=False)


# class VIPPerson(Person):
#     class Meta:
#         proxy = True
#
#     objects = ...

class Group(models.Model):
    name = models.CharField(max_length=100, null=False)
    persons = models.ManyToManyField(Person, blank=True, related_name="groups", through="Membership")


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="memberships")
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True, editable=False)
    invite_reason = models.CharField(max_length=200, null=True, blank=True)

# mahsan = Person.objects.create(name="mahsan gilani")
# sport = Group.objects.create(name="Sport")
#
# sport.persons.add(mahsan)
#
# parsa = Person.objects.create(name="parsa ahmadian")
# sport.persons.add(parsa, through_defaults={"invite_reason": "For Abolzal ^_*"})
