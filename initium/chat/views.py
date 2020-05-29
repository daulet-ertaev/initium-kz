from django.shortcuts import render, redirect, reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
def index(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        amount = int(amount)
    return redirect(reverse('room'))

def paypalCharge(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        amount = int(amount)
    return redirect(reverse('paypal', args=[amount]))

@login_required
def room(request, room_name, post_author):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'dest': mark_safe(json.dumps(request.POST.get['value'])),
    })