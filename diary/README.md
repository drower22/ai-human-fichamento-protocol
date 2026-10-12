# Diário de bordo

Um arquivo por dia de trabalho: `YYYY-MM-DD.md`. O diário faz parte da
auditoria do protocolo — registra decisões, comandos executados, bloqueios
e aprendizados que não aparecem nos artefatos finais.

## Template de entrada

```markdown
# YYYY-MM-DD

## Feito
- …

## Decisões (e por quê)
- …

## Comandos / gerações relevantes
- `fichamento pdf2md --round 1` → …

## Bloqueios / pendências
- …

## Próximos passos
- …
```

Regras:

1. **Toda** sessão de trabalho gera (ou atualiza) a entrada do dia.
2. Decisões metodológicas relevantes também vão para `protocol/` — o diário
   aponta, o protocolo formaliza.
3. Entradas são append-only: corrija adicionando nota, não reescrevendo.
