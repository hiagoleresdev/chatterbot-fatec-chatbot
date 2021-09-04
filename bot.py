#-*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot('Test')

convI = ['que bom','ok','','voce pode me ajudar','Claro, como posso te ajudar?', 'oi, tudo bem?','tudo, obrigado por perguntar?','obrigado','disponha','oi!','oi','olá','como vai','estou bem','tchau','até mais','bom dia', 'bom dia, como posso ajudar?', 'boa tarde', 'boa tarde, como posso ajudar?', 'boa noite', 'boa noite, como posso ajudar?']
convV = ['quando será a prova','a prova acontecerá dia 20/09/2021','a prova e dificil?','não, basta estudar!','tenho duvidas sobre o vestibular','Ok, vamos lá','até quando será a inscrição para o vestibular?','ate dia 14/09/2021','e as inscrições','ate dia 14/09/2021','quando é o vestibular?','a prova acontecerá dia 20/09/2021', 'quais cursos são oferecidos?','os cursos são: ADS - Análise e Desenvolvimento de Sistemas e Gestão de Negócios',]
convN = ['Qual é o seu nome?','pode me chamar de Bot.','quem és tu','pode me chamar de Bot.','o que você faz?','Sou o estagiário virtual da Fatec RP. Posso te ajudar com algumas dúvidas sobre o vestibular', 'qual a sua missão?', 'destruir a humanidade', 'como posso te chamar?', 'me chame de bot']
convPG = ['qual o valor da inscrição','R$75,00','quanto custa','R$75,00','quanto custa a inscrição','R$75,00','perdi meu boleto','sem problemas, você pode fazer a reimpressão pelo site','meu boleto venceu','sem problemas, você pode fazer a reimpressão pelo site','meus dados estão errados','sem problemas, faremos a correção no ato da matrícula','meu nome esta errado','sem problemas, faremos a correção no ato da matrícula','meu rg esta errado','sem problemas, faremos a correção no ato da matrícula']
convRec=['onde posso pagar a taxa do vestibular?','você pode realizar o pagamento em qualque casa lotérica','voces recebem?','por favor faça o pagamento no banco','posso pagar ai?','por favor faça o pagamento no banco','posso pagar na fatec','não, por favor faça o pagamento no banco','posso pagar por pix','aceitamos pix']
convise=['quem tem direito a isenção','Funcionários e seus dependentes tem direito','como pedir a isenção','ainda nao sei','quais documenos sao necessarios para solicitar a isenção','ainda não sei']


trainer = ListTrainer(bot)

#trainer.train(conversation)

#bot.set_trainer(ListTrainer)
trainer.train(convI)
trainer.train(convV)
trainer.train(convN)
trainer.train(convPG)
trainer.train(convRec)         
trainer.train(convise)         

print('Bem vindo ao Fatebot, irei responder suas dúvidas sobre o vestibular da fatec. Como posso te ajudar?')
while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    if float(response.confidence)>=0.001:
        print('FateBot: ', response)
    else:
        print('FateBot: Desculpe, não entendi, por favor refaça a pergunta.')