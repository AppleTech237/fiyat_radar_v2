from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Alert

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} ! Login in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def user_profile(request):
    
    all_alerts = Alert.objects.filter(user=request.user)
    count_alerts = all_alerts.count()
    
    
    triggered_alerts = all_alerts.filter(is_triggered=True)
    number_of_alerts = triggered_alerts.count()
    
    context = {
        'count_alerts': count_alerts,
        'number_of_alerts': number_of_alerts,
        'triggered_alerts': triggered_alerts,
    }
    return render(request, 'accounts/user_profile.html', context)