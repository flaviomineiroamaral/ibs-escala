import json

with open('all_services.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

# Base volunteers map
volunteers_map = {
    'bruno': {'name': 'Bruno', 'role': 'Louvor - Violão / Ministro', 'dept': 'Ministério de Louvor', 'initials': 'BR'},
    'leandro': {'name': 'Leandro', 'role': 'Diaconato - Acolhimento / Portaria', 'dept': 'Diaconato & Logística', 'initials': 'LE'},
    'ana_carolina': {'name': 'Ana Carolina', 'role': 'Coordenação Shamah Kids', 'dept': 'Shamah Kids', 'initials': 'AC'},
    'felipe': {'name': 'Felipe', 'role': 'Mesa de Som e Iluminação', 'dept': 'Mídia & Tecnologia', 'initials': 'FE'},
    'pastor': {'name': 'Pr. Flávio Amaral', 'role': 'Direção Geral & Ministrante', 'dept': 'Liderança Pastoral', 'initials': 'PF'},
    'manu': {'name': 'Manú', 'role': 'Ministra de Louvor', 'dept': 'Ministério de Louvor', 'initials': 'MN'},
    'karol': {'name': 'Karol', 'role': 'Mídia Social / Back-vocal', 'dept': 'Mídia / Louvor', 'initials': 'KR'},
    'efrain': {'name': 'Efrain', 'role': 'Coord. Louvor & Teclado', 'dept': 'Ministério de Louvor', 'initials': 'EF'},
    'icaro': {'name': 'Ícaro', 'role': 'Bateria', 'dept': 'Ministério de Louvor', 'initials': 'IC'},
    'leticia': {'name': 'Letícia', 'role': 'Shamah Kids & Intercessão', 'dept': 'Shamah Kids', 'initials': 'LT'},
}

# Scan each volunteer's assignments per month
user_schedules = {}
for u_key, u_info in volunteers_map.items():
    user_schedules[u_key] = {}
    search_terms = [u_info['name'].lower()]
    if u_key == 'pastor': search_terms += ['flávio', 'flavio']
    if u_key == 'leandro': search_terms += ['leadnro']
    if u_key == 'icaro': search_terms += ['ícaro', 'icaro']
    if u_key == 'manu': search_terms += ['manú', 'manu', 'manuele']
    if u_key == 'efrain': search_terms += ['efrain', 'asp. efrain', 'efrain rael']
    
    for m, services in all_data.items():
        m_list = []
        for s in services:
            assigned_roles = []
            txt_all = f"{s.get('preacher','')} {s.get('worship','')} {s.get('kids','')} {s.get('media','')} {s.get('diaconia','')}".lower()
            if any(term in txt_all for term in search_terms):
                if any(term in s.get('preacher','').lower() for term in search_terms):
                    assigned_roles.append('Palavra / Preletor')
                if any(term in s.get('worship','').lower() for term in search_terms):
                    assigned_roles.append('Ministério de Louvor')
                if any(term in s.get('kids','').lower() for term in search_terms):
                    assigned_roles.append('Shamah Kids')
                if any(term in s.get('media','').lower() for term in search_terms):
                    assigned_roles.append('Mídia / Som')
                if any(term in s.get('diaconia','').lower() for term in search_terms):
                    assigned_roles.append('Diaconato / Acolhimento')
                    
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

# Team templates
team_templates = {
    "Equipe 01": {
        "acolhimento": "Edinho e Sandra",
        "estacionamento": "Equipe 01",
        "kids1": "Ana Carolina e Maria Eduarda",
        "kids2": "Maria Eduarda",
        "sound": "Felipe",
        "proj": "Ramon e Samuel",
        "stream": "Lorivaldo",
        "minister": "Manú",
        "back1": "Karol",
        "back2": "Kamynnsky",
        "guitar_ac": "Bruno",
        "keys": "Efrain",
        "bass": "Italo",
        "drums": "Ícaro"
    },
    "Equipe 02": {
        "acolhimento": "Johnatan e Tatiana",
        "estacionamento": "Equipe 02",
        "kids1": "Letícia, Ana Júlia e Ester",
        "kids2": "Ana Júlia",
        "sound": "Efrain",
        "proj": "Jordana e Lucas",
        "stream": "Lorivaldo",
        "minister": "Manú",
        "back1": "Karol",
        "back2": "Kamynnsky",
        "guitar_ac": "Bruno",
        "keys": "Teclado Base",
        "bass": "João Paulo",
        "drums": "Ícaro"
    },
    "Equipe 03": {
        "acolhimento": "Joel e Nadir",
        "estacionamento": "Equipe 03",
        "kids1": "Valéria e Jordana",
        "kids2": "Jordana",
        "sound": "Kauê",
        "proj": "Edla e Ana C. da Tatiana",
        "stream": "Lorivaldo",
        "minister": "Karol",
        "back1": "Bruno",
        "back2": "Kamynnsky",
        "guitar_ac": "Flávio F.",
        "keys": "Efrain",
        "bass": "Italo",
        "drums": "Ícaro"
    }
}
team_templates_json_str = json.dumps(team_templates, ensure_ascii=False)

template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IBS Escala - Lançamento e Gestão de Escalas</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    ::-webkit-scrollbar { width: 4px; height: 4px; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    .tab-active { color: #2563eb; border-top: 3px solid #2563eb; }
    .badge-verde { background-color: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
    .badge-amarelo { background-color: #fef9c3; color: #a16207; border: 1px solid #fef08a; }
    .badge-vermelho { background-color: #fee2e2; color: #b91c1c; border: 1px solid #fecaca; }
    .badge-roxo { background-color: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }
    .badge-azul { background-color: #dbeafe; color: #1d4ed8; border: 1px solid #bfdbfe; }
  </style>
</head>
<body class="bg-slate-100 text-slate-800 antialiased font-sans min-h-screen flex flex-col items-center justify-start p-2 sm:p-4">

  <!-- Container do Smartphone Mockup -->
  <div class="w-full max-w-md bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col min-h-[850px] relative">
    
    <!-- Top Header do App -->
    <header class="bg-gradient-to-r from-blue-700 to-indigo-800 text-white p-3.5 pt-4 pb-3 shadow-md sticky top-0 z-20">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <div class="w-9 h-9 rounded-xl bg-white/20 backdrop-blur-md flex items-center justify-center font-bold text-lg text-white shadow-inner">
            <i class="fa-solid fa-church text-sm"></i>
          </div>
          <div>
            <h1 class="text-base font-bold tracking-tight leading-tight">IBS Escala</h1>
            <p class="text-[11px] text-blue-200 font-medium">Igreja Batista Shamah • 2026</p>
          </div>
        </div>

        <!-- Botões de Ação Rápida de Cadastro no Header -->
        <div class="flex items-center gap-1">
          <button onclick="openNewPersonModal()" class="bg-white/20 hover:bg-white/30 text-white text-[10px] sm:text-[11px] font-bold px-2 py-1 rounded-lg border border-white/30 flex items-center gap-1 transition shadow-sm active:scale-95" title="Cadastrar Pessoa">
            <i class="fa-solid fa-user-plus text-[9px]"></i> +Pessoa
          </button>
          <button onclick="openNewCultoModal()" class="bg-white/20 hover:bg-white/30 text-white text-[10px] sm:text-[11px] font-bold px-2 py-1 rounded-lg border border-white/30 flex items-center gap-1 transition shadow-sm active:scale-95" title="Cadastrar Culto">
            <i class="fa-solid fa-calendar-plus text-[9px]"></i> +Culto
          </button>
          <button onclick="openEditScaleModal(0)" class="bg-amber-400 hover:bg-amber-500 text-slate-900 text-[10px] sm:text-[11px] font-extrabold px-2 py-1 rounded-lg border border-amber-300 flex items-center gap-1 transition shadow-sm active:scale-95" title="Lançar / Editar Escala">
            <i class="fa-solid fa-pen-to-square text-[9px]"></i> Escalar
          </button>
        </div>
      </div>

      <!-- Barra de Controle Duplo: Simular Como & Mês Ativo -->
      <div class="mt-2.5 grid grid-cols-2 gap-2 bg-black/20 p-2 rounded-xl backdrop-blur-sm border border-white/10 text-xs">
        <div>
          <label class="text-[10px] text-blue-200 font-semibold uppercase block mb-0.5">Simular como:</label>
          <select id="userSelector" onchange="changeUser(this.value)" class="w-full bg-white text-slate-800 text-[11px] font-bold rounded-lg px-2 py-1 outline-none shadow-sm cursor-pointer border border-blue-200">
            <!-- Populado dinamicamente -->
          </select>
        </div>

        <div>
          <label class="text-[10px] text-blue-200 font-semibold uppercase block mb-0.5">Mês da Escala:</label>
          <select id="globalMonthSelector" onchange="onMonthChange(this.value)" class="w-full bg-white text-slate-800 text-[11px] font-bold rounded-lg px-2 py-1 outline-none shadow-sm cursor-pointer border border-blue-200">
            <option value="Jan">Janeiro (Mês 01)</option>
            <option value="Fev">Fevereiro (Mês 02)</option>
            <option value="Mar">Março (Mês 03)</option>
            <option value="Abr">Abril (Mês 04)</option>
            <option value="Mai">Maio (Mês 05)</option>
            <option value="Jun">Junho (Mês 06)</option>
            <option value="Jul">Julho (Mês 07)</option>
            <option value="Ago">Agosto (Mês 08)</option>
            <option value="Set">Setembro (Mês 09)</option>
            <option value="Out" selected>Outubro (Mês 10) ⭐</option>
            <option value="Nov">Novembro (Mês 11)</option>
            <option value="Dez">Dezembro (Mês 12)</option>
          </select>
        </div>
      </div>
    </header>

    <!-- Conteúdo Principal Dinâmico -->
    <main class="flex-1 overflow-y-auto p-4 pb-20 space-y-4">

      <!-- ABA 1: MEUS CULTOS (Página Inicial do Voluntário) -->
      <section id="tab-meus-cultos" class="space-y-4">
        
        <!-- Boas-vindas personalizadas -->
        <div class="flex items-center justify-between bg-blue-50/80 p-3 rounded-2xl border border-blue-100 shadow-sm">
          <div class="flex items-center space-x-3">
            <div id="userAvatar" class="w-11 h-11 rounded-full bg-blue-600 text-white font-bold flex items-center justify-center text-sm shadow">
              BR
            </div>
            <div>
              <p class="text-xs text-slate-500">Paz do Senhor,</p>
              <h2 id="userName" class="text-base font-bold text-slate-800 leading-tight">Bruno</h2>
              <span id="userRoleBadge" class="inline-block text-[11px] px-2 py-0.5 rounded-full font-medium bg-blue-100 text-blue-700 mt-0.5">Ministério de Louvor</span>
            </div>
          </div>
          <div class="text-right">
            <span class="text-[10px] text-slate-400 block font-bold uppercase">Mês Ativo</span>
            <span id="currentMonthBadge" class="text-xs font-extrabold text-blue-800 bg-blue-100/80 px-2 py-0.5 rounded-md">OUTUBRO</span>
          </div>
        </div>

        <!-- Card de Destaque: Próximo Culto do Mês Selecionado -->
        <div id="nextServiceCard" class="bg-white rounded-2xl border-2 border-blue-500 shadow-md p-4 relative overflow-hidden">
          <div class="absolute -right-6 -bottom-6 text-slate-100 pointer-events-none">
            <i class="fa-solid fa-calendar-check text-8xl opacity-40"></i>
          </div>

          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] uppercase tracking-wider font-extrabold text-blue-600 bg-blue-50 px-2.5 py-1 rounded-full flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-blue-600 animate-pulse"></span>
              Próximo Serviço
            </span>
            <span id="statusTag" class="text-xs font-semibold text-amber-700 bg-amber-50 border border-amber-200 px-2.5 py-0.5 rounded-full flex items-center gap-1">
              <i class="fa-solid fa-clock text-[10px]"></i> Aguardando Confirmação
            </span>
          </div>

          <div class="my-3">
            <h3 id="serviceTitle" class="text-lg font-extrabold text-slate-900 leading-tight">Carregando...</h3>
            <p id="serviceTheme" class="text-xs text-slate-600 mt-1 italic">Tema da mensagem</p>
          </div>

          <div class="grid grid-cols-2 gap-2 text-xs bg-slate-50 p-3 rounded-xl border border-slate-100 mb-3">
            <div>
              <span class="text-slate-400 block text-[10px] uppercase font-semibold">Data e Culto</span>
              <span id="serviceDateTime" class="font-bold text-slate-800 flex items-center gap-1 mt-0.5">
                <i class="fa-regular fa-calendar text-blue-600"></i> --/--
              </span>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px] uppercase font-semibold">Sua Função</span>
              <span id="serviceFunction" class="font-bold text-blue-700 flex items-center gap-1 mt-0.5">
                <i class="fa-solid fa-circle-check text-blue-600"></i> Escalado
              </span>
            </div>
          </div>

          <!-- Ações em 1 Toque (Botões Grandes e Diretos) -->
          <div id="actionButtons" class="flex gap-2">
            <button onclick="confirmPresence()" class="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-3 rounded-xl text-xs sm:text-sm flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/20 active:scale-95 transition-all">
              <i class="fa-solid fa-check text-sm"></i>
              Confirmar Presença
            </button>
            <button onclick="openSwapModal()" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold py-3 px-3 rounded-xl text-xs sm:text-sm flex items-center justify-center gap-1.5 active:scale-95 transition-all border border-slate-200">
              <i class="fa-solid fa-arrows-rotate text-xs"></i>
              Pedir Troca
            </button>
          </div>

          <!-- Mensagem de Sucesso -->
          <div id="confirmedFeedback" class="hidden bg-emerald-50 border border-emerald-200 p-3 rounded-xl text-center">
            <p class="text-xs font-bold text-emerald-800 flex items-center justify-center gap-1.5">
              <i class="fa-solid fa-circle-check text-emerald-600"></i> Presença Confirmada! Deus abençoe seu serviço.
            </p>
            <button onclick="resetConfirmation()" class="text-[11px] text-emerald-700 underline mt-1 hover:text-emerald-900">Desfazer confirmação</button>
          </div>
        </div>

        <!-- Todas as Escalas do Voluntário no Mês -->
        <div>
          <div class="flex items-center justify-between mb-2 px-1">
            <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400">Escalas de <span id="monthNameLabel">Outubro</span></h4>
            <span id="serviceCountBadge" class="text-[11px] font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded-full">0 escalas</span>
          </div>
          <div id="futureServicesList" class="space-y-2">
            <!-- Injetado dinamicamente -->
          </div>
        </div>
      </section>

      <!-- ABA 2: ESCALA GERAL DO MÊS (Visão de Toda a Igreja) -->
      <section id="tab-escala-geral" class="hidden space-y-3">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-base font-extrabold text-slate-900">Escala Geral da Igreja</h2>
            <p class="text-xs text-slate-500">Mês de <span id="generalMonthTitle" class="font-bold text-blue-700">Outubro 2026</span></p>
          </div>
          <div class="flex gap-1.5">
            <button onclick="openEditScaleModal(0)" class="bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold px-2.5 py-1.5 rounded-xl shadow-sm flex items-center gap-1.5 active:scale-95 transition">
              <i class="fa-solid fa-pen-to-square text-xs"></i> Lançar Escala
            </button>
            <button onclick="openNewCultoModal()" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-2.5 py-1.5 rounded-xl shadow-sm flex items-center gap-1.5 active:scale-95 transition">
              <i class="fa-solid fa-plus text-xs"></i> +Culto
            </button>
          </div>
        </div>

        <!-- Lista de Cultos do Mês Selecionado (Acordeão) -->
        <div id="monthServicesAccordion" class="space-y-2.5">
          <!-- Acordeão renderizado via JS -->
        </div>
      </section>

      <!-- ABA 3: REPERTÓRIO DE LOUVOR (Bloco de Cores) -->
      <section id="tab-repertorio" class="hidden space-y-3">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-base font-extrabold text-slate-900">Repertório de Louvor</h2>
            <p class="text-xs text-slate-500">Faixas de cores oficiais da IBS</p>
          </div>
          <select id="worshipServiceSelector" onchange="renderSongsForService(this.value)" class="bg-blue-50 border border-blue-200 text-xs font-bold text-blue-800 rounded-lg px-2 py-1 outline-none">
            <!-- Preenchido via JS -->
          </select>
        </div>

        <div class="bg-amber-50 border border-amber-200 rounded-xl p-2.5 text-xs text-amber-900 flex items-start gap-2">
          <i class="fa-solid fa-circle-info text-amber-600 mt-0.5"></i>
          <span>Toque no botão de cifra ou reproduzir para estudar o arranjo e tom da música.</span>
        </div>

        <div class="space-y-2" id="songListContainer">
          <!-- Injetado dinamicamente -->
        </div>
      </section>

      <!-- ABA 4: PAINEL DA COORDENAÇÃO / PASTORAL (Visão de Liderança) -->
      <section id="tab-coordenacao" class="hidden space-y-3">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-base font-extrabold text-slate-900">Painel de Liderança</h2>
            <p class="text-xs text-slate-500">Mês ativo: <span id="leadMonthTitle" class="font-bold text-blue-700">Outubro 2026</span></p>
          </div>
          <div class="flex gap-1.5">
            <button onclick="openEditScaleModal(0)" class="bg-amber-500 hover:bg-amber-600 text-white text-[11px] font-bold px-2 py-1.5 rounded-lg flex items-center gap-1 shadow-sm">
              <i class="fa-solid fa-pen-to-square"></i> Escalar
            </button>
            <button onclick="sendWhatsAppReminders()" class="bg-emerald-600 hover:bg-emerald-700 text-white text-[11px] font-bold px-2 py-1.5 rounded-lg flex items-center gap-1 shadow-sm">
              <i class="fa-brands fa-whatsapp text-sm"></i> Avisar
            </button>
          </div>
        </div>

        <!-- Indicadores (Cards de Status) -->
        <div class="grid grid-cols-3 gap-2 text-center">
          <div class="bg-emerald-50 border border-emerald-200 rounded-xl p-2.5">
            <span id="kpiConfirmados" class="text-lg font-extrabold text-emerald-700">19</span>
            <span class="block text-[10px] text-emerald-800 font-semibold uppercase">Confirmados</span>
          </div>
          <div class="bg-amber-50 border border-amber-200 rounded-xl p-2.5">
            <span id="kpiPendentes" class="text-lg font-extrabold text-amber-700">2</span>
            <span class="block text-[10px] text-amber-800 font-semibold uppercase">Pendentes</span>
          </div>
          <div class="bg-rose-50 border border-rose-200 rounded-xl p-2.5">
            <span id="kpiDesfalques" class="text-lg font-extrabold text-rose-700">0</span>
            <span class="block text-[10px] text-rose-800 font-semibold uppercase">Desfalques</span>
          </div>
        </div>

        <!-- Gestão da Rotação de Equipes -->
        <div class="bg-white rounded-xl border border-slate-200 p-3 shadow-sm space-y-2">
          <h4 class="text-xs font-bold text-slate-800 flex items-center gap-1.5">
            <i class="fa-solid fa-users text-blue-600"></i> Rodízio de Equipes deste Mês
          </h4>
          <div id="teamRotationList" class="text-xs space-y-1.5">
            <!-- Injetado dinamicamente -->
          </div>
        </div>

        <!-- Checklist do Próximo Domingo -->
        <div class="bg-white rounded-xl border border-slate-200 p-3 shadow-sm space-y-2">
          <h4 class="text-xs font-bold text-slate-800">Checklist do 1º Culto do Mês</h4>
          <div id="leadChecklist" class="divide-y divide-slate-100 text-xs">
            <!-- Injetado dinamicamente -->
          </div>
        </div>
      </section>

    </main>

    <!-- Barra de Navegação Inferior (Bottom Navigation Bar) -->
    <nav class="bg-white border-t border-slate-200 flex justify-around items-center absolute bottom-0 w-full h-16 shadow-lg z-20">
      <button onclick="switchTab('meus-cultos')" id="nav-meus-cultos" class="flex-1 flex flex-col items-center justify-center py-1 text-blue-600 tab-active">
        <i class="fa-solid fa-user-check text-base"></i>
        <span class="text-[10px] font-bold mt-1">Meu Culto</span>
      </button>

      <button onclick="switchTab('escala-geral')" id="nav-escala-geral" class="flex-1 flex flex-col items-center justify-center py-1 text-slate-400 hover:text-slate-600">
        <i class="fa-solid fa-calendar-days text-base"></i>
        <span class="text-[10px] font-medium mt-1">Escala Geral</span>
      </button>

      <button onclick="switchTab('repertorio')" id="nav-repertorio" class="flex-1 flex flex-col items-center justify-center py-1 text-slate-400 hover:text-slate-600">
        <i class="fa-solid fa-music text-base"></i>
        <span class="text-[10px] font-medium mt-1">Músicas</span>
      </button>

      <button onclick="switchTab('coordenacao')" id="nav-coordenacao" class="flex-1 flex flex-col items-center justify-center py-1 text-slate-400 hover:text-slate-600">
        <i class="fa-solid fa-shield-halved text-base"></i>
        <span class="text-[10px] font-medium mt-1">Liderança</span>
      </button>
    </nav>

    <!-- ======================================================== -->
    <!-- MODAL PRINCIPAL: LANÇAR E EDITAR ESCALA DO CULTO -->
    <!-- ======================================================== -->
    <div id="editScaleModal" class="hidden absolute inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-end sm:items-center justify-center p-2 sm:p-3">
      <div class="bg-white rounded-2xl w-full p-4 space-y-3 shadow-2xl animate-fade-in max-h-[92vh] overflow-y-auto">
        
        <!-- Header do Modal -->
        <div class="flex items-center justify-between border-b pb-2">
          <div>
            <h3 class="text-sm font-extrabold text-slate-900 flex items-center gap-1.5">
              <i class="fa-solid fa-pen-to-square text-amber-500"></i> Lançar / Editar Escala
            </h3>
            <p class="text-[11px] text-slate-500">Atribua os voluntários para cada função</p>
          </div>
          <button onclick="closeEditScaleModal()" class="text-slate-400 hover:text-slate-600 text-sm p-1">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <!-- Seletor do Culto a Editar -->
        <div class="bg-blue-50/70 p-2.5 rounded-xl border border-blue-100 text-xs space-y-1">
          <label class="block font-bold text-blue-900">Selecione o Culto a Escalar:</label>
          <select id="scaleServiceSelector" onchange="loadServiceIntoEditor(this.value)" class="w-full bg-white text-slate-800 font-bold border border-blue-300 rounded-lg p-2 outline-none shadow-sm">
            <!-- Populado via JS -->
          </select>
        </div>

        <!-- Botões de Preenchimento Rápido por Equipe -->
        <div class="bg-slate-50 p-2 rounded-xl border border-slate-200 text-xs">
          <span class="text-[10px] uppercase font-bold text-slate-400 block mb-1">Preenchimento Rápido por Equipe Base:</span>
          <div class="grid grid-cols-3 gap-1.5">
            <button type="button" onclick="applyTeamTemplate('Equipe 01')" class="bg-white hover:bg-blue-50 text-blue-700 font-bold py-1.5 px-2 rounded-lg border border-blue-200 text-[11px] transition shadow-xs">
              ⚡ Equipe 01
            </button>
            <button type="button" onclick="applyTeamTemplate('Equipe 02')" class="bg-white hover:bg-blue-50 text-blue-700 font-bold py-1.5 px-2 rounded-lg border border-blue-200 text-[11px] transition shadow-xs">
              ⚡ Equipe 02
            </button>
            <button type="button" onclick="applyTeamTemplate('Equipe 03')" class="bg-white hover:bg-blue-50 text-blue-700 font-bold py-1.5 px-2 rounded-lg border border-blue-200 text-[11px] transition shadow-xs">
              ⚡ Equipe 03
            </button>
          </div>
        </div>

        <!-- Formulário Granular de Funções -->
        <form id="scaleEditorForm" onsubmit="handleSaveScale(event)" class="space-y-3 text-xs">
          
          <!-- SEÇÃO 1: PALAVRA / PÚLPITO -->
          <div class="border border-slate-200 rounded-xl p-2.5 bg-slate-50/50 space-y-2">
            <h4 class="font-extrabold text-slate-800 flex items-center gap-1 text-[11px] text-blue-800">
              <i class="fa-solid fa-book-bible"></i> Palavra & Liturgia
            </h4>
            <div class="grid grid-cols-2 gap-2">
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Ministrante / Preletor</label>
                <input type="text" id="editPreacher" placeholder="Ex: Pr. Flávio Amaral" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Texto Bíblico</label>
                <input type="text" id="editText" placeholder="Ex: Zacarias 4:10" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
            </div>
            <div>
              <label class="block font-semibold text-slate-600 text-[10px]">Tema da Mensagem</label>
              <input type="text" id="editTheme" placeholder="Ex: Comece onde você está" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
            </div>
          </div>

          <!-- SEÇÃO 2: LOUVOR E BANDA -->
          <div class="border border-slate-200 rounded-xl p-2.5 bg-slate-50/50 space-y-2">
            <h4 class="font-extrabold text-slate-800 flex items-center gap-1 text-[11px] text-indigo-800">
              <i class="fa-solid fa-music"></i> Louvor e Instrumentistas
            </h4>
            <div class="grid grid-cols-2 gap-2">
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Ministro(a) de Louvor</label>
                <input type="text" id="editMinister" placeholder="Ex: Manú" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Back-vocals</label>
                <input type="text" id="editBacks" placeholder="Ex: Karol, Kamynnsky" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
            </div>
            <div class="grid grid-cols-3 gap-1.5">
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Violão</label>
                <input type="text" id="editGuitar" placeholder="Ex: Bruno" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Teclado</label>
                <input type="text" id="editKeys" placeholder="Ex: Efrain" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Baixo</label>
                <input type="text" id="editBass" placeholder="Ex: Italo" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
            </div>
            <div>
              <label class="block font-semibold text-slate-600 text-[10px]">Bateria</label>
              <input type="text" id="editDrums" placeholder="Ex: Ícaro" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
            </div>
          </div>

          <!-- SEÇÃO 3: SHAMAH KIDS -->
          <div class="border border-slate-200 rounded-xl p-2.5 bg-slate-50/50 space-y-2">
            <h4 class="font-extrabold text-slate-800 flex items-center gap-1 text-[11px] text-rose-800">
              <i class="fa-solid fa-children"></i> Shamah Kids (Infantil)
            </h4>
            <div class="grid grid-cols-2 gap-2">
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Turma 01 (3 a 7 anos)</label>
                <input type="text" id="editKids1" placeholder="Ex: Ana Carolina e Mª Eduarda" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Turma 02 (8 a 11 anos)</label>
                <input type="text" id="editKids2" placeholder="Ex: Letícia e Ester" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
            </div>
          </div>

          <!-- SEÇÃO 4: MÍDIA E CABINE -->
          <div class="border border-slate-200 rounded-xl p-2.5 bg-slate-50/50 space-y-2">
            <h4 class="font-extrabold text-slate-800 flex items-center gap-1 text-[11px] text-amber-800">
              <i class="fa-solid fa-sliders"></i> Mídia, Som & Transmissão
            </h4>
            <div class="grid grid-cols-3 gap-1.5">
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Mesa de Som</label>
                <input type="text" id="editSound" placeholder="Ex: Felipe" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Projeção</label>
                <input type="text" id="editProj" placeholder="Ex: Jordana" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Transmissão</label>
                <input type="text" id="editStream" placeholder="Ex: Lorivaldo" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
            </div>
          </div>

          <!-- SEÇÃO 5: DIACONATO & LOGÍSTICA -->
          <div class="border border-slate-200 rounded-xl p-2.5 bg-slate-50/50 space-y-2">
            <h4 class="font-extrabold text-slate-800 flex items-center gap-1 text-[11px] text-emerald-800">
              <i class="fa-solid fa-door-open"></i> Diaconato, Acolhimento & Apoio
            </h4>
            <div class="grid grid-cols-2 gap-2">
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Acolhimento / Portaria</label>
                <input type="text" id="editAcolhimento" placeholder="Ex: Johnatan e Tatiana" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
              <div>
                <label class="block font-semibold text-slate-600 text-[10px]">Estacionamento / Nave</label>
                <input type="text" id="editEstacionamento" placeholder="Ex: Equipe 02" class="w-full bg-white border border-slate-300 rounded p-1.5 outline-none">
              </div>
            </div>
          </div>

          <!-- Botões de Ação -->
          <div class="flex gap-2 pt-2">
            <button type="submit" class="flex-1 bg-amber-500 hover:bg-amber-600 text-slate-900 font-extrabold py-3 rounded-xl text-xs shadow-md active:scale-95 transition">
              💾 Salvar Escala deste Culto
            </button>
            <button type="button" onclick="closeEditScaleModal()" class="bg-slate-100 hover:bg-slate-200 text-slate-600 font-semibold py-3 px-3 rounded-xl text-xs">
              Cancelar
            </button>
          </div>
        </form>

      </div>
    </div>

    <!-- MODAL 2: CADASTRAR NOVA PESSOA -->
    <div id="newPersonModal" class="hidden absolute inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-end sm:items-center justify-center p-3">
      <div class="bg-white rounded-2xl w-full p-4 space-y-3 shadow-2xl animate-fade-in max-h-[90vh] overflow-y-auto">
        <div class="flex items-center justify-between border-b pb-2">
          <h3 class="text-sm font-extrabold text-slate-900 flex items-center gap-1.5">
            <i class="fa-solid fa-user-plus text-blue-600"></i> Cadastrar Novo Voluntário
          </h3>
          <button onclick="closeNewPersonModal()" class="text-slate-400 hover:text-slate-600 text-sm">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <form id="newPersonForm" onsubmit="handleSavePerson(event)" class="space-y-2.5 text-xs">
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Nome Completo *</label>
            <input type="text" id="personNameInput" required placeholder="Ex: Gabriel Souza" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none focus:border-blue-500">
          </div>

          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block font-semibold text-slate-700 mb-1">WhatsApp / Celular</label>
              <input type="text" id="personPhoneInput" placeholder="(00) 90000-0000" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
            </div>
            <div>
              <label class="block font-semibold text-slate-700 mb-1">Equipe Base</label>
              <select id="personTeamInput" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
                <option value="Equipe 01">Equipe 01</option>
                <option value="Equipe 02">Equipe 02</option>
                <option value="Equipe 03">Equipe 03</option>
                <option value="Geral">Equipe Geral / Flutuante</option>
              </select>
            </div>
          </div>

          <div>
            <label class="block font-semibold text-slate-700 mb-1">Ministério Principal *</label>
            <select id="personDeptInput" required class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
              <option value="Ministério de Louvor">Ministério de Louvor</option>
              <option value="Shamah Kids">Shamah Kids (Infantil)</option>
              <option value="Diaconato & Logística">Diaconato & Logística</option>
              <option value="Mídia & Tecnologia">Mídia & Tecnologia</option>
              <option value="Liderança Pastoral">Liderança Pastoral</option>
            </select>
          </div>

          <div>
            <label class="block font-semibold text-slate-700 mb-1">Função / Instrumento Específico *</label>
            <input type="text" id="personRoleInput" required placeholder="Ex: Teclado, Canto, Turma 01, Projeção" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none focus:border-blue-500">
          </div>

          <div>
            <label class="block font-semibold text-slate-700 mb-1">Restrições / Observações</label>
            <input type="text" id="personNotesInput" placeholder="Ex: Só pode aos domingos à noite" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
          </div>

          <div class="flex gap-2 pt-2">
            <button type="submit" class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-xl text-xs shadow-md">
              Salvar Voluntário
            </button>
            <button type="button" onclick="closeNewPersonModal()" class="bg-slate-100 text-slate-600 font-semibold py-2.5 px-3 rounded-xl text-xs">
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- MODAL 3: CADASTRAR NOVO CULTO -->
    <div id="newCultoModal" class="hidden absolute inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-end sm:items-center justify-center p-3">
      <div class="bg-white rounded-2xl w-full p-4 space-y-3 shadow-2xl animate-fade-in max-h-[90vh] overflow-y-auto">
        <div class="flex items-center justify-between border-b pb-2">
          <h3 class="text-sm font-extrabold text-slate-900 flex items-center gap-1.5">
            <i class="fa-solid fa-calendar-plus text-emerald-600"></i> Cadastrar Novo Culto / Evento
          </h3>
          <button onclick="closeNewCultoModal()" class="text-slate-400 hover:text-slate-600 text-sm">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <form id="newCultoForm" onsubmit="handleSaveCulto(event)" class="space-y-2.5 text-xs">
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block font-semibold text-slate-700 mb-1">Mês de Referência *</label>
              <select id="cultoMonthInput" required class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
                <option value="Jan">Janeiro</option>
                <option value="Fev">Fevereiro</option>
                <option value="Mar">Março</option>
                <option value="Abr">Abril</option>
                <option value="Mai">Maio</option>
                <option value="Jun">Junho</option>
                <option value="Jul">Julho</option>
                <option value="Ago">Agosto</option>
                <option value="Set">Setembro</option>
                <option value="Out" selected>Outubro</option>
                <option value="Nov">Novembro</option>
                <option value="Dez">Dezembro</option>
              </select>
            </div>
            <div>
              <label class="block font-semibold text-slate-700 mb-1">Data do Culto *</label>
              <input type="date" id="cultoDateInput" required class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
            </div>
          </div>

          <div>
            <label class="block font-semibold text-slate-700 mb-1">Nome / Tipo da Celebração *</label>
            <input type="text" id="cultoTitleInput" required placeholder="Ex: Culto de Celebração FAMÍLIA ou Vigília" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none focus:border-blue-500">
          </div>

          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block font-semibold text-slate-700 mb-1">Equipe Escalada</label>
              <select id="cultoTeamInput" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
                <option value="Equipe 01">Equipe 01</option>
                <option value="Equipe 02">Equipe 02</option>
                <option value="Equipe 03">Equipe 03</option>
                <option value="Equipe Especial">Equipe Especial / Geral</option>
              </select>
            </div>
            <div>
              <label class="block font-semibold text-slate-700 mb-1">Horário</label>
              <input type="text" id="cultoTimeInput" value="18:00" placeholder="18:00 ou 19:30" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
            </div>
          </div>

          <div>
            <label class="block font-semibold text-slate-700 mb-1">Preletor / Ministrante da Palavra</label>
            <input type="text" id="cultoPreacherInput" placeholder="Ex: Pr. Flávio Amaral" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
          </div>

          <div>
            <label class="block font-semibold text-slate-700 mb-1">Tema da Mensagem</label>
            <input type="text" id="cultoThemeInput" placeholder="Ex: O Poder da Aliança" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
          </div>

          <div>
            <label class="block font-semibold text-slate-700 mb-1">Louvor / Banda</label>
            <input type="text" id="cultoWorshipInput" placeholder="Ex: Manú (Ministro) • Bruno (Violão) • Ícaro (Bateria)" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
          </div>

          <div class="flex gap-2 pt-2">
            <button type="submit" class="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-2.5 rounded-xl text-xs shadow-md">
              Salvar Culto na Escala
            </button>
            <button type="button" onclick="closeNewCultoModal()" class="bg-slate-100 text-slate-600 font-semibold py-2.5 px-3 rounded-xl text-xs">
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal de Troca -->
    <div id="swapModal" class="hidden absolute inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-end sm:items-center justify-center p-3">
      <div class="bg-white rounded-2xl w-full p-4 space-y-3 shadow-2xl animate-fade-in">
        <div class="flex items-center justify-between border-b pb-2">
          <h3 class="text-sm font-extrabold text-slate-900 flex items-center gap-1.5">
            <i class="fa-solid fa-arrows-rotate text-blue-600"></i> Pedir Substituição de Escala
          </h3>
          <button onclick="closeSwapModal()" class="text-slate-400 hover:text-slate-600 text-sm">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <div class="space-y-2 text-xs">
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Qual o motivo da ausência?</label>
            <select class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
              <option>Viagem programada</option>
              <option>Compromisso de trabalho / estudo</option>
              <option>Saúde / Motivo pessoal</option>
              <option>Outro</option>
            </select>
          </div>

          <div>
            <label class="block font-semibold text-slate-700 mb-1">Deseja sugerir alguém para cobrir?</label>
            <select id="swapCandidateSelect" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 outline-none">
              <!-- Preenchido dinamicamente -->
            </select>
          </div>
        </div>

        <div class="flex gap-2 pt-2">
          <button onclick="submitSwapRequest()" class="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-xl text-xs shadow-md">
            Enviar Pedido de Troca
          </button>
          <button onclick="closeSwapModal()" class="bg-slate-100 text-slate-600 font-semibold py-2.5 px-3 rounded-xl text-xs">
            Cancelar
          </button>
        </div>
      </div>
    </div>

  </div>

  <script>
    // DADOS INICIAIS
    const DEFAULT_SERVICES = __DATA_JSON__;
    const DEFAULT_VOLUNTEERS = __VOLUNTEERS_JSON__;
    const TEAM_TEMPLATES = __TEAM_TEMPLATES_JSON__;

    let ALL_SERVICES = DEFAULT_SERVICES;
    try {
      const stored = JSON.parse(localStorage.getItem('ibs_services_v3'));
      if (stored && stored['Out'] && stored['Out'].length > 0) {
        ALL_SERVICES = stored;
      }
    } catch(e) {
      ALL_SERVICES = DEFAULT_SERVICES;
    }

    let VOLUNTEERS = DEFAULT_VOLUNTEERS;
    try {
      const storedV = JSON.parse(localStorage.getItem('ibs_volunteers_v3'));
      if (storedV && Object.keys(storedV).length > 0) {
        VOLUNTEERS = storedV;
      }
    } catch(e) {
      VOLUNTEERS = DEFAULT_VOLUNTEERS;
    }

    const MONTH_NAMES = {
      'Jan': 'Janeiro', 'Fev': 'Fevereiro', 'Mar': 'Março', 'Abr': 'Abril',
      'Mai': 'Maio', 'Jun': 'Junho', 'Jul': 'Julho', 'Ago': 'Agosto',
      'Set': 'Setembro', 'Out': 'Outubro', 'Nov': 'Novembro', 'Dez': 'Dezembro'
    };

    let currentUserId = 'bruno';
    let currentMonth = 'Out';
    let editingServiceIndex = 0;

    function initUserDropdown() {
      const sel = document.getElementById('userSelector');
      sel.innerHTML = '';
      Object.keys(VOLUNTEERS).forEach(k => {
        const v = VOLUNTEERS[k];
        const opt = document.createElement('option');
        opt.value = k;
        opt.innerText = v.name + ' (' + v.dept + ')';
        if (k === currentUserId) opt.selected = true;
        sel.appendChild(opt);
      });
    }

    function onMonthChange(monthKey) {
      currentMonth = monthKey;
      const mName = MONTH_NAMES[monthKey] || monthKey;
      document.getElementById('currentMonthBadge').innerText = mName.toUpperCase();
      document.getElementById('monthNameLabel').innerText = mName;
      document.getElementById('generalMonthTitle').innerText = mName + ' 2026';
      document.getElementById('leadMonthTitle').innerText = mName + ' 2026';

      updateUserView();
      renderGeneralMonth();
      updateWorshipSelector();
      updateLeadershipView();
    }

    function changeUser(userId) {
      currentUserId = userId;
      const v = VOLUNTEERS[userId];
      document.getElementById('userName').innerText = v.name;
      document.getElementById('userAvatar').innerText = v.initials;
      document.getElementById('userRoleBadge').innerText = v.role;

      updateUserView();
    }

    function updateUserView() {
      const vName = VOLUNTEERS[currentUserId].name.toLowerCase();
      const services = ALL_SERVICES[currentMonth] || [];

      const userServices = [];
      services.forEach(s => {
        const txt = (s.preacher || '') + ' ' + (s.worship || '') + ' ' + (s.kids || '') + ' ' + (s.media || '') + ' ' + (s.diaconia || '');
        const txtLower = txt.toLowerCase();
        if (txtLower.includes(vName) || (currentUserId === 'pastor' && txtLower.includes('flávio'))) {
          userServices.push(s);
        }
      });

      const count = userServices.length;
      document.getElementById('serviceCountBadge').innerText = count + ' escala' + (count === 1 ? '' : 's');
      resetConfirmation();

      if (count > 0) {
        const next = userServices[0];
        document.getElementById('nextServiceCard').classList.remove('hidden');
        document.getElementById('serviceTitle').innerText = next.title;
        document.getElementById('serviceTheme').innerText = next.theme ? 'Tema: ' + next.theme : 'Culto regular';
        document.getElementById('serviceDateTime').innerHTML = '<i class="fa-regular fa-calendar text-blue-600"></i> ' + next.date;
        document.getElementById('serviceFunction').innerHTML = '<i class="fa-solid fa-circle-check text-blue-600"></i> ' + VOLUNTEERS[currentUserId].role;

        const container = document.getElementById('futureServicesList');
        container.innerHTML = '';
        userServices.forEach((s, idx) => {
          const el = document.createElement('div');
          el.className = 'bg-white p-2.5 rounded-xl border border-slate-200 flex items-center justify-between text-xs shadow-sm';
          const badgeClass = idx === 0 ? 'text-amber-700 bg-amber-50 border border-amber-200' : 'text-slate-400 bg-slate-100';
          const badgeText = idx === 0 ? 'Próximo' : 'Confirmado';
          el.innerHTML = '<div><span class="font-bold text-slate-800">' + s.date + '</span> • <span class="text-slate-600">' + s.title + '</span><p class="text-[11px] text-blue-600 font-medium">' + VOLUNTEERS[currentUserId].role + '</p></div><span class="text-[10px] ' + badgeClass + ' px-2 py-0.5 rounded font-medium">' + badgeText + '</span>';
          container.appendChild(el);
        });
      } else {
        const mName = MONTH_NAMES[currentMonth] || currentMonth;
        document.getElementById('serviceTitle').innerText = 'Sem escalas em ' + mName;
        document.getElementById('serviceTheme').innerText = 'Você não possui cultos agendados neste mês.';
        document.getElementById('serviceDateTime').innerText = '--/--';
        document.getElementById('serviceFunction').innerText = 'Folga programada';
        document.getElementById('futureServicesList').innerHTML = '<div class="p-3 bg-slate-50 text-slate-500 rounded-xl text-center text-xs">Nenhuma escala atribuída para ' + VOLUNTEERS[currentUserId].name + ' em ' + mName + '.</div>';
      }
    }

    function renderGeneralMonth() {
      const services = ALL_SERVICES[currentMonth] || [];
      const container = document.getElementById('monthServicesAccordion');
      container.innerHTML = '';

      if (services.length === 0) {
        container.innerHTML = '<div class="p-4 bg-slate-50 text-slate-500 rounded-xl text-center text-xs">Nenhum culto cadastrado para este mês ainda.<button onclick="openNewCultoModal()" class="mt-2 block mx-auto text-blue-600 font-bold underline">+ Cadastrar 1º Culto</button></div>';
        return;
      }

      services.forEach((s, idx) => {
        const card = document.createElement('div');
        card.className = 'bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm';
        
        let preacherHtml = '';
        if (s.preacher) {
          preacherHtml = '<div><span class="text-[10px] uppercase font-bold text-slate-400 block">Palavra & Tema</span><p class="text-slate-800 font-bold">Ministrante: ' + s.preacher + '</p>' + (s.theme ? '<p class="text-slate-600 italic text-[11px]">' + s.theme + '</p>' : '') + (s.text ? '<p class="text-slate-400 text-[10px]">Texto: ' + s.text + '</p>' : '') + '</div>';
        }

        let diaconiaHtml = '';
        if (s.diaconia) {
          diaconiaHtml = '<div class="pt-1 border-t border-slate-100"><span class="text-[10px] uppercase font-bold text-slate-400 block">Diaconato & Acolhimento</span><p class="text-[11px] text-slate-700">' + s.diaconia + '</p></div>';
        }

        const teamTag = s.team ? '<span class="text-[10px] font-bold bg-blue-100 text-blue-800 px-1.5 py-0.2 rounded">' + s.team + '</span>' : '';
        const hiddenClass = idx === 0 ? '' : 'hidden';

        card.innerHTML = '<div class="p-3 bg-slate-50/80 flex items-center justify-between"><div onclick="toggleAccordion(\\'acc-' + idx + '\\')" class="cursor-pointer flex-1"><div class="flex items-center gap-1.5"><span class="text-xs font-extrabold text-blue-700">' + s.date + '</span>' + teamTag + '</div><h4 class="text-xs font-bold text-slate-800 leading-tight mt-0.5">' + s.title + '</h4></div><div class="flex items-center gap-2"><button onclick="openEditScaleModal(' + idx + ')" class="text-[11px] font-bold text-amber-700 bg-amber-50 hover:bg-amber-100 border border-amber-200 px-2 py-1 rounded-lg flex items-center gap-1 shadow-2xs transition" title="Editar Escala deste Culto"><i class="fa-solid fa-pen-to-square text-[10px]"></i> Escalar</button><i onclick="toggleAccordion(\\'acc-' + idx + '\\')" class="fa-solid fa-chevron-down text-xs text-slate-400 cursor-pointer p-1"></i></div></div><div id="acc-' + idx + '" class="p-3 text-xs space-y-2 border-t border-slate-100 ' + hiddenClass + '">' + preacherHtml + '<div class="pt-1 border-t border-slate-100"><span class="text-[10px] uppercase font-bold text-slate-400 block">Louvor</span><p class="text-[11px] text-slate-700">' + s.worship + '</p></div><div class="grid grid-cols-2 gap-2 pt-1 border-t border-slate-100"><div><span class="text-[10px] uppercase font-bold text-slate-400 block">Shamah Kids</span><p class="text-[11px] text-slate-700">' + s.kids + '</p></div><div><span class="text-[10px] uppercase font-bold text-slate-400 block">Mídia & Cabine</span><p class="text-[11px] text-slate-700">' + s.media + '</p></div></div>' + diaconiaHtml + '<div class="pt-2 border-t border-slate-100 flex justify-end"><button onclick="openEditScaleModal(' + idx + ')" class="text-xs font-bold text-blue-700 hover:text-blue-900 flex items-center gap-1"><i class="fa-solid fa-pen-to-square"></i> Editar Escala Completa</button></div></div>';
        
        container.appendChild(card);
      });
    }

    function toggleAccordion(id) {
      const el = document.getElementById(id);
      if (el) el.classList.toggle('hidden');
    }

    function updateWorshipSelector() {
      const services = ALL_SERVICES[currentMonth] || [];
      const sel = document.getElementById('worshipServiceSelector');
      sel.innerHTML = '';
      services.forEach((s, idx) => {
        if (s.songs && s.songs.length > 0) {
          const opt = document.createElement('option');
          opt.value = idx;
          opt.innerText = s.date + ' - ' + s.title;
          sel.appendChild(opt);
        }
      });
      if (sel.options.length > 0) {
        renderSongsForService(sel.options[0].value);
      } else {
        document.getElementById('songListContainer').innerHTML = '<div class="p-4 bg-slate-50 text-slate-500 rounded-xl text-center text-xs">Nenhum repertório de músicas detalhado registrado para este mês.</div>';
      }
    }

    function renderSongsForService(svcIdx) {
      const services = ALL_SERVICES[currentMonth] || [];
      const s = services[svcIdx];
      const container = document.getElementById('songListContainer');
      container.innerHTML = '';

      if (!s || !s.songs || s.songs.length === 0) {
        container.innerHTML = '<div class="p-3 text-center text-xs text-slate-400">Repertório a definir</div>';
        return;
      }

      s.songs.forEach(song => {
        const item = document.createElement('div');
        item.className = 'bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between';
        item.innerHTML = '<div class="flex items-center space-x-2.5"><span class="badge-' + song.color + ' text-[10px] font-extrabold px-2 py-0.5 rounded-md">' + song.badge + '</span><div><h4 class="text-xs font-bold text-slate-800">' + song.title + '</h4><p class="text-[10px] text-slate-400">Arranjo Oficial IBS</p></div></div><div class="flex gap-1.5"><button class="w-8 h-8 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 flex items-center justify-center text-xs" title="Ouvir"><i class="fa-solid fa-play"></i></button><button class="w-8 h-8 rounded-lg bg-blue-50 hover:bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold" title="Cifra"><i class="fa-solid fa-file-lines"></i></button></div>';
        container.appendChild(item);
      });
    }

    function updateLeadershipView() {
      const services = ALL_SERVICES[currentMonth] || [];
      const rotationContainer = document.getElementById('teamRotationList');
      rotationContainer.innerHTML = '';

      const sundays = services.filter(s => (s.weekday || '').toLowerCase().includes('domingo'));
      sundays.forEach((s, sIdx) => {
        const originalIdx = services.indexOf(s);
        const el = document.createElement('div');
        el.className = 'flex items-center justify-between bg-slate-50 p-2 rounded-lg';
        el.innerHTML = '<div class="flex-1"><span class="font-bold text-slate-700">' + s.date + '</span><span class="text-slate-500 block text-[11px]">' + s.title + '</span></div><div class="flex items-center gap-1.5"><span class="font-extrabold text-blue-700 bg-blue-100 px-2 py-0.5 rounded text-[11px]">' + (s.team || 'Equipe Geral') + '</span><button onclick="openEditScaleModal(' + originalIdx + ')" class="text-[10px] bg-white border border-slate-300 px-1.5 py-0.5 rounded hover:bg-slate-100 font-semibold" title="Editar"><i class="fa-solid fa-pen"></i></button></div>';
        rotationContainer.appendChild(el);
      });

      const checklist = document.getElementById('leadChecklist');
      checklist.innerHTML = '';
      if (services.length > 0) {
        const first = services[0];
        checklist.innerHTML = '<div class="py-2 flex items-center justify-between"><div><span class="font-bold text-slate-700">' + first.date + ' - Louvor</span><p class="text-[10px] text-slate-400">' + first.worship + '</p></div><span class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">Completo</span></div><div class="py-2 flex items-center justify-between"><div><span class="font-bold text-slate-700">Shamah Kids</span><p class="text-[10px] text-slate-400">' + first.kids + '</p></div><span class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">Escalado</span></div><div class="py-2 flex items-center justify-between"><div><span class="font-bold text-slate-700">Mídia e Som</span><p class="text-[10px] text-slate-400">' + first.media + '</p></div><span class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">Confirmado</span></div>';
      }
    }

    // =========================================================
    // LANÇAR / EDITAR ESCALA DO CULTO
    // =========================================================
    function openEditScaleModal(svcIdx) {
      const services = ALL_SERVICES[currentMonth] || [];
      if (services.length === 0) {
        alert('Nenhum culto cadastrado neste mês para escalar. Crie um culto primeiro em +Culto.');
        return;
      }

      editingServiceIndex = svcIdx || 0;
      if (editingServiceIndex >= services.length) editingServiceIndex = 0;

      // Popular dropdown de cultos do mês
      const sel = document.getElementById('scaleServiceSelector');
      sel.innerHTML = '';
      services.forEach((s, idx) => {
        const opt = document.createElement('option');
        opt.value = idx;
        opt.innerText = s.date + ' - ' + s.title;
        if (idx === editingServiceIndex) opt.selected = true;
        sel.appendChild(opt);
      });

      loadServiceIntoEditor(editingServiceIndex);
      document.getElementById('editScaleModal').classList.remove('hidden');
    }

    function closeEditScaleModal() {
      document.getElementById('editScaleModal').classList.add('hidden');
    }

    function loadServiceIntoEditor(svcIdx) {
      editingServiceIndex = parseInt(svcIdx);
      const services = ALL_SERVICES[currentMonth] || [];
      const s = services[editingServiceIndex];
      if (!s) return;

      const d = s.details || {};

      document.getElementById('editPreacher').value = d.preacher || s.preacher || '';
      document.getElementById('editTheme').value = d.theme || s.theme || '';
      document.getElementById('editText').value = d.text || s.text || '';

      document.getElementById('editMinister').value = d.minister || '';
      const backs = [d.back1, d.back2].filter(b => b && b !== '-').join(', ');
      document.getElementById('editBacks').value = backs;
      document.getElementById('editGuitar').value = d.guitar_ac || '';
      document.getElementById('editKeys').value = d.keys || '';
      document.getElementById('editBass').value = d.bass || '';
      document.getElementById('editDrums').value = d.drums || 'Ícaro';

      document.getElementById('editKids1').value = d.kids1 || '';
      document.getElementById('editKids2').value = d.kids2 || '';

      document.getElementById('editSound').value = d.sound || '';
      document.getElementById('editProj').value = d.proj || '';
      document.getElementById('editStream').value = d.stream || 'Lorivaldo';

      document.getElementById('editAcolhimento').value = d.acolhimento || '';
      document.getElementById('editEstacionamento').value = d.estacionamento || s.team || '';
    }

    function applyTeamTemplate(teamKey) {
      const t = TEAM_TEMPLATES[teamKey];
      if (!t) return;

      document.getElementById('editAcolhimento').value = t.acolhimento;
      document.getElementById('editEstacionamento').value = t.estacionamento;
      document.getElementById('editKids1').value = t.kids1;
      document.getElementById('editKids2').value = t.kids2;
      document.getElementById('editSound').value = t.sound;
      document.getElementById('editProj').value = t.proj;
      document.getElementById('editStream').value = t.stream;
      document.getElementById('editMinister').value = t.minister;
      document.getElementById('editBacks').value = [t.back1, t.back2].filter(Boolean).join(', ');
      document.getElementById('editGuitar').value = t.guitar_ac;
      document.getElementById('editKeys').value = t.keys;
      document.getElementById('editBass').value = t.bass;
      document.getElementById('editDrums').value = t.drums;

      alert('Base da ' + teamKey + ' aplicada com sucesso! Você pode editar campos específicos agora.');
    }

    function handleSaveScale(e) {
      e.preventDefault();
      const services = ALL_SERVICES[currentMonth] || [];
      const s = services[editingServiceIndex];
      if (!s) return;

      const preacher = document.getElementById('editPreacher').value.trim();
      const theme = document.getElementById('editTheme').value.trim();
      const text = document.getElementById('editText').value.trim();

      const minister = document.getElementById('editMinister').value.trim();
      const backs = document.getElementById('editBacks').value.trim();
      const guitar = document.getElementById('editGuitar').value.trim();
      const keys = document.getElementById('editKeys').value.trim();
      const bass = document.getElementById('editBass').value.trim();
      const drums = document.getElementById('editDrums').value.trim();

      const kids1 = document.getElementById('editKids1').value.trim();
      const kids2 = document.getElementById('editKids2').value.trim();

      const sound = document.getElementById('editSound').value.trim();
      const proj = document.getElementById('editProj').value.trim();
      const stream = document.getElementById('editStream').value.trim();

      const acolhimento = document.getElementById('editAcolhimento').value.trim();
      const estacionamento = document.getElementById('editEstacionamento').value.trim();

      // Atualizar objeto s
      s.preacher = preacher;
      s.theme = theme;
      s.text = text;

      // Reconstruir strings visuais
      const wParts = [];
      if (minister) wParts.push(minister + ' (Ministro)');
      if (backs) wParts.push(backs + ' (Back)');
      if (guitar) wParts.push(guitar + ' (Violão)');
      if (keys) wParts.push(keys + ' (Teclado)');
      if (bass) wParts.push(bass + ' (Baixo)');
      if (drums) wParts.push(drums + ' (Bateria)');
      s.worship = wParts.join(' • ') || 'A definir';

      const kParts = [];
      if (kids1) kParts.push('T1: ' + kids1);
      if (kids2) kParts.push('T2: ' + kids2);
      s.kids = kParts.join(' • ') || 'A definir';

      const mParts = [];
      if (sound) mParts.push('Som: ' + sound);
      if (proj) mParts.push('Proj: ' + proj);
      if (stream) mParts.push('Transm: ' + stream);
      s.media = mParts.join(' • ') || 'A definir';

      const dParts = [];
      if (acolhimento) dParts.push('Acolhimento: ' + acolhimento);
      if (estacionamento) dParts.push('Estacionamento: ' + estacionamento);
      s.diaconia = dParts.join(' • ') || '';

      // Atualizar details granulares
      s.details = {
        preacher: preacher,
        theme: theme,
        text: text,
        minister: minister,
        back1: backs.split(',')[0] ? backs.split(',')[0].trim() : '',
        back2: backs.split(',')[1] ? backs.split(',')[1].trim() : '',
        guitar_ac: guitar,
        keys: keys,
        bass: bass,
        drums: drums,
        kids1: kids1,
        kids2: kids2,
        sound: sound,
        proj: proj,
        stream: stream,
        acolhimento: acolhimento,
        estacionamento: estacionamento
      };

      try {
        localStorage.setItem('ibs_services_v3', JSON.stringify(ALL_SERVICES));
      } catch(err) {}

      closeEditScaleModal();
      renderGeneralMonth();
      updateUserView();
      updateLeadershipView();
      alert('Escala do culto "' + s.title + '" atualizada e salva com sucesso!');
    }

    // CADASTROS PESSOA E CULTO
    function openNewPersonModal() {
      document.getElementById('newPersonModal').classList.remove('hidden');
    }
    function closeNewPersonModal() {
      document.getElementById('newPersonModal').classList.add('hidden');
      document.getElementById('newPersonForm').reset();
    }
    function handleSavePerson(e) {
      e.preventDefault();
      const name = document.getElementById('personNameInput').value.trim();
      const phone = document.getElementById('personPhoneInput').value.trim();
      const team = document.getElementById('personTeamInput').value;
      const dept = document.getElementById('personDeptInput').value;
      const role = document.getElementById('personRoleInput').value.trim();

      const id = name.toLowerCase().replace(/[^a-z0-9]/g, '_');
      const initials = name.split(' ').map(p => p[0]).join('').substring(0, 2).toUpperCase();

      VOLUNTEERS[id] = {
        name: name,
        role: dept + ' - ' + role,
        dept: dept,
        team: team,
        phone: phone,
        initials: initials
      };

      try {
        localStorage.setItem('ibs_volunteers_v3', JSON.stringify(VOLUNTEERS));
      } catch(err) {}

      initUserDropdown();
      changeUser(id);
      closeNewPersonModal();
      alert('Voluntário(a) "' + name + '" cadastrado(a) com sucesso! Já foi selecionado(a) na simulação.');
    }

    function openNewCultoModal() {
      document.getElementById('newCultoModal').classList.remove('hidden');
      document.getElementById('cultoMonthInput').value = currentMonth;
    }
    function closeNewCultoModal() {
      document.getElementById('newCultoModal').classList.add('hidden');
      document.getElementById('newCultoForm').reset();
    }
    function handleSaveCulto(e) {
      e.preventDefault();
      const month = document.getElementById('cultoMonthInput').value;
      const dateRaw = document.getElementById('cultoDateInput').value;
      const title = document.getElementById('cultoTitleInput').value.trim();
      const team = document.getElementById('cultoTeamInput').value;
      const time = document.getElementById('cultoTimeInput').value.trim() || '18:00';
      const preacher = document.getElementById('cultoPreacherInput').value.trim() || 'Pr. Flávio Amaral';
      const theme = document.getElementById('cultoThemeInput').value.trim() || 'Celebração Especial';
      const worship = document.getElementById('cultoWorshipInput').value.trim() || 'Banda IBS';

      if (!dateRaw) return;
      const parts = dateRaw.split('-');
      const dtFormatted = parts[2] + '/' + parts[1] + '/' + parts[0];
      const dateObj = new Date(parts[0], parseInt(parts[1]) - 1, parts[2]);
      const weekdays = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'];
      const weekdayName = weekdays[dateObj.getDay()];

      if (!ALL_SERVICES[month]) {
        ALL_SERVICES[month] = [];
      }

      ALL_SERVICES[month].push({
        date: weekdayName + ', ' + dtFormatted + ' • ' + time,
        date_raw: dateRaw,
        weekday: weekdayName,
        title: title,
        team: team,
        preacher: preacher,
        theme: theme,
        text: 'A definir',
        worship: worship,
        kids: 'Equipe Shamah Kids',
        media: 'Felipe (Som) • Lorivaldo (Mídia)',
        diaconia: 'Equipe de Acolhimento',
        details: {
          preacher: preacher,
          theme: theme,
          text: 'A definir',
          minister: worship.split('•')[0] ? worship.split('•')[0].trim() : '',
          sound: 'Felipe',
          proj: 'Lorivaldo',
          stream: 'Lorivaldo',
          acolhimento: 'Equipe de Acolhimento',
          estacionamento: team
        },
        songs: []
      });

      try {
        localStorage.setItem('ibs_services_v3', JSON.stringify(ALL_SERVICES));
      } catch(err) {}

      document.getElementById('globalMonthSelector').value = month;
      onMonthChange(month);
      closeNewCultoModal();
      alert('Culto "' + title + '" cadastrado com sucesso para ' + weekdayName + ', ' + dtFormatted + '!');
    }

    function switchTab(tabId) {
      ['meus-cultos', 'escala-geral', 'repertorio', 'coordenacao'].forEach(t => {
        const el = document.getElementById('tab-' + t);
        const btn = document.getElementById('nav-' + t);
        if (t === tabId) {
          el.classList.remove('hidden');
          btn.classList.add('text-blue-600', 'tab-active');
          btn.classList.remove('text-slate-400');
        } else {
          el.classList.add('hidden');
          btn.classList.remove('text-blue-600', 'tab-active');
          btn.classList.add('text-slate-400');
        }
      });
    }

    function confirmPresence() {
      document.getElementById('actionButtons').classList.add('hidden');
      document.getElementById('confirmedFeedback').classList.remove('hidden');
      const tag = document.getElementById('statusTag');
      tag.className = 'text-xs font-semibold text-emerald-800 bg-emerald-50 border border-emerald-300 px-2.5 py-0.5 rounded-full flex items-center gap-1';
      tag.innerHTML = '<i class="fa-solid fa-circle-check text-emerald-600 text-[10px]"></i> Presença Confirmada';
    }

    function resetConfirmation() {
      document.getElementById('actionButtons').classList.remove('hidden');
      document.getElementById('confirmedFeedback').classList.add('hidden');
      const tag = document.getElementById('statusTag');
      tag.className = 'text-xs font-semibold text-amber-700 bg-amber-50 border border-amber-200 px-2.5 py-0.5 rounded-full flex items-center gap-1';
      tag.innerHTML = '<i class="fa-solid fa-clock text-[10px]"></i> Aguardando Confirmação';
    }

    function openSwapModal() {
      const sel = document.getElementById('swapCandidateSelect');
      sel.innerHTML = '';
      Object.keys(VOLUNTEERS).forEach(k => {
        if (k !== currentUserId) {
          const opt = document.createElement('option');
          opt.value = k;
          opt.innerText = VOLUNTEERS[k].name + ' (' + VOLUNTEERS[k].role + ')';
          sel.appendChild(opt);
        }
      });
      document.getElementById('swapModal').classList.remove('hidden');
    }

    function closeSwapModal() {
      document.getElementById('swapModal').classList.add('hidden');
    }

    function submitSwapRequest() {
      closeSwapModal();
      alert('Pedido de substituição enviado com sucesso para a coordenação!');
      const tag = document.getElementById('statusTag');
      tag.className = 'text-xs font-semibold text-rose-700 bg-rose-50 border border-rose-200 px-2.5 py-0.5 rounded-full flex items-center gap-1';
      tag.innerHTML = '<i class="fa-solid fa-arrows-rotate text-[10px]"></i> Substituição Solicitada';
    }

    function sendWhatsAppReminders() {
      const mName = MONTH_NAMES[currentMonth] || currentMonth;
      alert('Disparando lembrete automático via WhatsApp para os voluntários pendentes de ' + mName + '!');
    }

    // Inicialização
    initUserDropdown();
    onMonthChange('Out');
    changeUser('bruno');
  </script>
</body>
</html>
"""

html_final = template.replace('__DATA_JSON__', data_json_str).replace('__USER_SCHEDULES_JSON__', user_schedules_json_str).replace('__VOLUNTEERS_JSON__', volunteers_map_json_str).replace('__TEAM_TEMPLATES_JSON__', team_templates_json_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_final)

with open(r'C:\Users\sigma\.gemini\antigravity\brain\abfefb37-5e54-4455-bf09-7a27be839382\app_demo.html', 'w', encoding='utf-8') as f:
    f.write(html_final)

print("index.html e app_demo.html atualizados com o editor e lançador completo de escalas!")
