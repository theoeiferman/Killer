from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import formset_factory, forms
from .models import PlayerContact, PlayerContactForm, Games
from link import *
from messaging import SendEmail


def player_contact_form(request):
    PlayerContactFormSet = formset_factory(PlayerContactForm, extra=5)
    if request.method == 'POST':
        formset = PlayerContactFormSet(request.POST, prefix='playercontact_set')
        list_email = []
        list_players = []
        list_perso_actions = []
        if formset.is_valid():
            new_game = Games()
            new_game.save()

            for form in formset: #first loop to extract datas from the form
                if form.has_changed():
                    player_contact = form.save(commit=False)
                    list_email.append(player_contact.player_email)
                    list_players.append(player_contact.surname)
                    list_perso_actions.append(player_contact.action)

            dict_player_target = assign_players_a_target(list_players)
            list_actions = get_actions()[0:len(list_players)] 
            list_actions_merged = update_perso_action(list_actions, list_perso_actions)

            i = 0
            for form in formset: #second loop to save datas
                if form.has_changed():
                    player_contact = form.save(commit=False)
                    player_contact.action = list_actions_merged[i]
                    player_contact.target = dict_player_target[player_contact.surname]
                    player_contact.game_name = new_game.name
                    player_contact.save()
                    new_game.players.add(player_contact)
                    i += 1

            return redirect('/select_game_mode/')
        else: 
            form_errors = formset.non_form_errors()
            if form_errors:
                return render(request, 'info/players.html', {'form_errors': form_errors})
    else:
        formset = PlayerContactFormSet(prefix='playercontact_set')
    return render(request, 'info/players.html', {'formset': formset})


def select_game_mode(request):
    if request.method == 'POST':
        game_mode = request.POST.get('game_mode')

        # Game class
        last_game = Games.objects.latest('id')
        last_game.gamemode = game_mode
        last_game.save()     

        # PlayerContact class & actions
        player_contacts = PlayerContact.objects.filter(game_name=last_game)
        player_contacts = update_action(player_contacts,game_mode) 
        print(player_contacts)

        print('This where you send mail or SMS, PRECISE IF ENGLISH OR FRENCH')
        SendEmail(player_contacts,game_mode)
        
        return redirect('/success/')

    return render(request, 'info/game_mode_selection.html')


def success(request):
    return render(request, 'info/success.html')

def rules(request):
    return render(request, 'info/rules.html')

def donate(request):
    return render(request, 'info/donate.html')


def handler404(request, exception):
    response = render(request, '404.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response




#HOMEMADE FUNCTIONS FOR ACTIONS
def update_action(player_contacts, game_mode):
    #print(game_mode)
    if game_mode=="French" : 
        #list_actions = get_actions("actions.txt")[0:len(player_contacts)] 
        print("do nothing, list_actions_merged is set by defaut")
        
    if game_mode=="English" :
        list_actions = get_actions("actions_en.txt")[0:len(player_contacts)] 
        j=0
        for player in player_contacts:
            player.action = list_actions[j]
            j=j+1

    if game_mode=="vacation_fr" : 
        list_actions = get_actions("actions_vacances_fr.txt")[0:len(player_contacts)] 
        j=0
        for player in player_contacts:
            player.action = list_actions[j]
            j=j+1
            
    if game_mode=="vacation_en" : 
        list_actions = get_actions("actions_vacances_en.txt")[0:len(player_contacts)] 
        j=0
        for player in player_contacts:
            player.action = list_actions[j]
            j=j+1

    if game_mode=="party_fr" : 
        list_actions = get_actions("actions_party_fr.txt")[0:len(player_contacts)] 
        j=0
        for player in player_contacts:
            player.action = list_actions[j]
            j=j+1

    if game_mode=="party_en" : 
        list_actions = get_actions("actions_party_en.txt")[0:len(player_contacts)] 
        j=0
        for player in player_contacts:
            player.action = list_actions[j]
            j=j+1

    return player_contacts

def update_perso_action(list_actions, list_perso_actions):
    if len(list_actions)!=len(list_perso_actions):
        print("Both list should be the same size ! Error")

    for i in range (len(list_actions)):
        if list_perso_actions[i] == '':
            list_perso_actions[i]=list_actions[i]

    return list_perso_actions

