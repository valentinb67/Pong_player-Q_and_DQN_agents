import matplotlib.pyplot as plt
import pandas as pd

# Lire les fichiers CSV
df_q_learning_discret = pd.read_csv('/Users/valen/Documents/GitHub/Pong-player-DQN-agent/LearningData/1_q_learning_log.csv')
df_q_learning_decay = pd.read_csv('/Users/valen/Documents/GitHub/Pong-player-DQN-agent/LearningData/1.1_q_learning_decay_log.csv')
df_q_learning_rdm = pd.read_csv('/Users/valen/Documents/GitHub/Pong-player-DQN-agent/LearningData/1.2_q_learning_rdm_log.csv')
df_q_continuous = pd.read_csv('/Users/valen/Documents/GitHub/Pong-player-DQN-agent/LearningData/1.5_q_learning_continuous_log.csv')
df_dqn_discret = pd.read_csv('/Users/valen/Documents/GitHub/Pong-player-DQN-agent/LearningData/2_pong_dqn_discret_training_log.csv')
df_dqn_continu = pd.read_csv('/Users/valen/Documents/GitHub/Pong-player-DQN-agent/LearningData/2.5_pong_dqn_continuous_training_log.csv')
df_Ddqn_discret = pd.read_csv('/Users/valen/Documents/GitHub/Pong-player-DQN-agent/LearningData/3_pong_double_dqn_discret_training_log.csv')
df_Ddqn_continu = pd.read_csv('/Users/valen/Documents/GitHub/Pong-player-DQN-agent/LearningData/3.5_pong_double_dqn_continuous_training_log.csv')

# Liste des DataFrames et leurs étiquettes pour les légendes
df_q_discret = [
    (df_q_learning_rdm, 'Q-Learning Rdm'),
    (df_q_learning_discret, 'Q-Learning Discret'),
    (df_q_continuous, 'Q-Learning Continu'),
    (df_q_learning_decay,'Q-learning Decay')
]

# Définir une palette de couleurs unique
colors = ['blue', 'orange', 'green', 'violet']
color_map = {label: color for (_, label), color in zip(df_q_discret, colors)}

# Créer des graphiques pour visualiser les données
fig, axs = plt.subplots(4, 1, figsize=(10, 15))

# Graphique 1: Epsilon
for df, label in df_q_discret:
    df_filtered = df[df['Episode'] <= 1000]  # Filtrer les épisodes jusqu'à 1000
    if 'Epsilon' in df_filtered.columns:
        axs[0].plot(df_filtered['Episode'], df_filtered['Epsilon'], label=label, color=color_map[label])
axs[0].set_title("Évolution de l'Epsilon")
axs[0].set_xlabel("Épisode")
axs[0].set_ylabel("Epsilon")
axs[0].legend(loc='best')

# Graphique 2: Estimate Value and True Value
for df, label in df_q_discret:
    df_filtered = df[df['Episode'] <= 100]  # Filtrer les épisodes jusqu'à 1000
    if 'Estimate Value' in df_filtered.columns and 'True Value' in df_filtered.columns:
        axs[1].plot(df_filtered['Episode'], df_filtered['Estimate Value'], label=f"{label} (Estimate)", color=color_map[label])
        axs[1].plot(df_filtered['Episode'], df_filtered['True Value'], label=f"{label} (True)", linestyle='--', color=color_map[label])
axs[1].set_title("Valeurs Estimées et Réelles")
axs[1].set_xlabel("Épisode")
axs[1].set_ylabel("Valeur")
axs[1].legend(loc='best')

# Graphique 3: Fonction de perte (Loss)
for df, label in df_q_discret:
    df_filtered = df[df['Episode'] <= 1000]
    if 'Loss' in df_filtered.columns:
        axs[2].plot(df_filtered['Episode'], df_filtered['Loss'], label=label, color=color_map[label])
axs[2].set_title('Évolution de la fonction de perte (Loss)')
axs[2].set_xlabel("Épisode")
axs[2].set_ylabel("Loss")
axs[2].legend(loc='best')

# Graphique 4: Nombre de touche
for df, label in df_q_discret:
    df_filtered = df[df['Episode'] <= 1000]
    if 'Touches Globales' in df_filtered.columns:
        axs[3].plot(df_filtered['Episode'], df_filtered['Touches Globales'], label=label, color=color_map[label])
axs[3].set_title("Évolution du Nombre de touches")
axs[3].set_xlabel("Épisode")
axs[3].set_ylabel("Nombre de touches cumulées")
axs[3].legend(loc='best')

# Afficher les graphiques
plt.tight_layout()
plt.show()
