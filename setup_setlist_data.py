import json

# Catálogo Litúrgico Oficial de Canções Aprovadas (Diretrizes IBS 2026 - Anexo I)
APPROVED_SONGS = [
    # BLOCO 1. Chamada à Adoração e Celebração (O Despertar)
    {
        "id": "vem_esta_e_a_hora",
        "title": "Vem, esta é a hora",
        "artist": "Vineyard",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Pop-Rock Médio (110 BPM)",
        "key": "D",
        "notes": "Padrão-ouro de abertura. Convite imperativo à adoração pública.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "nosso_deus_e_soberano",
        "title": "Nosso Deus é Soberano",
        "artist": "Asaph Borba / Koinonya",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Médio (95 BPM)",
        "key": "G",
        "notes": "Afirmação firme da soberania e do controle de Deus sobre a história.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "jesus_venceu",
        "title": "Jesus Venceu",
        "artist": "Adhemar de Campos",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Rápido (120 BPM)",
        "key": "A",
        "notes": "Celebração da ressurreição, substituindo o ufanismo humano.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "filho_do_deus_vivo",
        "title": "Filho do Deus vivo",
        "artist": "Nívea Soares",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Rápido / Moderado (118 BPM)",
        "key": "D",
        "notes": "Declaração rápida de identidade cristológica (Mateus 16).",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "todas_as_coisas",
        "title": "Todas as coisas",
        "artist": "Fernandinho",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Pop-Rock (122 BPM)",
        "key": "G",
        "notes": "Celebração da providência soberana (Romanos 8:28).",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "rei_do_meu_coracao",
        "title": "Rei do Meu Coração",
        "artist": "Be One Music",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Médio (72/144 BPM)",
        "key": "G",
        "notes": "Declara a constância de Deus independente das circunstâncias.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "pra_sempre",
        "title": "Pra Sempre (Forever)",
        "artist": "Fernandinho / Bethel",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Crescente (72 BPM)",
        "key": "G",
        "notes": "Celebração do túmulo vazio e do inferno derrotado. Transição: Bloco 3 (Cruz).",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "hosana",
        "title": "Hosana",
        "artist": "Diante do Trono",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Dinâmica Crescente (115 BPM)",
        "key": "G",
        "notes": "Dinâmica crescente. A entrada triunfal do Rei. Transição: Bloco 5 (Escatologia).",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "grande_e_o_senhor",
        "title": "Grande é o Senhor",
        "artist": "Adhemar de Campos",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Médio / Festivo (100 BPM)",
        "key": "C",
        "notes": "O Salmo 48 musicado. Clássico nivelador para todas as idades.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "cantarei_teu_amor",
        "title": "Cantarei Teu Amor...",
        "artist": "Aline Barros / Vineyard",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Andamento Médio (105 BPM)",
        "key": "D",
        "notes": "Foco na constância da misericórdia de Deus.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "abram_se_os_portais",
        "title": "Abram-se os Portais",
        "artist": "Fhop Music",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Solene / Enérgico (110 BPM)",
        "key": "E",
        "notes": "Invocação baseada no Salmo 24.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "aclame_ao_senhor",
        "title": "Aclame ao Senhor",
        "artist": "Diante do Trono",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Majestoso (85 BPM)",
        "key": "A",
        "notes": "Salmo 100 cantado. Assimilação universal.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "eu_te_agradeco",
        "title": "Eu te agradeço",
        "artist": "Diante do Trono",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Médio (95 BPM)",
        "key": "E",
        "notes": "Ação de graças sem barganhas. Ótima transição rítmica.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "estamos_de_pe",
        "title": "Estamos de pé",
        "artist": "Marcos Salles",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Firme (100 BPM)",
        "key": "G",
        "notes": "Resiliência firmada na suficiência de Cristo.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "quem_e_esse",
        "title": "Quem é esse",
        "artist": "Juliana Souza",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Ritmo Vibrante (115 BPM)",
        "key": "D",
        "notes": "Exaltação dos feitos de Jesus em ritmo vibrante.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },
    {
        "id": "hcc_193",
        "title": "HCC 193 - A Deus demos glória",
        "artist": "Hinário Batista",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Solene / Triunfal (95 BPM)",
        "key": "G",
        "notes": "Doxologia e resgate histórico para cultos solenes. Transição: Bloco 4.",
        "badge": "BLOCO 1 • HISTÓRICO",
        "color": "blue"
    },
    {
        "id": "celebrai",
        "title": "Celebrai",
        "artist": "Cântico Tradicional",
        "block": 1,
        "block_name": "Bloco 1 - Chamada à Adoração",
        "tempo": "Rápido / Festivo (125 BPM)",
        "key": "F",
        "notes": "Afirmação direta e energética da ressurreição. Nivelador geracional.",
        "badge": "BLOCO 1 • CELEBRAÇÃO",
        "color": "blue"
    },

    # BLOCO 2. Contrição, Confissão e Dependência (O Quebrantamento)
    {
        "id": "tua_graca_me_basta",
        "title": "Tua Graça me Basta",
        "artist": "Davi Sacer",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento (65 BPM)",
        "key": "G",
        "notes": "O paradoxo bíblico: gloriar-se na fraqueza (2 Coríntios 12:9).",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "senhor_te_quero",
        "title": "Senhor te quero",
        "artist": "Vineyard",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento / Íntimo (68 BPM)",
        "key": "G",
        "notes": "Declaração de total dependência.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "meu_respirar",
        "title": "Meu respirar",
        "artist": "Gabriela Rocha / Vineyard",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento (64 BPM)",
        "key": "G",
        "notes": "Cristo como sustentação vital (o pão de cada dia). Prepara para a Ceia.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "fogo_purificador",
        "title": "Fogo Purificador",
        "artist": "Vineyard",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento (66 BPM)",
        "key": "D",
        "notes": "Busca por santificação e caráter refinado (Malaquias 3).",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "me_esvaziar",
        "title": "Me esvaziar",
        "artist": "Nívea Soares",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento / Reflexivo (62 BPM)",
        "key": "E",
        "notes": "Preparo mental e reflexivo para a exposição bíblica.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "vaso_novo",
        "title": "Vaso Novo",
        "artist": "Corinho Tradicional",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento (65 BPM)",
        "key": "D",
        "notes": "Submissão passiva e absoluta às mãos do Oleiro.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "coracao_igual_ao_teu",
        "title": "Coração Igual ao Teu",
        "artist": "Diante do Trono",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento / Arrependimento (65 BPM)",
        "key": "A",
        "notes": "Cântico de arrependimento e alinhamento de caráter.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "fome_e_sede",
        "title": "Fome e Sede",
        "artist": "Vineyard",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento (68 BPM)",
        "key": "C",
        "notes": "Anseio puramente focado na necessidade de Deus.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "em_tua_presenca",
        "title": "Em tua presença",
        "artist": "Nívea Soares",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento / Reverente (60 BPM)",
        "key": "D",
        "notes": "Foco no descanso reverente.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "me_derramar",
        "title": "Me derramar",
        "artist": "Vineyard",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento (65 BPM)",
        "key": "G",
        "notes": "Cântico clássico de consagração e entrega.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "ha_um_lugar",
        "title": "Há um lugar",
        "artist": "Heloísa Rosa",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento (62 BPM)",
        "key": "C",
        "notes": "Convite à intimidade longe dos ruídos externos.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "te_louvarei",
        "title": "Te louvarei",
        "artist": "Davi Sacer",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento para Médio (70 BPM)",
        "key": "E",
        "notes": "Inicia na fraqueza humana e culmina no Senhorio de Jesus. Transição: Bloco 4.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "mais_perto_quero_estar",
        "title": "Mais Perto Quero Estar (HCC 283)",
        "artist": "Hinário Batista",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento / Solene (60 BPM)",
        "key": "G",
        "notes": "Contrição clássica; peso de reverência geracional.",
        "badge": "BLOCO 2 • HISTÓRICO",
        "color": "purple"
    },
    {
        "id": "gratidao",
        "title": "Gratidão",
        "artist": "Bruna Olly",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento / Resposta (68 BPM)",
        "key": "A",
        "notes": "Canção de resposta; o esvaziamento do homem que oferece o que tem. Transição: Bloco 4.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },
    {
        "id": "quebrantado",
        "title": "Quebrantado",
        "artist": "Vineyard",
        "block": 2,
        "block_name": "Bloco 2 - Contrição & Dependência",
        "tempo": "Lento (68 BPM)",
        "key": "C",
        "notes": "Queda de andamento; reconhecimento da falibilidade humana diante da cruz.",
        "badge": "BLOCO 2 • CONTRIÇÃO",
        "color": "purple"
    },

    # BLOCO 3. A Cruz e a Salvação / Soteriologia (O Ápice da Ceia e Apelo)
    {
        "id": "nada_alem_do_sangue",
        "title": "Nada além do sangue",
        "artist": "Fernandinho",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Médio / Intenso (76 BPM)",
        "key": "E",
        "notes": "A suficiência expiatória. Clímax absoluto de adoração e justificação.",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },
    {
        "id": "somente_em_cristo",
        "title": "Somente em Cristo",
        "artist": "Livres / VPC",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Moderado (66 BPM)",
        "key": "D",
        "notes": "O maior hino moderno. Cobre encarnação, morte propiciatória e retorno.",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },
    {
        "id": "diante_da_cruz",
        "title": "Diante da Cruz",
        "artist": "Aline Barros",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Lento / Rendição (68 BPM)",
        "key": "D",
        "notes": "Resposta humana de rendição absoluta ao Calvário. Quebra autossuficiência.",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },
    {
        "id": "digno_e_o_cordeiro",
        "title": "Digno é o Cordeiro",
        "artist": "Diante do Trono",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Solene (65 BPM)",
        "key": "G",
        "notes": "Conecta a cruz ao trono ('Obrigado pela cruz, Senhor'). Transição: Bloco 4.",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },
    {
        "id": "foi_na_cruz_hcc_115",
        "title": "Foi na Cruz (Calvário) - HCC 115",
        "artist": "Aline Barros / Hinário",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Moderado (80 BPM)",
        "key": "E",
        "notes": "A centralidade do sacrifício e a libertação do fardo do pecado.",
        "badge": "BLOCO 3 • HISTÓRICO",
        "color": "rose"
    },
    {
        "id": "mensagem_da_cruz",
        "title": "Mensagem da Cruz (HCC 111)",
        "artist": "Harpa / Hinário Batista",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Moderado (75 BPM)",
        "key": "A",
        "notes": "A centralidade e a loucura da cruz (1 Coríntios 1).",
        "badge": "BLOCO 3 • HISTÓRICO",
        "color": "rose"
    },
    {
        "id": "alvo_mais_que_a_neve",
        "title": "Alvo Mais Que a Neve (HCC 205)",
        "artist": "Hinário Batista",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Moderado (85 BPM)",
        "key": "G",
        "notes": "Aula sobre justificação cantada de forma uníssona.",
        "badge": "BLOCO 3 • HISTÓRICO",
        "color": "rose"
    },
    {
        "id": "a_cruz_la_na_cruz",
        "title": "A Cruz (Lá na Cruz)",
        "artist": "Hillsong / DT",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Balada / Crescente (72 BPM)",
        "key": "D",
        "notes": "Abertura de olhos espirituais ('foi lá na cruz onde a luz brilhou').",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },
    {
        "id": "jesus_o_plano_perfeito",
        "title": "Jesus o plano perfeito",
        "artist": "Renascer Praise",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Balada (70 BPM)",
        "key": "C",
        "notes": "Soteriologia explicada de forma simples para toda a igreja.",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },
    {
        "id": "maravilhosa_graca",
        "title": "Maravilhosa Graça",
        "artist": "Drops",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Worship (72 BPM)",
        "key": "G",
        "notes": "Profunda didática sobre o favor divino imerecido.",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },
    {
        "id": "porque_ele_vive",
        "title": "Porque ele vive",
        "artist": "Fernandinho / Hino",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Crescente (76 BPM)",
        "key": "A",
        "notes": "O triunfo da ressurreição sobre o medo do futuro. Transição: Bloco 5.",
        "badge": "BLOCO 3 • HISTÓRICO",
        "color": "rose"
    },
    {
        "id": "tao_profundo",
        "title": "Tão profundo",
        "artist": "Vineyard",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Lento (64 BPM)",
        "key": "D",
        "notes": "Excelente para acompanhamento sonoro da Ceia do Senhor.",
        "badge": "BLOCO 3 • CEIA",
        "color": "rose"
    },
    {
        "id": "cancao_ao_cordeiro",
        "title": "Canção ao Cordeiro",
        "artist": "Igreja Projeto",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Solene (68 BPM)",
        "key": "G",
        "notes": "Foco na coroa, cravos e trono (descritiva da realeza).",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },
    {
        "id": "eu_me_rendo",
        "title": "Eu me rendo",
        "artist": "Renascer Praise",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Lento (60 BPM)",
        "key": "F",
        "notes": "Apelo de conversão, entrega e renúncia.",
        "badge": "BLOCO 3 • APELO",
        "color": "rose"
    },
    {
        "id": "cruz_casa_worship",
        "title": "Cruz",
        "artist": "Casa Worship / Bigair Dy Jaime",
        "block": 3,
        "block_name": "Bloco 3 - A Cruz & Soteriologia",
        "tempo": "Build-up crescente (68 BPM)",
        "key": "D",
        "notes": "Exegese poética de Isaías 53. Requer controle rigoroso de volume.",
        "badge": "BLOCO 3 • CRUZ & SALVAÇÃO",
        "color": "rose"
    },

    # BLOCO 4. Adoração Doxológica e Teontologia (A Majestade Divina)
    {
        "id": "a_ele_a_gloria",
        "title": "A Ele a glória",
        "artist": "Diante do Trono",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Majestoso / Clímax (65 BPM)",
        "key": "C",
        "notes": "Romanos 11:36. O fechamento perfeito para não roubarmos a glória.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "pai_nosso",
        "title": "Pai Nosso",
        "artist": "Pedras Vivas / Hillsong",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Crescente (72 BPM)",
        "key": "G",
        "notes": "A oração perfeita musicada. Antídoto contra o antropocentrismo.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "alfa_e_omega",
        "title": "Alfa e Ômega",
        "artist": "Marine Friesen",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Moderado / Íntimo (68 BPM)",
        "key": "D",
        "notes": "Exaltação da eternidade e autossuficiência de Deus (Apocalipse 1:8).",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "santo_santo_santo",
        "title": "Santo, Santo, Santo (HCC 01)",
        "artist": "Hinário Batista",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Solene / Triunfal (80 BPM)",
        "key": "D",
        "notes": "A Trindade perfeita. Cobre onipotência, tri-unidade e santidade.",
        "badge": "BLOCO 4 • HISTÓRICO",
        "color": "amber"
    },
    {
        "id": "quao_grande_e_meu_deus",
        "title": "Quão grande é meu Deus",
        "artist": "Soraya Morais",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Lento / Grandioso (68 BPM)",
        "key": "C",
        "notes": "Eleva a visão da igreja e nivela as gerações em uma só voz.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "soberano",
        "title": "Soberano",
        "artist": "Koinonya",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Moderado (75 BPM)",
        "key": "G",
        "notes": "O controle absoluto do Criador sobre a história e o caos.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "ao_unico",
        "title": "Ao Único",
        "artist": "Aline Barros / Koinonya",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Reverente (70 BPM)",
        "key": "C",
        "notes": "Coroação e reverência máxima ao Rei Jesus.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "digno_de_gloria",
        "title": "Digno de Glória",
        "artist": "Asaph Borba",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Solene (72 BPM)",
        "key": "D",
        "notes": "Ensina a postura de adoração horizontal e vertical.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "majestade",
        "title": "Majestade (Majesty)",
        "artist": "Vineyard",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Balada (66 BPM)",
        "key": "G",
        "notes": "Balada que constrói um ambiente de puro assombro reverente.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "tu_es_santo",
        "title": "Tu És Santo (Príncipe)",
        "artist": "Michael W. Smith",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Enérgico / Contracanto (100 BPM)",
        "key": "G",
        "notes": "Cristologia descritiva com contracanto envolvente.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "em_espirito_em_verdade",
        "title": "Em Espírito, em Verdade",
        "artist": "Koinonya",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Lento (64 BPM)",
        "key": "F",
        "notes": "O padrão de adoração ensinado em João 4.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "e_ele",
        "title": "É Ele",
        "artist": "Drops",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Worship Moderno (70 BPM)",
        "key": "G",
        "notes": "A preeminência absoluta de Jesus explicada (Colossenses 1).",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "poderoso_deus",
        "title": "Poderoso Deus",
        "artist": "Antônio Cirilo",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Espontâneo / Lento (60 BPM)",
        "key": "D",
        "notes": "Majestosa para adoração prolongada (requer controle de tempo).",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "jesus_e_o_caminho",
        "title": "Jesus é o caminho",
        "artist": "Heloísa Rosa",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Médio / Firme (90 BPM)",
        "key": "Em",
        "notes": "Afirmação firme de exclusividade contra o pluralismo e relativismo.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "maravilhado",
        "title": "Maravilhado",
        "artist": "Nívea Soares",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Lento (65 BPM)",
        "key": "D",
        "notes": "Espanto e admiração diante da glória de Deus.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "unico",
        "title": "Único",
        "artist": "Fernandinho",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Lento / Singelo (68 BPM)",
        "key": "G",
        "notes": "Singeleza e reconhecimento da singularidade divina.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },
    {
        "id": "o_quao_lindo_esse_nome_e",
        "title": "O quão lindo esse nome é",
        "artist": "Hillsong",
        "block": 4,
        "block_name": "Bloco 4 - Adoração Doxológica",
        "tempo": "Worship Crescente (68 BPM)",
        "key": "D",
        "notes": "Exaltação do poder invencível e singularidade do nome de Cristo.",
        "badge": "BLOCO 4 • MAJESTADE",
        "color": "amber"
    },

    # BLOCO 5. Visão Celestial, Escatologia e Envio (Conclusão e Esperança)
    {
        "id": "cancao_do_apocalipse",
        "title": "Canção do Apocalipse",
        "artist": "Diante do Trono",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Solene / Épico (62 BPM)",
        "key": "C",
        "notes": "A visão celestial de Apocalipse 4. Transforma o teto da igreja no céu.",
        "badge": "BLOCO 5 • ESCATOLOGIA",
        "color": "emerald"
    },
    {
        "id": "maranata",
        "title": "Maranata",
        "artist": "Ministério Avivah",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Crescente (70 BPM)",
        "key": "D",
        "notes": "O anseio urgente da noiva pelo noivo.",
        "badge": "BLOCO 5 • ESCATOLOGIA",
        "color": "emerald"
    },
    {
        "id": "o_rei_esta_voltando",
        "title": "O Rei Está Voltando (HCC 138)",
        "artist": "Hinário Batista / Harpa",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Marcha Triunfal (78 BPM)",
        "key": "G",
        "notes": "A marcha triunfal que alicerça a esperança na soberania divina.",
        "badge": "BLOCO 5 • HISTÓRICO",
        "color": "emerald"
    },
    {
        "id": "vitorioso_es",
        "title": "Vitorioso És",
        "artist": "Gabriel Guedes",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Vibrante / Triunfal (74 BPM)",
        "key": "C",
        "notes": "A derrota definitiva da morte e o estabelecimento do reinado de Cristo.",
        "badge": "BLOCO 5 • ESCATOLOGIA",
        "color": "emerald"
    },
    {
        "id": "a_bencao",
        "title": "A Benção",
        "artist": "Gabriel Guedes",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Lento / Bênção (68 BPM)",
        "key": "G",
        "notes": "A ministração apostólica (Números 6) para as famílias para a semana.",
        "badge": "BLOCO 5 • ENVIO",
        "color": "emerald"
    },
    {
        "id": "ele_vem",
        "title": "Ele vem",
        "artist": "Gabriel Guedes",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Worship (72 BPM)",
        "key": "E",
        "notes": "Declaração firme e direta do retorno corpóreo de Cristo.",
        "badge": "BLOCO 5 • ESCATOLOGIA",
        "color": "emerald"
    },
    {
        "id": "o_espirito_e_a_noiva",
        "title": "O Espírito e a Noiva",
        "artist": "Fhop Music / Vários",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Clamor Crescente (70 BPM)",
        "key": "Am",
        "notes": "Apocalipse 22. Clamor coletivo com intensidade crescente.",
        "badge": "BLOCO 5 • ESCATOLOGIA",
        "color": "emerald"
    },
    {
        "id": "dias_de_elias",
        "title": "Dias de Elias",
        "artist": "Paul Wilbur",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Rítmica e Enérgica (120 BPM)",
        "key": "A",
        "notes": "Conecta a história da redenção com a volta nas nuvens.",
        "badge": "BLOCO 5 • ESCATOLOGIA",
        "color": "emerald"
    },
    {
        "id": "quando_a_trombeta_tocar",
        "title": "Quando a Trombeta Tocar",
        "artist": "Harpa / Vários",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Triunfal (95 BPM)",
        "key": "G",
        "notes": "A promessa final da consumação e o encontro com o Rei.",
        "badge": "BLOCO 5 • HISTÓRICO",
        "color": "emerald"
    },
    {
        "id": "vai_valer_a_pena",
        "title": "Vai valer a pena",
        "artist": "Juliano Son",
        "block": 5,
        "block_name": "Bloco 5 - Escatologia & Envio",
        "tempo": "Worship / Esperança (68 BPM)",
        "key": "D",
        "notes": "Foco na recompensa e visão da eternidade frente ao sofrimento atual.",
        "badge": "BLOCO 5 • ESCATOLOGIA",
        "color": "emerald"
    }
]

# Roteiros Litúrgicos Oficiais (Parte 2 do Manual)
LITURGICAL_ROUTINES = {
    "roteiro_1": {
        "id": "roteiro_1",
        "title": "Roteiro 1: Foco na Obra Redentora (Domingo pela Manhã)",
        "objective": "Reajustar a identidade da igreja no evangelho puro, preparando o solo para a exposição bíblica.",
        "songs": [
            {
                "order": 1,
                "step": "Chamada",
                "title": "Vem, esta é a hora",
                "artist": "Vineyard",
                "block": 1,
                "block_name": "Bloco 1 - Chamada",
                "key": "D",
                "tempo": "Pop-Rock (110 BPM)",
                "transition": "Linkagem harmônica contínua",
                "notes": "Quebra o gelo e convoca a igreja à adoração pública.",
                "badge": "BLOCO 1 • CELEBRAÇÃO",
                "color": "blue"
            },
            {
                "order": 2,
                "step": "Celebração",
                "title": "Todas as coisas",
                "artist": "Fernandinho",
                "block": 1,
                "block_name": "Bloco 1 - Celebração",
                "key": "G",
                "tempo": "Pop-Rock (122 BPM)",
                "transition": "Modulação direta D -> G com pad",
                "notes": "Afirma a soberania de Deus sobre as circunstâncias (Rm 8:28).",
                "badge": "BLOCO 1 • CELEBRAÇÃO",
                "color": "blue"
            },
            {
                "order": 3,
                "step": "Contrição",
                "title": "Quebrantado",
                "artist": "Vineyard",
                "block": 2,
                "block_name": "Bloco 2 - Contrição",
                "key": "C",
                "tempo": "Lento (68 BPM)",
                "transition": "Queda de andamento; entrada suave violão/teclado",
                "notes": "Queda de andamento; reconhecimento da falibilidade humana.",
                "badge": "BLOCO 2 • CONTRIÇÃO",
                "color": "purple"
            },
            {
                "order": 4,
                "step": "Adoração (Ápice)",
                "title": "Nada além do sangue",
                "artist": "Fernandinho",
                "block": 3,
                "block_name": "Bloco 3 - Cruz & Salvação",
                "key": "E",
                "tempo": "Moderado Intenso (76 BPM)",
                "transition": "Pad em Em -> E; build-up na ponte",
                "notes": "O clímax na suficiência do sacrifício substitutivo.",
                "badge": "BLOCO 3 • CRUZ",
                "color": "rose"
            },
            {
                "order": 5,
                "step": "Fechamento",
                "title": "A Ele a glória",
                "artist": "Diante do Trono",
                "block": 4,
                "block_name": "Bloco 4 - Adoração Doxológica",
                "key": "C",
                "tempo": "Majestoso (65 BPM)",
                "transition": "Modulação de encerramento; igreja a cappella no refrão",
                "notes": "Resposta doxológica de Romanos 11:36, olhos fixos no trono.",
                "badge": "BLOCO 4 • MAJESTADE",
                "color": "amber"
            }
        ]
    },
    "roteiro_2": {
        "id": "roteiro_2",
        "title": "Roteiro 2: Foco na Majestade Divina (Domingo à Noite)",
        "objective": "Tirar o foco das circunstâncias humanas e focar nos atributos imutáveis de Deus.",
        "songs": [
            {
                "order": 1,
                "step": "Abertura",
                "title": "Filho do Deus vivo",
                "artist": "Nívea Soares",
                "block": 1,
                "block_name": "Bloco 1 - Chamada",
                "key": "D",
                "tempo": "Rápido / Moderado (118 BPM)",
                "transition": "Abertura firme sem enrolação",
                "notes": "Declaração rápida de identidade cristológica (Mateus 16).",
                "badge": "BLOCO 1 • CELEBRAÇÃO",
                "color": "blue"
            },
            {
                "order": 2,
                "step": "Transição",
                "title": "Jesus é o caminho",
                "artist": "Heloísa Rosa",
                "block": 4,
                "block_name": "Bloco 4 - Adoração Doxológica",
                "key": "Em",
                "tempo": "Médio / Firme (90 BPM)",
                "transition": "Transição harmônica com pad em Ré menor/Mi menor",
                "notes": "Vacina teológica contra o pluralismo e o relativismo.",
                "badge": "BLOCO 4 • MAJESTADE",
                "color": "amber"
            },
            {
                "order": 3,
                "step": "Contrição",
                "title": "Diante da Cruz",
                "artist": "Aline Barros",
                "block": 2,
                "block_name": "Bloco 2 - Contrição",
                "key": "D",
                "tempo": "Lento (68 BPM)",
                "transition": "Banda reduz a intensidade; só violão e piano",
                "notes": "A banda reduz volume; a igreja canta o abandono do orgulho.",
                "badge": "BLOCO 2 • CONTRIÇÃO",
                "color": "purple"
            },
            {
                "order": 4,
                "step": "Imersão",
                "title": "É Ele",
                "artist": "Drops",
                "block": 4,
                "block_name": "Bloco 4 - Adoração Doxológica",
                "key": "G",
                "tempo": "Worship Moderno (70 BPM)",
                "transition": "Crescente contínuo de dinâmica até o refrão",
                "notes": "Letra focada na preeminência absoluta de Cristo (Colossenses 1).",
                "badge": "BLOCO 4 • MAJESTADE",
                "color": "amber"
            },
            {
                "order": 5,
                "step": "Encerramento",
                "title": "Quão grande é meu Deus",
                "artist": "Soraya Morais",
                "block": 4,
                "block_name": "Bloco 4 - Adoração Doxológica",
                "key": "C",
                "tempo": "Lento / Grandioso (68 BPM)",
                "transition": "Modulação suave para Dó; congregação cantando em uníssono",
                "notes": "Nivela todas as faixas etárias de Inhumas em uníssono.",
                "badge": "BLOCO 4 • MAJESTADE",
                "color": "amber"
            }
        ]
    },
    "roteiro_3": {
        "id": "roteiro_3",
        "title": "Roteiro 3: Foco na Escatologia e Esperança (Culto de Ceia)",
        "objective": "Foco na mesa, na comunhão e na urgência do retorno corpóreo de Cristo.",
        "songs": [
            {
                "order": 1,
                "step": "Abertura Histórica",
                "title": "HCC 193 - A Deus demos glória",
                "artist": "Hinário Batista",
                "block": 1,
                "block_name": "Bloco 1 - Histórico",
                "key": "G",
                "tempo": "Solene / Moderno (95 BPM)",
                "transition": "Resgate histórico com arranjo contemporâneo",
                "notes": "Resgate da densidade teológica com arranjo atual da banda.",
                "badge": "BLOCO 1 • HISTÓRICO",
                "color": "blue"
            },
            {
                "order": 2,
                "step": "Celebração",
                "title": "Vitorioso És",
                "artist": "Gabriel Guedes",
                "block": 5,
                "block_name": "Bloco 5 - Escatologia",
                "key": "C",
                "tempo": "Vibrante / Triunfal (74 BPM)",
                "transition": "Entrada de bateria cheia nos toms",
                "notes": "Celebra o túmulo vazio e a derrota definitiva da morte.",
                "badge": "BLOCO 5 • ESCATOLOGIA",
                "color": "emerald"
            },
            {
                "order": 3,
                "step": "Dependência",
                "title": "Meu respirar",
                "artist": "Gabriela Rocha / Vineyard",
                "block": 2,
                "block_name": "Bloco 2 - Contrição",
                "key": "G",
                "tempo": "Lento / Íntimo (64 BPM)",
                "transition": "Queda de dinâmica para momento solene da Ceia",
                "notes": "Prepara para a Ceia; Cristo como sustentação diária e vital.",
                "badge": "BLOCO 2 • CONTRIÇÃO",
                "color": "purple"
            },
            {
                "order": 4,
                "step": "Adoração",
                "title": "Canção do Apocalipse",
                "artist": "Diante do Trono",
                "block": 5,
                "block_name": "Bloco 5 - Escatologia",
                "key": "C",
                "tempo": "Solene / Épico (62 BPM)",
                "transition": "Construção épica; transição do teto da igreja para o céu",
                "notes": "Transporta a igreja para a visão celestial de Apocalipse 4.",
                "badge": "BLOCO 5 • ESCATOLOGIA",
                "color": "emerald"
            },
            {
                "order": 5,
                "step": "Envio",
                "title": "A Benção",
                "artist": "Gabriel Guedes",
                "block": 5,
                "block_name": "Bloco 5 - Envio",
                "key": "G",
                "tempo": "Lento / Bênção (68 BPM)",
                "transition": "Modulação suave para a oração pastoral final",
                "notes": "Liberação pastoral apostólica (Números 6) sobre as famílias.",
                "badge": "BLOCO 5 • ENVIO",
                "color": "emerald"
            }
        ]
    }
}

# Atualizar all_services.json para os cultos de Outubro com setlists litúrgicos reais
with open('all_services.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

oct_services = all_data.get('Out', [])
if len(oct_services) > 1:
    # 04/10: Ceia do Senhor -> Roteiro 3
    oct_services[1]['songs'] = LITURGICAL_ROUTINES['roteiro_3']['songs']
if len(oct_services) > 3:
    # 11/10: Gerações -> Roteiro 2
    oct_services[3]['songs'] = LITURGICAL_ROUTINES['roteiro_2']['songs']
if len(oct_services) > 5:
    # 18/10: Reviva Canções -> Roteiro 1
    oct_services[5]['songs'] = LITURGICAL_ROUTINES['roteiro_1']['songs']
if len(oct_services) > 7:
    # 25/10: Profético -> Setlist especial focado na soberania e visão do Espírito
    oct_services[7]['songs'] = [
        {
            "order": 1,
            "step": "Abertura",
            "title": "Hosana",
            "artist": "Diante do Trono",
            "block": 1,
            "block_name": "Bloco 1 - Chamada",
            "key": "G",
            "tempo": "Dinâmica Crescente (115 BPM)",
            "transition": "Pad em G -> Emenda direta",
            "notes": "Dinâmica crescente convocando a congregação.",
            "badge": "BLOCO 1 • CELEBRAÇÃO",
            "color": "blue"
        },
        {
            "order": 2,
            "step": "Clamor",
            "title": "Abram-se os Portais",
            "artist": "Fhop Music",
            "block": 1,
            "block_name": "Bloco 1 - Chamada",
            "key": "E",
            "tempo": "Solene / Enérgico (110 BPM)",
            "transition": "Modulação direta",
            "notes": "Invocação baseada no Salmo 24.",
            "badge": "BLOCO 1 • CELEBRAÇÃO",
            "color": "blue"
        },
        {
            "order": 3,
            "step": "Quebrantamento",
            "title": "Fogo Purificador",
            "artist": "Vineyard",
            "block": 2,
            "block_name": "Bloco 2 - Contrição",
            "key": "D",
            "tempo": "Lento (66 BPM)",
            "transition": "Queda de dinâmica para oração e arrependimento",
            "notes": "Busca por santificação e caráter refinado (Malaquias 3).",
            "badge": "BLOCO 2 • CONTRIÇÃO",
            "color": "purple"
        },
        {
            "order": 4,
            "step": "Adoração",
            "title": "Canção do Apocalipse",
            "artist": "Diante do Trono",
            "block": 5,
            "block_name": "Bloco 5 - Escatologia",
            "key": "C",
            "tempo": "Solene / Épico (62 BPM)",
            "transition": "Construção de dinâmica progressiva",
            "notes": "A visão celestial de Apocalipse 4.",
            "badge": "BLOCO 5 • ESCATOLOGIA",
            "color": "emerald"
        },
        {
            "order": 5,
            "step": "Envio",
            "title": "O Espírito e a Noiva",
            "artist": "Fhop Music",
            "block": 5,
            "block_name": "Bloco 5 - Escatologia",
            "key": "Am",
            "tempo": "Clamor Crescente (70 BPM)",
            "transition": "Espontâneo final com ministração pastoral",
            "notes": "Apocalipse 22. Clamor coletivo com intensidade crescente.",
            "badge": "BLOCO 5 • ESCATOLOGIA",
            "color": "emerald"
        }
    ]

# Salva all_services.json atualizado
with open('all_services.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print("all_services.json atualizado com setlists litúrgicos reais!")

# Salva arquivo auxiliar songs_data.json
with open('songs_data.json', 'w', encoding='utf-8') as f:
    json.dump({
        'approved_songs': APPROVED_SONGS,
        'liturgical_routines': LITURGICAL_ROUTINES
    }, f, ensure_ascii=False, indent=2)

print("songs_data.json gerado com sucesso!")
