import json

with open('all_services.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

# Base volunteers map
volunteers_map = {
    'bruno': {'name': 'Bruno', 'role': 'Louvor - Violão / Ministro', 'dept': 'Ministério de Louvor', 'initials': 'BR'},
    'leandro': {'name': 'Leandro', 'role': 'Diaconato - Acolhimento / Portaria', 'dept': 'Diaconato & Logística', 'initials': 'LE'},
    'ana_carolina': {'name': 'Ana Carolina', 'role': 'Coordenação Shamah Kid\'s', 'dept': 'Shamah Kid\'s', 'initials': 'AC'},
    'felipe': {'name': 'Felipe', 'role': 'Mesa de Som e Iluminação', 'dept': 'Mídia & Tecnologia', 'initials': 'FE'},
    'pastor': {'name': 'Pr. Flávio Amaral', 'role': 'Direção Geral & Ministrante', 'dept': 'Liderança Pastoral', 'initials': 'PF'},
    'manu': {'name': 'Manú', 'role': 'Ministra de Louvor', 'dept': 'Ministério de Louvor', 'initials': 'MN'},
    'karol': {'name': 'Karol', 'role': 'Mídia Social / Back-vocal', 'dept': 'Mídia / Louvor', 'initials': 'KR'},
    'efrain': {'name': 'Efrain', 'role': 'Coord. Louvor & Teclado', 'dept': 'Ministério de Louvor', 'initials': 'EF'},
    'icaro': {'name': 'Ícaro', 'role': 'Bateria', 'dept': 'Ministério de Louvor', 'initials': 'IC'},
    'leticia': {'name': 'Letícia', 'role': 'Shamah Kid\'s & Intercessão', 'dept': 'Shamah Kid\'s', 'initials': 'LT'},
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
                    assigned_roles.append('Shamah Kid\'s')
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

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IBS Escala - Sistema e App Mobile</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    ::-webkit-scrollbar {{ width: 4px; height: 4px; }}
    ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 4px; }}
    .tab-active {{ color: #2563eb; border-top: 3px solid #2563eb; }}
    .badge-verde {{ background-color: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }}
    .badge-amarelo {{ background-color: #fef9c3; color: #a16207; border: 1px solid #fef08a; }}
    .badge-vermelho {{ background-color: #fee2e2; color: #b91c1c; border: 1px solid #fecaca; }}
    .badge-roxo {{ background-color: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }}
    .badge-azul {{ background-color: #dbeafe; color: #1d4ed8; border: 1px solid #bfdbfe; }}
  </style>
</head>
<body class="bg-slate-100 text-slate-800 antialiased font-sans min-h-screen flex flex-col items-center justify-start p-2 sm:p-4">

  <!-- Container do Smartphone Mockup -->
  <div class="w-full max-w-md bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col min-h-[820px] relative">
    
    <!-- Top Header do App -->
    <header class="bg-gradient-to-r from-blue-700 to-indigo-800 text-white p-4 pt-4 pb-3 shadow-md sticky top-0 z-20">
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
        <div class="flex items-center gap-1.5">
          <button onclick="openNewPersonModal()" class="bg-white/20 hover:bg-white/30 text-white text-[11px] font-bold px-2 py-1 rounded-lg border border-white/30 flex items-center gap-1 transition" title="Cadastrar Pessoa">
            <i class="fa-solid fa-user-plus text-[10px]"></i> +Pessoa
          </button>
          <button onclick="openNewCultoModal()" class="bg-emerald-500/80 hover:bg-emerald-600 text-white text-[11px] font-bold px-2 py-1 rounded-lg border border-emerald-400/40 flex items-center gap-1 transition" title="Cadastrar Culto">
            <i class="fa-solid fa-calendar-plus text-[10px]"></i> +Culto
          </button>
        </div>
      </div>

      <!-- Barra de Controle Duplo: Simular Como & Mês Ativo -->
      <div class="mt-3 grid grid-cols-2 gap-2 bg-black/20 p-2 rounded-xl backdrop-blur-sm border border-white/10 text-xs">
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

          <!-- Mensagem de Sucesso (Oculta por padrão) -->
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
          <button onclick="openNewCultoModal()" class="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-2.5 py-1.5 rounded-xl shadow-sm flex items-center gap-1.5 active:scale-95 transition">
            <i class="fa-solid fa-plus text-xs"></i> Adicionar Culto
          </button>
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
            <button onclick="openNewPersonModal()" class="bg-blue-600 hover:bg-blue-700 text-white text-[11px] font-bold px-2 py-1.5 rounded-lg flex items-center gap-1 shadow-sm">
              <i class="fa-solid fa-user-plus"></i> +Pessoa
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

    <!-- MODAL 1: CADASTRAR NOVA PESSOA -->
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

    <!-- MODAL 2: CADASTRAR NOVO CULTO -->
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
    // CARREGAR DADOS COM SUPORTE A LOCALSTORAGE
    const DEFAULT_SERVICES = {data_json_str};
    const DEFAULT_VOLUNTEERS = {volunteers_map_json_str};

    let ALL_SERVICES = DEFAULT_SERVICES;
    try {
      const stored = JSON.parse(localStorage.getItem('ibs_services_v2'));
      if (stored && stored['Out'] && stored['Out'].length > 0) {
        ALL_SERVICES = stored;
      }
    } catch(e) {
      ALL_SERVICES = DEFAULT_SERVICES;
    }

    let VOLUNTEERS = DEFAULT_VOLUNTEERS;
    try {
      const storedV = JSON.parse(localStorage.getItem('ibs_volunteers_v2'));
      if (storedV && Object.keys(storedV).length > 0) {
        VOLUNTEERS = storedV;
      }
    } catch(e) {
      VOLUNTEERS = DEFAULT_VOLUNTEERS;
    }
    let USER_SCHEDULES = {user_schedules_json_str};

    const MONTH_NAMES = {{
      'Jan': 'Janeiro', 'Fev': 'Fevereiro', 'Mar': 'Março', 'Abr': 'Abril',
      'Mai': 'Maio', 'Jun': 'Junho', 'Jul': 'Julho', 'Ago': 'Agosto',
      'Set': 'Setembro', 'Out': 'Outubro', 'Nov': 'Novembro', 'Dez': 'Dezembro'
    }};

    let currentUserId = 'bruno';
    let currentMonth = 'Out';

    // Inicializar dropdown de usuários
    function initUserDropdown() {{
      const sel = document.getElementById('userSelector');
      sel.innerHTML = '';
      Object.keys(VOLUNTEERS).forEach(k => {{
        const v = VOLUNTEERS[k];
        const opt = document.createElement('option');
        opt.value = k;
        opt.innerText = `${{v.name}} (${{v.dept}})`;
        if (k === currentUserId) opt.selected = true;
        sel.appendChild(opt);
      }});
    }}

    // Troca de Mês Global
    function onMonthChange(monthKey) {{
      currentMonth = monthKey;
      document.getElementById('currentMonthBadge').innerText = (MONTH_NAMES[monthKey] || monthKey).toUpperCase();
      document.getElementById('monthNameLabel').innerText = MONTH_NAMES[monthKey] || monthKey;
      document.getElementById('generalMonthTitle').innerText = `${{MONTH_NAMES[monthKey] || monthKey}} 2026`;
      document.getElementById('leadMonthTitle').innerText = `${{MONTH_NAMES[monthKey] || monthKey}} 2026`;

      updateUserView();
      renderGeneralMonth();
      updateWorshipSelector();
      updateLeadershipView();
    }}

    // Troca de Usuário Simulado
    function changeUser(userId) {{
      currentUserId = userId;
      const v = VOLUNTEERS[userId];
      document.getElementById('userName').innerText = v.name;
      document.getElementById('userAvatar').innerText = v.initials;
      document.getElementById('userRoleBadge').innerText = v.role;

      updateUserView();
    }}

    // Atualiza a tela 'Meu Culto'
    function updateUserView() {{
      const vName = VOLUNTEERS[currentUserId].name.toLowerCase();
      const services = ALL_SERVICES[currentMonth] || [];

      // Filtrar cultos do voluntário para o mês selecionado
      const userServices = [];
      services.forEach(s => {{
        const txt = `${{s.preacher || ''}} ${{s.worship || ''}} ${{s.kids || ''}} ${{s.media || ''}} ${{s.diaconia || ''}}`.toLowerCase();
        if (txt.includes(vName) || (currentUserId === 'pastor' && txt.includes('flávio'))) {{
          userServices.push(s);
        }}
      }});

      const count = userServices.length;
      document.getElementById('serviceCountBadge').innerText = `${{count}} escala${{count === 1 ? '' : 's'}}`;
      resetConfirmation();

      if (count > 0) {{
        const next = userServices[0];
        document.getElementById('nextServiceCard').classList.remove('hidden');
        document.getElementById('serviceTitle').innerText = next.title;
        document.getElementById('serviceTheme').innerText = next.theme ? `Tema: ${{next.theme}}` : 'Culto regular';
        document.getElementById('serviceDateTime').innerHTML = `<i class="fa-regular fa-calendar text-blue-600"></i> ${{next.date}}`;
        document.getElementById('serviceFunction').innerHTML = `<i class="fa-solid fa-circle-check text-blue-600"></i> ${{VOLUNTEERS[currentUserId].role}}`;

        const container = document.getElementById('futureServicesList');
        container.innerHTML = '';
        userServices.forEach((s, idx) => {{
          const el = document.createElement('div');
          el.className = 'bg-white p-2.5 rounded-xl border border-slate-200 flex items-center justify-between text-xs shadow-sm';
          el.innerHTML = `
            <div>
              <span class="font-bold text-slate-800">${{s.date}}</span> • <span class="text-slate-600">${{s.title}}</span>
              <p class="text-[11px] text-blue-600 font-medium">${{VOLUNTEERS[currentUserId].role}}</p>
            </div>
            <span class="text-[10px] ${{idx === 0 ? 'text-amber-700 bg-amber-50 border border-amber-200' : 'text-slate-400 bg-slate-100'}} px-2 py-0.5 rounded font-medium">
              ${{idx === 0 ? 'Próximo' : 'Confirmado'}}
            </span>
          `;
          container.appendChild(el);
        }});
      }} else {{
        document.getElementById('serviceTitle').innerText = `Sem escalas em ${{MONTH_NAMES[currentMonth] || currentMonth}}`;
        document.getElementById('serviceTheme').innerText = 'Você não possui cultos agendados neste mês.';
        document.getElementById('serviceDateTime').innerText = '--/--';
        document.getElementById('serviceFunction').innerText = 'Folga programada';
        document.getElementById('futureServicesList').innerHTML = `
          <div class="p-3 bg-slate-50 text-slate-500 rounded-xl text-center text-xs">
            Nenhuma escala atribuída para ${{VOLUNTEERS[currentUserId].name}} em ${{MONTH_NAMES[currentMonth] || currentMonth}}.
          </div>
        `;
      }}
    }}

    // Renderiza a Escala Geral
    function renderGeneralMonth() {{
      const services = ALL_SERVICES[currentMonth] || [];
      const container = document.getElementById('monthServicesAccordion');
      container.innerHTML = '';

      if (services.length === 0) {{
        container.innerHTML = `
          <div class="p-4 bg-slate-50 text-slate-500 rounded-xl text-center text-xs">
            Nenhum culto cadastrado para este mês ainda.
            <button onclick="openNewCultoModal()" class="mt-2 block mx-auto text-blue-600 font-bold underline">
              + Cadastrar 1º Culto
            </button>
          </div>
        `;
        return;
      }}

      services.forEach((s, idx) => {{
        const card = document.createElement('div');
        card.className = 'bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm';
        card.innerHTML = `
          <div onclick="toggleAccordion('acc-${{idx}}')" class="p-3 bg-slate-50/80 flex items-center justify-between cursor-pointer hover:bg-slate-100 transition">
            <div>
              <div class="flex items-center gap-1.5">
                <span class="text-xs font-extrabold text-blue-700">${{s.date}}</span>
                ${{s.team ? `<span class="text-[10px] font-bold bg-blue-100 text-blue-800 px-1.5 py-0.2 rounded">${{s.team}}</span>` : ''}}
              </div>
              <h4 class="text-xs font-bold text-slate-800 leading-tight mt-0.5">${{s.title}}</h4>
            </div>
            <i class="fa-solid fa-chevron-down text-xs text-slate-400" id="icon-acc-${{idx}}"></i>
          </div>
          <div id="acc-${{idx}}" class="p-3 text-xs space-y-2 border-t border-slate-100 ${{idx === 0 ? '' : 'hidden'}}">
            ${{s.preacher ? `
            <div>
              <span class="text-[10px] uppercase font-bold text-slate-400 block">Palavra & Tema</span>
              <p class="text-slate-800 font-bold">Ministrante: ${{s.preacher}}</p>
              ${{s.theme ? `<p class="text-slate-600 italic text-[11px]">${{s.theme}}</p>` : ''}}
              ${{s.text ? `<p class="text-slate-400 text-[10px]">Texto: ${{s.text}}</p>` : ''}}
            </div>` : ''}}

            <div class="pt-1 border-t border-slate-100">
              <span class="text-[10px] uppercase font-bold text-slate-400 block">Louvor</span>
              <p class="text-[11px] text-slate-700">${{s.worship}}</p>
            </div>

            <div class="grid grid-cols-2 gap-2 pt-1 border-t border-slate-100">
              <div>
                <span class="text-[10px] uppercase font-bold text-slate-400 block">Shamah Kids</span>
                <p class="text-[11px] text-slate-700">${{s.kids}}</p>
              </div>
              <div>
                <span class="text-[10px] uppercase font-bold text-slate-400 block">Mídia & Cabine</span>
                <p class="text-[11px] text-slate-700">${{s.media}}</p>
              </div>
            </div>

            ${{s.diaconia ? `
            <div class="pt-1 border-t border-slate-100">
              <span class="text-[10px] uppercase font-bold text-slate-400 block">Diaconato & Acolhimento</span>
              <p class="text-[11px] text-slate-700">${{s.diaconia}}</p>
            </div>` : ''}}
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    function toggleAccordion(id) {{
      const el = document.getElementById(id);
      el.classList.toggle('hidden');
    }}

    // Músicas
    function updateWorshipSelector() {{
      const services = ALL_SERVICES[currentMonth] || [];
      const sel = document.getElementById('worshipServiceSelector');
      sel.innerHTML = '';
      services.forEach((s, idx) => {{
        if (s.songs && s.songs.length > 0) {{
          const opt = document.createElement('option');
          opt.value = idx;
          opt.innerText = `${{s.date}} - ${{s.title}}`;
          sel.appendChild(opt);
        }}
      }});
      if (sel.options.length > 0) {{
        renderSongsForService(sel.options[0].value);
      }} else {{
        document.getElementById('songListContainer').innerHTML = `
          <div class="p-4 bg-slate-50 text-slate-500 rounded-xl text-center text-xs">
            Nenhum repertório de músicas detalhado registrado para este mês.
          </div>
        `;
      }}
    }}

    function renderSongsForService(svcIdx) {{
      const services = ALL_SERVICES[currentMonth] || [];
      const s = services[svcIdx];
      const container = document.getElementById('songListContainer');
      container.innerHTML = '';

      if (!s || !s.songs || s.songs.length === 0) {{
        container.innerHTML = '<div class="p-3 text-center text-xs text-slate-400">Repertório a definir</div>';
        return;
      }}

      s.songs.forEach(song => {{
        const item = document.createElement('div');
        item.className = 'bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between';
        item.innerHTML = `
          <div class="flex items-center space-x-2.5">
            <span class="badge-${{song.color}} text-[10px] font-extrabold px-2 py-0.5 rounded-md">${{song.badge}}</span>
            <div>
              <h4 class="text-xs font-bold text-slate-800">${{song.title}}</h4>
              <p class="text-[10px] text-slate-400">Arranjo Oficial IBS</p>
            </div>
          </div>
          <div class="flex gap-1.5">
            <button class="w-8 h-8 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 flex items-center justify-center text-xs" title="Ouvir">
              <i class="fa-solid fa-play"></i>
            </button>
            <button class="w-8 h-8 rounded-lg bg-blue-50 hover:bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-bold" title="Cifra">
              <i class="fa-solid fa-file-lines"></i>
            </button>
          </div>
        `;
        container.appendChild(item);
      }});
    }}

    // Visão de Liderança
    function updateLeadershipView() {{
      const services = ALL_SERVICES[currentMonth] || [];
      const rotationContainer = document.getElementById('teamRotationList');
      rotationContainer.innerHTML = '';

      const sundays = services.filter(s => (s.weekday || '').toLowerCase().includes('domingo'));
      sundays.forEach(s => {{
        const el = document.createElement('div');
        el.className = 'flex items-center justify-between bg-slate-50 p-2 rounded-lg';
        el.innerHTML = `
          <span class="font-bold text-slate-700">${{s.date}}</span>
          <span class="text-slate-500">${{s.title}}</span>
          <span class="font-extrabold text-blue-700 bg-blue-100 px-2 py-0.5 rounded text-[11px]">${{s.team || 'Equipe Geral'}}</span>
        `;
        rotationContainer.appendChild(el);
      }});

      const checklist = document.getElementById('leadChecklist');
      checklist.innerHTML = '';
      if (services.length > 0) {{
        const first = services[0];
        checklist.innerHTML = `
          <div class="py-2 flex items-center justify-between">
            <div>
              <span class="font-bold text-slate-700">${{first.date}} - Louvor</span>
              <p class="text-[10px] text-slate-400">${{first.worship}}</p>
            </div>
            <span class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">Completo</span>
          </div>
          <div class="py-2 flex items-center justify-between">
            <div>
              <span class="font-bold text-slate-700">Shamah Kids</span>
              <p class="text-[10px] text-slate-400">${{first.kids}}</p>
            </div>
            <span class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">Escalado</span>
          </div>
          <div class="py-2 flex items-center justify-between">
            <div>
              <span class="font-bold text-slate-700">Mídia e Som</span>
              <p class="text-[10px] text-slate-400">${{first.media}}</p>
            </div>
            <span class="text-[10px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">Confirmado</span>
          </div>
        `;
      }}
    }}

    // MODAL DE CADASTRO DE PESSOA
    function openNewPersonModal() {{
      document.getElementById('newPersonModal').classList.remove('hidden');
    }}
    function closeNewPersonModal() {{
      document.getElementById('newPersonModal').classList.add('hidden');
      document.getElementById('newPersonForm').reset();
    }}
    function handleSavePerson(e) {{
      e.preventDefault();
      const name = document.getElementById('personNameInput').value.trim();
      const phone = document.getElementById('personPhoneInput').value.trim();
      const team = document.getElementById('personTeamInput').value;
      const dept = document.getElementById('personDeptInput').value;
      const role = document.getElementById('personRoleInput').value.trim();

      const id = name.toLowerCase().replace(/[^a-z0-9]/g, '_');
      const initials = name.split(' ').map(p => p[0]).join('').substring(0, 2).toUpperCase();

      VOLUNTEERS[id] = {{
        name: name,
        role: `${{dept}} - ${{role}}`,
        dept: dept,
        team: team,
        phone: phone,
        initials: initials
      }};

      localStorage.setItem('ibs_volunteers_v2', JSON.stringify(VOLUNTEERS));

      initUserDropdown();
      changeUser(id);
      closeNewPersonModal();
      alert(`Voluntário(a) "${{name}}" cadastrado(a) com sucesso!\nJá foi selecionado(a) na simulação.`);
    }}

    // MODAL DE CADASTRO DE CULTO
    function openNewCultoModal() {{
      document.getElementById('newCultoModal').classList.remove('hidden');
      // pré-selecionar mês ativo
      document.getElementById('cultoMonthInput').value = currentMonth;
    }}
    function closeNewCultoModal() {{
      document.getElementById('newCultoModal').classList.add('hidden');
      document.getElementById('newCultoForm').reset();
    }}
    function handleSaveCulto(e) {{
      e.preventDefault();
      const month = document.getElementById('cultoMonthInput').value;
      const dateRaw = document.getElementById('cultoDateInput').value; // YYYY-MM-DD
      const title = document.getElementById('cultoTitleInput').value.trim();
      const team = document.getElementById('cultoTeamInput').value;
      const time = document.getElementById('cultoTimeInput').value.trim() || '18:00';
      const preacher = document.getElementById('cultoPreacherInput').value.trim() || 'Pr. Flávio Amaral';
      const theme = document.getElementById('cultoThemeInput').value.trim() || 'Celebração Especial';
      const worship = document.getElementById('cultoWorshipInput').value.trim() || 'Banda IBS';

      if (!dateRaw) return;
      const parts = dateRaw.split('-');
      const dtFormatted = `${{parts[2]}}/${{parts[1]}}/${{parts[0]}}`;
      const dateObj = new Date(parts[0], parseInt(parts[1]) - 1, parts[2]);
      const weekdays = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'];
      const weekdayName = weekdays[dateObj.getDay()];

      if (!ALL_SERVICES[month]) {{
        ALL_SERVICES[month] = [];
      }}

      ALL_SERVICES[month].push({{
        date: `${{weekdayName}}, ${{dtFormatted}} • ${{time}}`,
        date_raw: dateRaw,
        weekday: weekdayName,
        title: title,
        team: team,
        preacher: preacher,
        theme: theme,
        text: 'A definir',
        worship: worship,
        kids: "Equipe Shamah Kids",
        media: 'Felipe (Som) • Lorivaldo (Mídia)',
        diaconia: 'Equipe de Acolhimento',
        songs: []
      }});

      localStorage.setItem('ibs_services_v2', JSON.stringify(ALL_SERVICES));

      // Mudar para o mês do culto cadastrado
      document.getElementById('globalMonthSelector').value = month;
      onMonthChange(month);
      closeNewCultoModal();
      alert(`Culto "${{title}}" cadastrado com sucesso para ${{weekdayName}}, ${{dtFormatted}}!`);
    }}

    // Navegação entre Abas
    function switchTab(tabId) {{
      ['meus-cultos', 'escala-geral', 'repertorio', 'coordenacao'].forEach(t => {{
        const el = document.getElementById(`tab-${{t}}`);
        const btn = document.getElementById(`nav-${{t}}`);
        if (t === tabId) {{
          el.classList.remove('hidden');
          btn.classList.add('text-blue-600', 'tab-active');
          btn.classList.remove('text-slate-400');
        }} else {{
          el.classList.add('hidden');
          btn.classList.remove('text-blue-600', 'tab-active');
          btn.classList.add('text-slate-400');
        }}
      }});
    }}

    function confirmPresence() {{
      document.getElementById('actionButtons').classList.add('hidden');
      document.getElementById('confirmedFeedback').classList.remove('hidden');
      const tag = document.getElementById('statusTag');
      tag.className = 'text-xs font-semibold text-emerald-800 bg-emerald-50 border border-emerald-300 px-2.5 py-0.5 rounded-full flex items-center gap-1';
      tag.innerHTML = '<i class="fa-solid fa-circle-check text-emerald-600 text-[10px]"></i> Presença Confirmada';
    }}

    function resetConfirmation() {{
      document.getElementById('actionButtons').classList.remove('hidden');
      document.getElementById('confirmedFeedback').classList.add('hidden');
      const tag = document.getElementById('statusTag');
      tag.className = 'text-xs font-semibold text-amber-700 bg-amber-50 border border-amber-200 px-2.5 py-0.5 rounded-full flex items-center gap-1';
      tag.innerHTML = '<i class="fa-solid fa-clock text-[10px]"></i> Aguardando Confirmação';
    }}

    function openSwapModal() {{
      const sel = document.getElementById('swapCandidateSelect');
      sel.innerHTML = '';
      Object.keys(VOLUNTEERS).forEach(k => {{
        if (k !== currentUserId) {{
          const opt = document.createElement('option');
          opt.value = k;
          opt.innerText = `${{VOLUNTEERS[k].name}} (${{VOLUNTEERS[k].role}})`;
          sel.appendChild(opt);
        }}
      }});
      document.getElementById('swapModal').classList.remove('hidden');
    }}

    function closeSwapModal() {{
      document.getElementById('swapModal').classList.add('hidden');
    }}

    function submitSwapRequest() {{
      closeSwapModal();
      alert('Pedido de substituição enviado com sucesso para a coordenação!');
      const tag = document.getElementById('statusTag');
      tag.className = 'text-xs font-semibold text-rose-700 bg-rose-50 border border-rose-200 px-2.5 py-0.5 rounded-full flex items-center gap-1';
      tag.innerHTML = '<i class="fa-solid fa-arrows-rotate text-[10px]"></i> Substituição Solicitada';
    }}

    function sendWhatsAppReminders() {{
      alert('Disparando lembrete automático via WhatsApp para os voluntários pendentes de ' + (MONTH_NAMES[currentMonth] || currentMonth) + '!');
    }}

    // Inicialização
    initUserDropdown();
    onMonthChange('Out');
    changeUser('bruno');
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'C:\Users\sigma\.gemini\antigravity\brain\abfefb37-5e54-4455-bf09-7a27be839382\app_demo.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Simulador com formulários de cadastro de Pessoa e Culto atualizado com sucesso!')
