from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from calc import TestApp
from dati import Dati
 
# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
TOKEN="5461678538:AAEcnJsd-0_kU29U7m5RoALSBVFGyDfHjJE"
K=3
def extract_number(text):
     nDomande=text.split()[1].strip()
     giusta=text.split()[2].strip()
     sbagliata=text.split()[3].strip()
     bianca=text.split()[4].strip()
     soglia=text.split()[5].strip()
     dati=Dati(nDomande,giusta,sbagliata,bianca,soglia)
     return dati

     
def insert(update,context):
     dati=extract_number(update.message.text)
    # print(f'il compito ha {dati.N} domande\nrisposta giusta:{dati.giusta}  sbagliata:{dati.sbagliata}  bianca:{dati.bianca}\nLa soglia è {dati.soglia}')
     update.message.reply_text(f'il compito ha {dati.N} domande\nrisposta giusta:{dati.giusta}  sbagliata:{dati.sbagliata}  bianca:{dati.bianca}\nLa soglia è {dati.soglia}')
     t=TestApp(dati,K)
     t.prova(update)

class App:
     @staticmethod
     def main() :

        upd= Updater(TOKEN, use_context=True)
        disp=upd.dispatcher
        disp.add_handler(CommandHandler("insert", insert))
     
        upd.start_polling()
        upd.idle()
     
if __name__=='__main__':
   App.main()