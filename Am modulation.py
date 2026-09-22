import numpy as np
import matplotlib.pyplot as plt

# 1. Parâmetros dos Sinais
fs = 3000                          
t = np.linspace(0, 1, fs)          

fc = 45                            # Frequência bem mais alta para mudar a densidade visual
fm = 3                             # Frequência ligeiramente alterada

Ac = 1.0                           
Am = 0.7                           

# 2. Geração dos Sinais
carrier = Ac * np.sin(2 * np.pi * fc * t)
modulating = Am * np.sin(2 * np.pi * fm * t)
modulated = (Ac + modulating) * np.sin(2 * np.pi * fc * t)

# 3. Construção dos Gráficos com Proporções e Alturas Diferentes
# gridspec_kw={'height_ratios': [1, 1.6, 1.2]} muda o tamanho vertical de cada gráfico
fig, axs = plt.subplots(3, 1, figsize=(10, 7), sharex=True, 
                       gridspec_kw={'height_ratios': [1, 1.6, 1.2]})


cor_unica = '#1A365D'

# Primeiro Gráfico: Portadora (Menor altura vertical)
axs[0].plot(t, carrier, color=cor_unica, linewidth=1.2)
axs[0].set_ylabel('Portadora', fontsize=10, fontweight='bold')
axs[0].grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')

# Segundo Gráfico: Sinal Modulante (Destacado - Muito maior que os outros)
axs[1].plot(t, modulating, color=cor_unica, linewidth=2.5) # Linha bem mais grossa
axs[1].set_ylabel('Informação', fontsize=10, fontweight='bold')
axs[1].grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')

# Terceiro Gráfico: Sinal Modulado 
axs[2].plot(t, modulated, color=cor_unica, linewidth=1.2)
axs[2].set_ylabel('Sinal AM', fontsize=10, fontweight='bold')
axs[2].set_xlabel('Tempo (s)', fontsize=10)
axs[2].grid(True, linestyle=':', alpha=0.5, color='#CBD5E1')

# Estilização das bordas para criar um visual de relatório técnico
for ax in axs:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#94A3B8')
    ax.spines['bottom'].set_color('#94A3B8')
    ax.tick_params(colors='#64748B', labelsize=9)

plt.tight_layout()
plt.show()
