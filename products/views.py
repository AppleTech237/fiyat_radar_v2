
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Price, Alert

from django.contrib.auth.decorators import login_required
from .forms import AlertForm
 



def all_products(request):
    categories = Category.objects.prefetch_related('products').all()
    
    return render(request, 'products/all_products.html', {'categories': categories})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    prices = Price.objects.filter(product_id=pk).order_by('price')
    best_price = prices.first() 
    
    if request.user.is_authenticated and best_price:
        
        alert = Alert.objects.filter(
            user=request.user, 
            product=product, 
            is_triggered=False
        ).first()

        if alert and best_price.price <= alert.target_price:
            alert.is_triggered = True 
            alert.save()


    return render(request, 'products/product_detail.html', {
        'product': product,
        'prices': prices,
        'best_price': best_price,
    })


def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.none()
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        results = Product.objects.none()

    return render(request, 'products/search_product_list.html', {
        'products': products,
        'query': query
    })

@login_required
def dashboard_home(request):
    user_alerts = Alert.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard_home.html', {'alerts': user_alerts})



@login_required
def create_alert(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.product = product
            alert.save()
            return redirect('dashboard') 
    else:
        form = AlertForm()
    return render(request, 'alerts/alerts_form.html', {'form': form, 'product': product})




@login_required
def update_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id, user=request.user)
    if request.method == 'POST':
        form = AlertForm(request.POST, instance=alert)
        if form.is_valid():
            alert = form.save(commit=False)

            best_price = Price.objects.filter(product=alert.product).order_by('price').first()
            if best_price and best_price.price <= alert.target_price:
                 alert.is_triggered = True
            else:
                alert.is_triggered = False
                alert.last_checked_price = None

            alert.save()
            return redirect('dashboard')
    else:
        form = AlertForm(instance=alert)

    return render(request, 'alerts/alerts_form.html', {
        'form': form,
        'product': alert.product,
        'is_update': True
        })

@login_required
def delete_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id, user=request.user)
    if request.method == "POST":
        alert.delete()
        return redirect('dashboard')
    return render(request, 'alerts/alerts_confirm_delete.html', {'alert': alert})

def about(request):
    about_us = Product.objects.all()
    return render(request, 'products/about.html', {
        'products': about_us
    })
def contact(request):
    contact_us = Product.objects.all()
    return render(request, 'products/contact.html', {
        'products': contact_us
    })