# lembretes de coisas para fazer e não perder o horario
# impportar datetime para manipular datas e horas e notify.
import time
from datetime import datetime
from plyer import notification
#class lembrete para armazenar os lembretes
class Lembrete:
    def __init__(self, titulo, descricao, hora):
        self.titulo = titulo
        self.descricao = descricao
        self.data_hora = hora

    def __str__(self):
        return f"{self.titulo} - {self.descricao} - {self.data_hora}"
#configurar lista de lembretes
Agenda_padrao = [
    Lembrete("Encerrando o 1° turno","1° turno encerrado verificar atividades","15:00"),
    Lembrete("Lanche","Vai parar pra lanchar?","17:00"),
    Lembrete("Jantar","Parar para janatar","20:10"),
    Lembrete("Go Home","Finalizar o dia","21:50")
]
Agenda_dia = []
#variavel para armazenar o dia atual
resposta = input("Deseja adicionar lembretes extras? (s/n)").lower()
while resposta == "s":
    titulo = input("Title")
    descricao = input("Descrição")
    hora = input("Hora")
    Agenda_dia.append(Lembrete(titulo, descricao, hora))
    resposta = input("Deseja adicionar mais lembretes extras? (s/n)").lower()

Agenda = Agenda_padrao + Agenda_dia
resumo ="\n".join(str(itens.titulo) for itens in Agenda)
notification.notify("Itens de Hoje",resumo, timeout = 30)

try:
    while True:
        if "22:00" == datetime.now().strftime('%H:%M'):
            notification.notify("Encerrando","Finalizando dia",timeout = 15)
            break
        for lembrete in Agenda:
            if lembrete.data_hora == datetime.now().strftime('%H:%M'):
                notification.notify(title=lembrete.titulo, message=lembrete.descricao + " - Agora são " + lembrete.data_hora, timeout=10)
                time.sleep(60)
    time.sleep(60)
    
except KeyboardInterrupt:
    print("Parou de rodar")