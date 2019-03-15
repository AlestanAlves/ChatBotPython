from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot ('test')

trainer = ListTrainer(chatbot)
trainer.train (['oi', 'tudo bem?', 'sou seu fã', 'Bárbara é linda', 'Bom dia', 'Oi, bem?', 'Eu estou bem'])


response = chatbot.get_response('OLÁAAAAAAAAAAA')
print (response)