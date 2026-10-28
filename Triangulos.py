import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Laboratorio de Trigonometría",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# FUNCIÓN PARA CREAR EL LIENZO PROPORCIONAL (1:1)
# ==========================================
def crear_lienzo_trigonometrico(max_x, max_y):
    """
    Crea una gráfica de Plotly con escala 1:1 garantizada para que los ángulos
    y longitudes de los triángulos no sufran distorsión visual.
    """
    margen = max(max_x, max_y) * 0.25 + 2.0
    fig = go.Figure()
    
    fig.update_layout(
        xaxis=dict(
            title="Distancia Horizontal X (m)",
            range=[-margen * 0.6, max_x + margen],
            zeroline=True,
            zerolinecolor="rgba(150, 150, 150, 0.4)",
            gridcolor="rgba(200, 200, 200, 0.3)"
        ),
        yaxis=dict(
            title="Altura / Distancia Y (m)",
            range=[-margen * 0.5, max_y + margen],
            zeroline=True,
            zerolinecolor="rgba(150, 150, 150, 0.4)",
            gridcolor="rgba(200, 200, 200, 0.3)",
            scaleanchor="x",  # Mantiene proporción geométrica exacta 1:1
            scaleratio=1
        ),
        height=550,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white"
    )
    return fig

# ==========================================
# BARRA LATERAL (SELECCIÓN DE TEMA)
# ==========================================
st.sidebar.title("📐 Trigonometría Interactiva")
st.sidebar.markdown("Modifica los lados y ángulos para explorar las relaciones de los triángulos.")

tema = st.sidebar.radio(
    "Selecciona el tema de estudio:",
    [
        "1. Triángulo Rectángulo",
        "2. Ley de Senos",
        "3. Ley de Cosenos"
    ]
)

st.sidebar.markdown("---")

# ==============================================================================
# MÓDULO 1: TRIÁNGULO RECTÁNGULO (PITÁGORAS Y RAZONES TRIGONOMÉTRICAS)
# ==============================================================================
if tema == "1. Triángulo Rectángulo":
    st.title("📐 Relaciones en el Triángulo Rectángulo")
    st.markdown(
        "Un **triángulo rectángulo** tiene un ángulo recto ($90^\\circ$). Sus lados se relacionan mediante el "
        "**Teorema de Pitágoras** y las **Razones Trigonométricas** (*SOH-CAH-TOA*)."
    )

    modo_control = st.sidebar.selectbox(
        "¿Qué datos deseas ajustar?",
        ["Dos catetos (a y b)", "Base (b) y Ángulo (α)"]
    )

    if modo_control == "Dos catetos (a y b)":
        b = st.sidebar.slider("Cateto Adyacente / Base (b)", 1.0, 25.0, 12.0, 0.5)
        a = st.sidebar.slider("Cateto Opuesto / Altura (a)", 1.0, 25.0, 9.0, 0.5)
        c = np.sqrt(a**2 + b**2)
        alfa_rad = np.arctan2(a, b)
        alfa_deg = np.degrees(alfa_rad)
    else:
        b = st.sidebar.slider("Cateto Adyacente / Base (b)", 1.0, 25.0, 12.0, 0.5)
        alfa_deg = st.sidebar.slider("Ángulo de elevación α (grados)", 5.0, 80.0, 35.0, 1.0)
        alfa_rad = np.radians(alfa_deg)
        a = b * np.tan(alfa_rad)
        c = b / np.cos(alfa_rad)

    beta_deg = 90.0 - alfa_deg

    col_formulas, col_grafica = st.columns([1.1, 1.5], gap="large")

    with col_formulas:
        st.subheader("1. Teorema de Pitágoras")
        st.latex(r"c = \sqrt{a^2 + b^2}")
        st.latex(rf"c = \sqrt{{{a:.2f}^2 + {b:.2f}^2}} = {c:.2f} \text{{ m}}")

        st.subheader(rf"2. Razones Trigonométricas (para $\alpha = {alfa_deg:.1f}^\circ$)")
        st.markdown("**Seno (Opuesto sobre Hipotenusa):**")
        st.latex(rf"\sin(\alpha) = \frac{{\text{{Cateto Opuesto }}(a)}}{{\text{{Hipotenusa }}(c)}} = \frac{{{a:.2f}}}{{{c:.2f}}} = {np.sin(alfa_rad):.3f}")

        st.markdown("**Coseno (Adyacente sobre Hipotenusa):**")
        st.latex(rf"\cos(\alpha) = \frac{{\text{{Cateto Adyacente }}(b)}}{{\text{{Hipotenusa }}(c)}} = \frac{{{b:.2f}}}{{{c:.2f}}} = {np.cos(alfa_rad):.3f}")

        st.markdown("**Tangente (Opuesto sobre Adyacente):**")
        st.latex(rf"\tan(\alpha) = \frac{{\text{{Cateto Opuesto }}(a)}}{{\text{{Cateto Adyacente }}(b)}} = \frac{{{a:.2f}}}{{{b:.2f}}} = {np.tan(alfa_rad):.3f}")

        st.markdown("---")
        st.write(rf"• **Ángulo $\alpha$ (en el origen):** ${alfa_deg:.1f}^\circ$")
        st.write(rf"• **Ángulo complementario $\beta$ (arriba):** ${beta_deg:.1f}^\circ$")
        st.write(r"• **Ángulo recto $C$:** $90.0^\circ$")

    with col_grafica:
        fig = crear_lienzo_trigonometrico(b, a)

        # 1. Relleno y silueta del triángulo
        fig.add_trace(go.Scatter(
            x=[0, b, b, 0], y=[0, 0, a, 0],
            mode="lines+markers",
            fill="toself",
            fillcolor="rgba(31, 119, 180, 0.08)",
            line=dict(color="#1f77b4", width=3),
            marker=dict(size=8, color="#1f77b4"),
            name="Triángulo Rectángulo"
        ))

        # 2. Cuadrado del ángulo recto (90°) en (b, 0)
        tam_cuadro = min(a, b) * 0.12
        fig.add_trace(go.Scatter(
            x=[b - tam_cuadro, b - tam_cuadro, b],
            y=[0, tam_cuadro, tam_cuadro],
            mode="lines",
            line=dict(color="#d62728", width=2),
            name="Ángulo Recto (90°)"
        ))

        # 3. Arco del ángulo alfa (α) en el origen (0, 0)
        r_alfa = min(b, c) * 0.22
        t_alfa = np.linspace(0, alfa_rad, 30)
        fig.add_trace(go.Scatter(
            x=r_alfa * np.cos(t_alfa),
            y=r_alfa * np.sin(t_alfa),
            mode="lines",
            line=dict(color="#e65100", width=2.5),
            name=f"Ángulo α ({alfa_deg:.1f}°)"
        ))

        # 4. Arco del ángulo beta (β) en el vértice superior (b, a)
        r_beta = min(a, c) * 0.20
        # Barre en sentido horario desde la hipotenusa hacia el cateto vertical
        t_beta = np.linspace(-np.pi + alfa_rad, -np.pi / 2, 30)
        fig.add_trace(go.Scatter(
            x=b + r_beta * np.cos(t_beta),
            y=a + r_beta * np.sin(t_beta),
            mode="lines",
            line=dict(color="#6a1b9a", width=2.5),
            name=f"Ángulo β ({beta_deg:.1f}°)"
        ))

        # 5. Etiquetas de los LADOS (Azul marino oscuro para longitudes)
        fig.add_trace(go.Scatter(
            x=[b / 2, b + max(a, b) * 0.08, b / 2 - max(a, b) * 0.07],
            y=[-max(a, b) * 0.08, a / 2, a / 2 + max(a, b) * 0.07],
            mode="text",
            text=[
                f"<b>b = {b:.2f} m</b> (Adyacente)",
                f"<b>a = {a:.2f} m</b> (Opuesto)",
                f"<b>c = {c:.2f} m</b> (Hipotenusa)"
            ],
            textfont=dict(size=13, color="#0d47a1"),  # Azul oscuro
            name="Medidas de Lados"
        ))

        # 6. Etiquetas de los ÁNGULOS (Naranja para α y Púrpura para β)
        t_beta_mid = (-1.5 * np.pi + alfa_rad) / 2
        fig.add_trace(go.Scatter(
            x=[
                r_alfa * 1.55 * np.cos(alfa_rad / 2),
                b + r_beta * 1.55 * np.cos(t_beta_mid)
            ],
            y=[
                r_alfa * 1.55 * np.sin(alfa_rad / 2),
                a + r_beta * 1.55 * np.sin(t_beta_mid)
            ],
            mode="text",
            text=[
                f"<b>α = {alfa_deg:.1f}°</b>",
                f"<b>β = {beta_deg:.1f}°</b>"
            ],
            textfont=dict(size=14, color=["#b73e00", "#4a148c"]),  # Naranja oscuro y Violeta
            name="Medidas de Ángulos"
        ))

        st.plotly_chart(fig, use_container_width=True)

    # 3 EJERCICIOS APLICATIVOS DE TRIÁNGULO RECTÁNGULO
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos para Bachillerato (Triángulo Rectángulo)")
    tab1, tab2, tab3 = st.tabs([
        "🌲 Ejercicio 1: Altura de un árbol (Tangente)",
        "🛹 Ejercicio 2: Rampa de Skate (Seno y Pitágoras)",
        "🧗 Ejercicio 3: Cable de Tirolesa (Pitágoras y Tangente)"
    ])

    with tab1:
        st.info(
            "**Problema 1:** Durante una práctica en el patio del colegio, quieres medir la altura de un pino muy alto "
            "sin tener que subirte a él. Te alejas caminando por el suelo plano hasta estar a **$b = 12.0\\text{ metros}$** "
            "del tronco y miras hacia la punta del árbol con un transportador casero (clinómetro), midiendo un ángulo de "
            "elevación de **$\\alpha = 35^\\circ$**.\n\n"
            "1. ¿Qué razón trigonométrica relaciona el cateto opuesto ($a$) con el cateto adyacente ($b$)?\n"
            "2. ¿Cuál es la altura ($a$) del árbol? *(Cambia el modo en el menú izquierdo a 'Base (b) y Ángulo (α)' y pon $b = 12$ y $\\alpha = 35^\\circ$ para comprobarlo)*."
        )
        if st.button("Revelar solución del Ejercicio 1", key="btn_tr1"):
            st.success("**Solución paso a paso:**")
            st.markdown(
                "1. Conocemos el **cateto adyacente** ($b = 12.0\\text{ m}$) y el **ángulo** ($\\alpha = 35^\\circ$), "
                "y buscamos el **cateto opuesto** ($a$, la altura). Por tanto, usamos la **Tangente**:"
            )
            st.latex(r"\tan(\alpha) = \frac{\text{Cateto Opuesto }(a)}{\text{Cateto Adyacente }(b)}")
            st.markdown("2. Despejamos la altura $a$ y sustituimos los datos:")
            st.latex(r"a = b \cdot \tan(35^\circ) = 12.0 \cdot (0.7002) \approx 8.40 \text{ metros}")

    with tab2:
        st.info(
            "**Problema 2:** En el parque del barrio están construyendo una rampa recta para patinetas (*skate*). "
            "La tabla inclinada por donde suben los patinadores (la hipotenusa) mide **$c = 5.0\\text{ metros}$** de largo "
            "y su parte más alta está levantada a **$a = 3.0\\text{ metros}$** del suelo.\n\n"
            "1. ¿Cuánto espacio horizontal sobre el suelo ($b$) ocupa la base de la rampa?\n"
            "2. ¿Cuál es el ángulo de inclinación $\\alpha$ que forma la rampa con el piso? *(Pon $b = 4.0$ y $a = 3.0$ en el menú para verlo)*."
        )
        if st.button("Revelar solución del Ejercicio 2", key="btn_tr2"):
            st.success("**Solución paso a paso:**")
            st.markdown("1. **Calculamos la base ($b$) con el Teorema de Pitágoras:** Despejamos $b$ de $a^2 + b^2 = c^2$:")
            st.latex(r"b = \sqrt{c^2 - a^2} = \sqrt{5.0^2 - 3.0^2} = \sqrt{25 - 9} = \sqrt{16} = 4.0 \text{ metros}")
            st.markdown("2. **Calculamos el ángulo $\\alpha$ usando el Seno:** Sabemos que $\\sin(\\alpha) = \\frac{a}{c}$:")
            st.latex(r"\sin(\alpha) = \frac{3.0}{5.0} = 0.600 \implies \alpha = \arcsin(0.600) \approx 36.87^\circ")

    with tab3:
        st.info(
            "**Problema 3:** En un parque ecológico van a instalar una tirolesa (*canopy*) desde lo alto de una torre de madera "
            "de **$a = 9.0\\text{ metros}$** de altura hasta un poste de llegada en el suelo ubicado a **$b = 12.0\\text{ metros}$** "
            "de distancia horizontal desde la base de la torre.\n\n"
            "1. ¿Cuántos metros de cable de acero ($c$) se necesitan como mínimo para unir la torre con el punto de llegada?\n"
            "2. ¿Con qué ángulo de inclinación ($\\alpha$) bajará una persona por el cable?"
        )
        if st.button("Revelar solución del Ejercicio 3", key="btn_tr3"):
            st.success("**Solución paso a paso:**")
            st.markdown("1. **Longitud del cable ($c$):** El cable es la hipotenusa del triángulo rectángulo. Aplicamos Pitágoras con $a = 9.0$ y $b = 12.0$:")
            st.latex(r"c = \sqrt{9.0^2 + 12.0^2} = \sqrt{81 + 144} = \sqrt{225} = 15.0 \text{ metros de cable}")
            st.markdown("2. **Ángulo de inclinación ($\\alpha$):** Usamos la función inversa de la tangente ($\\arctan$):")
            st.latex(r"\tan(\alpha) = \frac{9.0}{12.0} = 0.750 \implies \alpha = \arctan(0.750) \approx 36.87^\circ")


# ==============================================================================
# MÓDULO 2: LEY DE SENOS (TRIÁNGULOS OBLICUÁNGULOS)
# ==============================================================================
elif tema == "2. Ley de Senos":
    st.title("📐 Ley de Senos (Triángulos No Rectángulos)")
    st.markdown(
        "Cuando un triángulo **no tiene ningún ángulo de $90^\\circ$**, no podemos usar Pitágoras directamente. "
        "La **Ley de Senos** establece que la razón entre la longitud de cualquier lado y el seno de su ángulo opuesto es siempre constante. "
        "Se usa especialmente cuando conocemos **dos ángulos y un lado (ALA o LAA)**."
    )

    st.sidebar.subheader("Parámetros de la Ley de Senos")
    c = st.sidebar.slider("Base c (distancia entre A y B)", 5.0, 30.0, 20.0, 1.0)
    A_deg = st.sidebar.slider("Ángulo A (izquierda, en grados)", 15.0, 110.0, 45.0, 1.0)
    B_deg = st.sidebar.slider("Ángulo B (derecha, en grados)", 15.0, 110.0, 60.0, 1.0)

    # Validar que la suma de ángulos sea menor a 180°
    if A_deg + B_deg >= 175.0:
        st.sidebar.error("La suma de los ángulos A y B debe ser menor a 175° para poder cerrar el triángulo.")
        B_deg = 175.0 - A_deg

    C_deg = 180.0 - (A_deg + B_deg)
    A_rad, B_rad, C_rad = np.radians(A_deg), np.radians(B_deg), np.radians(C_deg)

    # Cálculo de los lados a y b por Ley de Senos
    a = c * np.sin(A_rad) / np.sin(C_rad)
    b = c * np.sin(B_rad) / np.sin(C_rad)

    # Coordenadas de los tres vértices: A(0,0), B(c,0), C(x_C, y_C)
    x_C = b * np.cos(A_rad)
    y_C = b * np.sin(A_rad)

    col_formulas, col_grafica = st.columns([1.1, 1.5], gap="large")

    with col_formulas:
        st.subheader("Fórmula de la Ley de Senos")
        st.latex(r"\frac{a}{\sin(A)} = \frac{b}{\sin(B)} = \frac{c}{\sin(C)}")

        st.markdown("**1. Suma de ángulos internos ($180^\\circ$):**")
        st.latex(rf"C = 180^\circ - ({A_deg:.0f}^\circ + {B_deg:.0f}^\circ) = {C_deg:.1f}^\circ")

        st.markdown("**2. Cálculo de los lados desconocidos ($a$ y $b$):**")
        st.latex(rf"a = \frac{{c \cdot \sin(A)}}{{\sin(C)}} = \frac{{{c:.1f} \cdot \sin({A_deg:.0f}^\circ)}}{{\sin({C_deg:.1f}^\circ)}} = {a:.2f} \text{{ m}}")
        st.latex(rf"b = \frac{{c \cdot \sin(B)}}{{\sin(C)}} = \frac{{{c:.1f} \cdot \sin({B_deg:.0f}^\circ)}}{{\sin({C_deg:.1f}^\circ)}} = {b:.2f} \text{{ m}}")

        st.markdown("---")
        st.subheader("Resumen de Medidas")
        st.write(rf"• **Lado $a$ (opuesto a $A$):** ${a:.2f}$ m | **Ángulo $A$:** ${A_deg:.1f}^\circ$")
        st.write(rf"• **Lado $b$ (opuesto a $B$):** ${b:.2f}$ m | **Ángulo $B$:** ${B_deg:.1f}^\circ$")
        st.write(rf"• **Lado $c$ (opuesto a $C$):** ${c:.2f}$ m | **Ángulo $C$:** ${C_deg:.1f}^\circ$")

    with col_grafica:
        fig = crear_lienzo_trigonometrico(max(c, x_C), y_C)

        # Dibujo del triángulo oblicuángulo
        fig.add_trace(go.Scatter(
            x=[0, c, x_C, 0],
            y=[0, 0, y_C, 0],
            mode="lines+markers",
            fill="toself",
            fillcolor="rgba(44, 160, 44, 0.12)",
            line=dict(color="#2ca02c", width=3),
            marker=dict(size=9, color="#d62728"),
            name="Triángulo Oblicuángulo"
        ))

        # Etiquetas en los vértices
        desp = max(c, y_C) * 0.07
        fig.add_trace(go.Scatter(
            x=[0, c, x_C],
            y=[-desp, -desp, y_C + desp],
            mode="text",
            text=[
                f"<b>Vértice A ({A_deg:.0f}°)</b>",
                f"<b>Vértice B ({B_deg:.0f}°)</b>",
                f"<b>Vértice C ({C_deg:.0f}°)</b>"
            ],
            textfont=dict(size=13, color="#d62728"),
            showlegend=False
        ))

        # Etiquetas en los puntos medios de los lados
        fig.add_trace(go.Scatter(
            x=[c / 2, x_C / 2 - desp, (c + x_C) / 2 + desp],
            y=[-desp * 0.8, y_C / 2, y_C / 2],
            mode="text",
            text=[
                f"<b>c = {c:.2f} m</b>",
                f"<b>b = {b:.2f} m</b>",
                f"<b>a = {a:.2f} m</b>"
            ],
            textfont=dict(size=13, color="#1f77b4"),
            showlegend=False
        ))

        st.plotly_chart(fig, use_container_width=True)

    # 2 EJERCICIOS APLICATIVOS DE LEY DE SENOS
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos para Bachillerato (Ley de Senos)")
    tab_s1, tab_s2 = st.tabs([
        "🛸 Ejercicio 1: El dron en la cancha de fútbol",
        "🌉 Ejercicio 2: Medir el ancho de un río sin cruzarlo"
    ])

    with tab_s1:
        st.info(
            "**Problema 1:** Dos estudiantes, Sofía (en el punto $A$) y Mateo (en el punto $B$), están parados en una cancha "
            "de fútbol separados por una distancia de **$c = 20.0\\text{ metros}$**. Entre ellos vuela un dron fotográfico (en el punto $C$). "
            "Sofía mira el dron con un ángulo de elevación de **$A = 45^\\circ$** y Mateo lo mira con un ángulo de **$B = 60^\\circ$**.\n\n"
            "1. ¿Cuánto mide el ángulo superior $C$ que se forma en la posición del dron?\n"
            "2. ¿A qué distancia en línea recta ($b$) se encuentra el dron respecto a Sofía? "
            "*(Ajusta $c = 20$, $A = 45^\\circ$ y $B = 60^\\circ$ en la barra lateral para ver la respuesta gráfica)*."
        )
        if st.button("Revelar solución del Ejercicio 1", key="btn_sen1"):
            st.success("**Solución paso a paso:**")
            st.markdown("1. **Hallamos el tercer ángulo ($C$):** Como los tres ángulos internos de todo triángulo suman $180^\\circ$:")
            st.latex(r"C = 180^\circ - (45^\circ + 60^\circ) = 180^\circ - 105^\circ = 75^\circ")
            st.markdown(
                "2. **Calculamos la distancia de Sofía al dron (lado $b$, opuesto al ángulo $B$):** "
                "Planteamos la proporción de la Ley de Senos entre el lado $b$ y el lado conocido $c = 20.0\\text{ m}$:"
            )
            st.latex(r"\frac{b}{\sin(60^\circ)} = \frac{20.0}{\sin(75^\circ)} \implies b = \frac{20.0 \cdot \sin(60^\circ)}{\sin(75^\circ)}")
            st.latex(r"b = \frac{20.0 \cdot 0.8660}{0.9659} \approx 17.93 \text{ metros}")

    with tab_s2:
        st.info(
            "**Problema 2:** En un campamento juvenil necesitan saber qué tan lejos está una cabaña ($C$) ubicada al otro lado "
            "de un río caudaloso para lanzar una cuerda. Sin cruzar el agua, trazan una línea recta en su propia orilla de "
            "**$c = 15.0\\text{ metros}$** entre dos estacas $A$ y $B$. Desde la estaca $A$ miden un ángulo de **$A = 70^\\circ$** "
            "hacia la cabaña, y desde la estaca $B$ miden un ángulo de **$B = 50^\\circ$**.\n\n"
            "1. ¿Cuánto vale el ángulo $C$ en la cabaña?\n"
            "2. ¿Cuál es la distancia ($a$) desde la estaca $B$ hasta la cabaña $C$? *(Prueba poner $c=15, A=70^\\circ, B=50^\\circ$ en los deslizadores)*."
        )
        if st.button("Revelar solución del Ejercicio 2", key="btn_sen2"):
            st.success("**Solución paso a paso:**")
            st.markdown("1. **Ángulo $C$:** Restamos de $180^\\circ$ los dos ángulos conocidos:")
            st.latex(r"C = 180^\circ - (70^\circ + 50^\circ) = 60^\circ")
            st.markdown("2. **Distancia desde la estaca $B$ a la cabaña $C$ (lado $a$, opuesto al ángulo $A$):** Aplicamos la Ley de Senos:")
            st.latex(r"\frac{a}{\sin(70^\circ)} = \frac{15.0}{\sin(60^\circ)} \implies a = \frac{15.0 \cdot \sin(70^\circ)}{\sin(60^\circ)}")
            st.latex(r"a = \frac{15.0 \cdot 0.9397}{0.8660} \approx 16.28 \text{ metros}")


# ==============================================================================
# MÓDULO 3: LEY DE COSENOS (TRIÁNGULOS OBLICUÁNGULOS)
# ==============================================================================
elif tema == "3. Ley de Cosenos":
    st.title("📐 Ley de Cosenos (Generalización de Pitágoras)")
    st.markdown(
        "La **Ley de Cosenos** se utiliza cuando la Ley de Senos no tiene suficientes parejas de datos. "
        "Funciona en dos casos clásicos: cuando conocemos **dos lados y el ángulo comprendido entre ellos (Caso LAL)**, "
        "o cuando conocemos **los tres lados del triángulo y buscamos un ángulo (Caso LLL)**."
    )

    st.sidebar.subheader("Parámetros de la Ley de Cosenos (Caso LAL)")
    c = st.sidebar.slider("Lado c (base inferior)", 2.0, 25.0, 12.0, 0.5)
    b = st.sidebar.slider("Lado b (lado izquierdo)", 2.0, 25.0, 10.0, 0.5)
    A_deg = st.sidebar.slider("Ángulo A comprendido entre b y c (°)", 15.0, 150.0, 60.0, 1.0)

    A_rad = np.radians(A_deg)

    # Cálculo del tercer lado 'a' mediante la Ley de Cosenos
    a = np.sqrt(b**2 + c**2 - 2 * b * c * np.cos(A_rad))

    # Cálculo de los otros dos ángulos usando Ley de Cosenos (forma LLL)
    cos_B = np.clip((a**2 + c**2 - b**2) / (2 * a * c), -1.0, 1.0)
    B_deg = np.degrees(np.arccos(cos_B))
    C_deg = 180.0 - (A_deg + B_deg)

    # Coordenadas del vértice C
    x_C = b * np.cos(A_rad)
    y_C = b * np.sin(A_rad)

    col_formulas, col_grafica = st.columns([1.15, 1.45], gap="large")

    with col_formulas:
        st.subheader("1. Para hallar un lado (Caso LAL)")
        st.latex(r"a^2 = b^2 + c^2 - 2bc \cdot \cos(A)")
        st.markdown("**Con tus valores actuales:**")
        st.latex(rf"a = \sqrt{{{b:.1f}^2 + {c:.1f}^2 - 2({b:.1f})({c:.1f})\cos({A_deg:.0f}^\circ)}} = {a:.2f} \text{{ m}}")

        st.subheader("2. Para hallar un ángulo conociendo los 3 lados (Caso LLL)")
        st.latex(r"\cos(A) = \frac{b^2 + c^2 - a^2}{2bc}")
        st.latex(rf"\cos(B) = \frac{{a^2 + c^2 - b^2}}{{2ac}} \implies B = {B_deg:.1f}^\circ")

        st.markdown("---")
        st.subheader("Resumen del Triángulo")
        st.write(rf"• **Lado $a$ (calculado):** ${a:.2f}$ m | **Ángulo opuesto $A$:** ${A_deg:.1f}^\circ$")
        st.write(rf"• **Lado $b$ (conocido):** ${b:.2f}$ m | **Ángulo opuesto $B$:** ${B_deg:.1f}^\circ$")
        st.write(rf"• **Lado $c$ (conocido):** ${c:.2f}$ m | **Ángulo opuesto $C$:** ${C_deg:.1f}^\circ$")

    with col_grafica:
        fig = crear_lienzo_trigonometrico(max(c, x_C), y_C)

        # Triángulo
        fig.add_trace(go.Scatter(
            x=[0, c, x_C, 0],
            y=[0, 0, y_C, 0],
            mode="lines+markers",
            fill="toself",
            fillcolor="rgba(148, 103, 189, 0.12)",
            line=dict(color="#9467bd", width=3),
            marker=dict(size=9, color="#d62728"),
            name="Triángulo (Ley de Cosenos)"
        ))

        # Arco del ángulo A conocido
        r_arco = min(b, c) * 0.2
        t_arco = np.linspace(0, A_rad, 30)
        fig.add_trace(go.Scatter(
            x=r_arco * np.cos(t_arco),
            y=r_arco * np.sin(t_arco),
            mode="lines",
            line=dict(color="#ff7f0e", width=3),
            name=f"Ángulo A = {A_deg:.0f}°"
        ))

        # Etiquetas de vértices y lados
        desp = max(c, y_C) * 0.07
        fig.add_trace(go.Scatter(
            x=[0, c, x_C, c / 2, x_C / 2 - desp, (c + x_C) / 2 + desp],
            y=[-desp, -desp, y_C + desp, -desp * 0.8, y_C / 2, y_C / 2],
            mode="text",
            text=[
                f"<b>A ({A_deg:.1f}°)</b>",
                f"<b>B ({B_deg:.1f}°)</b>",
                f"<b>C ({C_deg:.1f}°)</b>",
                f"<b>c = {c:.2f} m</b>",
                f"<b>b = {b:.2f} m</b>",
                f"<b>a = {a:.2f} m</b>"
            ],
            textfont=dict(size=13, color="#222222"),
            showlegend=False
        ))

        st.plotly_chart(fig, use_container_width=True)

    # 2 EJERCICIOS APLICATIVOS DE LEY DE COSENOS
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos para Bachillerato (Ley de Cosenos)")
    tab_c1, tab_c2 = st.tabs([
        "🚴 Ejercicio 1: Dos rutas de ciclismo (Caso LAL)",
        "⚽ Ejercicio 2: El ángulo de tiro libre en el fútbol (Caso LLL)"
    ])

    with tab_c1:
        st.info(
            "**Problema 1 (Caso Lado-Ángulo-Lado):** Desde la entrada de una reserva natural ($A$) salen dos senderos rectos "
            "para bicicleta que se separan formando un ángulo de **$A = 60^\\circ$**. Natalia toma el primer sendero y recorre "
            "**$b = 8.0\\text{ km}$** hasta llegar a una cascada ($C$). Al mismo tiempo, Santiago toma el segundo sendero y pedalea "
            "**$c = 10.0\\text{ km}$** hasta llegar a un mirador ($B$).\n\n"
            "• Si quieren comunicarse con *walkie-talkies* cuyo alcance máximo es de $9.5\\text{ km}$, ¿qué distancia en línea recta ($a$) "
            "separa la cascada del mirador? ¿Lograrán comunicarse? *(Ajusta $c = 10$, $b = 8$ y $A = 60^\\circ$ en la barra lateral)*."
        )
        if st.button("Revelar solución del Ejercicio 1", key="btn_cos1"):
            st.success("**Solución paso a paso:**")
            st.markdown(
                "Como conocemos dos lados ($b = 8.0$, $c = 10.0$) y el ángulo justo en medio de ellos ($A = 60^\\circ$), "
                "aplicamos directamente la **Ley de Cosenos** para hallar el lado opuesto $a$:"
            )
            st.latex(r"a^2 = b^2 + c^2 - 2bc \cdot \cos(A)")
            st.latex(r"a^2 = (8.0)^2 + (10.0)^2 - 2(8.0)(10.0) \cdot \cos(60^\circ)")
            st.markdown("Recordando que $\\cos(60^\\circ) = 0.5$:")
            st.latex(r"a^2 = 64 + 100 - 160(0.5) = 164 - 80 = 84")
            st.latex(r"a = \sqrt{84} \approx 9.17 \text{ km}")
            st.markdown("¡Sí lograrán comunicarse!, ya que están a **$9.17\\text{ km}$**, que es menor al límite de $9.5\\text{ km}$.")

    with tab_c2:
        st.info(
            "**Problema 2 (Caso Lado-Lado-Lado):** En un partido de fútbol del torneo intercolegiado, vas a cobrar un tiro libre "
            "desde el punto $A$. La distancia desde el balón hasta el poste izquierdo de la portería ($C$) es de **$b = 10.0\\text{ metros}$**, "
            "y la distancia desde el balón hasta el poste derecho ($B$) es de **$c = 12.0\\text{ metros}$**. Si el ancho de la portería "
            "entre ambos postes es de **$a = 8.0\\text{ metros}$**:\n\n"
            "• ¿Con qué ángulo de apertura ($A$) ves el arco para patear y anotar el gol?"
        )
        if st.button("Revelar solución del Ejercicio 2", key="btn_cos2"):
            st.success("**Solución paso a paso:**")
            st.markdown(
                "Conocemos los **tres lados** del triángulo ($a = 8.0\\text{ m}$, $b = 10.0\\text{ m}$ y $c = 12.0\\text{ m}$). "
                "Despejamos $\\cos(A)$ de la Ley de Cosenos:"
            )
            st.latex(r"\cos(A) = \frac{b^2 + c^2 - a^2}{2bc}")
            st.latex(r"\cos(A) = \frac{10.0^2 + 12.0^2 - 8.0^2}{2(10.0)(12.0)} = \frac{100 + 144 - 64}{240} = \frac{180}{240} = 0.750")
            st.markdown("Aplicamos el coseno inverso ($\\arccos$) en la calculadora:")
            st.latex(r"A = \arccos(0.750) \approx 41.41^\circ")
            st.markdown(
                "Tienes un ángulo de disparo de **$41.4^\\circ$**. *(Si pones $b=10$, $c=12$ y mueves el ángulo $A$ a $41^\\circ$ en el menú, "
                "verás que el lado $a$ mide aproximadamente $8.0\\text{ m}$)*."
            )