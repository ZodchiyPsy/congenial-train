import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
vk_session = vk_api.VkApi(token = "3b986af66a3cd1bc600fb28a32d69aa94b4be145d282b757407f7b37dfe3a9bba323e1cc6d1d3f06abadd")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 200670284)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        from_id = event.object.from_id
        msg_text = event.object.text
        vk.messages.send( #Отправляем сообщение
            user_id=from_id,
            message=msg_text,
            random_id=0)