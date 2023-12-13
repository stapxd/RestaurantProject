from django.shortcuts import render
from .forms import OrderForm
from .models import Tables_orders, Tables


# Create your views here.
def index(request):
    title = 'Замовити столик'
    tables = Tables.objects.all()
    # orders = Tables_orders.objects.values_list('date')
    fDate = None

    isDisabled = []

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            selected_tables = request.POST.getlist('selected_items')
            print(selected_tables)
            # table_number = form.cleaned_data['table_number']
            fDate = form.cleaned_data['date']

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
