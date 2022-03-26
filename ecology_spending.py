from math import sqrt,pow
from plotly.graph_objs import Bar,Layout
from plotly import offline

alpha_of_city=[[ 1.19,1.34,1.72],
                [1.09,1.11,1.52],
                [1.25,1.00,1.63],
                [1.29,1.55,1.18],
                [1.07,1.14,1.96],
                [1.39,1.84,1.22],
                [1.03,1.04,1.19],
                [1.13,2.00,1.42]]
factory_inpackt=[[97.20,186.10,313.10,4.90,636.30,0],
                [176.30,135.90,116,70,1162.70,18.20,58.30],
                [0,72.40,0,80.40,0,3.10],
                [13.60,331.30,87.10,151.90,15.80,50.90],
                [35.00,1599.60,138.20,35.90,795.90,0],
                [0,233.80,0.10,0,192.70,0],
                [0.40,288.80,287.60,5.20,8.20,222.70],
                [36.50,269.60,95.30,64.10,317.30,55.80]]
def alpha_water(apha_city,factury_inpackts):
    """
    Этот метод принимает коэффициент alpha массивом,где элемент[0]-коэффициент для воды,
    элемент[1]-коэффициет для воздуха,элемент[2]-коэффициет для отходов.
    Показатели производства должны быть массивом со следующими элементами:
    элемент[0]-расходы на водные выбросы
    элемент[1]-расходы на воздушные выбросы
    элемент[2]-расходы на отходы
    элемент[3]-сверхрасходы на водные выбросы
    элемент[4]-сверхрасходы на воздушные выбросы
    элемент[5]-сверхрасходы на отходы
    
    """
    answer_array=[]
    for number_array in range(len(apha_city)):
        answer_array.append(compute_sqrt_pays(
                    form_for_one_spending(
                    apha_city[number_array][0],factury_inpackts[number_array][0],factury_inpackts[number_array][3]),
                    form_for_one_spending
                    (apha_city[number_array][1],factury_inpackts[number_array][1],factury_inpackts[number_array][4]),
                    form_for_one_spending
                    (apha_city[number_array][2],factury_inpackts[number_array][2],factury_inpackts[number_array][5])))
    return answer_array
def compute_sqrt_pays(water,air,waste):
    """
    Метод принимает суммы квадратов водных,воздушных и отходов.
    Возвращает квадратный корень из суммы
    """
    result=sqrt(water+air+waste)
    return result
def form_for_one_spending(coef,pay_norm_obj,pay_over_obj):
    """
    Метод для расчёта воды,воздуха и отходов
    по формуле
    """
    try:
        summ=(pay_norm_obj+pay_over_obj)
        div=(summ/pay_norm_obj) #<- по формуле нужно делить вот так , первоначально делил на pay_over_obj
        result=((div**2)*coef)
    except ZeroDivisionError:
        return 0
    return result
result_array=alpha_water(alpha_of_city,factory_inpackt)

#визуализация результатов
x_values=result_array
y_values=['Уренгой','Надым','Ямбург','Сургут','Тюмень','Оренбург','Астрахань','Красноярск']
data=[Bar(x=y_values,y=x_values)]
x_axis_config={'title':'Предприятия'}
y_axis_config={'title':'Рейтинг экологичности предприятия'}
my_layout=Layout(title=f'Результаты по даннымо от {len(factory_inpackt)} предприятий России',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='eco.html')