import matplotlib.pyplot as plt

# Dados das epocas
epocas = [1, 2, 3, 4, 5]

# Dados de acuracia
acuracia_treino = [0.65, 0.79, 0.85, 0.90, 0.92]
acuracia_valid = [0.62, 0.74, 0.82, 0.86, 0.89]

# Dados de perda
perda_treino = [0.80, 0.50, 0.35, 0.25, 0.18]
perda_valid = [0.88, 0.60, 0.45, 0.35, 0.30]

# Cria figura com 2 graficos lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- GRAFICO 1 - ACURACIA ---
ax1.plot(epocas, acuracia_treino, marker='o', label='Treino', linewidth=2)
ax1.plot(epocas, acuracia_valid, marker='s', label='Validacao', linewidth=2)
ax1.set_title('Acuracia do Modelo', fontweight='bold')
ax1.set_xlabel('Epocas')
ax1.set_ylabel('Acuracia')
ax1.set_ylim(0.5, 1.0)
ax1.legend()
ax1.grid(True, alpha=0.3)

# --- GRAFICO 2 - PERDA ---
ax2.plot(epocas, perda_treino, marker='o', label='Treino', linewidth=2)
ax2.plot(epocas, perda_valid, marker='s', label='Validacao', linewidth=2)
ax2.set_title('Perda do Modelo', fontweight='bold')
ax2.set_xlabel('Epocas')
ax2.set_ylabel('Perda (Loss)')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()

# Salva sem acento pra nao dar erro
plt.savefig('graficos_tcc_final.png', dpi=300)
plt.show()

print("2 GRAFICOS GERADOS COM SUCESSO!")