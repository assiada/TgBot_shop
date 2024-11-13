import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.database.requests as rq

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Welcome sneakers shop', reply_markup=kb.main)

@router.message(F.text=='Catalog')
async def catalog(message: Message):
    await message.answer(text='Select category of products', reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category(callback:CallbackQuery):
    await callback.answer('You selected category')
    await callback.message.answer(text='Select product', reply_markup=await kb.items(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('item_'))
async def category(callback:CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('You selected product')
    await callback.message.answer(text=f'Name:{item_data.name}\nDescr:{item_data.description}\nPrice:{item_data.price}$'
                                  , reply_markup=await kb.items(callback.data.split('_')[1]))


'''
#await message.reply('How are you?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('You select help button')


@router.message(F.text == 'Catalog')
async def nice(message: Message):
    await message.answer('Select catalog', reply_markup=kb.catalog)


@router.callback_query(F.data == 'T-shirts')
async def t_shirts(callback: CallbackQuery):
    await callback.answer('You selected category', show_alert=True)
    await callback.message.answer('You selected t-shirts')


@router.message(Command('register'))
async def cmd_reg(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Input your name')

@router.message(Register.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Input your age')

@router.message(Register.age)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Input your number', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data=await state.get_data()
    await message.answer(f'Name: {data["name"]}\nAge:{data["age"]}\nNumber:{data["number"]}')
    await state.clear() '''
