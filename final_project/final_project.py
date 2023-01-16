"""
DSC 20 Final Project
Name: Zehui Zhang
PID:  A16151490
"""
from util import Stack, Queue
from datetime import datetime


def doctest():
    """
    ------------------------ PRODUCT TEST ------------------------

    >>> p1 = Product("iphone",399)
    >>> p2 = Special_Product("macbook air",999)
    >>> p3 = Limited_Product("free iphone", 0, 10)
    >>> p1, p2, p3
    (PRODUCT <0>, PRODUCT <1>, PRODUCT <2>)
    >>> print(p1)
    <0> iphone - 399$
    >>> print(p2)
    <1> macbook air - 999$ (special)
    >>> print(p3)
    <2> free iphone - 0$ (10 left)

    ------------------------ WAREHOUSE TEST ------------------------

    >>> wh = Warehouse()
    >>> st = Store(wh)
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> print(wh)
    Warehouse with 3 products
    >>> print(wh.get_product(1))
    <1> macbook air - 999$ (special)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <0> iphone - 399$
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (10 left)
    ============================
    >>> wh.export_product(3)
    >>> wh.export_product(2)
    PRODUCT <2>
    >>> wh.remove_product(0)
    True
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    <2> free iphone - 0$ (9 left)
    ============================
    >>> st.view_products(sort = True)
    ============================
    <ID> Product - Price
    <2> free iphone - 0$ (9 left)
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.remove_product(0)
    False
    >>> [wh.export_product(2) for i in range(9)]
    [PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>,\
 PRODUCT <2>, PRODUCT <2>, PRODUCT <2>, PRODUCT <2>]
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <1> macbook air - 999$ (special)
    ============================
    >>> wh.show_log()
    Product <0> imported - 2020-11-26 07:09:17.709522
    Product <1> imported - 2020-11-26 07:09:17.709584
    Product <2> imported - 2020-11-26 07:09:17.709612
    Product <2> exported - 2020-11-26 07:09:17.709745
    Product <0> removed  - 2020-11-26 07:09:17.709776
    Product <2> exported - 2020-11-26 07:09:17.709886
    Product <2> exported - 2020-11-26 07:09:17.709893
    Product <2> exported - 2020-11-26 07:09:17.709897
    Product <2> exported - 2020-11-26 07:09:17.709901
    Product <2> exported - 2020-11-26 07:09:17.709905
    Product <2> exported - 2020-11-26 07:09:17.709909
    Product <2> exported - 2020-11-26 07:09:17.709913
    Product <2> exported - 2020-11-26 07:09:17.709916
    Product <2> exported - 2020-11-26 07:09:17.709920
    Product <2> removed  - 2020-11-26 07:09:17.709924

    ------------------------ USER TEST ------------------------

    >>> u1 = User( 'Jerry', st)
    >>> u2 = Premium_User( 'FYX', st)
    >>> u1
    USER<0>
    >>> u2
    USER<1>
    >>> print(u1)
    standard user: Jerry - 0$
    >>> u2.add_balance(2000)
    >>> print(u2)
    premium user: FYX - 2000$

    >>> wh.import_product(p1)
    >>> u1 = User("A",st)
    >>> u1.add_cart(0)
    >>> u1.add_cart(0)
    >>> u1.view_cart()
    (front) <0> iphone - 399$ -- <0> iphone - 399$ (rear)
    >>> u1.checkout()
    STORE: Not enough money QQ
    []
    >>> u1.add_balance(1000)
    >>> u1.checkout()
    STORE: A ordered iphone. A has 562$ left.
    STORE: A ordered iphone. A has 124$ left.
    [PRODUCT <0>, PRODUCT <0>]
    >>> p4 = Limited_Product("Ipad", 600, 5)
    >>> wh.import_product(p4)
    >>> u2.buy_all(3)
    STORE: FYX ordered Ipad. FYX has 1400$ left.
    STORE: FYX ordered Ipad. FYX has 800$ left.
    STORE: FYX ordered Ipad. FYX has 200$ left.
    STORE: Not enough money QQ
    [PRODUCT <3>, PRODUCT <3>, PRODUCT <3>]

    ------------------- HISTORY / UNDO TEST -------------------

    >>> u1.view_history()
    (bottom) <0> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903632 -- \
<1> 2 bought <0> iphone - 399$ at 2020-12-03 21:27:54.903658 (top)
    >>> u1.undo_purchase()
    STORE: A refunded iphone. A has 523$ left.

    -------------------------- EC TEST ------------------------
    >>> p1 = Product("A",20)
    >>> p2 = Special_Product("B",7)
    >>> p3 = Limited_Product("C", 1, 2)
    >>> wh = Warehouse()
    >>> wh.import_product(p1)
    >>> wh.import_product(p2)
    >>> wh.import_product(p3)
    >>> st = Store(wh)
    >>> st.view_products()
    ============================
    <ID> Product - Price
    <4> A - 20$
    <5> B - 7$ (special)
    <6> C - 1$ (2 left)
    ============================
    >>> st.so_rich(45)
    1
    >>> st.so_rich(61)
    0
    >>> st.so_rich_recursive(45)
    1
    >>> st.so_rich_recursive(61)
    0
    """
    pass


#######################################################################
#                               PRODUCT                               #
#######################################################################
class Product:
    """ The Product class provides abstraction to the products available
    in our system. Note that each Product instance represents a listing
    or kind of products, instead of an individual product. """

    product_counter = 0
    ##### Part 1.1 #####
    def __init__(self, name, price):
        """ Initialized instance variables in constructor  """
        self.name = name
        self.price = price
        self.id = Product.product_counter
        Product.product_counter += 1

    def __str__(self):
        """ return what print is called, the string representation """
        return "<{}> {} - {}$".format(self.id,self.name,self.price)

    def __repr__(self):
        """ return the string representation in python form """
        return "PRODUCT <{}>".format(self.id)


class Limited_Product(Product):
    """ A class represrnts limited view_products whcih are a kind of product
    that has a limited number of offerings """

    ##### Part 1.2 #####
    def __init__(self, name, price, amount):
        """ Initialized instance variables in constructor """
        super().__init__(name,price)
        self.amount = amount

    def __str__(self):
        """ return what print is called, the string representation """
        return "<{}> {} - {}$ ({} left)".format(self.id,self.name,\
        self.price,self.amount)


class Special_Product(Product):
    """ A class represents special products which are products
    only sell to premium users """

    ##### Part 1.3 #####
    def __init__(self, name, price, description="special"):
        """ Initialized instance variables in constructor """
        self.description = description
        super().__init__(name,price)

    def __str__(self):
        """ return what print is called, the string representation """
        return "<{}> {} - {}$ ({})".format(self.id,self.name,\
        self.price,self.description)


#######################################################################
#                              WAREHOUSE                              #
#######################################################################


class Warehouse:
    """ The Warehouse class provides abstraction to the warehouses,
    which stores all products for a particular store. """

    ##### Part 2 #####
    def __init__(self):
        """ Initialized instance variables in constructor """
        self.inventory = {}
        self.log = []

    def __str__(self):
        """ Return what print is called, the string representation """
        return "Warehouse with {} products".format(len(self.inventory))

    def get_product(self, product_id):
        """ Return the product instance with the given id from the inventory."""
        return self.inventory[product_id]

    def list_products(self):
        """ Return a list of all actual product instances stored in the
        inventory. """
        return list(self.inventory.values())

    def remove_product(self, product_id):
        """ Remove the product instance with the given id from the inventory."""
        if product_id not in self.inventory.keys():
            return False
        else:
            del self.inventory[product_id]
            self.log.append("Product <" + str(product_id) + \
            "> removed - {}".format(datetime.now()))
            return True

    def import_product(self, product):
        """ Import the product instance (Product) to the inventory. """
        if product not in self.inventory.values():
            self.inventory[product.id] = product
            self.log.append("Product <{}> imported - {}".format(product.id,\
            datetime.now()))

    def export_product(self, product_id):
        """ Export the product instance with the given id from the inventory."""
        if product_id not in self.inventory.keys():
            return None
        else:
            product = self.inventory[product_id]
            if isinstance(product,Limited_Product):
                product.amount -= 1
                self.log.append("Product <" + str(product_id) + \
                "> exported - {}".format(datetime.now()))
                if product.amount == 0:
                    self.remove_product(product_id)
                return product

            else:
                self.log.append("Product <" + str(product_id) + \
                "> exported - {}".format(datetime.now()))
                return product

    def size(self):
        """ Return the number of products stored in the inventory."""
        return len(self.inventory)

    def show_log(self):
        """ Print all log strings in the log """
        for i in self.log:
            print(i)


#######################################################################
#                               HISTORY                               #
#######################################################################
class History:
    """ The History class provides abstraction to the purchase history records.
    After finalizing an order, the store will return a History instance to
    users for record, so that users can keep track of their order and
    cancel the order if they need.  """

    ##### Part 3 #####
    history_counter = 0
    def __init__(self, product, user):
        """ Initialized instance variables in constructor """
        self.product = product
        self.user = user
        self.id = History.history_counter
        History.history_counter += 1
        self.time = datetime.now()

    def __str__(self):
        """ Return what print is called, the string representation """
        return "<{}> {} bought {} at {}".format(self.id,self.user.id,\
        self.product,self.time)

    def __repr__(self):
        """ return the string representation in python form """
        return "HISTORY<{}> - {}".format(self.id,self.time)


#######################################################################
#                                USER                                 #
#######################################################################
class User:
    """ The User class provides abstraction to the users. You can view the
    user instance here as similar to the membership card offered by different
    stores: each user instance must be registered to one and only one store. """

    ##### Part 4.1 #####
    user_counter = 0
    def __init__(self, name, store):
        """ Initialized instance variables in constructor """
        self.name = name
        self.store = store
        self.balance = 0
        self.id = User.user_counter
        User.user_counter += 1
        self.purchase_history = Stack()
        self.cart = Queue()
        self.store.add_user(self)

    def __str__(self):
        """ Return what print is called, the string representation """
        return "standard user: {} - {}$".format(self.name,self.balance)

    def __repr__(self):
        """ Return the string representation in python form """
        return "USER<{}>".format(self.id)

    def set_name(self, new_name):
        """ Set the name attribute to the new_name."""
        self.name = new_name

    def get_name(self):
        """ Get the name attribute. """
        return str(self.name)

    def set_balance(self, amount):
        """ Set the balance attribute to the amount. """
        self.balance = amount

    def get_balance(self):
        """ Get the balance attribute """
        return int(self.balance)

    def add_balance(self, amount):
        """ Increment the balance attribute by the specified amount. """
        self.balance = self.balance + amount

    def last_purchase(self):
        """ Retrieve the last purchased history instance of this user and
        return it. If the purchase history is empty, return None. """
        if not self.purchase_history.is_empty():
            return self.purchase_history.peek()
        else:
            return None

    def view_history(self):
        """ Print the purchase history of this user. """
        print(self.purchase_history)

    def view_cart(self):
        """ Print the cart of this user. """
        print(self.cart)

    def clear_cart(self):
        """ Remove all products in the cart. """
        self.cart.clear()

    ##### Part 5.2 #####
    def add_cart(self, product_id):
        """ A function that takes a product id (int) and adds the
        corresponding product to the user’s shopping cart.  """
        if product_id in self.store.warehouse.inventory:
            self.cart.enqueue(self.store.get_product(product_id))

    def checkout(self):
        """ A function that orders every item in the shopping cart from the
        store and returns a list of purchased products.  """
        bought = []
        while True:
            item = self.cart.peek()
            if item != None:
                order = self.store.order(self.id, item.id)
                if order == False:
                    break
                self.purchase_history.push(order)
                self.cart.dequeue()
                bought.append(item)
            else:
                break
        return bought

    ##### Part 5.3 #####
    def undo_purchase(self):
        """ A function that undoes the last purchase of the user. """
        if self.purchase_history.is_empty():
            return 'USER: no purchase history'
        else:
            purchase = self.store.undo_order(self.id,self.last_purchase().product)
            if purchase != False:
                self.purchase_history.pop()

class Premium_User(User):
    """ The Premium_User class provides abstraction to the premium users.
    Premium users can enjoy more benefits than ordinary users, including
    waiving shipment fee and using more purchasing options. """

    ##### Part 4.2 #####
    def __str__(self):
        """ Return what print is called, the string representation """
        return "premium user: {} - {}$".format(self.name,self.balance)

    ##### Part 5.4 #####
    def buy_all(self, product_id):
        """ A function that supports batch ordering for limited products. """
        product = self.store.warehouse.inventory[product_id]
        if type(product) == Limited_Product:
            all_buy = []
            while True:
                order = self.store.order(self.id, product_id)
                if order == False:
                    break
                all_buy.append(product)
                self.purchase_history.push(order)
            return all_buy
        else:
            print("USER: not a limited product")
            return []

    def undo_all(self):
        """ A function that iteratively cancels the last purchases until the
        user does not have any records in purchase history, or the last
        purchase is a limited product. """
        len = history.size()
        while True:
            if type(self.purchase_history.peek().product) == Limited_Product \
            or len == 0:
                break
            else:
                self.undo_purchase()
                len -= 1



#######################################################################
#                               STORE                                 #
#######################################################################
class Store:
    """ The Store class provides abstraction to the stores. The stores will
    accept user registrations, handle user orders, and deliver the products
    in the warehouse to the users """

    ##### Part 4.3 #####
    def __init__(self, warehouse):
        """ Initialized instance variables in constructor """
        self.users = {} # keys user id, value user instance
        self.warehouse = warehouse

    def __str__(self):
        """ Return what print is called, the string representation """
        return "STORE: store with {} users and {} products".format(\
        len(self.users),self.warehouse.size())

    def get_product(self, product_id):
        """ Lookup a product instance with the provided product_id (int)
        from the warehouse and return this product.  """
        return self.warehouse.get_product(product_id)

    def view_products(self, sort=False):
        """ Print all products in the inventory in a human readable format """
        items = {}
        products = []
        if sort == True:
            for i in self.warehouse.inventory.values():
                items[i.price] = i
            sorted_order = sorted(items)
            for j in sorted_order:
                products.append(items[j])
            print('============================')
            print('<ID> Product - Price')
            for i in products:
                print(i)
            print('============================')
        else:
            print('============================')
            print('<ID> Product - Price')
            for i in self.warehouse.inventory.keys():
                print(self.warehouse.get_product(i))
            print('============================')

    ##### Part 5.1 #####
    def add_user(self, user):
        """ A function that takes a user instance and records this
        instance to the users dictionary. """
        if user in self.users.values():
            print("STORE: User already exists")
            return False
        else:
            self.users[user.id] = user
            return True

    ##### Part 5.2 #####
    def order(self, user_id, product_id):
        """ A function that takes the ids (int) of the user who
        makes this order and the product this user orders, """
        product = self.get_product(product_id)
        user = self.users[user_id]
        multi = 1.1
        if product == None:
            print('STORE: Product not found')
            return False
        elif ((isinstance(user,Premium_User))and(user.balance < product.price))\
        or(not isinstance(user,Premium_User)\
        and(user.balance < int(product.price * multi))):
            print('STORE: Not enough money QQ')
            return False
        elif isinstance(product,Special_Product) \
        and (not isinstance(user,Premium_User)):
            print('STORE: Special product is limited to premium user')
            return False
        else:
            if isinstance(user,Premium_User):
                user.balance -= product.price
            else:
                user.balance -= int(product.price * multi)
            result = History(product,user)
            print('STORE: {} ordered {}. {} has {}$ left.'\
            .format(user.name,product.name,user.name,user.balance))
            return result


    ##### Part 5.3 #####
    def undo_order(self, user_id, product):
        """ A function that takes the id (int) of the user who requested
        order cancellation and the product instance (Product) in this order,
        and processes the refund process. """
        if type(product) != Limited_Product:
            self.users[user_id].add_balance(product.price)
            print("STORE: {} refunded {}. {} has {}$ left."\
            .format(self.users[user_id].name, product.name, \
            self.users[user_id].name, self.users[user_id].get_balance()))
        else:
            print("STORE: can't refund Limited_Product")
            return False

    ##### Part 6 #####
    def so_rich(self, money):
        """ A function that return a sequence of purchase that costs the
        customers the most of their money, given an arbitrary amount of
        available money """
        # YOUR CODE GOES HERE #

        # suppose you haven't seen any product yet
        # the only possible amount of money left is "money"
        # this is a set to record the possible money left
        left = set([money])

        # get products
        lst = list(self.warehouse.list_products())

        for product in lst:

            # a temporary set to save the updates of "left"
            # you don't want to modify the set you're iterating through
            tmp_left = set()

            for m in left:
                # update tmp_left
                if type(product) != Limited_Product:
                    new_left = m
                    while new_left >= 0:
                        tmp_left.add(new_left)
                        new_left = new_left - product.price
                else:
                    # handle limited product
                    new_left = m
                    num = int(product.amount)
                    while new_left >= 0 and num >= 0:
                        tmp_left.add(new_left)
                        new_left = new_left - product.price
                        num -= 1
            left = tmp_left

        return min(left)

    def so_rich_recursive(self, money):
        """ A function by recursion that return a sequence of purchase that
        costs the customers the most of their money, given an arbitrary amount
        of available money """
        # YOUR CODE GOES HERE #

        # get products
        lst = list(self.warehouse.list_products())

        def helper(lst, money):
            # base case
            if len(lst) == 0:
                return money

            cur_min = money
            product = lst[0]
            if type(product) != Limited_Product:
                tmp = money
                while tmp >= 0:
                    cur_min = min(helper(lst[1:],tmp),cur_min)
                    tmp -= product.price
            else:
                tmp = money
                num = product.amount
                while tmp >= 0 and num >= 0:
                    num -= 1
                    cur_min = min(helper(lst[1:],tmp),cur_min)
                    tmp -= product.price
            return cur_min

        return helper(lst, money)
