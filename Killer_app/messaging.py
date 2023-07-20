from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django_rq import job


@job
def send_email_job(subject, message, from_email, recipient_list, html_message=None):
    send_mail(subject, message, from_email, recipient_list, html_message=html_message)


def SendEmail(player_contacts,game_mode):
    subject = 'Lets play the Killer game'
    from_email = 'killer-gamemaster@outlook.com' #BACKEND CONFIGURATION

    for player in player_contacts:
            action = player.action # this might change if game mode is put before (ie. various game mode)
            target = player.target
            player_email = player.player_email
            player_name = player.surname

            if game_mode =='French' or game_mode == 'vacation_fr' or game_mode == 'party_fr'  : 
                message = f"NE LISEZ PAS À HAUTE VOIX! <br> Bonjour {player_name},<br>Voici votre 1ère cible: {target} .<br>Votre mission, si vous l'acceptez : {action} .<br>Bonne chasse !"
                plain_message = message.replace('<br>', '\n')
            elif game_mode =='English' or game_mode == 'vacation_en' or game_mode == 'party_en' :
                message = f"DON'T READ IT OUT LOUD! <br> Hello {player_name},<br>This is your 1st target: {target} .<br>Your mission, if you accept it : {action} .<br>Happy hunting!"
                plain_message = message.replace('<br>', '\n')
            else : 
                message = f"DON'T READ IT OUT LOUD! <br> Hello {player_name},<br>This is your 1st target: {target} .<br>Your mission, if you accept it : {action} .<br>Happy hunting!"
                plain_message = message.replace('<br>', '\n')
                
            # Add the email task to the queue
            #send_email_job.delay(subject, plain_message, from_email, [player_email], html_message=message) 
            #i didn't understand what redis is actually doing
            send_mail(subject, plain_message, from_email, [player_email], html_message=message) 
            
