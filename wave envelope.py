import numpy as np
import matplotlib.pyplot as plt

# 1. Parâmetros dos Sinais
fs = 3000                          # Taxa de amostragem alta para curvas suaves
t = np.linspace(0, 1, fs)          

fc = 30                            # Frequência da portadora (alta frequência)
fm = 3                             # Frequência do sinal modulante (baixa frequência)

Ac = 1.0                           # Amplitude da portadora
Am = 0.6                           # Amplitude do sinal modulante

# 2. Geração dos Sinais e da Envoltória
modulating = Am * np.sin(2 * np.pi * fm * t)
modulated = (Ac + modulating) * np.sin(2 * np.pi * fc * t)

# As envoltórias positiva e negativa correspondem a: Ac + m(t) e -(Ac + m(t))
envelope_pos = Ac + modulating
envelope_neg = -(Ac + modulating)

# 3. Construção dos Gráficos Lado a Lado (1 linha, 2 colunas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharey=True)

# Cor principal para os sinais 
cor_sinal = '#1A365D'
# Cor para a envoltória tracejada 
cor_envoltoria = '#64748B'

# --- GRÁFICO DA ESQUERDA: Sinal Modulante (Informação) ---
ax1.plot(t, modulating, color=cor_sinal, linewidth=2.5, label='Sinal Modulante $m(t)$')
ax1.set_title('Sinal Modulante (Informação)', fontsize=12, fontweight='bold', color='#1A365D')
ax1.set_xlabel('Tempo (s)', fontsize=10)
ax1.set_ylabel('Amplitude', fontsize=10)
ax1.grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')
ax1.legend(loc='upper right')

# --- GRÁFICO DA DIREITA: Sinal Modulado com Envoltória ---
# Sinal AM interno
ax2.plot(t, modulated, color=cor_sinal, linewidth=1.0, alpha=0.7, label='Sinal Modulado AM')

# Envoltória Superior Tracejada
ax2.plot(t, envelope_pos, color=cor_envoltoria, linestyle='--', linewidth=2.0, 
         label='Envoltória $A_c + m(t)$')

# Envoltória Inferior Tracejada
ax2.plot(t, envelope_neg, color=cor_envoltoria, linestyle='--', linewidth=2.0)

ax2.set_title('Sinal Modulado com Envoltória', fontsize=12, fontweight='bold', color='#1A365D')
ax2.set_xlabel('Tempo (s)', fontsize=10)
ax2.grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')
ax2.legend(loc='upper right')

# --- Estilização de Bordas e Eixos (Mantendo o estilo anterior) ---
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#94A3B8')
    ax.spines['bottom'].set_color('#94A3B8')
    ax.tick_params(colors='#64748B', labelsize=9)

# Ajusta o espaçamento para evitar cortes nas legendas e títulos
plt.tight_layout()

# Exibe o gráfico estruturado
plt.show()
