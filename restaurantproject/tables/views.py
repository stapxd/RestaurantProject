from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Tables_orders, Tables
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def index(request):

    # selected_tables = []

    title = 'Замовити столик'
    tables = Tables.objects.all()
    # orders = Tables_orders.objects.values_list('date')
    fDate = None

    isDisabled = []

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # selected_tables = request.POST.getlist('selected_items')
            selected_tables = list(map(int, request.POST.getlist('selected_items')))
            print(len(selected_tables))
            print(selected_tables)
            # table_number = form.cleaned_data['table_number']
            fDate = form.cleaned_data['date']

            if len(selected_tables) > 0:
                # for selected in selected_tables:
                #     one_order = Tables_orders(date=fDate, table_number=selected)
                #     one_order.save()

                request.session['data'] = {
                    "date": fDate.isoformat(),
                    "selected_tables": selected_tables
                }
                return redirect('confirmation')

            for table in tables:
                try:
                    order = Tables_orders.objects.get(table_number=table.table_number, date=fDate)
                    isDisabled.append(True)
                except Tables_orders.DoesNotExist:
                    isDisabled.append(False)

            print(isDisabled)
            combined_list = zip(tables, isDisabled)


            #
            # existing_reservation = Tables_orders.objects.filter(
            #     table_number=table_number,
            #     reservation_date=reservation_date
            # ).exists()
            # exeplar = Tables_orders(date='2023-12-14', table_number='1')
            # exeplar.save()
            # if existing_reservation:
            #     print("NO")
            # else:
            #     print("YES")
            #     # # Здесь вы можете создать заказ
            #     # reservation = form.save(commit=False)
            #     # reservation.user = request.user
            #     # reservation.save()
            #     # return render(request, 'reservation/success.html', {'message': 'Reservation successful!'})
    else:
        form = OrderForm()

    return render(request, 'tables/bookTable.html', locals())


def confirmation(request):

    data = request.session.get('data', None)

    username = request.user.username

    if request.method == 'POST':

        confirmation = request.POST.get('confirm')
        print(confirmation)
        print(type(confirmation))

        if confirmation == 'submit':

            existing_order = False

            for selected in data.get('selected_tables'):
                existing_reservation = Tables_orders.objects.filter(date=data.get('date'), table_number=selected).exists()
                if existing_reservation:
                    existing_order = True
                    break

            if existing_order:
                messages.success(request, ('Якісь столики з ваших вже зарезервовані. Спробуйте ще раз'))

            else:
                for selected in data.get('selected_tables'):
                    one_order = Tables_orders(date=data.get('date'), table_number=selected, user=username)
                    one_order.save()

                return redirect('home')

        elif confirmation == 'back':
            return redirect('booking')

        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "foxionhk@gmail.com",
        #     ["ptrukenpavel@gmail.com"],
        #     fail_silently=False,
        # )

    return render(request, 'tables/confirmation.html', locals())
