import openpyxl, json, datetime

wb = openpyxl.load_workbook('sheet.xlsx')

months_data = {}

for m in ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out']:
    ws = wb[m]
    services = []
    
    rows = {}
    for r in range(6, 49):
        c1 = ws.cell(r, 1).value
        c2 = ws.cell(r, 2).value
        label = (c2 or c1 or '').strip().replace('\n', ' ')
        if 'Acolhimento' in label or 'Recep' in label: rows['acolhimento'] = r
        elif 'Estacionamento' in label: rows['estacionamento'] = r
        elif 'Intercess' in label: rows['intercessao'] = r
        elif 'Ministrante' in label: rows['preacher'] = r
        elif 'Texto' in label: rows['text'] = r
        elif 'Tema' in label: rows['theme'] = r
        elif 'Turma 01' in label: rows['kids1'] = r
        elif 'Turma 02' in label: rows['kids2'] = r
        elif 'Mesa Som' in label: rows['sound'] = r
        elif 'Transmiss' in label and 'Proje' not in label: rows['stream'] = r
        elif 'Proje' in label: rows['proj'] = r
        elif 'Ministro' in label: rows['minister'] = r
        elif 'Back-vocal' in label and 'back1' not in rows: rows['back1'] = r
        elif 'Back-vocal' in label and 'back2' not in rows: rows['back2'] = r
        elif 'Viol' in label: rows['guitar_ac'] = r
        elif 'Guitarra' in label: rows['guitar_el'] = r
        elif 'Teclado' in label: rows['keys'] = r
        elif 'Contra-baixo' in label: rows['bass'] = r
        elif 'Bateria' in label: rows['drums'] = r
        elif '(Verde)' in label or 'Música 1' in label or 'Msica 1' in label: rows['song_green'] = r
        elif '(Amarelo)' in label or 'Música 2' in label or 'Msica 2' in label: rows['song_yellow'] = r
        elif '(Vermelho)' in label or 'Música 3' in label or 'Msica 3' in label: rows['song_red'] = r
        elif '(Roxo)' in label or 'Música 4' in label or 'Msica 4' in label: rows['song_purple'] = r
        elif '(Azul)' in label or 'Música 5' in label or 'Msica 5' in label: rows['song_blue'] = r
        
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
            return str(v).strip() if v else ''
            
        preacher = g('preacher')
        theme = g('theme')
        text = g('text')
        
        # Build worship string
        w_parts = []
        if g('minister'): w_parts.append(g('minister') + " (Ministro)")
        backs = [g('back1'), g('back2')]
        backs = [b for b in backs if b and b != '-']
        if backs: w_parts.append(", ".join(backs) + " (Back)")
        if g('guitar_ac'): w_parts.append(g('guitar_ac') + " (Violão)")
        if g('keys') and g('keys') != '-': w_parts.append(g('keys') + " (Teclado)")
        if g('bass') and g('bass') != '-': w_parts.append(g('bass') + " (Baixo)")
        if g('drums'): w_parts.append(g('drums') + " (Bateria)")
        
        # Build kids string
        k_parts = []
        if g('kids1') and g('kids1') != '-': k_parts.append("T1: " + g('kids1'))
        if g('kids2') and g('kids2') != '-': k_parts.append("T2: " + g('kids2'))
        
        # Build media string
        m_parts = []
        if g('sound') and g('sound') != '-': m_parts.append("Som: " + g('sound'))
        if g('proj') and g('proj') != '-': m_parts.append("Proj: " + g('proj'))
        if g('stream') and g('stream') != '-': m_parts.append("Transm: " + g('stream'))
        
        # Build diaconia string
        d_parts = []
        if g('acolhimento'): d_parts.append("Acolhimento: " + g('acolhimento'))
        if g('estacionamento') and g('estacionamento') != '-': d_parts.append("Estacionamento: " + g('estacionamento'))
        
        songs = [
            {'color': 'verde', 'badge': 'VERDE • 01-19', 'title': g('song_green')},
            {'color': 'amarelo', 'badge': 'AMARELO • 20-39', 'title': g('song_yellow')},
            {'color': 'vermelho', 'badge': 'VERMELHO • 40-59', 'title': g('song_red')},
            {'color': 'roxo', 'badge': 'ROXO • 60-79', 'title': g('song_purple')},
            {'color': 'azul', 'badge': 'AZUL • 80-99', 'title': g('song_blue')},
        ]
        songs = [s for s in songs if s['title']]
        
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
            'worship': ' • '.join(w_parts) or 'A definir',
            'kids': ' • '.join(k_parts) or 'A definir',
            'media': ' • '.join(m_parts) or 'A definir',
            'diaconia': ' • '.join(d_parts) or '',
            'details': {
                'preacher': preacher,
                'theme': theme,
                'text': text,
                'minister': g('minister'),
                'back1': g('back1'),
                'back2': g('back2'),
                'guitar_ac': g('guitar_ac'),
                'guitar_el': g('guitar_el'),
                'keys': g('keys'),
                'bass': g('bass'),
                'drums': g('drums'),
                'kids1': g('kids1'),
                'kids2': g('kids2'),
                'sound': g('sound'),
                'proj': g('proj'),
                'stream': g('stream'),
                'acolhimento': g('acolhimento'),
                'estacionamento': g('estacionamento'),
            },
            'songs': songs
        })
        
    months_data[m] = services

with open('all_services.json', 'w', encoding='utf-8') as f:
    json.dump(months_data, f, ensure_ascii=False, indent=2)

print('all_services.json gerado com granular details com sucesso!')
