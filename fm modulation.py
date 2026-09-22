import numpy as np
import matplotlib.pyplot as plt

# 1. Parâmetros dos Sinais
fs = 4000                          
t = np.linspace(0, 1, fs)          

fc = 30                            # Frequência central da Portadora
fm = 3                             # Frequência do Sinal Modulante (Informação)

Ac = 1.0                           
Am = 1.0                           
beta = 8.0                         # Índice de modulação FM

# 2. Geração dos Sinais (Matemática do FM)
carrier = Ac * np.sin(2 * np.pi * fc * t)
modulating = Am * np.sin(2 * np.pi * fm * t)
modulated_fm = Ac * np.sin(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))

# 3. Construção dos Gráficos com Índices Corrigidos
fig, axs = plt.subplots(3, 1, figsize=(10, 7), sharex=True, 
                       gridspec_kw={'height_ratios': [1, 1.6, 1.2]})


cor_fm_distinta = '#7A1C32'

# Primeiro Gráfico: Portadora (Acessado via axs[0])
axs[0].plot(t, carrier, color=cor_fm_distinta, linewidth=1.2)
axs[0].set_ylabel('Portadora', fontsize=10, fontweight='bold')
axs[0].grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')

# Segundo Gráfico: Sinal Modulante (Acessado via axs[1])
axs[1].plot(t, modulating, color=cor_fm_distinta, linewidth=2.5)
axs[1].set_ylabel('Informação', fontsize=10, fontweight='bold')
axs[1].grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')

# Terceiro Gráfico: Sinal Modulado em Frequência (Acessado via axs[2])
axs[2].plot(t, modulated_fm, color=cor_fm_distinta, linewidth=1.2)
axs[2].set_ylabel('Sinal FM', fontsize=10, fontweight='bold')
axs[2].set_xlabel('Tempo (s)', fontsize=10)
axs[2].grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')

# Estilização das bordas aplicando em cada elemento do array axs
for ax in axs:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#94A3B8')
    ax.spines['bottom'].set_color('#94A3B8')
    ax.tick_params(colors='#64748B', labelsize=9)

plt.tight_layout()
plt.show()
