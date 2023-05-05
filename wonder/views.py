from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render, redirect

# Create your views here.
from wonder.forms import SignUpForm
from wonder.models import Evento
from django.contrib.auth import get_user_model, authenticate, login

User = get_user_model()

def home(request):
    return render(request, "wonder/home_HTML.html")


def contactanos(request):
    return render(request, "wonder/contactanos_HTML.html")

class ReservaForm(ModelForm):
    class Meta:
        model = Evento
        fields= ['title', 'description', 'start', 'end', 'user']


@login_required
def entornoVirtual(request):
    reserva = Evento.objects.order_by('start')
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.created_by = request.user
            reserva.save()
            return redirect(to='entornoVirtual')
    else:
        form = ReservaForm()


    users = User.objects.exclude(username=request.user.username)
    context = {'evento': reserva,'users':users, 'form': form}

    return render(request, "wonder/entornoVirtual_HTML.html", context)

def entornoVirtualChat(request, username):
    reserva = Evento.objects.order_by('start')
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.created_by = request.user
            reserva.save()
            return redirect(to='entornoVirtual')
    else:
        form = ReservaForm()

    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)
    context = {'evento': reserva, 'users': users, 'form': form}
    return render(request, "wonder/entornoVirtual_HTML.html", context)


def remove_reserva(request, reserva_id):
    reserva = Evento.objects.get(pk=reserva_id)
    context = {'events': reserva}
    if request.method == 'POST':
        reserva.delete()
        return redirect(to='entornoVirtual')

    return render(request, 'wonder/remove_reserva.html', context)


def update_reserva(request, reserva_id):
    reserva = Evento.objects.get(pk=reserva_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.created_by = request.user
            reserva.save()
            return redirect(to='entornoVirtual')

    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'wonder/update_reserva.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'wonder/registro_HTML.html', {'form': form})



def proyectos(request):
    return render(request, "wonder/proyectos_HTML.html")
