import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as Bs

token = "1853942469:AAG4Mpp4oPN3mJ5SSc3zciSxA2nvpvo5C7M"
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=["start"])
def main_func(message):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_1 = types.KeyboardButton("Погода")
    button_2 = types.KeyboardButton("Новости")
    button_3 = types.KeyboardButton("button_3")
    buttons.add(button_1, button_2, button_3)
    button_text = bot.send_message(message.chat.id, text="Нажми на интересующую тебя кнопку", reply_markup=buttons)
    bot.register_next_step_handler(button_text, func_press_button)


def func_press_button(message):
    if message.text == "Погода":
        func_city_name(message)
    elif message.text == "Новости":
        pass
    elif message.text == "button_3":
        pass


def func_city_name(message):
    buttons = types.ReplyKeyboardRemove(selective=False)
    message_text = bot.send_message(message.chat.id, "Введите название населенного пункта: ",
                                    reply_markup=buttons)
    bot.register_next_step_handler(message_text, weather)


def weather(message):
    url = "https://sinoptik.ua/погода-" + message.text
    response = requests.get(url)
    site_text = Bs(response.content, "html.parser")

    for i in site_text.select("#header"):
        city_name = i.select(".cityName > h1 > strong")[0].text
        region_name = i.select(".currentRegion")[0].text

    for i in site_text.select("#mainContentBlock"):
        text_1 = i.select(".rSide > .description")[-2].text
        text_2 = i.select(".rSide > .description")[-1].text

    bot.send_message(message.chat.id, text=f"погода {city_name}\n"
                                           f"{region_name}\n\n"
                                           f"{text_1}\n\n"
                                           f"{text_2}")
    main_func(message)


if __name__ == "__main__":
    bot.polling(none_stop=True)
