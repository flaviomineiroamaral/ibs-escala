import openpyxl, json, datetime, os

wb = openpyxl.load_workbook('sheet.xlsx')

# Carregar serviços existentes para preservar setlists e dados enriquecidos se houver
existing_data = {}
if os.path.exists('all_services.json'):
    try:
        with open('all_services.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    except Exception as e:
        print(f"Aviso ao ler all_services.json existente: {e}")

months_data = {}

for m in ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out']:
    ws = wb[m]
    services = []
    
    rows = {}
    for r in range(6, 49):
        c1 = str(ws.cell(r, 1).value or '').strip()
        c2 = str(ws.cell(r, 2).value or '').strip()
        lbl = (c1 + ' ' + c2).lower().replace('\n', ' ')
        
        if 'coordena' in lbl and 'geral' in lbl or 'dire' in lbl and 'geral' in lbl: rows['coord_geral'] = r
        elif 'coordena' in lbl and 'diaconato' in lbl or 'atmosfera' in lbl: rows['coord_diaconato'] = r
        elif 'acolhimento' in lbl or ('recep' in lbl and 'intercess' not in lbl): rows['acolhimento'] = r
        elif 'estacionamento' in lbl: rows['estacionamento'] = r
        elif 'copa' in lbl or 'banheiro' in lbl or 'cantina' in lbl: rows['copa_banheiros'] = r
        elif 'coordena' in lbl and 'celebra' in lbl or 'dire' in lbl and 'celebra' in lbl: rows['coord_celebracao'] = r
        elif 'intercess' in lbl: rows['intercessao'] = r
        elif 'dirigente' in lbl or ('abertura' in lbl and 'avisos' in lbl): rows['dirigente'] = r
        elif 'ministrante' in lbl: rows['preacher'] = r
        elif 'tipo da mensagem' in lbl: rows['msg_type'] = r
        elif 'texto-base' in lbl or ('texto' in lbl and 'base' in lbl): rows['text'] = r
        elif 'tema da mensagem' in lbl: rows['theme'] = r
        elif 'ben' in lbl and 'apost' in lbl: rows['bencao'] = r
        elif 'shamah' in lbl or ('infantil' in lbl and 'dire' in lbl) or ('coordena' in lbl and 'kid' in lbl): rows['coord_kids'] = r
        elif 'turma 01' in lbl or 'turma 1' in lbl: rows['kids1'] = r
        elif 'turma 02' in lbl or 'turma 2' in lbl: rows['kids2'] = r
        elif 'coordena' in lbl and 'm' in lbl and 'dia' in lbl: rows['coord_midia'] = r
        elif ('m' in lbl and 'dia social' in lbl) or 'fotografia' in lbl: rows['midia_social'] = r
        elif 'mesa som' in lbl: rows['sound'] = r
        elif 'transmiss' in lbl and 'proje' not in lbl: rows['stream'] = r
        elif 'proje' in lbl: rows['proj'] = r
        elif 'coordena' in lbl and 'louvor' in lbl or ('dire' in lbl and 'louvor' in lbl): rows['coord_louvor'] = r
        elif 'ministro' in lbl and 'dire' not in lbl and 'coord' not in lbl: rows['minister'] = r
        elif 'back' in lbl:
            if 'back1' not in rows: rows['back1'] = r
            elif 'back2' not in rows: rows['back2'] = r
            elif 'back3' not in rows: rows['back3'] = r
        elif 'viol' in lbl: rows['guitar_ac'] = r
        elif 'guitarra' in lbl: rows['guitar_el'] = r
        elif 'teclado' in lbl: rows['keys'] = r
        elif 'contra-baixo' in lbl or 'baixo' in lbl: rows['bass'] = r
        elif 'bateria' in lbl: rows['drums'] = r
        elif '(verde)' in lbl or 'música 1' in lbl or 'msica 1' in lbl: rows['song_green'] = r
        elif '(amarelo)' in lbl or 'música 2' in lbl or 'msica 2' in lbl: rows['song_yellow'] = r
        elif '(vermelho)' in lbl or 'música 3' in lbl or 'msica 3' in lbl: rows['song_red'] = r
        elif '(roxo)' in lbl or 'música 4' in lbl or 'msica 4' in lbl: rows['song_purple'] = r
        elif '(azul)' in lbl or 'música 5' in lbl or 'msica 5' in lbl: rows['song_blue'] = r
        
    for c in range(3, ws.max_column+1):
        dt_val = ws.cell(3, c).value
        day_str = ws.cell(4, c).value
        ev_str = ws.cell(5, c).value
        team_str = ws.cell(2, c).value
        if not dt_val: continue
        
        if isinstance(dt_val, datetime.datetime):
            dt_formatted = dt_val.strftime('%d/%m/%Y')
            dt_iso = dt_val.strftime('%Y-%m-%d')
        else:
            dt_formatted = str(dt_val)[:10]
            dt_iso = dt_formatted
            
        def g(key):
            r = rows.get(key)
            if not r: return ''
            v = ws.cell(r, c).value
            if v is None: return ''
            s = str(v).strip()
            return '' if s in ['-', '---', 'None'] else s
            
        preacher = g('preacher')
        theme = g('theme')
        text = g('text')
        msg_type = g('msg_type')
        coord_geral = g('coord_geral')
        coord_celebracao = g('coord_celebracao')
        dirigente = g('dirigente')
        intercessao = g('intercessao')
        bencao = g('bencao')
        
        # Louvor
        coord_louvor = g('coord_louvor')
        minister = g('minister')
        backs = [g('back1'), g('back2'), g('back3')]
        backs = [b for b in backs if b]
        guitar_ac = g('guitar_ac')
        guitar_el = g('guitar_el')
        keys = g('keys')
        bass = g('bass')
        drums = g('drums')
        
        w_parts = []
        if coord_louvor: w_parts.append(f"Coord: {coord_louvor}")
        if minister: w_parts.append(f"{minister} (Ministro)")
        if backs: w_parts.append(f"{', '.join(backs)} (Back)")
        if guitar_ac: w_parts.append(f"{guitar_ac} (Violão)")
        if guitar_el: w_parts.append(f"{guitar_el} (Guitarra)")
        if keys: w_parts.append(f"{keys} (Teclado)")
        if bass: w_parts.append(f"{bass} (Baixo)")
        if drums: w_parts.append(f"{drums} (Bateria)")
        
        # Kids
        coord_kids = g('coord_kids')
        kids1 = g('kids1')
        kids2 = g('kids2')
        k_parts = []
        if coord_kids: k_parts.append(f"Coord: {coord_kids}")
        if kids1: k_parts.append(f"T1: {kids1}")
        if kids2: k_parts.append(f"T2: {kids2}")
        
        # Mídia
        coord_midia = g('coord_midia')
        midia_social = g('midia_social')
        sound = g('sound')
        proj = g('proj')
        stream = g('stream')
        m_parts = []
        if coord_midia: m_parts.append(f"Coord: {coord_midia}")
        if midia_social: m_parts.append(f"Social: {midia_social}")
        if sound: m_parts.append(f"Som: {sound}")
        if proj: m_parts.append(f"Proj: {proj}")
        if stream: m_parts.append(f"Transm: {stream}")
        
        # Diaconato
        coord_diaconato = g('coord_diaconato')
        acolhimento = g('acolhimento')
        estacionamento = g('estacionamento')
        copa_banheiros = g('copa_banheiros')
        d_parts = []
        if coord_diaconato: d_parts.append(f"Coord: {coord_diaconato}")
        if acolhimento: d_parts.append(f"Acolhimento: {acolhimento}")
        if estacionamento: d_parts.append(f"Estacionamento: {estacionamento}")
        if copa_banheiros: d_parts.append(f"Copa: {copa_banheiros}")
        
        # Liturgia
        l_parts = []
        if coord_geral: l_parts.append(f"Coord. Geral: {coord_geral}")
        if coord_celebracao and coord_celebracao != coord_geral: l_parts.append(f"Coord. Celebração: {coord_celebracao}")
        if dirigente: l_parts.append(f"Dirigente: {dirigente}")
        if intercessao: l_parts.append(f"Intercessão: {intercessao}")
        if bencao: l_parts.append(f"Bênção: {bencao}")
        
        # Músicas da planilha (se não houver setlist litúrgico já cadastrado)
        songs = []
        # Verificar se já existe setlist detalhado na base existente
        ex_month = existing_data.get(m, [])
        matched_ex = None
        for ex in ex_month:
            if ex.get('date_raw') == dt_iso or ex.get('date') == f"{day_str[:3]}, {dt_formatted}":
                matched_ex = ex
                break
                
        if matched_ex and matched_ex.get('songs') and len(matched_ex['songs']) > 0:
            songs = matched_ex['songs']
        else:
            raw_songs = [
                {'color': 'verde', 'badge': 'VERDE • 01-19', 'title': g('song_green')},
                {'color': 'amarelo', 'badge': 'AMARELO • 20-39', 'title': g('song_yellow')},
                {'color': 'vermelho', 'badge': 'VERMELHO • 40-59', 'title': g('song_red')},
                {'color': 'roxo', 'badge': 'ROXO • 60-79', 'title': g('song_purple')},
                {'color': 'azul', 'badge': 'AZUL • 80-99', 'title': g('song_blue')},
            ]
            songs = [s for s in raw_songs if s['title']]
        
        weekday_label = (day_str or '')[:3]
        
        services.append({
            'date': f"{weekday_label}, {dt_formatted}" if weekday_label else dt_formatted,
            'date_raw': dt_iso,
            'weekday': day_str or '',
            'title': ev_str or 'Culto',
            'team': team_str or '',
            'preacher': preacher,
            'theme': theme,
            'text': text,
            'msg_type': msg_type,
            'liturgia': ' • '.join(l_parts) or '',
            'worship': ' • '.join(w_parts) or 'A definir',
            'kids': ' • '.join(k_parts) or 'A definir',
            'media': ' • '.join(m_parts) or 'A definir',
            'diaconia': ' • '.join(d_parts) or '',
            'details': {
                'preacher': preacher,
                'theme': theme,
                'text': text,
                'msg_type': msg_type,
                'coord_geral': coord_geral,
                'coord_celebracao': coord_celebracao,
                'dirigente': dirigente,
                'intercessao': intercessao,
                'bencao': bencao,
                
                'coord_louvor': coord_louvor,
                'minister': minister,
                'back1': g('back1'),
                'back2': g('back2'),
                'back3': g('back3'),
                'guitar_ac': guitar_ac,
                'guitar_el': guitar_el,
                'keys': keys,
                'bass': bass,
                'drums': drums,
                
                'coord_kids': coord_kids,
                'kids1': kids1,
                'kids2': kids2,
                
                'coord_midia': coord_midia,
                'midia_social': midia_social,
                'sound': sound,
                'proj': proj,
                'stream': stream,
                
                'coord_diaconato': coord_diaconato,
                'acolhimento': acolhimento,
                'estacionamento': estacionamento,
                'copa_banheiros': copa_banheiros
            },
            'songs': songs
        })
        
    months_data[m] = services

with open('all_services.json', 'w', encoding='utf-8') as f:
    json.dump(months_data, f, ensure_ascii=False, indent=2)

print('all_services.json gerado com todos os 30 cargos e funções completos!')
