import json

with open('all_services.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

# Master list of volunteers from IBS with their departments and primary & secondary roles
volunteers_raw = {
    'pastor': {
        'name': 'Pr. Flávio Amaral',
        'dept_principal': 'Liderança Pastoral',
        'role_principal': 'Pastor Presidente & Preletor',
        'dept_secundaria': 'Ensino Bíblico',
        'role_secundaria': 'Doutrina & Formação',
        'team': 'Geral',
        'initials': 'PF'
    },
    'iracilene': {
        'name': 'Pra. Iracilene',
        'dept_principal': 'Liderança Pastoral',
        'role_principal': 'Pastora & Preletora',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Coordenação Diaconato',
        'team': 'Geral',
        'initials': 'PI'
    },
    'carlos': {
        'name': 'Pr. Carlos',
        'dept_principal': 'Liderança Pastoral',
        'role_principal': 'Preletor Auxiliar',
        'dept_secundaria': 'Ensino Bíblico',
        'role_secundaria': 'Discipulado',
        'team': 'Geral',
        'initials': 'PC'
    },
    
    # Louvor
    'manu': {
        'name': 'Manú',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Ministra de Louvor',
        'dept_secundaria': 'Liderança Pastoral',
        'role_secundaria': 'Preletora',
        'team': 'Equipe 01',
        'initials': 'MN'
    },
    'karol': {
        'name': 'Karol',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Ministra de Louvor',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Back-vocal',
        'team': 'Equipe 02',
        'initials': 'KR'
    },
    'bruno': {
        'name': 'Bruno',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Violão',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Ministro de Louvor',
        'team': 'Equipe 01',
        'initials': 'BR'
    },
    'kamynnsky': {
        'name': 'Kamynnsky',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Back-vocal',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Ministro de Louvor',
        'team': 'Equipe 01',
        'initials': 'KM'
    },
    'flavio_f': {
        'name': 'Flávio F.',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Violão',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Louvor / Voz',
        'team': 'Equipe 03',
        'initials': 'FF'
    },
    'efrain': {
        'name': 'Efrain',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Teclado',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Mesa de Som',
        'team': 'Equipe 01',
        'initials': 'EF'
    },
    'italo': {
        'name': 'Ítalo',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Contra-baixo',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Guitarra',
        'team': 'Equipe 01',
        'initials': 'IT'
    },
    'joao_paulo': {
        'name': 'João Paulo',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Contra-baixo',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Acolhimento',
        'team': 'Equipe 02',
        'initials': 'JP'
    },
    'icaro': {
        'name': 'Ícaro',
        'dept_principal': 'Ministério de Louvor',
        'role_principal': 'Bateria',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Percussão',
        'team': 'Geral',
        'initials': 'IC'
    },
    
    # Shamah Kids
    'ana_carolina': {
        'name': 'Ana Carolina',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Coordenação Shamah Kids',
        'dept_secundaria': 'Shamah Kids',
        'role_secundaria': 'Turma 01 / 02',
        'team': 'Equipe 01',
        'initials': 'AC'
    },
    'leticia': {
        'name': 'Letícia',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Turma 01 / 02',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Back-vocal',
        'team': 'Equipe 02',
        'initials': 'LT'
    },
    'valeria': {
        'name': 'Valéria',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Turma 01 / 02',
        'dept_secundaria': 'Shamah Kids',
        'role_secundaria': 'Dirigente Infantil',
        'team': 'Equipe 03',
        'initials': 'VL'
    },
    'jordana': {
        'name': 'Jordana',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Turma 01 / 02',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Projeção Multimídia',
        'team': 'Equipe 03',
        'initials': 'JD'
    },
    'maria_eduarda': {
        'name': 'Maria Eduarda',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Turma 01 / 02',
        'dept_secundaria': 'Shamah Kids',
        'role_secundaria': 'Berçário',
        'team': 'Equipe 01',
        'initials': 'ME'
    },
    'ester': {
        'name': 'Ester',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Turma 01 (Apoio)',
        'dept_secundaria': 'Shamah Kids',
        'role_secundaria': 'Turma 02',
        'team': 'Equipe 02',
        'initials': 'ES'
    },
    'ana_julia': {
        'name': 'Ana Júlia',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Turma 02',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Back-vocal',
        'team': 'Equipe 02',
        'initials': 'AJ'
    },
    'yasmin': {
        'name': 'Yasmin',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Turma 01',
        'dept_secundaria': '',
        'role_secundaria': '',
        'team': 'Geral',
        'initials': 'YS'
    },
    'mariana': {
        'name': 'Mariana',
        'dept_principal': 'Shamah Kids',
        'role_principal': 'Turma 02',
        'dept_secundaria': '',
        'role_secundaria': '',
        'team': 'Geral',
        'initials': 'MR'
    },
    
    # Mídia & Tecnologia
    'felipe': {
        'name': 'Felipe',
        'dept_principal': 'Mídia & Tecnologia',
        'role_principal': 'Mesa de Som',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Iluminação',
        'team': 'Equipe 01',
        'initials': 'FE'
    },
    'kaue': {
        'name': 'Kauê',
        'dept_principal': 'Mídia & Tecnologia',
        'role_principal': 'Mesa de Som',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Mídia Geral',
        'team': 'Equipe 03',
        'initials': 'KU'
    },
    'lorivaldo': {
        'name': 'Lorivaldo',
        'dept_principal': 'Mídia & Tecnologia',
        'role_principal': 'Transmissão Online',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Mídia Geral',
        'team': 'Geral',
        'initials': 'LO'
    },
    'ramon': {
        'name': 'Ramon',
        'dept_principal': 'Mídia & Tecnologia',
        'role_principal': 'Projeção Multimídia',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Transmissão Online',
        'team': 'Equipe 01',
        'initials': 'RM'
    },
    'samuel': {
        'name': 'Samuel',
        'dept_principal': 'Mídia & Tecnologia',
        'role_principal': 'Projeção Multimídia',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Apoio Som',
        'team': 'Equipe 01',
        'initials': 'SM'
    },
    'lucas': {
        'name': 'Lucas',
        'dept_principal': 'Mídia & Tecnologia',
        'role_principal': 'Projeção Multimídia',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Transmissão Online',
        'team': 'Equipe 02',
        'initials': 'LC'
    },
    
    # Diaconato & Acolhimento
    'edinho_sandra': {
        'name': 'Edinho e Sandra',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Acolhimento & Recepção',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Organização da Nave',
        'team': 'Equipe 01',
        'initials': 'ES'
    },
    'johnatan_tatiana': {
        'name': 'Johnatan e Tatiana',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Acolhimento & Recepção',
        'dept_secundaria': 'Intercessão',
        'role_secundaria': 'Intercessão no Culto',
        'team': 'Equipe 02',
        'initials': 'JT'
    },
    'joel_nadir': {
        'name': 'Joel e Nadir',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Acolhimento & Recepção',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Organização da Nave',
        'team': 'Equipe 03',
        'initials': 'JN'
    },
    'leandro': {
        'name': 'Leandro',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Estacionamento & Nave',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Acolhimento',
        'team': 'Geral',
        'initials': 'LE'
    },
    'leandro_paula': {
        'name': 'Leadnro e Paula',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Estacionamento & Apoio',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Recepção',
        'team': 'Geral',
        'initials': 'LP'
    },
    'moises_thaynara': {
        'name': 'Moisés e Thaynará',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Acolhimento & Nave',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Estacionamento',
        'team': 'Geral',
        'initials': 'MT'
    },
    'edson_sandra': {
        'name': 'Edson e Sandra',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Recepção & Apoio',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Acolhimento',
        'team': 'Geral',
        'initials': 'ES'
    },
    'angela': {
        'name': 'Ângela',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Copa & Limpeza',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Apoio Geral',
        'team': 'Equipe 01',
        'initials': 'AG'
    },
    'valci': {
        'name': 'Valci',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Copa & Limpeza',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Apoio Geral',
        'team': 'Equipe 02',
        'initials': 'VC'
    },
    'divina': {
        'name': 'Divina',
        'dept_principal': 'Diaconato & Logística',
        'role_principal': 'Copa & Limpeza',
        'dept_secundaria': 'Diaconato & Logística',
        'role_secundaria': 'Apoio Geral',
        'team': 'Equipe 03',
        'initials': 'DV'
    },
    
    # Intercessão & Pregação Auxiliar
    'ana_paula': {
        'name': 'Ana Paula',
        'dept_principal': 'Intercessão',
        'role_principal': 'Intercessão & Oração',
        'dept_secundaria': 'Liderança Pastoral',
        'role_secundaria': 'Preletora',
        'team': 'Geral',
        'initials': 'AP'
    },
    'edla': {
        'name': 'Edla',
        'dept_principal': 'Intercessão',
        'role_principal': 'Intercessão & Dirigente',
        'dept_secundaria': 'Mídia & Tecnologia',
        'role_secundaria': 'Projeção Multimídia',
        'team': 'Equipe 03',
        'initials': 'ED'
    },
    'efrain_rael': {
        'name': 'Efrain Rael',
        'dept_principal': 'Liderança Pastoral',
        'role_principal': 'Preletor',
        'dept_secundaria': 'Ministério de Louvor',
        'role_secundaria': 'Ministro de Louvor',
        'team': 'Geral',
        'initials': 'ER'
    }
}

volunteers_map = {}
for k, v in volunteers_raw.items():
    v_copy = dict(v)
    v_copy['dept'] = v_copy['dept_principal']
    if v_copy.get('role_secundaria'):
        v_copy['role'] = f"{v_copy['role_principal']} (Principal) • {v_copy['role_secundaria']} (Secundária)"
    else:
        v_copy['role'] = f"{v_copy['role_principal']} (Principal)"
    volunteers_map[k] = v_copy

# Scan each volunteer's assignments per month
user_schedules = {}
for u_key, u_info in volunteers_map.items():
    user_schedules[u_key] = {}
    search_terms = [u_info['name'].lower()]
    if u_key == 'pastor': search_terms += ['flávio', 'flavio']
    if u_key == 'leandro': search_terms += ['leadnro']
    if u_key == 'icaro': search_terms += ['ícaro', 'icaro']
    if u_key == 'manu': search_terms += ['manú', 'manu', 'manuele']
    if u_key == 'efrain': search_terms += ['efrain', 'asp. efrain']
    if u_key == 'italo': search_terms += ['ítalo', 'italo']
    if u_key == 'flavio_f': search_terms += ['flávio f.', 'flavio f', 'flávio f']
    
    for m, services in all_data.items():
        m_list = []
        for s in services:
            assigned_roles = []
            dtl = s.get('details', {})
            dtl_txt = " ".join(str(v) for v in dtl.values() if v)
            txt_all = f"{s.get('preacher','')} {s.get('liturgia','')} {s.get('worship','')} {s.get('kids','')} {s.get('media','')} {s.get('diaconia','')} {dtl_txt}".lower()
            
            if any(term in txt_all for term in search_terms):
                lit_txt = f"{s.get('preacher','')} {s.get('liturgia','')} {dtl.get('dirigente','')} {dtl.get('intercessao','')} {dtl.get('bencao','')} {dtl.get('coord_geral','')}".lower()
                if any(term in lit_txt for term in search_terms):
                    assigned_roles.append('Palavra & Liturgia')
                    
                w_txt = f"{s.get('worship','')} {dtl.get('minister','')} {dtl.get('guitar_ac','')} {dtl.get('guitar_el','')} {dtl.get('keys','')} {dtl.get('bass','')} {dtl.get('drums','')} {dtl.get('back1','')} {dtl.get('back2','')} {dtl.get('coord_louvor','')}".lower()
                if any(term in w_txt for term in search_terms):
                    assigned_roles.append('Ministério de Louvor')
                    
                k_txt = f"{s.get('kids','')} {dtl.get('kids1','')} {dtl.get('kids2','')} {dtl.get('coord_kids','')}".lower()
                if any(term in k_txt for term in search_terms):
                    assigned_roles.append('Shamah Kids')
                    
                m_txt = f"{s.get('media','')} {dtl.get('sound','')} {dtl.get('proj','')} {dtl.get('stream','')} {dtl.get('coord_midia','')} {dtl.get('midia_social','')}".lower()
                if any(term in m_txt for term in search_terms):
                    assigned_roles.append('Mídia & Cabine')
                    
                d_txt = f"{s.get('diaconia','')} {dtl.get('acolhimento','')} {dtl.get('estacionamento','')} {dtl.get('copa_banheiros','')} {dtl.get('coord_diaconato','')}".lower()
                if any(term in d_txt for term in search_terms):
                    assigned_roles.append('Diaconato & Apoio')
                    
                m_list.append({
                    'date': s['date'],
                    'title': s['title'],
                    'theme': s.get('theme', ''),
                    'roles': ' / '.join(assigned_roles) or 'Escalado(a)',
                    'team': s.get('team', '')
                })
        user_schedules[u_key][m] = m_list

data_json_str = json.dumps(all_data, ensure_ascii=False)
user_schedules_json_str = json.dumps(user_schedules, ensure_ascii=False)
volunteers_map_json_str = json.dumps(volunteers_map, ensure_ascii=False)

team_templates = {
    "Equipe 01": {
        "coord_geral": "Pr. Flávio",
        "coord_celebracao": "Pr. Flávio",
        "dirigente": "Jordana",
        "intercessao": "Edinho e Sandra",
        "bencao": "Pr. Flávio",
        "coord_louvor": "Efrain",
        "minister": "Manú",
        "back1": "Karol",
        "back2": "Kamynnsky",
        "guitar_ac": "Bruno",
        "guitar_el": "Ítalo",
        "keys": "Efrain",
        "bass": "Italo",
        "drums": "Ícaro",
        "coord_kids": "Ana Carolina",
        "kids1": "Ana Carolina e Maria Eduarda",
        "kids2": "Maria Eduarda",
        "coord_midia": "Felipe",
        "midia_social": "Karol e Equipe",
        "sound": "Felipe",
        "proj": "Ramon e Samuel",
        "stream": "Lorivaldo",
        "coord_diaconato": "Pra. Iracilene",
        "acolhimento": "Edinho e Sandra",
        "estacionamento": "Equipe 01",
        "copa_banheiros": "Divina"
    },
    "Equipe 02": {
        "coord_geral": "Pr. Flávio",
        "coord_celebracao": "Pr. Flávio",
        "dirigente": "Pra. Iracilene",
        "intercessao": "Ângela e Nadir",
        "bencao": "Pr. Flávio",
        "coord_louvor": "Asp. Efrain",
        "minister": "Manú",
        "back1": "Karol",
        "back2": "Kamynnsky",
        "guitar_ac": "Bruno",
        "guitar_el": "Ítalo",
        "keys": "Teclado Base",
        "bass": "João Paulo",
        "drums": "Ícaro",
        "coord_kids": "Ana Carolina",
        "kids1": "Letícia, Ana Júlia e Ester",
        "kids2": "Ana Júlia",
        "coord_midia": "Felipe",
        "midia_social": "Karol e Equipe",
        "sound": "Efrain",
        "proj": "Jordana e Lucas",
        "stream": "Lorivaldo",
        "coord_diaconato": "Pra. Iracilene",
        "acolhimento": "Johnatan e Tatiana",
        "estacionamento": "Equipe 02",
        "copa_banheiros": "Valci"
    },
    "Equipe 03": {
        "coord_geral": "Pr. Flávio",
        "coord_celebracao": "Pr. Flávio",
        "dirigente": "Mané",
        "intercessao": "Joel e Nadir",
        "bencao": "Pr. Flávio",
        "coord_louvor": "Efrain",
        "minister": "Karol",
        "back1": "Bruno",
        "back2": "Kamynnsky",
        "guitar_ac": "Flávio F.",
        "guitar_el": "Flávio F.",
        "keys": "Efrain",
        "bass": "Italo",
        "drums": "Ícaro",
        "coord_kids": "Ana Carolina",
        "kids1": "Valéria e Jordana",
        "kids2": "Jordana",
        "coord_midia": "Felipe",
        "midia_social": "Karol e Equipe",
        "sound": "Kauê",
        "proj": "Edla e Ana C. da Tatiana",
        "stream": "Lorivaldo",
        "coord_diaconato": "Pra. Iracilene",
        "acolhimento": "Joel e Nadir",
        "estacionamento": "Equipe 03",
        "copa_banheiros": "Valci"
    }
}
team_templates_json_str = json.dumps(team_templates, ensure_ascii=False)

with open('songs_data.json', 'r', encoding='utf-8') as f:
    songs_data = json.load(f)

approved_songs_json_str = json.dumps(songs_data.get('approved_songs', []), ensure_ascii=False)
liturgical_routines_json_str = json.dumps(songs_data.get('liturgical_routines', {}), ensure_ascii=False)

with open('template_v4.html', 'r', encoding='utf-8') as f:
    template = f.read()

html_final = template.replace('__DATA_JSON__', data_json_str)\
                     .replace('__USER_SCHEDULES_JSON__', user_schedules_json_str)\
                     .replace('__VOLUNTEERS_JSON__', volunteers_map_json_str)\
                     .replace('__TEAM_TEMPLATES_JSON__', team_templates_json_str)\
                     .replace('__APPROVED_SONGS_JSON__', approved_songs_json_str)\
                     .replace('__LITURGICAL_ROUTINES_JSON__', liturgical_routines_json_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_final)

with open(r'C:\Users\sigma\.gemini\antigravity\brain\abfefb37-5e54-4455-bf09-7a27be839382\app_demo.html', 'w', encoding='utf-8') as f:
    f.write(html_final)

print("index.html e app_demo.html compilados com sucesso com canções e roteiros litúrgicos!")
