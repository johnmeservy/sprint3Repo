import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django; django.setup()
from django.contrib.auth import models as conmod
import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType

# populating data for photographs
for data in [
    {'date_taken': '2001-1-1', 'place_taken': 'Russia', 'description': 'photo1', 'image': 'photo1.jpg'},
    {'date_taken': '2002-2-2', 'place_taken': 'Japan', 'description': 'photo2', 'image': 'photo2.jpg'},
    {'date_taken': '2003-3-3', 'place_taken': 'France', 'description': 'photo3', 'image': 'photo3.jpg'},
    {'date_taken': '2004-4-4', 'place_taken': 'Mexico', 'description': 'photo4', 'image': 'photo4.jpg'},
    {'date_taken': '2005-5-5', 'place_taken': 'Germany', 'description': 'photo5', 'image': 'photo5.jpg'},
]:

    d = hmod.Photograph()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# Create Super Group, Permissions, and User
permission = Permission()
permission.codename = 'super'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Super Privileges'
permission.save()

group = Group()
group.name = "super"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=61)
group.permissions.add(permission)

user = hmod.User()
user.is_staff = 'True'
user.is_active = 'True'
user.is_superuser = 'True'
user.username = 'super'
user.set_password('asdf')
user.first_name = 'Super'
user.last_name = 'User'
user.email = 'super@cheritage.org'
user.address1 = '4387 South 1400 East'
user.address2 = ''
user.city = 'Sandy'
user.state = 'Utah'
user.zipcode = '84118'
user.phone_number = '8015558765'
user.security_question = 'What is your favorite color?'
user.security_answer = 'green'
user.emergency_contact = 'Jackson Murdock'
user.emergency_phone = '8015556543'
user.emergency_relationship = 'Friend'
user.id_photo = hmod.Photograph.objects.get(id=1)
user.organization_name = ''
user.save()

group.user_set.add(user)


# Create Staff Group, Permissions, and User
permission = Permission()
permission.codename = 'staff'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Staff Privileges'
permission.save()

group = Group()
group.name = "staff"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=62)
group.permissions.add(permission)

user = hmod.User()
user.is_staff = 'True'
user.is_active = 'True'
user.is_superuser = 'False'
user.username = 'staff'
user.set_password('asdf')
user.first_name = 'Staff'
user.last_name = 'User'
user.email = 'staff@cheritage.org'
user.address1 = '1300 East 400 North'
user.address2 = ''
user.city = 'Logan'
user.state = 'Utah'
user.zipcode = '84708'
user.phone_number = '4356897732'
user.security_question = 'What is your favorite color?'
user.security_answer = 'blue'
user.emergency_contact = 'Luis Mark'
user.emergency_phone = '8016751234'
user.emergency_relationship = 'Friend'
user.id_photo = hmod.Photograph.objects.get(id=1)
user.organization_name = ''
user.save()

group.user_set.add(user)


# Create Guest Group, Permissions, and User
permission = Permission()
permission.codename = 'guest'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Guest Privileges'
permission.save()

group = Group()
group.name = "guest"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=63)
group.permissions.add(permission)


user = hmod.User()
user.is_staff = 'False'
user.is_active = 'True'
user.is_superuser = 'False'
user.username = 'guest'
user.set_password('asdf')
user.first_name = 'Guest'
user.last_name = 'User'
user.email = 'guest@cheritage.org'
user.address1 = '5534 Youth Street'
user.address2 = ''
user.city = 'Hyrum'
user.state = 'Utah'
user.zipcode = '84704'
user.phone_number = '4356872334'
user.security_question = 'What is your favorite color?'
user.security_answer = 'purple'
user.emergency_contact = 'Andy Rawlings'
user.emergency_phone = '8019875623'
user.emergency_relationship = 'Friend'
user.id_photo = hmod.Photograph.objects.get(id=1)
user.organization_name = ''
user.save()

group.user_set.add(user)

# populating data for events
for data in [
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-1-1', 'end_date': '2015-1-10', 'map_file_name': 'map1.jpg', 'venue_name': 'Colonial Heritage Park', 'address1': '400 July Street', 'address2': '', 'city': 'Pittsburgh', 'state': 'PA', 'zipcode': '99999'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-2-2', 'end_date': '2015-2-10', 'map_file_name': 'map2.jpg', 'venue_name': 'Battlefield Park', 'address1': '501 North Street', 'address2': '', 'city': 'Boston', 'state': 'MA', 'zipcode': '44444'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-3-3', 'end_date': '2015-3-10', 'map_file_name': 'map3.jpg', 'venue_name': 'Flaming Island', 'address1': '325 South Street', 'address2': '', 'city': 'Pittsburgh', 'state': 'PA', 'zipcode': '99999'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-4-4', 'end_date': '2015-4-10', 'map_file_name': 'map4.jpg', 'venue_name': 'Mt Rushmore', 'address1': '400 June Ave', 'address2': '', 'city': 'Boston', 'state': 'MA', 'zipcode': '44444'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'start_date': '2015-5-5', 'end_date': '2015-5-10', 'map_file_name': 'map5.jpg', 'venue_name': 'Grand Canyon', 'address1': '23500 Battlefield Street', 'address2': '', 'city': 'Pittsburgh', 'state': 'PA', 'zipcode': '99999'}
]:

    d = hmod.Event()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for events
for data in [
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'name': 'Bakery', 'place_number': '1'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'name': 'Mayflower Exhibit', 'place_number': '2'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'name': 'Printing Press', 'place_number': '3'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'name': 'Blacksmith', 'place_number': '4'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'name': 'Candle Maker', 'place_number': '5'},
    {'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'name': 'Guest Services', 'place_number': '6'},
]:
    d = hmod.Area()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for products
for data in [
    {'name': 'Cannonball', 'category': 'Weapons', 'current_price': '201.15', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '40', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product1.jpg'},
    {'name': 'Pistol', 'category': 'Weapons', 'current_price': '22.45', 'product_type': 'Made to Order', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '4', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product2.jpg'},
    {'name': 'Waistcoat', 'category': 'Clothing', 'current_price': '30.16', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '15', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product3.jpg'},
    {'name': 'Mayflower', 'category': 'Artifacts', 'current_price': '1.25', 'product_type': 'Made to Order', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '2', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product4.jpg'},
    {'name': 'Bullets', 'category': 'Weapons', 'current_price': '999.43', 'product_type': 'Mass Produced', 'producer_name': 'Gove Allen', 'quantity_on_hand': '535', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product5.jpg'},
    {'name': 'Gun Powder', 'category': 'Weapons', 'current_price': '4.75', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product6.jpg'},
    {'name': 'Printing Press', 'category': 'Artifacts', 'current_price': '44.60', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product7.jpg'},
    {'name': 'Pilgrim Hat', 'category': 'Clothing', 'current_price': '45.63', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product8.jpg'},
    {'name': 'Wig', 'category': 'Clothing', 'current_price': '22.10', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product9.jpg'},
    {'name': 'Bonnet', 'category': 'Clothing', 'current_price': '19.99', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product10.jpg'},
    {'name': 'Coins', 'category': 'Collectibles', 'current_price': '199.99', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product11.jpg'},
    {'name': 'Spectacles', 'category': 'Clothing', 'current_price': '87.75', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product12.jpg'},
    {'name': 'Sword', 'category': 'Weapons', 'current_price': '234.84', 'product_type': 'Mass Produced', 'producer_name': 'Colonial Heritage Foundation', 'quantity_on_hand': '400', 'date_made': '2015-03-06', 'order_form_name': 'Pittsburgh', 'production_time': '2015-03-06', 'photo': 'product13.jpg'},
]:

    d = hmod.Product()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data for item
for data in [
    {'name': 'Rental Item 1', 'description': 'Description 1', 'item_value': '5.00', 'standard_rental_price': '3.00', 'is_rentable': 'TRUE', 'owner_id': '1'},
    {'name': 'Rental Item 2', 'description': 'Description 2', 'item_value': '5.00', 'standard_rental_price': '3.00', 'is_rentable': 'TRUE', 'owner_id': '1'},
]:

    d = hmod.Rental()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating data rental item
for data in [
    {'condition': 'Like New', 'new_damage': 'True', 'damage_fee': '10.00', 'due_date': '2015-03-04', 'returned': 'TRUE'},
    {'condition': 'Fair', 'new_damage': 'False', 'damage_fee': '10.00', 'due_date': '2015-03-04'},
    {'condition': 'Fair', 'new_damage': 'False', 'damage_fee': '10.00', 'due_date': '2014-03-04'},
    {'condition': 'Fair', 'new_damage': 'False', 'damage_fee': '10.00', 'due_date': '2015-01-04'},
    {'condition': 'Fair', 'new_damage': 'False', 'damage_fee': '10.00', 'due_date': '2014-12-04'},
    {'condition': 'Fair', 'new_damage': 'False', 'damage_fee': '10.00', 'due_date': '2014-12-27'},
    {'condition': 'Fair', 'new_damage': 'False', 'damage_fee': '10.00', 'due_date': '2014-11-04'},
]:

    d = hmod.RentalItem()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()

# populating artisan items
for data in [
    {'area': 'Candle Maker', 'name': 'Candle', 'description': 'Description 1', 'low_price': '10.00', 'high_price': '35.74', 'artisan_name': 'John', 'photo': 'product1.jpg'},
    {'area': 'Blacksmith', 'name': 'Musket', 'description': 'Description 2', 'low_price': '10.00', 'high_price': '25.74', 'artisan_name': 'Ben', 'photo': 'product2.jpg'},
    {'area': 'Guest Services', 'name': 'American Flag', 'description': 'Description 3', 'low_price': '10.00', 'high_price': '45.74', 'artisan_name': 'Taylor', 'photo': 'product3.jpg'},
    {'area': 'Guest Services', 'name': 'Plymouth Rock', 'description': 'Description 4', 'low_price': '10.00', 'high_price': '75.74', 'artisan_name': 'Landon', 'photo': 'product4.jpg'},
    {'area': 'Guest Services', 'name': 'Colonial Art', 'description': 'Description 5', 'low_price': '10.00', 'high_price': '34.74', 'artisan_name': 'Steve', 'photo': 'product5.jpg'},
    {'area': 'Blacksmith', 'name': 'Sword', 'description': 'Description 6', 'low_price': '10.00', 'high_price': '30.74', 'artisan_name': 'Thomas', 'photo': 'product6.jpg'},
    {'area': 'Guest Services', 'name': 'Yo Yo', 'description': 'Description 7', 'low_price': '10.00', 'high_price': '29.74', 'artisan_name': 'Conan', 'photo': 'product7.jpg'},
]:

    d = hmod.SaleItem()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()



for data in [
    {'name': 'Cannonball', 'description': 'Weapons', 'current_price': '48.99', 'photo': 'product1.jpg'},
    {'name': 'Pistol', 'description': 'Weapons', 'current_price': '5.43', 'photo': 'product2.jpg'},
    {'name': 'Waistcoat', 'description': 'Clothing', 'current_price': '8.63', 'photo': 'product3.jpg'},
    {'name': 'Mayflower', 'description': 'Artifacts', 'current_price': '.32', 'photo': 'product4.jpg'},
    {'name': 'Bullets', 'description': 'Weapons', 'current_price': '227.49', 'photo': 'product5.jpg'},
    {'name': 'Gun Powder', 'description': 'Weapons', 'current_price': '1.25', 'photo': 'product6.jpg'},
    {'name': 'Printing Press', 'description': 'Artifacts', 'current_price': '10.99', 'photo': 'product7.jpg'},
    {'name': 'Pilgrim Hat', 'description': 'Clothing', 'current_price': '19.19', 'photo': 'product8.jpg'},
    {'name': 'Wig', 'description': 'Clothing', 'current_price': '6.78', 'photo': 'product9.jpg'},
    {'name': 'Bonnet', 'description': 'Clothing', 'current_price': '4.99', 'photo': 'product10.jpg'},
    {'name': 'Coins', 'description': 'Collectibles', 'current_price': '67.88', 'photo': 'product11.jpg'},
    {'name': 'Spectacles', 'description': 'Clothing', 'current_price': '28.73', 'photo': 'product12.jpg'},
    {'name': 'Sword', 'description': 'Weapons', 'current_price': '87.56', 'photo': 'product13.jpg'},
]:

    d = hmod.Item()
    for k, v in data.items():
        setattr(d, k, v)
    d.save()
