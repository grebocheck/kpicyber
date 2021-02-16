from django.http import Http404 , HttpResponseRedirect , HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Tournament , Team

def list(request):
    # отображение листа турниров
    posts = Tournament.objects.all().order_by('-post_date')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)
    context = {
        "posts": paginator.get_page(page),
        'title':"Турніри",
        'year':datetime.now().year,
    }
    return render(request, "tournament/list.html", context)



def single(request, tournament_id):
    # отображение туринров в открытом виде
    try:
        a = Tournament.objects.get(id = tournament_id)
    except:
        raise Http404("Турнір не знайдено")

    # параметры необходимые для скрытия лишних полей
    rich_3 = False
    rich_4 = False
    rich_5 = False
    dopr_1 = False
    dopr_2 = False

    if Tournament.objects.get(id = tournament_id).players_osn > 2:
        rich_3 = True
    if Tournament.objects.get(id = tournament_id).players_osn > 3:
        rich_4 = True
    if Tournament.objects.get(id = tournament_id).players_osn > 4:
        rich_5 = True

    if Tournament.objects.get(id = tournament_id).players_dop > 0:
        dopr_1 = True
    if Tournament.objects.get(id = tournament_id).players_dop > 1:
        dopr_2 = True

    #отображение контента в зависимости от прав
    forma = False               # форма заявки
    mess_auth = False           # сообщение о неообходимости авторизацыи
    capitan_contact = False     # отображение контактов капитана
    mess_reg = False            # если заявка подана то ее отображает
    teg = []                    # массив заявок к mess_reg
    
    if request.user.has_perm('auth.change_user'):
        # администратор
        forma = True
        mess_auth = False
        capitan_contact = True
        mess_reg = False

        # якщо час реєстрацій закінчився то реєстрація буде не можлива
        if Tournament.objects.get(id = tournament_id).deadline_reg.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
            forma = True

    elif request.user.username == "":
        # пользователь который не авторизовался
        forma = False
        mess_auth = True
        capitan_contact = False
        mess_reg = False

    else:
        # пользователь который авторизовался
        forma = True
        mess_auth = False
        capitan_contact = False
        mess_reg = False

        # якщо час реєстрацій закінчився то реєстрація буде не можлива
        if Tournament.objects.get(id = tournament_id).deadline_reg.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
            forma = False

        asse = a.team_set.order_by('-id')
        ima = request.user.username
        for r in asse:
            if r.capitan == ima:
                forma = False
                mess_reg = True
                teg.append(r)
        if teg != []:
            forma = False
            mess_reg = True

    latest_team_list = a.team_set.order_by('-id')

    return render(request , "tournament/detail.html" , {'forma':forma ,'mess_auth':mess_auth ,'capitan_contact':capitan_contact , "mess_reg":mess_reg ,'teg':teg,"tournament": a, 'latest_team_list': latest_team_list,'title':a.title, 'year':datetime.now().year,'author':a.author ,
                                                        'rich_3':rich_3 , 'rich_4':rich_4 , 'rich_5':rich_5 , 'dopr_1':dopr_1 , 'dopr_2':dopr_2 ,})
    
def leave_team(request , tournament_id ):
    if request.user.username == "":
        ima = "Невідомий"
    else:
        ima = request.user.username
    try:
        a = Tournament.objects.get(id = tournament_id)
    except:
        raise Http404("Статтю не знайдено")

    pn_3 = ''
    st_3 = ''
    vz_3 = ''
    fk_3 = ''
    gr_3 = ''
    rt_3 = ''
    pn_4 = ''
    st_4 = ''
    vz_4 = ''
    fk_4 = ''
    gr_4 = ''
    rt_4 = ''
    pn_5 = ''
    st_5 = ''
    vz_5 = ''
    fk_5 = ''
    gr_5 = ''
    rt_5 = ''
    pn_6 = ''
    st_6 = ''
    vz_6 = ''
    fk_6 = ''
    gr_6 = ''
    rt_6 = ''
    pn_7 = ''
    st_7 = ''
    vz_7 = ''
    fk_7 = ''
    gr_7 = ''
    rt_7 = ''

    try:
        pn_3 = request.POST['player_name_3']
        st_3 = request.POST['steam_link_3']
        vz_3 = request.POST['vuz_3']
        fk_3 = request.POST['fuck_3']
        gr_3 = request.POST['group_3']
        rt_3 = request.POST['rate_3']
        
        try:
            pn_4 = request.POST['player_name_4']
            st_4 = request.POST['steam_link_4']
            vz_4 = request.POST['vuz_4']
            fk_4 = request.POST['fuck_4']
            gr_4 = request.POST['group_4']
            rt_4 = request.POST['rate_4']

            try:
                pn_5 = request.POST['player_name_5']
                st_5 = request.POST['steam_link_5']
                vz_5 = request.POST['vuz_5']
                fk_5 = request.POST['fuck_5']
                gr_5 = request.POST['group_5']
                rt_5 = request.POST['rate_5']
            except:
                pass
        except:
            pass
    except:
        pass

    try:
        pn_6 = request.POST['player_name_6']
        st_6 = request.POST['steam_link_6']
        vz_6 = request.POST['vuz_6']
        fk_6 = request.POST['fuck_6']
        gr_6 = request.POST['group_6']
        rt_6 = request.POST['rate_6']
        
        try:
            pn_7 = request.POST['player_name_7']
            st_7 = request.POST['steam_link_7']
            vz_7 = request.POST['vuz_7']
            fk_7 = request.POST['fuck_7']
            gr_7 = request.POST['group_7']
            rt_7 = request.POST['rate_7']

        except:
            pass
    except:
        pass

    if Tournament.objects.get(id = tournament_id).deadline_reg.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
        pass
    else:
        a.team_set.create(capitan = ima, contact_capitan = request.POST['contact_capitan'] , team_name = request.POST['team_name'] ,
                         player_name_1 = request.POST['player_name_1'] , steam_link_1 = request.POST['steam_link_1'] , vuz_1 = request.POST['vuz_1'] , fuck_1 = request.POST['fuck_1'] , group_1 = request.POST['group_1'],rate_1 = request.POST['rate_1'],
                         player_name_2 = request.POST['player_name_2'] , steam_link_2 = request.POST['steam_link_2'] , vuz_2 = request.POST['vuz_2'] , fuck_2 = request.POST['fuck_2'] , group_2 = request.POST['group_2'],rate_2 = request.POST['rate_2'],
                         player_name_3 = pn_3 , steam_link_3 = st_3 , vuz_3 = vz_3 , fuck_3 = fk_3 , group_3 = gr_3, rate_3 = rt_3,
                         player_name_4 = pn_4 , steam_link_4 = st_4 , vuz_4 = vz_4 , fuck_4 = fk_4 , group_4 = gr_4, rate_4 = rt_4,
                         player_name_5 = pn_5 , steam_link_5 = st_5 , vuz_5 = vz_5 , fuck_5 = fk_5 , group_5 = gr_5, rate_5 = rt_5,
                         player_name_6 = pn_6 , steam_link_6 = st_6 , vuz_6 = vz_6 , fuck_6 = fk_6 , group_6 = gr_6, rate_6 = rt_6,
                         player_name_7 = pn_7 , steam_link_7 = st_7 , vuz_7 = vz_7 , fuck_7 = fk_7 , group_7 = gr_7, rate_7 = rt_7,)
                     

    return HttpResponseRedirect(reverse('tournament:single' , args = (a.id,)))
