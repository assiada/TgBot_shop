from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_item

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                     [KeyboardButton(text='Bag')],
                                     [KeyboardButton(text='Contacts'), KeyboardButton(text='About us')]
                                     ],
                           resize_keyboard=True,
                           input_field_placeholder='Select button'
                           )
async def categories():
    all_categories=await get_categories()
    print(all_categories)
    keyboard=InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='Home', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def items(category_id):
    all_items=await get_category_item(category_id)
    keyboard=InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    keyboard.add(InlineKeyboardButton(text='Home', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


'''
products = ['T-shirts', 'Sneakers', 'Caps']
catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=item, callback_data=item)]
                                                for item in products
                                                ]
                               )
get_number=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Share my number', request_contact=True)]],
                               resize_keyboard=True
                               )
'''