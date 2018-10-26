from django.shortcuts import render, redirect, HttpResponse
import random

# Create your views here.

def index(request):
    return render(request, "ninja_gold/index.html")

def process_money(request):
    if request.method == "POST":
        building_map = {
            "farm":random.randint(0,20),
            "cave":random.randint(5,10),
            "house":random.randint(2,5),
            "casino":random.randint(-50,50)
        }
        if "gold" in request.session:
            request.session['gold'] = request.session['gold']
        else:
            request.session['gold'] = 0
        if 'activities' in request.session:
            request.session['activites'] = request.session['activities']
        else:
            request.session['activities'] = []
        if request.POST['building'] == 'farm':
            building = "farm"
            new_gold = building_map[building]
            activity = {
                "content":"Earned " + str(new_gold) + " gold at the farm!",
                "color": "text-success"
            }
            request.session['activities'].append(activity)
            request.session['gold'] = request.session['gold'] + new_gold
        if request.POST['building'] == 'cave':
            building = "cave"
            new_gold = building_map[building]
            activity = {
                "content":"Earned " + str(new_gold) + " gold at the cave!",
                "color": "text-success"
            }
            request.session['activities'].append(activity)
            request.session['gold'] = request.session['gold'] + new_gold
        if request.POST['building'] == 'house':
            building = "house"
            new_gold = building_map[building]
            activity = {
                "content":"Earned " + str(new_gold) + " gold at the house!",
                "color": "text-success"
            }
            request.session['activities'].append(activity)
            request.session['gold'] = request.session['gold'] + new_gold
        if request.POST['building'] == 'casino':
            building = "casino"
            new_gold = building_map[building]
            if new_gold >= 0:
                activity = {
                    "content":"Earned " + str(new_gold) + " gold at the casino!",
                    "color": "text-success"
                }
            if new_gold < 0:
                activity = {
                    "content":"Entered a casino and lost " + str(new_gold) + " gold... Ouch...",
                    "color":"text-danger"
                }
            request.session['activities'].append(activity)
            request.session['gold'] = request.session['gold'] + new_gold
        request.session.modified = True
        return redirect("/")
