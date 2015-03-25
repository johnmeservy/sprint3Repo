# FILE:         models.py
# AUTHOR:       Group 1-9
# DATE:         2/18/15
#
# DESCRIPTION:  This is a Django models file that corresponds to the CHF case DCD
#
#
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session


class Photograph(models.Model):
    '''
        DESCRIPTION:     This contains photos of users, products, and events.
        NOTES:           Binary explained - https://docs.djangoproject.com/en/1.7/ref/models/fields/#binaryfield
    '''
    date_taken = models.DateField()
    place_taken = models.TextField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.description


class User(AbstractUser):
    '''
        DESCRIPTION:    A User within the CHF system. Extends the built-in AbstractUser.
        NOTES:          Participants need emergency contact information.
                        Organization representatives are required to have an organization_name associated with their account.
                        AbstractUser explained - https://docs.djangoproject.com/en/1.7/topics/auth/customizing/#extending-django-s-default-user
    '''
    # INHERITED FROM: AbstractUser
    # is_staff
    # is_active
    # date_joined
    # last_login
    # username
    # password
    # first_name
    # last_name
    # email
    address1 = models.TextField(max_length=200)
    address2 = models.TextField(max_length=200, null=True, blank=True)
    city = models.TextField(max_length=100)
    state = models.TextField(max_length=20)
    zipcode = models.TextField(max_length=20)
    phone_number = models.TextField(max_length=40)
    security_question = models.TextField(max_length=200, null=True)
    security_answer = models.TextField(max_length=200, null=True)
    emergency_contact = models.TextField(max_length=200, null=True, blank=True)
    emergency_phone = models.TextField(max_length=200, null=True, blank=True)
    emergency_relationship = models.TextField(max_length=200, null=True, blank=True)
    id_photo = models.ForeignKey(Photograph, null=True)
    organization_name = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
            return self.user.username


class Event(models.Model):
    '''
        DESCRIPTION:    Colonial Heritage Event Information.
        NOTES:          BinaryField explained - https://docs.djangoproject.com/en/1.7/ref/models/fields/#binaryfield
    '''
    name = models.TextField()
    description = models.TextField(max_length=500, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    map_file_name = models.TextField(max_length=500, null=True, blank=True)
    venue_name = models.TextField(max_length=200)
    address1 = models.TextField(max_length=200)
    address2 = models.TextField(max_length=200, null=True, blank=True)
    city = models.TextField(max_length=100)
    state = models.TextField(max_length=20)
    zipcode = models.TextField(max_length=20)
    photo = models.ForeignKey(Photograph, null=True)

    def __str__(self):
        return self.name


class Area(models.Model):
    '''
        DESCRIPTION:    Colonial Heritage Area Information.
        NOTES:
    '''
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    place_number = models.TextField(max_length=20)
    event = models.ForeignKey(Event, null=True)
    photo = models.ForeignKey(Photograph, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    '''
        DESCRIPTION:    Items are things that the foundation or organizations own.  Some items are rentable and some are not.
        NOTES:          is_rentable - used to determine if the item can be rented or not.
    '''
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    item_value = models.DecimalField(max_digits=10, decimal_places=2)
    standard_rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_rentable = models.BooleanField(default=False)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name


class WardrobeItem(Item):
    '''
        DESCRIPTION:    Extends Item class.  Wardrobe items only.
        NOTES:
    '''
    SIZE_CHOICES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large')
    )
    size = models.CharField(max_length=40, choices=SIZE_CHOICES, default='M')
    size_modifier = models.TextField(max_length=40, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    color = models.TextField(max_length=40)
    pattern = models.TextField(max_length=40)
    start_year = models.TextField(max_length=10)
    end_year = models.TextField(max_length=10)
    note = models.TextField(max_length=500, null=True)


class Rental(models.Model):
    '''
        DESCRIPTION:    On the front end, only staff will have the option to rent an item out to someone.
        NOTES:          rentee - a user the item is rented to.
                        time - the time and date that an individual initiates a rental.
                        rental_items - this field is required for the RentalItem association table to work between Rental and Item.
    '''
    time = models.DateField(null=True)
    due_date = models.DateField(null=True)
    discount_percent = models.TextField(null=True)
    rentee = models.ForeignKey(User, null=True)
    rental_items = models.ManyToManyField('Item', through='RentalItem', null=True)


class Return(models.Model):
    '''
        DESCRIPTION:    A class to track the return of a rented item.
        NOTES:          agent - the person authorized by CHF to handle rental returns.
                        time - the time that the rental item was returned to the foundation.
    '''
    time = models.DateField(null=True)
    fees_paid = models.BooleanField(default=False)
    fees_waived = models.BooleanField(default=False)
    agent = models.ForeignKey(User, related_name='returns_handled', null=True)


class RentalItem(models.Model):
    '''
        DESCRIPTION:    An association class that adds more information when a user rents an item.
        NOTES:
    '''
    condition = models.TextField(max_length=500)
    new_damage = models.BooleanField(default=False)
    damage_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    due_date = models.DateField(null=True)
    returned = models.BooleanField(default=False)
    rental_return = models.ForeignKey(Return, null=True, related_name='items_returned')
    rental = models.ForeignKey(Rental, null=True)
    item = models.ForeignKey(Item, null=True)


class Product(models.Model):
    '''
        DESCRIPTION:    A product that is sold by the foundation including: Mass Produced, One Off, and Made to Order.
        NOTES:          The front end needs to dynamically change the required fields based on the type of item it is.
                        The default selection for the drop down is "Mass Produced Product".
                        The following items are the required fields based on the drop down selection:
                            Mass Produced needs to have quantity on hand.
                            One Off needs to have date_made.
                            Made to Order needs to have order form name and production time.
    '''
    name = models.TextField(max_length=200)
    category = models.TextField(max_length=40, null=True)
    current_price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    PRODUCT_CHOICES = (
        ('MPP', 'Mass Produced Product'),
        ('OOP', 'One Off Product'),
        ('MTOP', 'Made to Order Product')
    )
    product_type = models.CharField(max_length=40, choices=PRODUCT_CHOICES, default='MPP')
    producer_name = models.TextField(max_length=200, null=True)
    quantity_on_hand = models.TextField(null=True)
    date_made = models.DateField(null=True)
    order_form_name = models.CharField(max_length=200, null=True)
    production_time = models.DateField(null=True)
    photo = models.TextField(null=True)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name


class Transaction(models.Model):
    '''
        DESCRIPTION:    Designates one line item of a shopping cart order.
        NOTES:          order_phone - contact number for order.
                        order_details - this field is required for the OrderDetail association table to work between Transaction and Product.

    '''
    date = models.DateField()
    order_phone = models.CharField(max_length=20)
    date_packed = models.DateField(null=True)
    date_paid = models.DateField(null=True)
    date_shipped = models.DateField(null=True)
    customer = models.ForeignKey(User, related_name='orders')
    order_details = models.ManyToManyField('Product', through='OrderDetail', null=True)


class OrderDetail(models.Model):
    '''
        DESCRIPTION:    Designates one line item of a shopping cart order.
        NOTES:          The front end needs to dynamically change the required fields based on the type of item it is.
                        The following items are the required fields based on the drop down selection:
                            Mass Produced needs to have quantity and price.
                            Made to Order needs to have order file.
    '''
    quantity = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_file = models.TextField(max_length=200, null=True)
    transaction = models.ForeignKey(Transaction)
    product = models.ForeignKey(Product)


class ShoppingCart(models.Model):
    '''
        DESCRIPTION:    Shopping cart is used to store items the visitor selects to purchase.
                        This will use the django session class.  This will allow a person to add items to a cart without signing into an account __
                            A person must sign into their account at checkout to complete the purchase order.
                        Reference textbook - pg. 341.
        NOTES:          Session explained - http://eli.thegreenplace.net/2011/06/29/django-sessions-part-ii-how-sessions-work/
                                            https://docs.djangoproject.com/en/1.7/topics/http/sessions/
                        sale_date - will be generated on the front end.
                        shipping_number - the number that UPS or FedEx provides us. Not an internal number
                        cart_items - this field is required for the CartItem association table to work between ShoppingCart and Product.

    '''
    sale_date = models.DateField()
    shipping_handling = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    shipping_tracking_number = models.TextField(max_length=200, null=True)
    customer = models.ForeignKey(User, null=True)
    session_id = models.ForeignKey(Session, null=True)
    cart_items = models.ManyToManyField('Product', through='CartItem', null=True)


class CartItem(models.Model):
    '''
        DESCRIPTION:    Designates one line item of a shopping cart order.  An association class between Product and ShoppingCart.
                        Reference textbook - pg. 341.
        NOTES:          Front End - Check the quantity when the user is checking out to verify that we have that many in stock.
                            Subtract the quantity purchased from the quantity on hand to update the inventory count not prevent other browsing users from purchasing out of stock inventory
                            If the user doesn't check out, update the inventory. (when the session expires)
    '''
    quantity = models.TextField(max_length=10000)
    sold_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    product = models.ForeignKey(Product)
    shopping_cart = models.ForeignKey(ShoppingCart)


class SaleItem(models.Model):
    '''
        DESCRIPTION:    Keeps track of the items sold by artisans at each area.
        NOTES:          artisan - must be a registered user.
    '''
    name = models.TextField()
    description = models.TextField(max_length=500)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    artisan_name = models.ForeignKey(User)
    area = models.ForeignKey(Area, null=True)

    def __str__(self):
        return self.name
