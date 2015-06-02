##----Adding a user to a group in django----
from django.contrib.auth.models import Group
g = Group.objects.get(name='groupname') 
g.user_set.add(your_user)
#user.groups.add(g) in mordern versions

##--- check if a user is in a certain group------
>>> from django.contrib.auth.models import User, Group
>>> group = Group(name="Editor")
>>> group.save()                  # save this new group for this example
>>> user = User.objects.get(pk=1) # assuming, there is one initial user 
>>> user.groups.add(group)        # user is now in the "Editor" group
>>> user.groups.all()
[<Group: Editor>]

'''
we can write a decorator @user_passes_test with following tests 
def is_member(user):
    return user.groups.filter(name='Member').exists()
def is_in_multiple_groups(user):
    return user.groups.filter(name__in=['group1', 'group2']).exists()
and decorate our views to allow only group user's access
@login_required
@user_passes_test(is_member) # or @user_passes_test(is_in_multiple_groups)
def myview(request):
    # Do your processing

'''
#actual checking:
if user.groups.filter(name=group_name).exists():
	pass # do something
#multiple group checking
if user.groups.filter(name__in=['group1', 'group2']).exists():
	pass