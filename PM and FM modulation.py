import numpy as np
import matplotlib.pyplot as plt

# 1. Parâmetros Ajustados para Máximo Destaque Visual
fs = 4000                          
t = np.linspace(0, 1, fs)          


fc = 12                            # Frequência menor = oscilações mais visíveis
fm = 2                             # Mantemos 2 ciclos completos de informação

Ac = 1.0                           
Am = 1.0                           


beta_fm = 9.0                      # Desvio forte no FM
kp_pm = 3.5                        # Desvio forte no PM

# 2. Geração dos Sinais
carrier = Ac * np.sin(2 * np.pi * fc * t)
modulating = Am * np.sin(2 * np.pi * fm * t)

# Fórmulas de modulação
modulated_fm = Ac * np.sin(2 * np.pi * fc * t - beta_fm * np.cos(2 * np.pi * fm * t))
modulated_pm = Ac * np.sin(2 * np.pi * fc * t + kp_pm * modulating)

# 3. Construção dos Gráficos
fig, axs = plt.subplots(4, 1, figsize=(10, 9), sharex=True, 
                       gridspec_kw={'height_ratios': [1, 1, 1.4, 1.4]})

cor_base = '#0F172A'       # Preto
cor_fm = '#7A1C32'         # Vinho
cor_pm = '#4F46E5'         # Indigo
cor_grid = '#E2E8F0'

# Primeiro Gráfico: Portadora
axs[0].plot(t, carrier, color=cor_base, linewidth=1.2)
axs[0].set_ylabel('Portadora', fontsize=10, fontweight='bold')

# Segundo Gráfico: Sinal Modulante Único
axs[1].plot(t, modulating, color=cor_base, linewidth=2.5)
axs[1].set_ylabel('Informação', fontsize=10, fontweight='bold')

# Terceiro Gráfico: Onda Modulada PM
axs[2].plot(t, modulated_pm, color=cor_pm, linewidth=1.5) # Linha ligeiramente mais grossa
axs[2].set_ylabel('Onda Modulada PM', fontsize=10, fontweight='bold')

# Quarto Gráfico: Onda Modulada FM
axs[3].plot(t, modulated_fm, color=cor_fm, linewidth=1.5) # Linha ligeiramente mais grossa
axs[3].set_ylabel('Onda Modulada FM', fontsize=10, fontweight='bold')
axs[3].set_xlabel('Tempo (s) →', fontsize=10)

# Traços Comparativos Verticais nos picos e vales da informação
picos_e_vales = [0.125, 0.375, 0.625, 0.875]
for pt in picos_e_vales:
    for ax in axs:
        ax.axvline(x=pt, color='#CBD5E1', linestyle='--', linewidth=1.2, zorder=0)

# Estilização
for ax in axs:
    ax.grid(True, linestyle=':', alpha=0.3, color='#CBD5E1')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#94A3B8')
    ax.spines['bottom'].set_color('#94A3B8')
    ax.tick_params(colors='#64748B', labelsize=9)

plt.tight_layout()
plt.show()
