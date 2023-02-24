import random

from model.contact import Contact
from model.group import Group


def test_remove_contact_from_group(app, db, orm):
    groups_list = orm.get_groups_list()
    if len(groups_list) < 1:
        group = Group(name="Pre-group", header="test_header", footer="aaaa")
        app.group.add(group)
        group.id = orm.get_max_group_id()
    else:
        group = random.choice(groups_list)
    contact = Contact(firstname="Worker", lastname="Kekov")
    app.contact.add_new(contact)
    contact.id = str(orm.get_max_contact_id())
    app.contact.add_contact_to_group(contact.id, group.id)
    app.contact.remove_contact_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)
