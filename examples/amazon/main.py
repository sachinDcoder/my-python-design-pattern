import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum
from abc import ABC


@dataclass
class ProductReview:
    review_desc: str
    review_time: datetime
    rating: int
    reviewer: 'Buyer'


class ProductCategory(Enum):
    GROCERY: 'GROCERY'
    MOBILE: 'MOBILE'
    ELECTRONICS: 'ELECTRONICS'
    FURNITURE: 'FURNITURE'


@dataclass
class Product:
    product_id: uuid
    name: str
    product_desc: str
    image_url: str
    cost: float
    seller: 'Seller'
    product_category: ProductCategory
    reviews: List[ProductReview]


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Customer:
    customer_id: uuid
    cart: 'ShoppingCart'
    search: 'Search'

    def get_shopping_cart(self):
        pass

    def add_items_to_shopping_cart(self, item: 'Item'):
        pass

    def remove_item_from_shopping_cart(self, item: 'Item'):
        pass

    def update_item_in_shopping_cart(self, item: 'Item'):
        pass


class Guest(Customer):
    def create_new_account(self) -> 'Account':
        pass


@dataclass
class User(Customer):
    account: 'Account'


class Seller(User):
    def add_product(self, product: 'Product'):
        pass


@dataclass
class Buyer(User):
    order: List['Order']

    def add_review(self, review: ProductReview):
        pass

    def edit_review(self, review: ProductReview):
        pass

    def place_order(self, cart: 'ShoppingCart') -> 'OrderStatus':
        pass


@dataclass
class Address:
    street: str
    city: str
    pincode: int
    state: str
    country: str


class CardType(Enum):
    DEBIT_CARD = 'DEBIT_CARD'
    CREDIT_CARD = 'CREDIT_CARD'


@dataclass
class Card:
    card_type: CardType
    cvv: str
    card_numer: str
    expiry: datetime


class AccountStatus(Enum):
    ACTIVE = 'ACTIVE'
    IN_ACTIVE = 'IN_ACTIVE'
    BLOCKED = 'BLOCKED'


@dataclass
class Account:
    name: str
    email: str
    phone_number: str
    user_name: str
    password: str
    shipping_addresses: List[Address]
    cards: List[Card]
    account_status: AccountStatus


@dataclass
class ShoppingCart:
    items: List[Item]
    cart_value: float = 0.0

    def add_item(self, item: Item):
        pass

    def update_item(self, item: Item):
        pass

    def delete_item(self, item: Item):
        pass

    def checkout_items(self):
        pass

    def get_items(self) -> List[Item]:
        return self.items

    def get_cart_value(self) -> float:
        return self.cart_value


class OrderStatus(Enum):
    PLACED: 'PLACED'
    PACKED: 'PACKED'
    SHIPPED: 'SHIPPED'
    OUT_FOR_DELIVERY: 'OUT_FOR_DELIVERY'
    DELIVERED: 'DELIVERED'
    CANCELLED: 'CANCELLED'


@dataclass
class OrderLog:
    order_details: str
    order_status: OrderStatus
    created_time: datetime


@dataclass
class Order:
    order_id: uuid
    items: List[Item]
    order_value: float
    buyer: Buyer
    order_logs: List[OrderLog]
    order_time: datetime

    def place_order(self) -> OrderStatus:
        pass

    def track_order(self) -> OrderStatus:
        pass

    def add_order_log(self, log: OrderLog):
        self.order_logs.append(log)

    def make_payment(self, payment_type: 'PaymentType') -> 'PaymentStatus':
        pass


class PaymentType(Enum):
    CARD: 'CARD'
    UPI: 'UPI'
    NET_BANKING: 'NET_BANKING'


class PaymentStatus(Enum):
    SUCCESS: 'SUCCESS'
    ERROR: 'ERROR'
    FAILED: 'FAILED'
    CANCELLED: 'CANCELLED'
    REFUND_INITIATED: 'REFUND_INITIATED'
    REFUNDED: 'REFUNDED'


class Search:
    def search_by_product_name(self, product_name: str) -> List[Product]:
        pass

    def search_by_category(self, category: ProductCategory) -> List[Product]:
        pass


@dataclass
class MessageAttribute:
    to: str
    from_: str
    desc: str


class Notification:
    def send_notification(self, message_attribute: MessageAttribute) -> bool:
        raise NotImplementedError


class EmailNotification(Notification):
    def send_notification(self, message_attribute: MessageAttribute) -> bool:
        pass


class WhatsappNotification(Notification):
    def send_notification(self, message_attribute: MessageAttribute) -> bool:
        pass


class SmsNotification(Notification):
    def send_notification(self, message_attribute: MessageAttribute) -> bool:
        pass


@dataclass
class NotificationType:
    EMAIL: 'EMAIL'
    SMS: 'SMS'
    WHATSAPP: 'WHATSAPP'


@dataclass
class NotificationDomain:
    notification_id: uuid
    notification_type: NotificationType
    user: User


@dataclass
class NotificationService:
    def send_notification(self, notification_domain: NotificationDomain) -> bool:
        if notification_domain.notification_type == NotificationType.EMAIL:
            notification = EmailNotification()
            message_attribute = MessageAttribute("test1.com", "test2.com", "desc")
        elif notification_domain.notification_type == NotificationType.WHATSAPP:
            notification = WhatsappNotification()
            message_attribute = MessageAttribute("556664", "77889", "desc")
        else:
            notification = SmsNotification()
            message_attribute = MessageAttribute("5556543", "23455", "desc")

        return notification.send_notification(message_attribute)
