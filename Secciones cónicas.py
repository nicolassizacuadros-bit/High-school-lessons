import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Laboratorio de Secciones Cónicas",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# FUNCIÓN BASE PARA EL LIENZO DE PLOTLY
# ==========================================
def crear_figura_base(rango=15):
    """
    Crea una figura de Plotly con proporción 1:1 garantizada para evitar 
    que una circunferencia se vea achatada como una elipse.
    """
    fig = go.Figure()
    
    # Ejes coordenados principales (X = 0, Y = 0)
    fig.add_hline(y=0, line_width=1.5, line_color="rgba(100, 100, 100, 0.5)")
    fig.add_vline(x=0, line_width=1.5, line_color="rgba(100, 100, 100, 0.5)")
    
    fig.update_layout(
        xaxis=dict(
            title="Eje X (metros)",
            range=[-rango, rango],
            zeroline=False,
            gridcolor="rgba(200, 200, 200, 0.3)",
            dtick=2
        ),
        yaxis=dict(
            title="Eje Y (metros)",
            range=[-rango, rango],
            zeroline=False,
            gridcolor="rgba(200, 200, 200, 0.3)",
            scaleanchor="x",  # Garantiza proporción geométrica 1:1
            scaleratio=1,
            dtick=2
        ),
        height=600,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        template="plotly_white"
    )
    return fig

def formatear_signo(valor):
    """Auxiliar para mostrar (x - h) o (x + h) limpiamente en LaTeX."""
    if valor >= 0:
        return f"- {abs(valor):.1f}"
    else:
        return f"+ {abs(valor):.1f}"

# ==========================================
# BARRA LATERAL (MENÚ Y CONTROLES GLOBALES)
# ==========================================
st.sidebar.title("📐 Secciones Cónicas")
st.sidebar.markdown("Explora cómo cambian las gráficas al mover sus parámetros.")

conica_seleccionada = st.sidebar.radio(
    "Selecciona la figura geométrica:",
    ["Circunferencia", "Parábola", "Elipse", "Hipérbola"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("Posición del Centro / Vértice")
h = st.sidebar.slider("Coordenada h (mover en X)", -8.0, 8.0, 0.0, 0.5)
k = st.sidebar.slider("Coordenada k (mover en Y)", -8.0, 8.0, 0.0, 0.5)

st.sidebar.markdown("---")
st.sidebar.subheader("Tamaño y Forma")

# ==========================================
# ENCABEZADO PRINCIPAL
# ==========================================
st.title(f"Explorador Interactivo: {conica_seleccionada}")
col_controles, col_grafica = st.columns([1, 1.6], gap="large")

# ==========================================
# 1. MÓDULO: CIRCUNFERENCIA
# ==========================================
if conica_seleccionada == "Circunferencia":
    r = st.sidebar.slider("Radio (r)", 0.5, 10.0, 5.0, 0.5)
    
    # Cálculos matemáticos
    theta = np.linspace(0, 2 * np.pi, 400)
    x = h + r * np.cos(theta)
    y = k + r * np.sin(theta)
    
    # Coeficientes de la ecuación general: x^2 + y^2 + Dx + Ey + F = 0
    D = -2 * h
    E = -2 * k
    F_gen = h**2 + k**2 - r**2
    
    with col_controles:
        st.subheader("Fórmulas")
        st.markdown("**Ecuación Canónica (Fórmula base):**")
        st.latex(r"(x - h)^2 + (y - k)^2 = r^2")
        
        st.markdown("**Ecuación con tus valores actuales:**")
        st.latex(rf"(x {formatear_signo(h)})^2 + (y {formatear_signo(k)})^2 = {r**2:.2f}")
        
        st.markdown("**Ecuación General Desarrollada:**")
        st.latex(rf"x^2 + y^2 {D:+.1f}x {E:+.1f}y {F_gen:+.2f} = 0")
        
        st.markdown("---")
        st.subheader("Elementos de la Circunferencia")
        st.write(rf"• **Centro $C(h, k)$:** $({h:.1f}, {k:.1f})$")
        st.write(rf"• **Radio ($r$):** ${r:.1f}$ unidades")
        st.write(rf"• **Diámetro ($2r$):** ${2 * r:.1f}$ unidades")
        st.write(rf"• **Perímetro o longitud ($2\pi r$):** ${2 * np.pi * r:.2f}$ unidades")
        st.write(rf"• **Área ($\pi r^2$):** ${np.pi * r**2:.2f}$ unidades²")

    with col_grafica:
        fig = crear_figura_base()
        fig.add_trace(go.Scatter(
            x=x, y=y, mode="lines", name="Circunferencia",
            line=dict(color="#1f77b4", width=3)
        ))
        fig.add_trace(go.Scatter(
            x=[h], y=[k], mode="markers+text", name="Centro C(h,k)",
            text=[f"C({h:.1f}, {k:.1f})"], textposition="top right",
            marker=dict(color="#d62728", size=10, symbol="circle")
        ))
        fig.add_trace(go.Scatter(
            x=[h, h + r * np.cos(np.pi/4)],
            y=[k, k + r * np.sin(np.pi/4)],
            mode="lines+text", name=f"Radio r = {r:.1f}",
            text=["", f"r = {r:.1f}"], textposition="bottom right",
            line=dict(color="#2ca02c", width=2, dash="dash")
        ))
        st.plotly_chart(fig, use_container_width=True)

    # Ejercicio Aplicativo de Bachillerato
    st.markdown("---")
    st.subheader("📶 Ejercicio Aplicativo: El alcance del Wi-Fi del colegio")
    st.info(
        "**Problema:** En el patio del colegio se instaló un router Wi-Fi en las coordenadas $C(2.0, -1.5)$ "
        "(medidas en metros desde el centro del patio). Si tú te sientas en una banca ubicada en el punto "
        "$P(6.0, 1.5)$ y estás justo en el límite donde todavía llega la señal:\n\n"
        "1. ¿Cuál es el radio máximo de cobertura ($r$) que tiene el router?\n"
        "2. ¿Cuál es la ecuación canónica que representa el borde de la zona con cobertura Wi-Fi? "
        "*(Prueba mover los deslizadores a $h = 2.0$, $k = -1.5$ y el radio que calcules para comprobarlo en la gráfica)*."
    )
    if st.button("Revelar solución paso a paso", key="btn_circ"):
        st.success("**Solución:**")
        st.markdown(
            "1. **Hallamos el radio ($r$):** El radio es la distancia entre el router $C(2.0, -1.5)$ "
            "y la banca $P(6.0, 1.5)$. Usamos el Teorema de Pitágoras (fórmula de distancia):"
        )
        st.latex(r"r = \sqrt{(6.0 - 2.0)^2 + (1.5 - (-1.5))^2}")
        st.latex(r"r = \sqrt{(4.0)^2 + (3.0)^2} = \sqrt{16 + 9} = \sqrt{25} = 5.0 \,m")
        st.markdown("2. **Escribimos la ecuación canónica:** Reemplazamos $h = 2.0$, $k = -1.5$ y $r = 5.0$:")
        st.latex(r"(x - 2.0)^2 + (y + 1.5)^2 = 25")


# ==========================================
# 2. MÓDULO: PARÁBOLA
# ==========================================
elif conica_seleccionada == "Parábola":
    orientacion = st.sidebar.selectbox(
        "Orientación de la parábola:", 
        ["Vertical (abre hacia arriba o abajo)", "Horizontal (abre hacia derecha o izquierda)"]
    )
    p = st.sidebar.slider("Distancia focal (p)", -5.0, 5.0, 2.0, 0.5)
    
    if p == 0:
        p = 0.5
        st.sidebar.warning("El valor de 'p' no puede ser 0. Se ajustó a 0.5.")

    t = np.linspace(-12, 12, 400)
    
    with col_controles:
        st.subheader("Fórmulas")
        if "Vertical" in orientacion:
            x = h + t
            y = k + (t**2) / (4 * p)
            foco_x, foco_y = h, k + p
            lr_x = [h - abs(2*p), h + abs(2*p)]
            lr_y = [k + p, k + p]
            
            st.markdown("**Ecuación Canónica (Vertical):**")
            st.latex(r"(x - h)^2 = 4p(y - k)")
            st.markdown("**Ecuación con tus valores actuales:**")
            st.latex(rf"(x {formatear_signo(h)})^2 = {4*p:.1f}(y {formatear_signo(k)})")
            ec_directriz = f"y = {k - p:.2f}"
        else:
            y = k + t
            x = h + (t**2) / (4 * p)
            foco_x, foco_y = h + p, k
            lr_x = [h + p, h + p]
            lr_y = [k - abs(2*p), k + abs(2*p)]
            
            st.markdown("**Ecuación Canónica (Horizontal):**")
            st.latex(r"(y - k)^2 = 4p(x - h)")
            st.markdown("**Ecuación con tus valores actuales:**")
            st.latex(rf"(y {formatear_signo(k)})^2 = {4*p:.1f}(x {formatear_signo(h)})")
            ec_directriz = f"x = {h - p:.2f}"

        st.markdown("---")
        st.subheader("Elementos de la Parábola")
        st.write(rf"• **Vértice $V(h, k)$:** $({h:.1f}, {k:.1f})$")
        st.write(rf"• **Distancia focal ($p$):** ${p:.1f}$ unidades")
        st.write(rf"• **Foco $F$:** $({foco_x:.2f}, {foco_y:.2f})$")
        st.write(rf"• **Recta Directriz:** ${ec_directriz}$")
        st.write(rf"• **Ancho del Lado Recto ($|4p|$):** ${abs(4*p):.1f}$ unidades")

    with col_grafica:
        fig = crear_figura_base()
        fig.add_trace(go.Scatter(
            x=x, y=y, mode="lines", name="Parábola",
            line=dict(color="#1f77b4", width=3)
        ))
        fig.add_trace(go.Scatter(
            x=[h], y=[k], mode="markers+text", name="Vértice V",
            text=[f"V({h:.1f},{k:.1f})"], textposition="bottom right",
            marker=dict(color="#d62728", size=9)
        ))
        fig.add_trace(go.Scatter(
            x=[foco_x], y=[foco_y], mode="markers+text", name="Foco F",
            text=[f"F({foco_x:.1f},{foco_y:.1f})"], textposition="top right",
            marker=dict(color="#ff7f0e", size=10, symbol="star")
        ))
        fig.add_trace(go.Scatter(
            x=lr_x, y=lr_y, mode="lines", name=f"Lado Recto ({abs(4*p):.1f})",
            line=dict(color="#2ca02c", width=2, dash="dot")
        ))
        if "Vertical" in orientacion:
            fig.add_trace(go.Scatter(
                x=[-15, 15], y=[k - p, k - p], mode="lines", name=f"Directriz ({ec_directriz})",
                line=dict(color="#9467bd", width=2, dash="dash")
            ))
        else:
            fig.add_trace(go.Scatter(
                x=[h - p, h - p], y=[-15, 15], mode="lines", name=f"Directriz ({ec_directriz})",
                line=dict(color="#9467bd", width=2, dash="dash")
            ))
        st.plotly_chart(fig, use_container_width=True)

    # Ejercicio Aplicativo de Bachillerato
    st.markdown("---")
    st.subheader("📡 Ejercicio Aplicativo: Antena parabólica de televisión")
    st.info(
        "**Problema:** Las antenas de televisión satelital tienen forma de parábola porque cualquier señal que llega "
        "desde el espacio rebota en el plato y se concentra en un único punto llamado **Foco**, donde se coloca el receptor. "
        "Imagina una antena grande vista de perfil con su vértice en $V(0, 0)$ que abre hacia arriba. Si la antena mide "
        "$8\,m$ de ancho total en su borde superior (de $x = -4$ a $x = 4$) y tiene una profundidad de $2\,m$ ($y = 2$):\n\n"
        "1. ¿A qué distancia $p$ del fondo del plato debe colocarse el micrófono o receptor para captar la señal?\n"
        "2. ¿Cuánto mide el lado recto de esta antena?"
    )
    if st.button("Revelar solución paso a paso", key="btn_par"):
        st.success("**Solución:**")
        st.markdown(
            "1. **Calculamos la distancia focal ($p$):** Como el vértice está en $(0,0)$ y abre hacia arriba, "
            "usamos la fórmula $x^2 = 4py$. Sabemos que el borde derecho del plato pasa por el punto $(x = 4, y = 2)$:"
        )
        st.latex(r"(4)^2 = 4p(2) \implies 16 = 8p \implies p = \frac{16}{8} = 2.0 \,\text{m}")
        st.markdown(
            "El receptor debe colocarse exactamente a **$2.0\,m$** sobre el vértice, es decir, en el foco $F(0, 2)$.\n\n"
            "2. **Lado Recto:** Mide $|4p| = 4 \\times 2.0 = 8.0\,m$. *(Ajusta $h=0, k=0$ y $p=2.0$ en el menú para verlo en pantalla)*."
        )


# ==========================================
# 3. MÓDULO: ELIPSE
# ==========================================
elif conica_seleccionada == "Elipse":
    a = st.sidebar.slider("Semieje horizontal (a)", 1.0, 12.0, 6.0, 0.5)
    b = st.sidebar.slider("Semieje vertical (b)", 1.0, 12.0, 4.0, 0.5)
    
    theta = np.linspace(0, 2 * np.pi, 400)
    x = h + a * np.cos(theta)
    y = k + b * np.sin(theta)
    
    c = np.sqrt(abs(a**2 - b**2))
    if a >= b:
        tipo_elipse = "Horizontal (más ancha que alta)"
        f1_x, f1_y = h - c, k
        f2_x, f2_y = h + c, k
        excentricidad = c / a if a != 0 else 0
    else:
        tipo_elipse = "Vertical (más alta que ancha)"
        f1_x, f1_y = h, k - c
        f2_x, f2_y = h, k + c
        excentricidad = c / b if b != 0 else 0

    with col_controles:
        st.subheader("Fórmulas")
        st.markdown("**Ecuación Canónica:**")
        st.latex(r"\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1")
        
        st.markdown("**Ecuación con tus valores actuales:**")
        st.latex(rf"\frac{{(x {formatear_signo(h)})^2}}{{{a**2:.2f}}} + \frac{{(y {formatear_signo(k)})^2}}{{{b**2:.2f}}} = 1")
        
        st.markdown("---")
        st.subheader("Elementos de la Elipse")
        st.write(f"• **Forma:** {tipo_elipse}")
        st.write(rf"• **Centro $C(h, k)$:** $({h:.1f}, {k:.1f})$")
        st.write(rf"• **Distancia del centro al foco ($c = \sqrt{{|a^2 - b^2|}}$):** ${c:.2f}$ unidades")
        st.write(rf"• **Focos:** $F_1({f1_x:.2f}, {f1_y:.2f})$ y $F_2({f2_x:.2f}, {f2_y:.2f})$")
        st.write(rf"• **Excentricidad ($e$, qué tan achatada es):** ${excentricidad:.2f}$")

    with col_grafica:
        fig = crear_figura_base()
        fig.add_trace(go.Scatter(
            x=x, y=y, mode="lines", name="Elipse",
            line=dict(color="#1f77b4", width=3)
        ))
        fig.add_trace(go.Scatter(
            x=[h], y=[k], mode="markers", name="Centro C",
            marker=dict(color="#d62728", size=8)
        ))
        fig.add_trace(go.Scatter(
            x=[f1_x, f2_x], y=[f1_y, f2_y], mode="markers+text", name="Focos (F1, F2)",
            text=["F1", "F2"], textposition="top center",
            marker=dict(color="#ff7f0e", size=10, symbol="star")
        ))
        fig.add_trace(go.Scatter(
            x=[h - a, h + a, h, h], y=[k, k, k - b, k + b],
            mode="markers", name="Vértices",
            marker=dict(color="#2ca02c", size=7)
        ))
        st.plotly_chart(fig, use_container_width=True)

    # Ejercicio Aplicativo de Bachillerato
    st.markdown("---")
    st.subheader("🗣️ Ejercicio Aplicativo: La Galería de los Susurros en un Museo")
    st.info(
        "**Problema:** En muchos museos de ciencias hay salas con forma de elipse llamadas *Galerías de los Susurros*. "
        "Si te paras en uno de los focos ($F_1$) y susurras algo muy bajito, el sonido rebota en las paredes curvas y tu amigo, "
        "parado en el otro foco ($F_2$) al otro lado del salón, te escuchará como si estuvieras a su lado. "
        "Si el salón tiene su centro en $C(0,0)$, mide $20\,m$ de largo total (semieje $a = 10\,m$) y "
        "$12\,m$ de ancho total (semieje $b = 6\,m$):\n\n"
        "1. ¿En qué coordenadas exactas ($F_1$ y $F_2$) deben pararse tú y tu amigo para escuchar el secreto?\n"
        "2. ¿Qué distancia los separa a ustedes dos?"
    )
    if st.button("Revelar solución paso a paso", key="btn_eli"):
        st.success("**Solución:**")
        st.markdown("1. **Buscamos la distancia focal ($c$):** En toda elipse se cumple que $c = \sqrt{a^2 - b^2}$. Sustituimos $a = 10$ y $b = 6$:")
        st.latex(r"c = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8.0\,\text{m}")
        st.markdown(
            "Por lo tanto, deben pararse a $8\,m$ a cada lado del centro: uno en **$F_1(-8.0, 0)$** y el otro en **$F_2(8.0, 0)$**.\n\n"
            "2. **Distancia entre ambos:** Como cada uno está a $8\,m$ del centro, la distancia total entre los dos amigos es $2c = 16.0\,m$. "
            "*(Pon $h=0, k=0, a=10$ y $b=6$ en los controles para ver dónde quedan las estrellas naranjas)*."
        )


# ==========================================
# 4. MÓDULO: HIPÉRBOLA
# ==========================================
elif conica_seleccionada == "Hipérbola":
    orientacion_hip = st.sidebar.selectbox(
        "Orientación de la hipérbola:", 
        ["Horizontal (abre a izquierda y derecha)", "Vertical (abre hacia arriba y abajo)"]
    )
    a = st.sidebar.slider("Semieje horizontal (a)", 1.0, 8.0, 3.0, 0.5)
    b = st.sidebar.slider("Semieje vertical (b)", 1.0, 8.0, 4.0, 0.5)
    
    c = np.sqrt(a**2 + b**2)
    t = np.linspace(-2.2, 2.2, 300)
    
    x_asin = np.linspace(h - 15, h + 15, 100)
    y_asin_pos = k + (b / a) * (x_asin - h)
    y_asin_neg = k - (b / a) * (x_asin - h)

    with col_controles:
        st.subheader("Fórmulas")
        if "Horizontal" in orientacion_hip:
            x_rama1 = h + a * np.cosh(t)
            y_rama1 = k + b * np.sinh(t)
            x_rama2 = h - a * np.cosh(t)
            y_rama2 = k + b * np.sinh(t)
            
            f1_x, f1_y = h - c, k
            f2_x, f2_y = h + c, k
            v1_x, v1_y = h - a, k
            v2_x, v2_y = h + a, k
            
            st.markdown("**Ecuación Canónica (Horizontal):**")
            st.latex(r"\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1")
            st.markdown("**Ecuación con tus valores actuales:**")
            st.latex(rf"\frac{{(x {formatear_signo(h)})^2}}{{{a**2:.2f}}} - \frac{{(y {formatear_signo(k)})^2}}{{{b**2:.2f}}} = 1")
        else:
            y_rama1 = k + b * np.cosh(t)
            x_rama1 = h + a * np.sinh(t)
            y_rama2 = k - b * np.cosh(t)
            x_rama2 = h + a * np.sinh(t)
            
            f1_x, f1_y = h, k - c
            f2_x, f2_y = h, k + c
            v1_x, v1_y = h, k - b
            v2_x, v2_y = h, k + b
            
            st.markdown("**Ecuación Canónica (Vertical):**")
            st.latex(r"\frac{(y - k)^2}{b^2} - \frac{(x - h)^2}{a^2} = 1")
            st.markdown("**Ecuación con tus valores actuales:**")
            st.latex(rf"\frac{{(y {formatear_signo(k)})^2}}{{{b**2:.2f}}} - \frac{{(x {formatear_signo(h)})^2}}{{{a**2:.2f}}} = 1")

        st.markdown("**Rectas Asíntotas (líneas guía):**")
        st.latex(rf"y {formatear_signo(k)} = \pm \frac{{{b:.1f}}}{{{a:.1f}}}(x {formatear_signo(h)})")
        
        st.markdown("---")
        st.subheader("Elementos de la Hipérbola")
        st.write(rf"• **Centro $C(h, k)$:** $({h:.1f}, {k:.1f})$")
        st.write(rf"• **Vértices:** $V_1({v1_x:.1f}, {v1_y:.1f})$ y $V_2({v2_x:.1f}, {v2_y:.1f})$")
        st.write(rf"• **Distancia focal ($c = \sqrt{{a^2 + b^2}}$):** ${c:.2f}$ unidades")
        st.write(rf"• **Focos:** $F_1({f1_x:.2f}, {f1_y:.2f})$ y $F_2({f2_x:.2f}, {f2_y:.2f})$")

    with col_grafica:
        fig = crear_figura_base()
        fig.add_trace(go.Scatter(
            x=x_rama1, y=y_rama1, mode="lines", name="Hipérbola",
            line=dict(color="#1f77b4", width=3)
        ))
        fig.add_trace(go.Scatter(
            x=x_rama2, y=y_rama2, mode="lines", name="Rama 2",
            line=dict(color="#1f77b4", width=3), showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=x_asin, y=y_asin_pos, mode="lines", name="Asíntotas",
            line=dict(color="rgba(150, 150, 150, 0.8)", width=1.5, dash="dash")
        ))
        fig.add_trace(go.Scatter(
            x=x_asin, y=y_asin_neg, mode="lines", name="Asíntota 2",
            line=dict(color="rgba(150, 150, 150, 0.8)", width=1.5, dash="dash"),
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=[h], y=[k], mode="markers", name="Centro C",
            marker=dict(color="#d62728", size=8)
        ))
        fig.add_trace(go.Scatter(
            x=[v1_x, v2_x], y=[v1_y, v2_y], mode="markers+text", name="Vértices",
            text=["V1", "V2"], textposition="bottom center",
            marker=dict(color="#2ca02c", size=8)
        ))
        fig.add_trace(go.Scatter(
            x=[f1_x, f2_x], y=[f1_y, f2_y], mode="markers+text", name="Focos",
            text=["F1", "F2"], textposition="top center",
            marker=dict(color="#ff7f0e", size=10, symbol="star")
        ))
        st.plotly_chart(fig, use_container_width=True)

    # Ejercicio Aplicativo de Bachillerato
    st.markdown("---")
    st.subheader("🏛️ Ejercicio Aplicativo: La torre con silueta de reloj de arena")
    st.info(
        "**Problema:** Muchos edificios modernos, torres de observación y lámparas tienen una silueta curva parecida "
        "a un reloj de arena, cuyos bordes laterales siguen una **hipérbola horizontal**. Imagina una torre centrada en "
        "$C(0,0)$ en su cintura más angosta, cuyos parámetros son $a = 3.0\,m$ y $b = 4.0\,m$:\n\n"
        "1. ¿Cuánto mide de ancho la torre en su parte más angosta (la distancia entre sus dos vértices $V_1$ y $V_2$)?\n"
        "2. ¿A qué distancia $c$ del centro están ubicados los focos de esta hipérbola?"
    )
    if st.button("Revelar solución paso a paso", key="btn_hip"):
        st.success("**Solución:**")
        st.markdown(
            "1. **Ancho en la cintura más angosta:** Los bordes más cercanos entre sí son los vértices $V_1(-3, 0)$ y $V_2(3, 0)$. "
            "La distancia total entre ellos es $2a = 2 \\times 3.0 = 6.0\,m$."
        )
        st.markdown("2. **Distancia a los focos ($c$):** En la hipérbola se usa el Teorema de Pitágoras sumando $a^2 + b^2$:")
        st.latex(r"c = \sqrt{a^2 + b^2} = \sqrt{3.0^2 + 4.0^2} = \sqrt{9 + 16} = \sqrt{25} = 5.0\,\text{m}")