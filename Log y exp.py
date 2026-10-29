import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Funciones y Ecuaciones: Exponencial y Logarítmica",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# FUNCIONES AUXILIARES DE FORMATO Y GRÁFICA
# ==========================================
def signo_str(val):
    """Formatea números con su signo para mostrar limpiamente en LaTeX."""
    return f"- {abs(val):.1f}" if val >= 0 else f"+ {abs(val):.1f}"

def suma_str(val):
    """Formatea constantes sumadas o restadas al final de una expresión."""
    if val > 0:
        return f"+ {val:.1f}"
    elif val < 0:
        return f"- {abs(val):.1f}"
    return ""

def crear_lienzo_cartesiano(rango_x=(-8, 8), rango_y=(-8, 15), titulo_x="Eje X", titulo_y="Eje Y"):
    """Crea una figura de Plotly con ejes coordenados bien definidos y alto contraste."""
    fig = go.Figure()
    fig.add_hline(y=0, line_width=1.5, line_color="rgba(80, 80, 80, 0.6)")
    fig.add_vline(x=0, line_width=1.5, line_color="rgba(80, 80, 80, 0.6)")
    
    fig.update_layout(
        xaxis=dict(
            title=titulo_x,
            range=list(rango_x),
            zeroline=False,
            gridcolor="rgba(200, 200, 200, 0.35)"
        ),
        yaxis=dict(
            title=titulo_y,
            range=list(rango_y),
            zeroline=False,
            gridcolor="rgba(200, 200, 200, 0.35)"
        ),
        height=540,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white"
    )
    return fig

# ==========================================
# BARRA LATERAL (NAVEGACIÓN)
# ==========================================
st.sidebar.title("📈 Exponenciales y Logaritmos")
st.sidebar.markdown("Laboratorio interactivo de funciones, modelación y resolución de ecuaciones.")

modulo = st.sidebar.radio(
    "Selecciona la sección de estudio:",
    [
        "1. Función Exponencial y Modelos",
        "2. Función Logarítmica y Modelos",
        "3. Ecuaciones Exponenciales (Bases Iguales)",
        "4. Ecuaciones Logarítmicas (Propiedades)"
    ]
)

st.sidebar.markdown("---")

# ==============================================================================
# MÓDULO 1: FUNCIÓN EXPONENCIAL Y MODELOS APLICADOS
# ==============================================================================
if modulo == "1. Función Exponencial y Modelos":
    st.title("📈 Función Exponencial: $f(x) = a \\cdot b^{x - h} + k$")
    st.markdown(
        "En una **función exponencial**, la variable independiente $x$ figura en el **exponente**. "
        "Sirve para modelar fenómenos que se multiplican por un factor constante en cada etapa "
        "(como poblaciones, interés compuesto o fractales geométricos)."
    )

    st.sidebar.subheader("Parámetros de la Función")
    a = st.sidebar.slider("Coeficiente inicial (a)", -5.0, 5.0, 1.0, 0.5)
    if a == 0:
        a = 1.0
        st.sidebar.warning("El coeficiente 'a' no puede ser 0. Se ajustó a 1.0.")

    b = st.sidebar.slider("Base exponencial (b)", 0.2, 4.0, 2.0, 0.1)
    if abs(b - 1.0) < 0.05:
        b = 2.0
        st.sidebar.warning("La base 'b' debe ser distinta de 1. Se ajustó a 2.0.")

    h = st.sidebar.slider("Desplazamiento horizontal (h)", -5.0, 5.0, 0.0, 0.5)
    k = st.sidebar.slider("Asíntota horizontal (k)", -5.0, 5.0, 0.0, 0.5)

    st.sidebar.markdown("---")
    st.sidebar.subheader("Calculadora de Evaluación y Despeje")
    x_eval = st.sidebar.number_input("1. Evaluar f(x) para x =", value=2.0, step=0.5)
    y_eval = a * (b ** (x_eval - h)) + k

    # Cálculo matemático de la curva
    x_vals = np.linspace(-8, 8, 500)
    y_vals = a * (b ** (x_vals - h)) + k
    corte_y = a * (b ** (-h)) + k

    if b > 1:
        comportamiento = "Crecimiento exponencial (b > 1)" if a > 0 else "Decrecimiento reflejado (b > 1, a < 0)"
    else:
        comportamiento = "Decaimiento exponencial (0 < b < 1)" if a > 0 else "Crecimiento reflejado (0 < b < 1, a < 0)"

    rango_str = rf"({k:.1f}, +\infty)" if a > 0 else rf"(-\infty, {k:.1f})"

    col_info, col_graf = st.columns([1.15, 1.45], gap="large")

    with col_info:
        st.subheader("Análisis Matemático")
        st.markdown("**Fórmula General:**")
        st.latex(r"f(x) = a \cdot b^{x - h} + k")

        st.markdown("**Ecuación con tus valores actuales:**")
        st.latex(rf"f(x) = {a:.1f} \cdot ({b:.1f})^{{x {signo_str(h)}}} {suma_str(k)}")

        st.markdown("---")
        st.subheader("Propiedades de la Gráfica")
        st.write(f"• **Tipo de curva:** {comportamiento}")
        st.write(r"• **Dominio:** Todos los números reales $(-\infty, +\infty)$")
        st.write(rf"• **Rango (Imagen):** ${rango_str}$")
        st.write(rf"• **Asíntota Horizontal:** Recta $y = {k:.1f}$")
        st.write(rf"• **Corte con el eje Y ($x = 0$):** $(0, {corte_y:.2f})$")

        st.markdown("---")
        st.subheader("🔎 Evaluar vs. Despejar en tu función")
        st.markdown(rf"**A) Evaluar para $x = {x_eval:.1f}$:**")
        st.latex(rf"f({x_eval:.1f}) = {a:.1f} \cdot ({b:.1f})^{{{x_eval:.1f} {signo_str(h)}}} {suma_str(k)} = {y_eval:.2f}")

        st.markdown("**B) Despejar $x$ si conocemos el resultado $y$:**")
        y_objetivo = st.number_input("Ingresa un valor de 'y' para despejar 'x':", value=float(round(y_eval, 2)), step=1.0)
        razon = (y_objetivo - k) / a
        if razon > 0:
            x_despejado = h + (np.log(razon) / np.log(b))
            st.latex(rf"{a:.1f} \cdot ({b:.1f})^{{x {signo_str(h)}}} {suma_str(k)} = {y_objetivo:.2f}")
            st.latex(rf"({b:.1f})^{{x {signo_str(h)}}} = \frac{{{y_objetivo:.2f} - ({k:.1f})}}{{{a:.1f}}} = {razon:.3f}")
            st.latex(rf"x = {h:.1f} + \log_{{{b:.1f}}}({razon:.3f}) = {x_despejado:.2f}")
        else:
            st.error(f"El valor y = {y_objetivo:.2f} está fuera del rango {rango_str} de la función (un exponente real no puede dar una potencia negativa o cero).")

    with col_graf:
        fig = crear_lienzo_cartesiano(rango_x=(-7, 7), rango_y=(-8, 16))

        # Curva exponencial
        fig.add_trace(go.Scatter(
            x=x_vals, y=y_vals, mode="lines", name="f(x) Exponencial",
            line=dict(color="#1f77b4", width=3.5)
        ))

        # Asíntota horizontal
        fig.add_trace(go.Scatter(
            x=[-8, 8], y=[k, k], mode="lines", name=f"Asíntota Horizontal (y = {k:.1f})",
            line=dict(color="#d62728", width=2, dash="dash")
        ))

        # Punto evaluado (x_eval, y_eval)
        fig.add_trace(go.Scatter(
            x=[x_eval], y=[y_eval], mode="markers", name=f"Punto Evaluado ({x_eval:.1f}, {y_eval:.2f})",
            marker=dict(color="#e65100", size=11, symbol="diamond")
        ))

        # Etiquetas con colores oscuros de alto contraste
        fig.add_trace(go.Scatter(
            x=[x_eval, -4.5],
            y=[y_eval + 1.0, k + (0.7 if a > 0 else -0.9)],
            mode="text",
            text=[
                f"<b>P({x_eval:.1f}, {y_eval:.2f})</b>",
                f"<b>Asíntota y = {k:.1f}</b>"
            ],
            textfont=dict(size=13, color=["#b73e00", "#b71c1c"]),
            showlegend=False
        ))

        st.plotly_chart(fig, use_container_width=True)

    # EJERCICIOS APLICATIVOS DE FUNCIÓN EXPONENCIAL
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos (Plantear función, Evaluar y Despejar)")
    tab_exp1, tab_exp2 = st.tabs([
        "🦠 Ejercicio 1: Crecimiento Poblacional de Bacterias",
        "🟦 Ejercicio 2: Comportamiento de una Figura Geométrica (Cuadrados Inscritos)"
    ])

    with tab_exp1:
        st.info(
            "**Problema 1 (Crecimiento Poblacional):** En el laboratorio de biología del colegio se estudia un cultivo "
            "de bacterias benéficas para fabricar yogur. El cultivo inicia con **$500\\text{ bacterias}$** y se observa que "
            "**la población se triplica cada hora** ($t$, medida en horas).\n\n"
            "1. **Función:** Escribe la función exponencial $P(t)$ que modela la cantidad de bacterias después de $t$ horas.\n"
            "2. **Evaluar:** ¿Cuántas bacterias habrá exactamente al cabo de **$t = 4\\text{ horas}$**?\n"
            "3. **Despejar la variable:** ¿Cuántas horas ($t$) deben transcurrir para que la población alcance exactamente **$135\\,000\\text{ bacterias}$**?"
        )
        if st.button("Revelar solución paso a paso (Ejercicio 1)", key="btn_exp1"):
            st.success("**Desarrollo completo:**")
            st.markdown("**1. Planteamiento de la función:** La población inicial es $a = 500$ y el factor de multiplicación por hora (base) es $b = 3$:")
            st.latex(r"P(t) = 500 \cdot 3^t")
            st.markdown("**2. Evaluar la función en $t = 4\\text{ horas}$:** Sustituimos $t = 4$ en el exponente:")
            st.latex(r"P(4) = 500 \cdot 3^4 = 500 \cdot 81 = 40\,500 \text{ bacterias}")
            st.markdown("**3. Despejar la variable $t$ cuando $P(t) = 135\,000$:** Igualamos la función a $135\,000$ y despejamos la potencia $3^t$:")
            st.latex(r"500 \cdot 3^t = 135\,000 \implies 3^t = \frac{135\,000}{500} \implies 3^t = 270")
            st.markdown("Aplicamos logaritmo en base $3$ (o cambio de base con calculadora) para bajar el exponente $t$:")
            st.latex(r"t = \log_3(270) = \frac{\ln(270)}{\ln(3)} \approx \frac{5.5984}{1.0986} \approx 5.10 \text{ horas}")

    with tab_exp2:
        st.info(
            "**Problema 2 (Modelación de una Figura Geométrica):** Dibuja un cuadrado grande de lado $8\\text{ cm}$, cuya área inicial "
            "(etapa $n = 0$) es de **$A_0 = 64\\text{ cm}^2$**. Para construir el paso $n = 1$, unes con líneas rectas los puntos medios "
            "de los cuatro lados para formar un nuevo cuadrado inclinado en su interior; por geometría, el área de cada nuevo cuadrado "
            "es exactamente **la mitad ($0.5$ o $\\frac{1}{2}$) del cuadrado anterior**. Este proceso se repite sucesivamente en cada etapa $n$.\n\n"
            "1. **Función:** Escribe la función exponencial $A(n)$ que modela el área del cuadrado (en $\\text{cm}^2$) en la etapa $n$.\n"
            "2. **Evaluar:** ¿Cuál será el área del cuadrado que se dibuja en la etapa **$n = 4$**?\n"
            "3. **Despejar la variable:** ¿En qué número de etapa ($n$) se obtendrá un cuadrado pequeño cuya área sea exactamente de **$0.5\\text{ cm}^2$**?"
        )
        if st.button("Revelar solución paso a paso (Ejercicio 2)", key="btn_exp2"):
            st.success("**Desarrollo completo:**")
            st.markdown(
                "**1. Planteamiento de la función:** El área en la etapa inicial ($n = 0$) es $a = 64\\text{ cm}^2$ y en cada etapa "
                "se multiplica por la base $b = 0.5 = \\frac{1}{2}$:"
            )
            st.latex(r"A(n) = 64 \cdot (0.5)^n \quad \text{o también} \quad A(n) = 64 \cdot \left(\frac{1}{2}\right)^n")
            st.markdown("**2. Evaluar el área en la etapa $n = 4$:** Reemplazamos $n = 4$ en la función:")
            st.latex(r"A(4) = 64 \cdot (0.5)^4 = 64 \cdot (0.0625) = 4.0 \text{ cm}^2")
            st.markdown("**3. Despejar la etapa $n$ cuando el área es $A(n) = 0.5\\text{ cm}^2$:**")
            st.latex(r"64 \cdot (0.5)^n = 0.5 \implies (0.5)^n = \frac{0.5}{64} = \frac{1}{128}")
            st.markdown("Como $\\frac{1}{2} = 0.5$ y $128 = 2^7$, podemos escribir ambos lados con la misma base $\\frac{1}{2}$ (o aplicar logaritmos):")
            st.latex(r"\left(\frac{1}{2}\right)^n = \left(\frac{1}{2}\right)^7 \implies n = 7 \text{ (en la séptima etapa)}")


# ==============================================================================
# MÓDULO 2: FUNCIÓN LOGARÍTMICA Y MODELOS APLICADOS
# ==============================================================================
elif modulo == "2. Función Logarítmica y Modelos":
    st.title("📉 Función Logarítmica: $f(x) = a \\cdot \\log_b(x - h) + k$")
    st.markdown(
        "La **función logarítmica** es la operación inversa de la exponencial: $\\log_b(x)$ responde a la pregunta "
        "*«¿a qué exponente debo elevar la base $b$ para obtener $x$?»*. Solo existe cuando su argumento $(x - h)$ es **estrictamente mayor que cero**."
    )

    st.sidebar.subheader("Parámetros de la Función")
    a = st.sidebar.slider("Coeficiente vertical (a)", -5.0, 5.0, 1.0, 0.5)
    if a == 0:
        a = 1.0
        st.sidebar.warning("El valor de 'a' no puede ser 0. Se ajustó a 1.0.")

    b = st.sidebar.slider("Base del logaritmo (b)", 1.5, 10.0, 2.0, 0.5)
    h = st.sidebar.slider("Asíntota vertical (h)", -6.0, 6.0, 0.0, 0.5)
    k = st.sidebar.slider("Desplazamiento vertical (k)", -5.0, 5.0, 0.0, 0.5)
    mostrar_inversa = st.sidebar.checkbox("Mostrar función exponencial inversa (b^x)", value=True)

    st.sidebar.markdown("---")
    st.sidebar.subheader("Calculadora de Evaluación")
    x_eval = st.sidebar.number_input(
        f"1. Evaluar f(x) para x > {h:.1f}:",
        min_value=float(h + 0.1),
        value=float(h + b),
        step=0.5
    )
    y_eval = a * (np.log(x_eval - h) / np.log(b)) + k

    # Puntos para graficar el logaritmo (empezando ligeramente a la derecha de h)
    x_vals = np.linspace(h + 0.01, h + 14, 500)
    y_vals = a * (np.log(x_vals - h) / np.log(b)) + k

    # Raíz o corte con el eje X (f(x) = 0 -> log_b(x - h) = -k/a -> x = h + b^(-k/a))
    x_raiz = h + (b ** (-k / a))

    col_info, col_graf = st.columns([1.15, 1.45], gap="large")

    with col_info:
        st.subheader("Análisis Matemático")
        st.markdown("**Definición Fundamental del Logaritmo:**")
        st.latex(r"\log_b(N) = y \iff b^y = N \quad (\text{con } N > 0)")

        st.markdown("**Ecuación con tus valores actuales:**")
        st.latex(rf"f(x) = {a:.1f} \cdot \log_{{{b:.1f}}}(x {signo_str(h)}) {suma_str(k)}")

        st.markdown("---")
        st.subheader("Propiedades de la Gráfica")
        st.write(rf"• **Condición de existencia:** $x - ({h:.1f}) > 0 \implies x > {h:.1f}$")
        st.write(rf"• **Dominio:** $({h:.1f}, +\infty)$")
        st.write(r"• **Rango (Imagen):** Todos los números reales $(-\infty, +\infty)$")
        st.write(rf"• **Asíntota Vertical:** Recta $x = {h:.1f}$")
        st.write(rf"• **Corte con el eje X ($y = 0$):** $({x_raiz:.2f}, 0)$")

        st.markdown("---")
        st.subheader("🔎 Evaluar vs. Despejar en tu función")
        st.markdown(rf"**A) Evaluar para $x = {x_eval:.2f}$:**")
        st.latex(rf"f({x_eval:.2f}) = {a:.1f} \cdot \log_{{{b:.1f}}}({x_eval - h:.2f}) {suma_str(k)} = {y_eval:.2f}")

        st.markdown("**B) Despejar $x$ si conocemos el resultado $y$:**")
        y_obj = st.number_input("Ingresa un valor de 'y' para despejar 'x':", value=float(round(y_eval, 2)), step=1.0)
        exp_despeje = (y_obj - k) / a
        x_desp = h + (b ** exp_despeje)
        st.latex(rf"\log_{{{b:.1f}}}(x {signo_str(h)}) = \frac{{{y_obj:.2f} - ({k:.1f})}}{{{a:.1f}}} = {exp_despeje:.2f}")
        st.latex(rf"x {signo_str(h)} = ({b:.1f})^{{{exp_despeje:.2f}}} \implies x = {x_desp:.2f}")

    with col_graf:
        fig = crear_lienzo_cartesiano(rango_x=(h - 4, h + 12), rango_y=(-8, 10))

        # Curva logarítmica
        fig.add_trace(go.Scatter(
            x=x_vals, y=y_vals, mode="lines", name="f(x) Logarítmica",
            line=dict(color="#2ca02c", width=3.5)
        ))

        # Asíntota vertical x = h
        fig.add_trace(go.Scatter(
            x=[h, h], y=[-12, 12], mode="lines", name=f"Asíntota Vertical (x = {h:.1f})",
            line=dict(color="#d62728", width=2, dash="dash")
        ))

        # Si el usuario activa ver la función inversa y la recta de simetría y = x
        if mostrar_inversa:
            t_inv = np.linspace(-6, 6, 300)
            fig.add_trace(go.Scatter(
                x=t_inv, y=b**t_inv, mode="lines", name=f"Inversa base: y = ({b:.1f})^x",
                line=dict(color="rgba(31, 119, 180, 0.45)", width=2, dash="dot")
            ))
            fig.add_trace(go.Scatter(
                x=[-10, 12], y=[-10, 12], mode="lines", name="Eje de simetría y = x",
                line=dict(color="rgba(120, 120, 120, 0.4)", width=1.5, dash="dashdot")
            ))

        # Punto evaluado
        fig.add_trace(go.Scatter(
            x=[x_eval], y=[y_eval], mode="markers", name=f"Evaluado ({x_eval:.2f}, {y_eval:.2f})",
            marker=dict(color="#6a1b9a", size=11, symbol="diamond")
        ))

        # Etiquetas con alto contraste
        fig.add_trace(go.Scatter(
            x=[x_eval + 0.4, h + 0.3],
            y=[y_eval + 0.6, -6.5],
            mode="text",
            text=[
                f"<b>P({x_eval:.2f}, {y_eval:.2f})</b>",
                f"<b>Asíntota x = {h:.1f}</b>"
            ],
            textfont=dict(size=13, color=["#4a148c", "#b71c1c"]),
            showlegend=False
        ))

        st.plotly_chart(fig, use_container_width=True)

    # EJERCICIOS APLICATIVOS DE FUNCIÓN LOGARÍTMICA
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos (Plantear función, Evaluar y Despejar)")
    tab_log1, tab_log2 = st.tabs([
        "🔊 Ejercicio 1: Nivel de Sonido en Decibeles (Acústica)",
        "🧠 Ejercicio 2: Curva de Retención de la Memoria (Psicología)"
    ])

    with tab_log1:
        st.info(
            "**Problema 1 (Escala de Decibeles):** El oído humano percibe sonidos desde un susurro hasta una turbina de avión. "
            "Por eso, el nivel de sensación sonora $\\beta$ (medido en decibeles, $\\text{dB}$) se modela con una función logarítmica de base $10$: "
            "**$\\beta(x) = 10 \\cdot \\log_{10}(x)$**, donde $x$ indica cuántas veces es más potente la onda sonora respecto al sonido mínimo audible.\n\n"
            "1. **Evaluar:** Si durante el ensayo de la banda del colegio los parlantes emiten una onda que es **$x = 100\\,000\\,000$** veces ($10^8$) "
            "más intensa que el umbral mínimo, ¿cuántos decibeles ($\\beta$) marca el sonómetro?\n"
            "2. **Despejar la variable:** Si una alarma escolar suena a **$\\beta = 90\\text{ dB}$**, ¿cuántas veces ($x$) supera el umbral mínimo audible?"
        )
        if st.button("Revelar solución paso a paso (Ejercicio 1)", key="btn_log1"):
            st.success("**Desarrollo completo:**")
            st.markdown("**1. Evaluar para $x = 100\\,000\\,000 = 10^8$:** Sustituimos $x = 10^8$ en la función $\\beta(x) = 10 \\cdot \\log_{10}(x)$:")
            st.latex(r"\beta(10^8) = 10 \cdot \log_{10}(10^8) = 10 \cdot 8 = 80 \text{ decibeles (dB)}")
            st.markdown("**2. Despejar la variable $x$ cuando $\\beta(x) = 90\\text{ dB}$:** Igualamos la función a $90$ y aislamos el logaritmo:")
            st.latex(r"10 \cdot \log_{10}(x) = 90 \implies \log_{10}(x) = \frac{90}{10} \implies \log_{10}(x) = 9")
            st.markdown("Aplicamos la definición fundamental del logaritmo ($\\log_{10}(x) = 9 \\iff x = 10^9$):")
            st.latex(r"x = 10^9 = 1\,000\,000\,000 \text{ (mil millones de veces el umbral mínimo)}")

    with tab_log2:
        st.info(
            "**Problema 2 (Curva de la Memoria):** Un grupo de estudiantes estudia una lista de vocabulario y luego no vuelve a repasarla. "
            "El porcentaje promedio de palabras que recuerdan después de $t$ días está modelado por la función logarítmica: "
            "**$R(t) = 85 - 25 \\cdot \\log_{10}(t + 1)$**.\n\n"
            "1. **Evaluar:** ¿Qué porcentaje de palabras recuerdan el mismo día del estudio ($t = 0$) y qué porcentaje recuerdan a los **$t = 9\\text{ días}$**?\n"
            "2. **Despejar la variable:** ¿Cuántos días ($t$) deben pasar sin repasar para que el estudiante recuerde únicamente el **$35\\%$** de los temas?"
        )
        if st.button("Revelar solución paso a paso (Ejercicio 2)", key="btn_log2"):
            st.success("**Desarrollo completo:**")
            st.markdown("**1. Evaluar en $t = 0$ y en $t = 9$ días:**")
            st.latex(r"R(0) = 85 - 25 \cdot \log_{10}(0 + 1) = 85 - 25 \cdot \log_{10}(1) = 85 - 0 = 85\%")
            st.latex(r"R(9) = 85 - 25 \cdot \log_{10}(9 + 1) = 85 - 25 \cdot \log_{10}(10) = 85 - 25(1) = 60\%")
            st.markdown("**2. Despejar los días $t$ cuando $R(t) = 35\\%$:** Igualamos la función a $35$ y despejamos el término logarítmico:")
            st.latex(r"85 - 25 \cdot \log_{10}(t + 1) = 35")
            st.latex(r"-25 \cdot \log_{10}(t + 1) = 35 - 85 \implies -25 \cdot \log_{10}(t + 1) = -50")
            st.latex(r"\log_{10}(t + 1) = \frac{-50}{-25} = 2")
            st.markdown("Pasamos a forma exponencial de base $10$:")
            st.latex(r"t + 1 = 10^2 \implies t + 1 = 100 \implies t = 99 \text{ días}")


# ==============================================================================
# MÓDULO 3: ECUACIONES EXPONENCIALES (MÉTODO DE BASES IGUALES)
# ==============================================================================
elif modulo == "3. Ecuaciones Exponenciales (Bases Iguales)":
    st.title("⚖️ Ecuaciones Exponenciales: Método de Igualación de Bases")
    st.markdown(
        "Cuando la incógnita $x$ está en los exponentes de ambos lados de una igualdad, la estrategia algebraica más directa "
        "consiste en **reescribir todos los números como potencias de una misma base común ($b$)**. Una vez que las bases son iguales, "
        "**se igualan directamente los exponentes**."
    )

    col_teoria, col_interactivo = st.columns([1.15, 1.45], gap="large")

    with col_teoria:
        st.subheader("Propiedad Fundamental de Inyectividad")
        st.latex(r"\text{Si } b^{M(x)} = b^{N(x)} \implies M(x) = N(x) \quad (b > 0, b \neq 1)")

        st.markdown("**Leyes de los exponentes necesarias para transformar bases:**")
        st.latex(r"1.\;\; (b^m)^n = b^{m \cdot n} \qquad 2.\;\; b^m \cdot b^n = b^{m + n}")
        st.latex(r"3.\;\; \frac{b^m}{b^n} = b^{m - n} \qquad 4.\;\; \frac{1}{b^n} = b^{-n}")

        st.markdown("**Tabla de potencias frecuentes para reconocer la base común:**")
        st.markdown(
            "| Base $2$ | Base $3$ | Base $5$ |\n"
            "| :--- | :--- | :--- |\n"
            "| $4 = 2^2$ | $9 = 3^2$ | $25 = 5^2$ |\n"
            "| $8 = 2^3$ | $27 = 3^3$ | $125 = 5^3$ |\n"
            "| $16 = 2^4$ | $81 = 3^4$ | $625 = 5^4$ |\n"
            "| $32 = 2^5$ | $243 = 3^5$ | $\\frac{1}{25} = 5^{-2}$ |"
        )

    with col_interactivo:
        st.subheader("Simulador Gráfico de Igualación de Bases")
        st.sidebar.subheader("Configura tu Ecuación Exponencial")
        base_comun = st.sidebar.selectbox("Selecciona la base común (b):", [2, 3, 5], index=0)
        k1 = st.sidebar.slider("Exponente de la primera base (potencia m):", 1, 4, 2)
        k2 = st.sidebar.slider("Exponente de la segunda base (potencia n):", 1, 4, 3)
        c_ind = st.sidebar.slider("Término independiente en el exponente derecho:", -6, 6, -2)

        base_izq = base_comun ** k1
        base_der = base_comun ** k2

        st.markdown("**Ecuación planteada con bases diferentes:**")
        st.latex(rf"({base_izq})^{{x + 1}} = ({base_der})^{{x {suma_str(c_ind)}}}")

        st.markdown(rf"**Paso 1:** Expresamos ${base_izq} = {base_comun}^{{{k1}}}$ y ${base_der} = {base_comun}^{{{k2}}}$:")
        st.latex(rf"\left({base_comun}^{{{k1}}}\right)^{{x + 1}} = \left({base_comun}^{{{k2}}}\right)^{{x {suma_str(c_ind)}}}")

        st.markdown("**Paso 2:** Multiplicamos los exponentes e igualamos por tener la misma base:")
        st.latex(rf"{k1}(x + 1) = {k2}(x {suma_str(c_ind)}) \implies {k1}x + {k1} = {k2}x {suma_str(k2 * c_ind)}")

        if k1 != k2:
            x_sol = (k2 * c_ind - k1) / (k1 - k2)
            y_sol_exp = k1 * (x_sol + 1)
            st.success(rf"**Solución única:** $x = {x_sol:.2f}$ (En ese punto ambos exponentes valen ${y_sol_exp:.2f}$).")

            # Gráfica de la intersección de los exponentes
            x_g = np.linspace(x_sol - 5, x_sol + 5, 200)
            y_exp1 = k1 * (x_g + 1)
            y_exp2 = k2 * (x_g + c_ind)

            fig_eq = crear_lienzo_cartesiano(
                rango_x=(x_sol - 5, x_sol + 5),
                rango_y=(y_sol_exp - 10, y_sol_exp + 10),
                titulo_x="Valor de la incógnita x",
                titulo_y="Valor del exponente en base común"
            )
            fig_eq.add_trace(go.Scatter(
                x=x_g, y=y_exp1, mode="lines", name=f"Exponente Izquierdo: {k1}(x + 1)",
                line=dict(color="#1f77b4", width=3)
            ))
            fig_eq.add_trace(go.Scatter(
                x=x_g, y=y_exp2, mode="lines", name=f"Exponente Derecho: {k2}(x {suma_str(c_ind)})",
                line=dict(color="#2ca02c", width=3)
            ))
            fig_eq.add_trace(go.Scatter(
                x=[x_sol], y=[y_sol_exp], mode="markers", name=f"Solución x = {x_sol:.2f}",
                marker=dict(color="#d62728", size=12, symbol="star")
            ))
            fig_eq.add_trace(go.Scatter(
                x=[x_sol], y=[y_sol_exp + 1.8], mode="text",
                text=[f"<b>Intersección: x = {x_sol:.2f}</b>"],
                textfont=dict(size=13, color="#b71c1c"),
                showlegend=False
            ))
            st.plotly_chart(fig_eq, use_container_width=True)
        else:
            st.warning("Elige exponentes de base (m y n) distintos en la barra lateral para que las rectas de los exponentes se crucen.")

    # EJERCICIOS DE ECUACIONES EXPONENCIALES
    st.markdown("---")
    st.subheader("📝 Ejercicios de Práctica (Dejar Bases Iguales para Igualar Exponentes)")
    tab_ee1, tab_ee2, tab_ee3 = st.tabs([
        "🟢 Ejercicio 1: Reducción a Base 2",
        "🟡 Ejercicio 2: Producto de Potencias y Fracción (Base 3)",
        "🔴 Ejercicio 3: Ecuación con Base 5 y Verificación"
    ])

    with tab_ee1:
        st.info(
            "**Ejercicio 1:** Resuelve la siguiente ecuación exponencial buscando una base común:\n\n"
            "$$8^{x - 1} = 4^{x + 2}$$"
        )
        if st.button("Ver solución paso a paso (Ejercicio 1)", key="btn_ee1"):
            st.success("**Solución:**")
            st.markdown("1. **Identificamos la base común:** Tanto el $8$ como el $4$ son potencias de **$2$** ($8 = 2^3$ y $4 = 2^2$).")
            st.latex(r"(2^3)^{x - 1} = (2^2)^{x + 2}")
            st.markdown("2. **Aplicamos potencia de una potencia** multiplicando los exponentes:")
            st.latex(r"2^{3(x - 1)} = 2^{2(x + 2)} \implies 2^{3x - 3} = 2^{2x + 4}")
            st.markdown("3. **Igualamos los exponentes** ya que las bases son idénticas ($2 = 2$):")
            st.latex(r"3x - 3 = 2x + 4 \implies 3x - 2x = 4 + 3 \implies x = 7")
            st.markdown("4. **Comprobación:** $8^{7-1} = 8^6 = 262\\,144$ y $4^{7+2} = 4^9 = 262\\,144$. ¡Correcto!")

    with tab_ee2:
        st.info(
            "**Ejercicio 2:** Utiliza las leyes de los exponentes para reducir todo a una sola base común y hallar $x$:\n\n"
            "$$9^x \\cdot 3^{x - 1} = \\frac{1}{27}$$"
        )
        if st.button("Ver solución paso a paso (Ejercicio 2)", key="btn_ee2"):
            st.success("**Solución:**")
            st.markdown(
                "1. **Llevamos todos los números a base $3$:** Sabemos que $9 = 3^2$, y por propiedad del exponente negativo, "
                "$\\frac{1}{27} = \\frac{1}{3^3} = 3^{-3}$."
            )
            st.latex(r"(3^2)^x \cdot 3^{x - 1} = 3^{-3} \implies 3^{2x} \cdot 3^{x - 1} = 3^{-3}")
            st.markdown("2. **Unificamos el lado izquierdo:** Como se están multiplicando potencias de igual base, **sumamos sus exponentes**:")
            st.latex(r"3^{2x + (x - 1)} = 3^{-3} \implies 3^{3x - 1} = 3^{-3}")
            st.markdown("3. **Igualamos los exponentes y despejamos $x$:**")
            st.latex(r"3x - 1 = -3 \implies 3x = -2 \implies x = -\frac{2}{3} \approx -0.67")

    with tab_ee3:
        st.info(
            "**Ejercicio 3:** Halla el valor de $x$ que satisface la igualdad:\n\n"
            "$$25^{2x - 1} = 125^{x}$$"
        )
        if st.button("Ver solución paso a paso (Ejercicio 3)", key="btn_ee3"):
            st.success("**Solución:**")
            st.markdown("1. **Expresamos ambos lados en base $5$:** Sabemos que $25 = 5^2$ y $125 = 5^3$:")
            st.latex(r"(5^2)^{2x - 1} = (5^3)^x")
            st.markdown("2. **Multiplicamos los exponentes e igualamos:**")
            st.latex(r"5^{4x - 2} = 5^{3x} \implies 4x - 2 = 3x")
            st.latex(r"4x - 3x = 2 \implies x = 2")


# ==============================================================================
# MÓDULO 4: ECUACIONES LOGARÍTMICAS (PROPIEDADES DE LOS LOGARITMOS)
# ==============================================================================
elif modulo == "4. Ecuaciones Logarítmicas (Propiedades)":
    st.title("🧩 Ecuaciones Logarítmicas: Aplicación de Propiedades")
    st.markdown(
        "Para resolver ecuaciones donde la incógnita $x$ está dentro de varios logaritmos, el método consiste en **comprimir (agrupar) "
        "los términos en un solo logaritmo** usando sus tres propiedades fundamentales y luego aplicar la definición exponencial."
    )

    col_prop, col_vis = st.columns([1.15, 1.45], gap="large")

    with col_prop:
        st.subheader("Las 3 Propiedades para Comprimir Logaritmos")
        st.markdown("**1. Logaritmo de un Producto (Suma $\\to$ Multiplicación):**")
        st.latex(r"\log_b(A) + \log_b(B) = \log_b(A \cdot B)")

        st.markdown("**2. Logaritmo de un Cociente (Resta $\\to$ División):**")
        st.latex(r"\log_b(A) - \log_b(B) = \log_b\left(\frac{A}{B}\right)")

        st.markdown("**3. Logaritmo de una Potencia (Coeficiente $\\to$ Exponente):**")
        st.latex(r"n \cdot \log_b(A) = \log_b(A^n)")

        st.markdown("---")
        st.subheader("⚠️ Regla de Oro: Comprobación del Dominio")
        st.warning(
            "En los números reales **no existen logaritmos de números negativos ni del cero**. "
            "Al terminar de despejar $x$, es obligatorio sustituir la solución en la ecuación original "
            "para verificar que todos los paréntesis internos sean **estrictamente mayores que $0$**."
        )

    with col_vis:
        st.subheader("Explorador Visual de Ecuaciones Logarítmicas")
        st.sidebar.subheader("Selecciona el tipo de ecuación a visualizar")
        tipo_ec_log = st.sidebar.radio(
            "Propiedad aplicada:",
            [
                "Suma (Producto): log₂(x) + log₂(x - 2) = 3",
                "Resta (Cociente): log₃(2x + 5) - log₃(x - 1) = 2",
                "Potencia: 2·log₁₀(x) = log₁₀(4x + 12)"
            ]
        )

        if "Suma" in tipo_ec_log:
            st.latex(r"\log_2(x) + \log_2(x - 2) = 3 \quad (\text{Dominio válido: } x > 2)")
            x_dom = np.linspace(2.05, 9.0, 400)
            y_izq = np.log2(x_dom) + np.log2(x_dom - 2)
            y_der = np.full_like(x_dom, 3.0)
            x_sol, y_sol = 4.0, 3.0
            rango_x, rango_y = (0, 8), (-2, 6)
            lim_dom = 2.0
        elif "Resta" in tipo_ec_log:
            st.latex(r"\log_3(2x + 5) - \log_3(x - 1) = 2 \quad (\text{Dominio válido: } x > 1)")
            x_dom = np.linspace(1.05, 8.0, 400)
            y_izq = (np.log(2 * x_dom + 5) - np.log(x_dom - 1)) / np.log(3)
            y_der = np.full_like(x_dom, 2.0)
            x_sol, y_sol = 2.0, 2.0
            rango_x, rango_y = (0, 7), (0, 5)
            lim_dom = 1.0
        else:
            st.latex(r"2\log_{10}(x) = \log_{10}(4x + 12) \quad (\text{Dominio válido: } x > 0)")
            x_dom = np.linspace(0.2, 10.0, 400)
            y_izq = 2 * np.log10(x_dom)
            y_der = np.log10(4 * x_dom + 12)
            x_sol, y_sol = 6.0, 2 * np.log10(6.0)
            rango_x, rango_y = (-1, 9), (-1, 3.5)
            lim_dom = 0.0

        fig_log = crear_lienzo_cartesiano(rango_x=rango_x, rango_y=rango_y)

        # Barrera de dominio
        fig_log.add_trace(go.Scatter(
            x=[lim_dom, lim_dom], y=[-10, 10], mode="lines",
            name=f"Frontera de Dominio (x > {lim_dom:.0f})",
            line=dict(color="#d62728", width=2, dash="dash")
        ))
        # Lado izquierdo
        fig_log.add_trace(go.Scatter(
            x=x_dom, y=y_izq, mode="lines", name="Miembro Izquierdo",
            line=dict(color="#1f77b4", width=3.5)
        ))
        # Lado derecho
        fig_log.add_trace(go.Scatter(
            x=x_dom, y=y_der, mode="lines", name="Miembro Derecho",
            line=dict(color="#2ca02c", width=3)
        ))
        # Punto de solución
        fig_log.add_trace(go.Scatter(
            x=[x_sol], y=[y_sol], mode="markers", name=f"Solución válida: x = {x_sol:.1f}",
            marker=dict(color="#e65100", size=12, symbol="star")
        ))
        fig_log.add_trace(go.Scatter(
            x=[x_sol], y=[y_sol + 0.45], mode="text",
            text=[f"<b>Solución: x = {x_sol:.1f}</b>"],
            textfont=dict(size=13, color="#b73e00"),
            showlegend=False
        ))

        st.plotly_chart(fig_log, use_container_width=True)

    # EJERCICIOS DE ECUACIONES LOGARÍTMICAS
    st.markdown("---")
    st.subheader("📝 Ejercicios Paso a Paso (Aplicando Propiedades de los Logaritmos)")
    tab_el1, tab_el2, tab_el3 = st.tabs([
        "🟢 Ejercicio 1: Propiedad del Producto y Descarte de Raíz",
        "🟡 Ejercicio 2: Propiedad del Cociente",
        "🔴 Ejercicio 3: Propiedad de la Potencia"
    ])

    with tab_el1:
        st.info(
            "**Ejercicio 1 (Suma de Logaritmos):** Resuelve la ecuación y verifica qué soluciones son válidas:\n\n"
            "$$\\log_2(x) + \\log_2(x - 2) = 3$$"
        )
        if st.button("Ver solución paso a paso (Ejercicio 1)", key="btn_el1"):
            st.success("**Solución:**")
            st.markdown("1. **Aplicamos la propiedad del producto** ($\\log_b(A) + \\log_b(B) = \\log_b(A \\cdot B)$) para unir ambos logaritmos:")
            st.latex(r"\log_2\big(x \cdot (x - 2)\big) = 3 \implies \log_2(x^2 - 2x) = 3")
            st.markdown("2. **Pasamos a forma exponencial** usando la base $2$ ($2^3 = 8$):")
            st.latex(r"x^2 - 2x = 2^3 \implies x^2 - 2x - 8 = 0")
            st.markdown("3. **Factorizamos la ecuación cuadrática:** Buscamos dos números que multiplicados den $-8$ y sumados den $-2$:")
            st.latex(r"(x - 4)(x + 2) = 0 \implies x_1 = 4, \quad x_2 = -2")
            st.markdown(
                "4. **Verificación del dominio:**\n"
                "• Con $x_1 = 4$: $\\log_2(4) + \\log_2(4 - 2) = 2 + 1 = 3$ (argumentos positivos $\\to$ **Solución válida**).\n"
                "• Con $x_2 = -2$: quedaría $\\log_2(-2)$, lo cual no existe en los reales ($\\to$ **Se descarta**).\n\n"
                "**Respuesta única:** $x = 4$."
            )

    with tab_el2:
        st.info(
            "**Ejercicio 2 (Resta de Logaritmos):** Resuelve la siguiente ecuación aplicando la propiedad del cociente:\n\n"
            "$$\\log_3(2x + 5) - \\log_3(x - 1) = 2$$"
        )
        if st.button("Ver solución paso a paso (Ejercicio 2)", key="btn_el2"):
            st.success("**Solución:**")
            st.markdown("1. **Aplicamos la propiedad del cociente** ($\\log_b(A) - \\log_b(B) = \\log_b(A / B)$):")
            st.latex(r"\log_3\left(\frac{2x + 5}{x - 1}\right) = 2")
            st.markdown("2. **Convertimos a forma exponencial** elevando la base $3$ al cuadrado ($3^2 = 9$):")
            st.latex(r"\frac{2x + 5}{x - 1} = 3^2 \implies \frac{2x + 5}{x - 1} = 9")
            st.markdown("3. **Despejamos $x$ de la ecuación lineal:**")
            st.latex(r"2x + 5 = 9(x - 1) \implies 2x + 5 = 9x - 9")
            st.latex(r"5 + 9 = 9x - 2x \implies 14 = 7x \implies x = 2")
            st.markdown("4. **Verificación:** Al evaluar $x = 2$, los argumentos son $2(2)+5 = 9 > 0$ y $2-1 = 1 > 0$. Por tanto, **$x = 2$** es válida.")

    with tab_el3:
        st.info(
            "**Ejercicio 3 (Coeficiente como Exponente):** Halla el valor positivo de $x$ que cumple la ecuación:\n\n"
            "$$2 \\cdot \\log_{10}(x) = \\log_{10}(4x + 12)$$"
        )
        if st.button("Ver solución paso a paso (Ejercicio 3)", key="btn_el3"):
            st.success("**Solución:**")
            st.markdown("1. **Aplicamos la propiedad de la potencia** ($n\\log_b(A) = \\log_b(A^n)$) para subir el $2$ como exponente:")
            st.latex(r"\log_{10}(x^2) = \log_{10}(4x + 12)")
            st.markdown("2. **Igualamos los argumentos** ya que ambos lados tienen un único $\\log_{10}$:")
            st.latex(r"x^2 = 4x + 12 \implies x^2 - 4x - 12 = 0")
            st.markdown("3. **Factorizamos y verificamos el dominio ($x > 0$):**")
            st.latex(r"(x - 6)(x + 2) = 0 \implies x_1 = 6, \quad x_2 = -2 \text{ (se descarta por ser negativo)}")
            st.markdown("**Respuesta única:** $x = 6$.")