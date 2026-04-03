# 📊 Análisis Estratégico de la Juventud — Parroquia de O Milladoiro

> Proyecto de ciencia de datos aplicado a una encuesta comunitaria real (n=30).  
> Los resultados fueron presentados a la parroquia de O Milladoiro como hoja de ruta para el diseño de actividades dirigidas a jóvenes de 18 a 35 años en el municipio de Ames (Galicia).

---

## 🗂️ Índice

1. [Contexto y objetivos](#-contexto-y-objetivos)
2. [Stack tecnológico](#-stack-tecnológico)
3. [Estructura del proyecto](#-estructura-del-proyecto)
4. [Metodología](#-metodología)
5. [Análisis exploratorio (EDA)](#-análisis-exploratorio-eda)
6. [Segmentación por clustering](#-segmentación-por-clustering)
7. [Validación con datos del IGE](#-validación-con-datos-del-ige)
8. [Canales de comunicación](#-canales-de-comunicación)
9. [Conclusiones estratégicas](#-conclusiones-estratégicas)
10. [Limitaciones y próximos pasos](#-limitaciones-y-próximos-pasos)
11. [Cómo ejecutar el proyecto](#-cómo-ejecutar-el-proyecto)

---

## 🎯 Contexto y objetivos

La parroquia de O Milladoiro (municipio de Ames, Galicia) detecta una desconexión creciente con el segmento de población joven. Este proyecto aplica técnicas de ciencia de datos para cuantificar esa brecha, identificar perfiles de jóvenes y proponer una hoja de ruta basada en evidencia.

**Objetivos técnicos:**

- Diseñar y analizar una encuesta comunitaria propia de 10 preguntas (n=30)
- Segmentar los perfiles de respuesta mediante **K-Means clustering**
- Contrastar la muestra con el censo oficial del **IGE 2025** vía API
- Identificar las actividades y canales de comunicación con mayor potencial de impacto

---

## 🛠️ Stack tecnológico

| Categoría | Herramientas |
|---|---|
| Lenguaje | Python 3.11 |
| Análisis de datos | pandas, numpy |
| Visualización | matplotlib, seaborn |
| Machine Learning | scikit-learn (K-Means) |
| Datos externos | API del IGE (Instituto Galego de Estatística) |
| Almacenamiento | CSV + módulos src/ |
| Entorno | Jupyter Notebook |

---

## 📁 Estructura del proyecto

```
analisis-secularizacion-milladoiro/
│
├── data/                  # Datos crudos: CSV de la encuesta y datos IGE
├── notebooks/             # Análisis principal en Jupyter
├── outputs/
│   └── figures/           # Gráficos generados automáticamente
├── src/
│   ├── base_datos.py      # Carga y limpieza de datos
│   └── modelos_ia.py      # Lógica de clustering K-Means
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔬 Metodología

**Recogida de datos**: encuesta de 10 preguntas diseñada ad hoc, distribuida entre el 23 y el 26 de marzo de 2026. Recoge variables sociodemográficas (edad, género, ocupación, tiempo de residencia), nivel de participación parroquial, conexión percibida con el mensaje de la iglesia, barreras de participación, preferencias de actividad, horario y canal de comunicación.

**Procesamiento**: limpieza con pandas, codificación de variables categóricas y respuestas múltiples (one-hot encoding), normalización para clustering.

**Validación externa**: contraste de la distribución muestral con los datos de población del IGE 2025 para el municipio de Ames, obtenidos vía API oficial.

**Segmentación**: algoritmo K-Means aplicado sobre las variables de interés, con número de clusters determinado por el método del codo.

---

## 📈 Análisis exploratorio (EDA)

### 1. Distribución de la muestra por grupos de edad

![Distribución por grupos](outputs/figures/01_distribucion_grupos.png)

La muestra recoge respuestas entre los 18 y los 52 años. El grueso de participantes se concentra en el tramo **30–40 años**, con predominio femenino (~83%). El tramo **18–25 años (Gen Z)** está infrarrepresentado respecto al censo real, lo que condiciona las conclusiones para ese segmento.

---

### 2. Nivel de conexión con la parroquia por grupo de edad

![Conexión por grupo](outputs/figures/02_conexion_por_grupo.png)

La mayoría de encuestados declara participar **"nunca o casi nunca"** en actividades parroquiales. La conexión autopercibida con el mensaje de la iglesia (escala 1–5) es mayoritariamente baja (1–2), con excepciones puntuales en perfiles que ya participan semanalmente.

---

### 3. Intereses desglosados por edad

![Intereses por edad](outputs/figures/03_intereses_por_edad.png)

Cruce entre tramos de edad y tipos de actividad preferida. El **deporte y las rutas** (incluyendo el Camino de Santiago) aparecen como el interés transversal más sólido en todos los grupos. Los eventos sociales son la segunda opción más elegida, especialmente entre 30–40 años.

---

### 4. Ranking de actividades de mayor interés

![Ranking de actividades](outputs/figures/04_intereses_final_corregido.png)

Ranking ponderado de preferencias sobre el total de la muestra:

| # | Actividad |
|---|---|
| 1 | 🏃 Deporte / Rutas / Camino de Santiago |
| 2 | 🍽️ Eventos sociales (cenas, música, debates) |
| 3 | 🤝 Voluntariado activo |
| 4 | 🧘 Espiritualidad moderna (meditación, silencio) |

---

## 🧠 Segmentación por Clustering

### 5. Mapa estratégico de clusters

![Mapa estratégico de clusters](outputs/figures/06_mapa_estrategico_clusters.png)

Aplicando **K-Means** sobre las variables de interés, actividad y conexión parroquial, se identificaron **3 perfiles diferenciados**:

| Cluster | Perfil | Características |
|---|---|---|
| 🟦 Desconectados activos | 26–35 años | Baja conexión parroquial, alta disposición a participar si la oferta es deportiva o social |
| 🟧 Vinculados ocasionales | 30–40 años | Participación en fechas señaladas, interés en voluntariado y espiritualidad moderna |
| 🟩 Núcleo fiel | Todas las edades | Participación semanal, alta conexión, prescriptores naturales |

> **Hallazgo clave**: el cluster más numeroso es el de *Desconectados activos*. Son jóvenes que **no participan, pero quieren participar** — la barrera no es el rechazo, sino la oferta y los horarios.

---

## 🌍 Validación con datos del IGE

### 6. Evolución de la población joven en Ames (2021–2025)

![Evolución jovenes Ames](outputs/figures/07_evolucion_jovenes_ames.png)

La población joven en Ames muestra una **tendencia de crecimiento sostenido**, especialmente en el tramo 18–26 años. El universo real asciende a **6.116 jóvenes** según las proyecciones del IGE 2025, lo que dimensiona el potencial de captación real.

---

### 7. Distribución detallada por edades simples (2025)

![Distribución Ames 2025](outputs/figures/08_distribucion_ames_2025.png)

Pirámide de edades simples del municipio. Permite identificar los cohortes más numerosos dentro del rango de interés y ajustar la priorización de segmentos.

---

### 8. Comparativa IGE vs. Encuesta

![Comparativa IGE vs Encuesta](outputs/figures/09_comparativa_ige_encuesta.png)

Contraste entre la distribución por edad de la muestra y la distribución real de la población. Se confirma la **infrarrepresentación del tramo 18–25** en la encuesta, lo que refuerza la necesidad de acciones específicas de captación para Gen Z.

---

## 💬 Canales de comunicación

### 9. Preferencia por canales de difusión

![Canales de comunicación](outputs/figures/05_canales_final.png)

Contra la intuición inicial, los encuestados muestran una preferencia por **canales de contacto personal y directo** sobre los puramente digitales. WhatsApp e Instagram son aceptados principalmente para recibir información puntual, no como canal de comunidad. Esto sugiere que la captación inicial requiere presencia física en el territorio.

---

## 💡 Conclusiones estratégicas

**1. El deporte es la palanca de entrada más potente.**
Es el único interés verdaderamente transversal: aparece en todos los grupos de edad y en todos los clusters, incluyendo los más alejados de la parroquia. Una liga deportiva o ruta mensual puede actuar como primer contacto de bajo umbral.

**2. Hay demanda latente sin oferta.**
El cluster *Desconectados activos* (el más numeroso) no rechaza la parroquia: rechaza la oferta actual y los horarios. La tarde (18:00–19:30) o la mañana del domingo (11:00–12:30) son las franjas más viables.

**3. La Gen Z es la oportunidad más urgente.**
La población de 18–26 años crece en Ames según el IGE pero está infrarrepresentada en la encuesta. Requiere una estrategia de captación diferenciada, más digital y centrada en causas concretas (voluntariado, sostenibilidad).

**4. El canal más efectivo es el boca a boca.**
Los datos de canales apuntan a que la comunicación personal supera a la digital en efectividad percibida. Los participantes del *Núcleo fiel* son el activo más valioso como prescriptores en sus redes cercanas.

---

## ⚠️ Limitaciones y próximos pasos

**Limitaciones actuales:**
- Muestra pequeña (n=30), no representativa estadísticamente del universo de 6.116 jóvenes
- Sesgo de género marcado (~83% mujeres)
- Presencia de respuestas fuera del rango objetivo (18–35 años)

**Próximos pasos:**
- Ampliar la muestra hasta n≥100 para validación estadística
- Aplicar test chi-cuadrado para confirmar asociaciones entre variables
- Desarrollar un dashboard interactivo con Dash/Plotly para presentación a la parroquia

---

## ▶️ Cómo ejecutar el proyecto

```bash
# 1. Clonar el repositorio
git clone https://github.com/Powfip/analisis-secularizacion-milladoiro.git
cd analisis-secularizacion-milladoiro

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Abrir el notebook principal
jupyter notebook notebooks/
```

---

*Analista: Filipi · Proyecto: Análisis Secularización O Milladoiro · Ames, Galicia · 2026*
