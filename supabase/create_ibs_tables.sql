-- =========================================================================================
-- IBS ESCALA • TABELAS DEDICADAS NO SUPABASE (OPCIONAL)
-- Projeto: Igreja Batista Shamah Inhumas
-- =========================================================================================

-- 1. TABELA DE ESCALAS MENSAIS E CULTOS
CREATE TABLE IF NOT EXISTS public.ibs_escalas (
  id VARCHAR(100) PRIMARY KEY,
  mes VARCHAR(20) NOT NULL,
  dados JSONB NOT NULL,
  atualizado_em TIMESTAMPTZ DEFAULT NOW()
);

-- 2. TABELA DE CANÇÕES LITÚRGICAS APROVADAS
CREATE TABLE IF NOT EXISTS public.ibs_cancoes (
  id VARCHAR(100) PRIMARY KEY,
  titulo VARCHAR(200) NOT NULL,
  artista VARCHAR(150),
  bloco INT,
  tom VARCHAR(10),
  andamento VARCHAR(50),
  notas TEXT,
  cor VARCHAR(20),
  badge VARCHAR(50),
  atualizado_em TIMESTAMPTZ DEFAULT NOW()
);

-- 3. PERMISSÕES DE ACESSO (ROW LEVEL SECURITY)
ALTER TABLE public.ibs_escalas ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Permitir leitura e escrita para o App IBS Escala"
  ON public.ibs_escalas FOR ALL TO anon
  USING (true) WITH CHECK (true);

ALTER TABLE public.ibs_cancoes ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Permitir leitura e escrita para canções IBS"
  ON public.ibs_cancoes FOR ALL TO anon
  USING (true) WITH CHECK (true);
