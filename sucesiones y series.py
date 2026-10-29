import streamlit as st

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Sucesiones, Progresiones y Series",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# FUNCIONES AUXILIARES DE FORMATO EN LATEX
# ==========================================
def fmt_num(val):
    """Muestra enteros sin decimales y flotantes con 2 decimales."""
    if abs(val - round(val)) < 1e-9:
        return f"{int(round(val))}"
    return f"{val:.2f}"

def fmt_signo(val, ConEspacio=True):
    """Formatea un número con su signo + o - para ecuaciones en LaTeX."""
    esp = " " if ConEspacio else ""
    if val >= 0:
        return f"+{esp}{fmt_num(abs(val))}"
    else:
        return f"-{esp}{fmt_num(abs(val))}"

# ==========================================
# BARRA LATERAL (MENÚ DE NAVEGACIÓN)
# ==========================================
st.sidebar.title("🔢 Sucesiones y Series")
st.sidebar.markdown("Laboratorio algebraico de términos generales, sistemas 2×2 y sumatorias.")

seccion = st.sidebar.radio(
    "Selecciona el módulo de la clase:",
    [
        "1. Conceptos y Sucesión Lineal",
        "2. Sucesión Geométrica",
        "3. Sucesión Cuadrática (Sistema 2×2)",
        "4. Series y Sumatorias (∑)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Nota didáctica:** Usa los controles de cada sección para generar sucesiones en vivo "
    "y verificar las fórmulas antes de resolver los ejercicios aplicativos."
)

# ==============================================================================
# MÓDULO 1: CONCEPTOS BASE Y SUCESIÓN LINEAL (PROGRESIÓN ARITMÉTICA)
# ==============================================================================
if seccion == "1. Conceptos y Sucesión Lineal":
    st.title("📏 Conceptos Fundamentales y Sucesión Lineal")

    # Tarjetas de definiciones conceptuales
    st.subheader("1. Diferencia entre Sucesión, Progresión y Serie")
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        st.info(
            "**1. ¿Qué es una Sucesión?**\n\n"
            "Es una lista ordenada de números ($a_1, a_2, a_3, \\dots, a_n$) que obedece una regla "
            "o patrón determinado. Cada número ocupa una posición específica $n \\in \\mathbb{N}$."
        )
    with col_c2:
        st.success(
            "**2. ¿Qué es una Progresión?**\n\n"
            "Es un tipo especial de sucesión que sigue una ley constante de crecimiento o decrecimiento "
            "entre términos consecutivos (como sumar siempre lo mismo o multiplicar siempre por lo mismo)."
        )
    with col_c3:
        st.warning(
            "**3. ¿Qué es una Serie?**\n\n"
            "Es la **suma indicada** de los términos de una sucesión o progresión:\n\n"
            "$S_n = a_1 + a_2 + a_3 + \\dots + a_n = \\sum_{k=1}^{n} a_k$"
        )

    st.markdown("---")
    st.subheader("2. Sucesión Lineal (Progresión Aritmética)")
    st.markdown(
        "Una **sucesión lineal** (o *progresión aritmética*) es aquella en la que la **diferencia ($d$)** "
        "entre cualquier término y su anterior es siempre **constante**."
    )

    col_teo, col_sim = st.columns([1.1, 1.3], gap="large")

    with col_teo:
        st.markdown("**Condición de diferencia constante ($d$):**")
        st.latex(r"a_{n+1} - a_n = d")

        st.markdown("**Fórmula del Término General ($a_n$):**")
        st.latex(r"a_n = a_1 + (n - 1)d")

        st.markdown("**Forma explícita lineal ($An + B$):**")
        st.markdown("Al distribuir $d$, la fórmula toma la estructura de una función lineal:")
        st.latex(r"a_n = d \cdot n + (a_1 - d)")
        st.write(
            "• **$a_1$:** Primer término de la sucesión ($n = 1$).\n"
            "• **$d$:** Diferencia común (si $d > 0$ es creciente; si $d < 0$ es decreciente).\n"
            "• **$n$:** Posición del término que deseamos hallar ($n = 1, 2, 3, \\dots$)."
        )

    with col_sim:
        st.markdown("#### 🛠️ Explorador Algebraico de Sucesiones Lineales")
        c1, c2, c3 = st.columns(3)
        a1_lin = c1.number_input("Primer término (a₁):", value=5.0, step=1.0)
        d_lin = c2.number_input("Diferencia constante (d):", value=4.0, step=1.0)
        n_lin = c3.number_input("Posición a calcular (n):", min_value=1, max_value=500, value=12, step=1)

        # Primeros 6 términos
        terminos_lin = [a1_lin + (i - 1) * d_lin for i in range(1, 7)]
        str_terminos = ", \\; ".join([fmt_num(t) for t in terminos_lin])
        an_val = a1_lin + (n_lin - 1) * d_lin
        indep_lin = a1_lin - d_lin

        st.markdown("**Primeros 6 términos de tu sucesión:**")
        st.latex(rf"\{{a_n\}} = \{{{str_terminos}, \dots\}}")

        st.markdown("**Verificación de la primera diferencia constante ($a_{n+1} - a_n = d$):**")
        st.latex(rf"\underbrace{{{fmt_num(terminos_lin[1])} - ({fmt_num(terminos_lin[0])})}}_{{d = {fmt_num(d_lin)}}} \;=\; "
                 rf"\underbrace{{{fmt_num(terminos_lin[2])} - ({fmt_num(terminos_lin[1])})}}_{{d = {fmt_num(d_lin)}}} \;=\; "
                 rf"\underbrace{{{fmt_num(terminos_lin[3])} - ({fmt_num(terminos_lin[2])})}}_{{d = {fmt_num(d_lin)}}}")

        st.markdown("**Término general sustituido y simplificado:**")
        st.latex(rf"a_n = {fmt_num(a1_lin)} + (n - 1)({fmt_num(d_lin)}) \implies a_n = {fmt_num(d_lin)}n {fmt_signo(indep_lin)}")

        st.success(rf"**Cálculo para la posición $n = {n_lin}$:**  $a_{{{n_lin}}} = {fmt_num(a1_lin)} + ({n_lin} - 1)({fmt_num(d_lin)}) = {fmt_num(an_val)}$")

    # EJERCICIOS APLICATIVOS DE SUCESIÓN LINEAL
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos: Sucesión Lineal")
    tab_l1, tab_l2 = st.tabs([
        "🏃‍♂️ Ejercicio 1: Plan de Entrenamiento de Atletismo (Hallar término y despejar n)",
        "🎭 Ejercicio 2: Filas de un Teatro Escolar (Construir la regla general)"
    ])

    with tab_l1:
        st.info(
            "**Problema 1:** Camila se está preparando para una carrera intercolegiada. En la primera semana de entrenamiento "
            "corre **$a_1 = 1\\,500\\text{ metros}$** diarios. Su entrenador le diseña un plan lineal en el que cada nueva semana "
            "aumenta la distancia diaria en **$d = 400\\text{ metros}$** respecto a la semana anterior.\n\n"
            "1. **Fórmula general:** Encuentra la expresión del término general $a_n$ para la distancia que corre en la semana $n$.\n"
            "2. **Evaluar:** ¿Cuántos metros diarios correrá Camila en la **semana $n = 8$**?\n"
            "3. **Despejar $n$:** ¿En qué semana de entrenamiento alcanzará exactamente la meta de correr **$5\\,900\\text{ metros}$** diarios?"
        )
        if st.button("Revelar solución paso a paso (Lineal 1)", key="btn_lin1"):
            st.success("**Solución estructurada:**")
            st.markdown("**1. Término general ($a_n$):** Identificamos $a_1 = 1\\,500$ y la diferencia constante $d = 400$:")
            st.latex(r"a_n = a_1 + (n - 1)d \implies a_n = 1\,500 + (n - 1)(400)")
            st.latex(r"a_n = 1\,500 + 400n - 400 \implies a_n = 400n + 1\,100")
            st.markdown("**2. Distancia en la semana $n = 8$:** Sustituimos $n = 8$:")
            st.latex(r"a_8 = 400(8) + 1\,100 = 3\,200 + 1\,100 = 4\,300 \text{ metros diarios}")
            st.markdown("**3. Despejar la semana $n$ cuando $a_n = 5\,900$:**")
            st.latex(r"400n + 1\,100 = 5\,900 \implies 400n = 5\,900 - 1\,100")
            st.latex(r"400n = 4\,800 \implies n = \frac{4\,800}{400} = 12 \text{ (En la semana 12)}")

    with tab_l2:
        st.info(
            "**Problema 2:** El auditorio del colegio tiene sus sillas organizadas de forma que cada fila tiene más asientos que la anterior. "
            "En la primera fila hay **$14\\text{ sillas}$**, en la segunda hay **$17\\text{ sillas}$**, en la tercera hay **$20\\text{ sillas}$** "
            "y en la cuarta hay **$23\\text{ sillas}$**.\n\n"
            "1. Demuestra que es una sucesión lineal hallando la diferencia constante $d$.\n"
            "2. ¿Cuántas sillas tiene la **fila $15$** (la última fila del auditorio)?"
        )
        if st.button("Revelar solución paso a paso (Lineal 2)", key="btn_lin2"):
            st.success("**Solución estructurada:**")
            st.markdown("**1. Verificación de la diferencia ($d$):** Restamos términos consecutivos ($a_{n+1} - a_n$):")
            st.latex(r"d = 17 - 14 = 3, \quad 20 - 17 = 3, \quad 23 - 20 = 3 \implies d = 3 \text{ sillas por fila}")
            st.markdown("**2. Sillas en la fila $n = 15$:** Con $a_1 = 14$ y $d = 3$:")
            st.latex(r"a_{15} = 14 + (15 - 1)(3) = 14 + 14(3) = 14 + 42 = 56 \text{ sillas en la fila 15}")


# ==============================================================================
# MÓDULO 2: SUCESIÓN GEOMÉTRICA (PROGRESIÓN GEOMÉTRICA)
# ==============================================================================
elif seccion == "2. Sucesión Geométrica":
    st.title("🚀 Sucesión Geométrica (Progresión Geométrica)")
    st.markdown(
        "Una **sucesión geométrica** es aquella en la que el **cociente o razón ($r$)** entre cualquier término "
        "y su término inmediatamente anterior es siempre **constante**. Para pasar de un término al siguiente, "
        "se multiplica siempre por el mismo número $r$."
    )

    col_teo_g, col_sim_g = st.columns([1.1, 1.3], gap="large")

    with col_teo_g:
        st.markdown("**Condición de razón constante ($r$):**")
        st.latex(r"\frac{a_{n+1}}{a_n} = r \quad (a_n \neq 0, \; r \neq 0)")

        st.markdown("**Fórmula del Término General ($a_n$):**")
        st.latex(r"a_n = a_1 \cdot r^{n-1}")

        st.markdown("**Comportamiento según el valor de la razón $r$ (con $a_1 > 0$):**")
        st.write(
            "• **Si $r > 1$:** La sucesión crece rápidamente de forma exponencial (ej. $2, 6, 18, 54, \\dots$).\n"
            "• **Si $0 < r < 1$:** La sucesión decrece acercándose a cero (ej. $80, 40, 20, 10, \\dots$).\n"
            "• **Si $r < 0$:** La sucesión es **alternante** (cambia de signo $+$ y $-$ en cada término)."
        )

    with col_sim_g:
        st.markdown("#### 🛠️ Explorador Algebraico de Sucesiones Geométricas")
        cg1, cg2, cg3 = st.columns(3)
        a1_geo = cg1.number_input("Primer término (a₁):", value=3.0, step=1.0, key="g_a1")
        r_geo = cg2.number_input("Razón constante (r):", value=2.0, step=0.5, key="g_r")
        n_geo = cg3.number_input("Posición a calcular (n):", min_value=1, max_value=30, value=7, step=1, key="g_n")

        if r_geo == 0:
            r_geo = 1.0
            st.warning("La razón 'r' no debe ser 0. Se ajustó a 1.0.")

        terminos_geo = [a1_geo * (r_geo ** (i - 1)) for i in range(1, 7)]
        str_term_g = ", \\; ".join([fmt_num(t) for t in terminos_geo])
        an_geo_val = a1_geo * (r_geo ** (n_geo - 1))

        st.markdown("**Primeros 6 términos de tu sucesión:**")
        st.latex(rf"\{{a_n\}} = \{{{str_term_g}, \dots\}}")

        if a1_geo != 0:
            st.markdown("**Verificación del cociente constante ($\\frac{a_{n+1}}{a_n} = r$):**")
            st.latex(rf"\frac{{{fmt_num(terminos_geo[1])}}}{{{fmt_num(terminos_geo[0])}}} = "
                     rf"\frac{{{fmt_num(terminos_geo[2])}}}{{{fmt_num(terminos_geo[1])}}} = "
                     rf"\frac{{{fmt_num(terminos_geo[3])}}}{{{fmt_num(terminos_geo[2])}}} = {fmt_num(r_geo)}")

        st.markdown("**Fórmula del término general particular:**")
        st.latex(rf"a_n = {fmt_num(a1_geo)} \cdot ({fmt_num(r_geo)})^{{n - 1}}")

        st.success(
            rf"**Cálculo para la posición $n = {n_geo}$:**  "
            rf"$a_{{{n_geo}}} = {fmt_num(a1_geo)} \cdot ({fmt_num(r_geo)})^{{{n_geo} - 1}} = "
            rf"{fmt_num(a1_geo)} \cdot ({fmt_num(r_geo)})^{{{n_geo - 1}}} = {fmt_num(an_geo_val)}$"
        )

    # EJERCICIOS APLICATIVOS DE SUCESIÓN GEOMÉTRICA
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos: Sucesión Geométrica")
    tab_g1, tab_g2 = st.tabs([
        "🏀 Ejercicio 1: Altura en los Rebotes de un Balón (Razón fraccionaria)",
        "🔬 Ejercicio 2: Bipartición de Levaduras en Laboratorio (Despejar n)"
    ])

    with tab_g1:
        st.info(
            "**Problema 1:** En una práctica de física, dejas caer un balón de baloncesto desde una ventana. "
            "En su **primer rebote** ($n = 1$), el balón alcanza una altura máxima de **$a_1 = 243\\text{ cm}$**. "
            "En cada rebote siguiente, debido a la pérdida de energía, el balón alcanza exactamente **dos tercios ($r = \\frac{2}{3}$)** "
            "de la altura alcanzada en el rebote inmediatamente anterior.\n\n"
            "1. **Fórmula general:** Escribe el término general $a_n$ que modela la altura (en $\\text{cm}$) del rebote número $n$.\n"
            "2. **Evaluar:** ¿Qué altura exacta alcanzará el balón en su **sexto rebote ($n = 6$)**?"
        )
        if st.button("Revelar solución paso a paso (Geométrica 1)", key="btn_geo1"):
            st.success("**Solución estructurada:**")
            st.markdown("**1. Planteamiento del término general:** Con $a_1 = 243\\text{ cm}$ y razón $r = \\frac{2}{3}$:")
            st.latex(r"a_n = a_1 \cdot r^{n-1} \implies a_n = 243 \cdot \left(\frac{2}{3}\right)^{n-1}")
            st.markdown("**2. Altura en el sexto rebote ($n = 6$):** Sustituimos $n = 6$ en el exponente ($6 - 1 = 5$):")
            st.latex(r"a_6 = 243 \cdot \left(\frac{2}{3}\right)^{6-1} = 243 \cdot \left(\frac{2}{3}\right)^5")
            st.markdown("Como $2^5 = 32$ y $3^5 = 243$, simplificamos directamente:")
            st.latex(r"a_6 = 243 \cdot \frac{32}{243} = 32 \text{ cm}")

    with tab_g2:
        st.info(
            "**Problema 2:** En un tubo de ensayo hay inicialmente **$a_1 = 5\\text{ células de levadura}$** en el minuto $n = 1$. "
            "Las células se reproducen duplicándose en cada etapa ($r = 2$), de modo que en la etapa $2$ hay $10$, en la etapa $3$ hay $20$, "
            "en la etapa $4$ hay $40$, y así sucesivamente.\n\n"
            "1. Escribe la fórmula del término general $a_n$.\n"
            "2. **Despejar la posición $n$:** ¿En qué número de etapa ($n$) la población será exactamente de **$2\\,560\\text{ células}$**?"
        )
        if st.button("Revelar solución paso a paso (Geométrica 2)", key="btn_geo2"):
            st.success("**Solución estructurada:**")
            st.markdown("**1. Término general:** Con $a_1 = 5$ y razón $r = 2 = \\frac{10}{5}$:")
            st.latex(r"a_n = 5 \cdot 2^{n-1}")
            st.markdown("**2. Despejar la etapa $n$ cuando $a_n = 2\,560$:** Igualamos y dividimos entre $5$:")
            st.latex(r"5 \cdot 2^{n-1} = 2\,560 \implies 2^{n-1} = \frac{2\,560}{5} \implies 2^{n-1} = 512")
            st.markdown("Expresamos $512$ como potencia de base $2$ ($512 = 2^9$) e igualamos los exponentes:")
            st.latex(r"2^{n-1} = 2^9 \implies n - 1 = 9 \implies n = 10 \text{ (En la décima etapa)}")


# ==============================================================================
# MÓDULO 3: SUCESIÓN CUADRÁTICA Y SISTEMA 2x2
# ==============================================================================
elif seccion == "3. Sucesión Cuadrática (Sistema 2×2)":
    st.title("📐 Sucesión Cuadrática y Método del Sistema 2×2")
    st.markdown(
        "Una **sucesión cuadrática** es aquella en la que las **primeras diferencias ($\\Delta^1$) no son constantes**, "
        "pero las **segundas diferencias ($\\Delta^2$) sí son constantes**. Su término general tiene forma de polinomio de segundo grado."
    )

    col_teo_c, col_sim_c = st.columns([1.15, 1.35], gap="large")

    with col_teo_c:
        st.subheader("Procedimiento Algebraico (3 Pasos)")
        st.markdown("**Forma General de una Sucesión Cuadrática:**")
        st.latex(r"a_n = An^2 + Bn + C")

        st.markdown("**Paso 1: Hallar el coeficiente $A$ con la segunda diferencia ($\\Delta^2$)**")
        st.markdown("Al evaluar $n=1, 2, 3$ en $An^2 + Bn + C$ y restar dos veces seguidas, se demuestra que la segunda diferencia constante equivale siempre al doble de $A$:")
        st.latex(r"\Delta^2 = 2A \implies A = \frac{\Delta^2}{2}")

        st.markdown("**Paso 2: Armar el Sistema de Ecuaciones Lineales $2 \\times 2$ para hallar $B$ y $C$**")
        st.markdown("Ya conociendo el valor de $A$, sustituimos las dos primeras posiciones ($n = 1$ y $n = 2$) en la fórmula general $a_n = An^2 + Bn + C$:")
        st.latex(r"\text{Para } n = 1: \quad A(1)^2 + B(1) + C = a_1 \implies B + C = a_1 - A \quad \text{(Ec. 1)}")
        st.latex(r"\text{Para } n = 2: \quad A(2)^2 + B(2) + C = a_2 \implies 2B + C = a_2 - 4A \quad \text{(Ec. 2)}")

        st.markdown("**Paso 3: Resolver el Sistema $2 \\times 2$ por Reducción (Resta)**")
        st.markdown("Si restamos $(\\text{Ec. 2}) - (\\text{Ec. 1})$, la incógnita $C$ se cancela inmediatamente:")
        st.latex(r"(2B + C) - (B + C) = (a_2 - 4A) - (a_1 - A) \implies B = (a_2 - a_1) - 3A")
        st.latex(r"\text{Finalmente, despejamos } C \text{ en la Ec. 1:} \quad C = a_1 - A - B")

    with col_sim_c:
        st.subheader("🧮 Solucionador Interactivo de Sucesiones Cuadráticas")
        st.markdown("Ingresa el primer término ($a_1$), la primera diferencia inicial ($d_1 = a_2 - a_1$) y la segunda diferencia constante ($\\Delta^2$) para ver la tabla y el sistema $2 \\times 2$ resuelto en vivo:")

        cc1, cc2, cc3 = st.columns(3)
        a1_cuad = cc1.number_input("Primer término (a₁):", value=4.0, step=1.0)
        d1_ini = cc2.number_input("1ra diferencia (a₂ - a₁):", value=5.0, step=1.0)
        delta2 = cc3.number_input("2da diferencia cte (Δ²):", value=2.0, step=2.0)

        if delta2 == 0:
            st.warning("Si Δ² = 0, la sucesión es lineal (A = 0). Elige Δ² distinto de cero.")
            delta2 = 2.0

        # Construcción de los primeros 5 términos a partir de a1, d1_ini y delta2
        A_calc = delta2 / 2.0
        a2_cuad = a1_cuad + d1_ini
        # Ecuaciones del sistema 2x2:
        # B + C = rhs1
        # 2B + C = rhs2
        rhs1 = a1_cuad - A_calc
        rhs2 = a2_cuad - 4 * A_calc
        B_calc = rhs2 - rhs1
        C_calc = rhs1 - B_calc

        t_cuad = [A_calc * (n**2) + B_calc * n + C_calc for n in range(1, 6)]
        dif1 = [t_cuad[i+1] - t_cuad[i] for i in range(4)]
        dif2 = [dif1[i+1] - dif1[i] for i in range(3)]

        st.markdown("**1. Esquema de diferencias de la sucesión:**")
        st.latex(
            rf"\begin{{array}}{{ccccccccc}}"
            rf"\textbf{{Posición }} (n): & 1 & & 2 & & 3 & & 4 & & 5 \\"
            rf"\textbf{{Términos }} (a_n): & {fmt_num(t_cuad[0])} & & {fmt_num(t_cuad[1])} & & {fmt_num(t_cuad[2])} & & {fmt_num(t_cuad[3])} & & {fmt_num(t_cuad[4])} \\"
            rf"\textbf{{1ra Dif. }} (\Delta^1): & & {fmt_signo(dif1[0], False)} & & {fmt_signo(dif1[1], False)} & & {fmt_signo(dif1[2], False)} & & {fmt_signo(dif1[3], False)} & \\"
            rf"\textbf{{2da Dif. }} (\Delta^2): & & & \mathbf{{{fmt_signo(dif2[0], False)}}} & & \mathbf{{{fmt_signo(dif2[1], False)}}} & & \mathbf{{{fmt_signo(dif2[2], False)}}} & & "
            rf"\end{{array}}"
        )

        st.markdown("**2. Cálculo de $A$ con la segunda diferencia:**")
        st.latex(rf"2A = \Delta^2 \implies 2A = {fmt_num(delta2)} \implies A = \frac{{{fmt_num(delta2)}}}{{2}} = {fmt_num(A_calc)}")

        st.markdown(rf"**3. Planteamiento del Sistema $2 \times 2$ con $a_1 = {fmt_num(t_cuad[0])}$ y $a_2 = {fmt_num(t_cuad[1])}$:**")
        st.latex(
            rf"\begin{{cases}} "
            rf"({fmt_num(A_calc)})(1)^2 + B(1) + C = {fmt_num(t_cuad[0])} \\ "
            rf"({fmt_num(A_calc)})(2)^2 + B(2) + C = {fmt_num(t_cuad[1])} "
            rf"\end{{cases}} \implies "
            rf"\begin{{cases}} "
            rf"B + C = {fmt_num(rhs1)} \quad \text{{(Ec. 1)}} \\ "
            rf"2B + C = {fmt_num(rhs2)} \quad \text{{(Ec. 2)}} "
            rf"\end{{cases}}"
        )

        st.markdown("**4. Resolución del sistema restando $(\\text{Ec. 2}) - (\\text{Ec. 1})$:**")
        st.latex(rf"B = ({fmt_num(rhs2)}) - ({fmt_num(rhs1)}) = {fmt_num(B_calc)} \quad \implies \quad C = {fmt_num(rhs1)} - ({fmt_num(B_calc)}) = {fmt_num(C_calc)}")

        st.success(rf"**Término General Resultante:**  $a_n = {fmt_num(A_calc)}n^2 {fmt_signo(B_calc)}n {fmt_signo(C_calc)}$")

    # EJERCICIOS APLICATIVOS DE SUCESIÓN CUADRÁTICA
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos: Sucesión Cuadrática (Sistema 2×2)")
    tab_c1, tab_c2 = st.tabs([
        "🔷 Ejercicio 1: Diseño Arquitectónico con Baldosas (Armar el Sistema 2×2)",
        "🧪 Ejercicio 2: Red de Conexiones en un Laboratorio de Cómputo"
    ])

    with tab_c1:
        st.info(
            "**Problema 1:** Un arquitecto está diseñando una serie de patios decorativos en el colegio. "
            "El diseño $n = 1$ utiliza **$6\\text{ baldosas}$**; el diseño $n = 2$ utiliza **$13\\text{ baldosas}$**; "
            "el diseño $n = 3$ utiliza **$24\\text{ baldosas}$**; y el diseño $n = 4$ utiliza **$39\\text{ baldosas}$**.\n\n"
            "1. Calcula las primeras y segundas diferencias para comprobar que es una sucesión cuadrática y halla el valor de $A$.\n"
            "2. Plantea y resuelve el **sistema de ecuaciones $2 \\times 2$** para encontrar $B$ y $C$, y escribe el término general $a_n = An^2 + Bn + C$.\n"
            "3. ¿Cuántas baldosas se necesitarán para construir el diseño número **$n = 10$**?"
        )
        if st.button("Revelar solución paso a paso (Cuadrática 1)", key="btn_cuad1"):
            st.success("**Solución paso a paso:**")
            st.markdown("**1. Esquema de diferencias y cálculo de $A$:**")
            st.latex(r"\text{Términos } (a_n): \quad 6, \quad 13, \quad 24, \quad 39")
            st.latex(r"\text{Primeras diferencias } (\Delta^1): \quad 13 - 6 = \mathbf{7}, \quad 24 - 13 = \mathbf{11}, \quad 39 - 24 = \mathbf{15}")
            st.latex(r"\text{Segundas diferencias } (\Delta^2): \quad 11 - 7 = \mathbf{4}, \quad 15 - 11 = \mathbf{4} \quad (\text{Constante } \Delta^2 = 4)")
            st.latex(r"2A = 4 \implies A = \frac{4}{2} = 2")
            st.markdown("**2. Sistema $2 \\times 2$ usando $a_1 = 6$ y $a_2 = 13$ en $a_n = 2n^2 + Bn + C$:**")
            st.latex(
                r"\begin{cases} "
                r"n = 1: \; 2(1)^2 + B(1) + C = 6 \implies B + C = 4 \quad \text{(Ec. 1)} \\ "
                r"n = 2: \; 2(2)^2 + B(2) + C = 13 \implies 8 + 2B + C = 13 \implies 2B + C = 5 \quad \text{(Ec. 2)} "
                r"\end{cases}"
            )
            st.markdown("Restamos $(\\text{Ec. 2}) - (\\text{Ec. 1})$:")
            st.latex(r"(2B + C) - (B + C) = 5 - 4 \implies B = 1")
            st.markdown("Sustituimos $B = 1$ en la $(\\text{Ec. 1})$:")
            st.latex(r"1 + C = 4 \implies C = 3 \quad \implies \quad \mathbf{a_n = 2n^2 + n + 3}")
            st.markdown("**3. Evaluar para el diseño $n = 10$:**")
            st.latex(r"a_{10} = 2(10)^2 + (10) + 3 = 2(100) + 10 + 3 = 213 \text{ baldosas}")

    with tab_c2:
        st.info(
            "**Problema 2:** En una feria de ciencia escolar se construyen estructuras triangulares con esferas imantadas. "
            "La figura $n = 1$ tiene **$3\\text{ esferas}$**, la figura $n = 2$ tiene **$6\\text{ esferas}$**, "
            "la figura $n = 3$ tiene **$10\\text{ esferas}$** y la figura $n = 4$ tiene **$15\\text{ esferas}$**.\n\n"
            "1. Halla el término general $a_n = An^2 + Bn + C$ mediante la segunda diferencia y el sistema $2 \\times 2$.\n"
            "2. ¿Cuántas esferas tendrá la figura **$n = 12$**?"
        )
        if st.button("Revelar solución paso a paso (Cuadrática 2)", key="btn_cuad2"):
            st.success("**Solución paso a paso:**")
            st.markdown("**1. Diferencias y coeficiente $A$:**")
            st.latex(r"\text{Términos: } 3, \; 6, \; 10, \; 15 \implies \Delta^1: \; 3, \; 4, \; 5 \implies \Delta^2 = 1")
            st.latex(r"2A = 1 \implies A = 0.5 = \frac{1}{2}")
            st.markdown("**2. Sistema $2 \\times 2$ con $a_1 = 3$ y $a_2 = 6$:**")
            st.latex(
                r"\begin{cases} "
                r"n = 1: \; 0.5(1)^2 + B + C = 3 \implies B + C = 2.5 \quad \text{(Ec. 1)} \\ "
                r"n = 2: \; 0.5(2)^2 + 2B + C = 6 \implies 2 + 2B + C = 6 \implies 2B + C = 4.0 \quad \text{(Ec. 2)} "
                r"\end{cases}"
            )
            st.markdown("Restando $(\\text{Ec. 2}) - (\\text{Ec. 1})$:")
            st.latex(r"B = 4.0 - 2.5 = 1.5 \quad \implies \quad C = 2.5 - 1.5 = 1.0")
            st.latex(r"a_n = 0.5n^2 + 1.5n + 1")
            st.markdown("**3. Evaluar en $n = 12$:**")
            st.latex(r"a_{12} = 0.5(12)^2 + 1.5(12) + 1 = 0.5(144) + 18 + 1 = 72 + 18 + 1 = 91 \text{ esferas}")


# ==============================================================================
# MÓDULO 4: SERIES Y SUMATORIAS (LINEAL, GEOMÉTRICA Y CUADRÁTICA)
# ==============================================================================
elif seccion == "4. Series y Sumatorias (∑)":
    st.title("∑ Series Matemáticas y Notación Sumatoria")
    st.markdown(
        "Cuando necesitamos **sumar los primeros $n$ términos** de una sucesión ($S_n = a_1 + a_2 + a_3 + \\dots + a_n$), "
        "estamos calculando una **Serie**. En matemáticas se escribe de forma compacta usando la letra griega **Sigma mayúscula ($\\sum$)**."
    )

    # Notación sigma explicada
    st.latex(r"S_n = \sum_{k=1}^{n} a_k = a_1 + a_2 + a_3 + \dots + a_n")
    st.caption("Donde 'k' es el índice de la sumatoria (empieza en k = 1), 'n' es el límite superior (cantidad de términos a sumar) y 'a_k' es la fórmula general de la sucesión.")

    st.markdown("---")
    st.subheader("1. Formulario General de Series (Los 3 Casos)")

    col_f1, col_f2, col_f3 = st.columns(3)

    with col_f1:
        st.markdown("#### A) Serie Lineal (Aritmética)")
        st.markdown("Para sumar $n$ términos de una sucesión lineal ($a_k = a_1 + (k-1)d$), usamos el **Método de Gauss** (el primero más el último, multiplicado por la mitad de términos):")
        st.latex(r"S_n = \sum_{k=1}^{n} a_k = \frac{n(a_1 + a_n)}{2}")
        st.markdown("O si no conocemos el último término $a_n$:")
        st.latex(r"S_n = \frac{n\big(2a_1 + (n - 1)d\big)}{2}")

    with col_f2:
        st.markdown("#### B) Serie Geométrica")
        st.markdown("Para sumar los primeros $n$ términos de una progresión geométrica ($a_k = a_1 \\cdot r^{k-1}$, con $r \\neq 1$):")
        st.latex(r"S_n = \sum_{k=1}^{n} a_1 r^{k-1} = a_1 \cdot \frac{r^n - 1}{r - 1}")
        st.markdown("**Serie Infinita ($|r| < 1$):** Si $-1 < r < 1$, al sumar infinitos términos la suma converge a:")
        st.latex(r"S_{\infty} = \sum_{k=1}^{\infty} a_1 r^{k-1} = \frac{a_1}{1 - r}")

    with col_f3:
        st.markdown("#### C) Serie Cuadrática")
        st.markdown("Para sumar $a_k = Ak^2 + Bk + C$, separamos la sumatoria en las **3 Sumas Notables**:")
        st.latex(r"S_n = A\sum_{k=1}^{n} k^2 + B\sum_{k=1}^{n} k + \sum_{k=1}^{n} C")
        st.markdown("**Fórmulas de las Sumas Notables:**")
        st.latex(r"\sum_{k=1}^{n} C = C \cdot n")
        st.latex(r"\sum_{k=1}^{n} k = \frac{n(n + 1)}{2}")
        st.latex(r"\sum_{k=1}^{n} k^2 = \frac{n(n + 1)(2n + 1)}{6}")

    # CALCULADORA INTERACTIVA DE SERIES
    st.markdown("---")
    st.subheader("2. Calculadora Paso a Paso de Sumatorias ($S_n$)")

    tipo_serie = st.radio(
        "Elige el tipo de serie que deseas desarrollar:",
        ["Serie Lineal (Aritmética)", "Serie Geométrica", "Serie Cuadrática"],
        horizontal=True
    )

    if tipo_serie == "Serie Lineal (Aritmética)":
        cs1, cs2, cs3 = st.columns(3)
        s_a1 = cs1.number_input("Primer término (a₁):", value=10.0, step=1.0, key="sl_a1")
        s_d = cs2.number_input("Diferencia (d):", value=5.0, step=1.0, key="sl_d")
        s_n = cs3.number_input("Cantidad de términos a sumar (n):", min_value=1, max_value=200, value=10, step=1, key="sl_n")

        s_an = s_a1 + (s_n - 1) * s_d
        suma_total = (s_n * (s_a1 + s_an)) / 2.0
        indep = s_a1 - s_d

        st.latex(rf"S_{{{s_n}}} = \sum_{{k=1}}^{{{s_n}}} \big({fmt_num(s_d)}k {fmt_signo(indep)}\big) = "
                 rf"{fmt_num(s_a1)} + {fmt_num(s_a1 + s_d)} + {fmt_num(s_a1 + 2*s_d)} + \dots + {fmt_num(s_an)}")
        st.latex(rf"\text{{Paso 1 (Hallamos el último término }} a_{{{s_n}}}\text{{):}} \quad "
                 rf"a_{{{s_n}}} = {fmt_num(s_a1)} + ({s_n} - 1)({fmt_num(s_d)}) = {fmt_num(s_an)}")
        st.latex(rf"\text{{Paso 2 (Fórmula de Gauss):}} \quad "
                 rf"S_{{{s_n}}} = \frac{{{s_n} \cdot ({fmt_num(s_a1)} + {fmt_num(s_an)})}}{{2}} = \mathbf{{{fmt_num(suma_total)}}}")

    elif tipo_serie == "Serie Geométrica":
        cs1, cs2, cs3 = st.columns(3)
        sg_a1 = cs1.number_input("Primer término (a₁):", value=4.0, step=1.0, key="sg_a1")
        sg_r = cs2.number_input("Razón (r ≠ 1):", value=2.0, step=0.5, key="sg_r")
        sg_n = cs3.number_input("Cantidad de términos a sumar (n):", min_value=1, max_value=25, value=8, step=1, key="sg_n")

        if abs(sg_r - 1.0) < 1e-6:
            st.warning("Si r = 1, todos los términos son iguales y S_n = n · a₁.")
            suma_g = sg_n * sg_a1
        else:
            suma_g = sg_a1 * ((sg_r ** sg_n - 1.0) / (sg_r - 1.0))
            st.latex(rf"S_{{{sg_n}}} = \sum_{{k=1}}^{{{sg_n}}} {fmt_num(sg_a1)} \cdot ({fmt_num(sg_r)})^{{k-1}} = "
                     rf"{fmt_num(sg_a1)} \cdot \frac{{({fmt_num(sg_r)})^{{{sg_n}}} - 1}}{{{fmt_num(sg_r)} - 1}} = \mathbf{{{fmt_num(suma_g)}}}")

        if abs(sg_r) < 1.0 and sg_r != 0:
            s_inf = sg_a1 / (1.0 - sg_r)
            st.info(rf"**Como $|r| = {abs(sg_r):.2f} < 1$, la serie infinita converge:**  $S_{{\infty}} = \frac{{{fmt_num(sg_a1)}}}{{1 - ({fmt_num(sg_r)})}} = \mathbf{{{fmt_num(s_inf)}}}$")

    else:
        cs1, cs2, cs3, cs4 = st.columns(4)
        sc_A = cs1.number_input("Coeficiente A (de k²):", value=1.0, step=1.0, key="sc_A")
        sc_B = cs2.number_input("Coeficiente B (de k):", value=2.0, step=1.0, key="sc_B")
        sc_C = cs3.number_input("Constante C:", value=0.0, step=1.0, key="sc_C")
        sc_n = cs4.number_input("Límite superior (n):", min_value=1, max_value=100, value=6, step=1, key="sc_n")

        sum_k2 = (sc_n * (sc_n + 1) * (2 * sc_n + 1)) / 6.0
        sum_k1 = (sc_n * (sc_n + 1)) / 2.0
        sum_c = sc_C * sc_n
        suma_cuad = sc_A * sum_k2 + sc_B * sum_k1 + sum_c

        st.latex(rf"S_{{{sc_n}}} = \sum_{{k=1}}^{{{sc_n}}} \big({fmt_num(sc_A)}k^2 {fmt_signo(sc_B)}k {fmt_signo(sc_C)}\big)")
        st.latex(
            rf"S_{{{sc_n}}} = {fmt_num(sc_A)} \left[\frac{{{sc_n}({sc_n}+1)(2\cdot{sc_n}+1)}}{{6}}\right] "
            rf"{fmt_signo(sc_B)} \left[\frac{{{sc_n}({sc_n}+1)}}{{2}}\right] "
            rf"{fmt_signo(sc_C)}({sc_n})"
        )
        st.latex(
            rf"S_{{{sc_n}}} = {fmt_num(sc_A)}({fmt_num(sum_k2)}) {fmt_signo(sc_B)}({fmt_num(sum_k1)}) {fmt_signo(sum_c)} = \mathbf{{{fmt_num(suma_cuad)}}}"
        )

    # EJERCICIOS APLICATIVOS DE SERIES Y SUMATORIAS
    st.markdown("---")
    st.subheader("🎯 Ejercicios Aplicativos Estructurados: Series y Sumatorias")
    tab_s1, tab_s2, tab_s3, tab_s4 = st.tabs([
        "🏟️ Problema 1: Serie Lineal (Capacidad Total de un Auditorio)",
        "💰 Problema 2: Serie Geométrica Finita (Ahorro Duplicado)",
        "🎾 Problema 3: Serie Geométrica Infinita (Distancia Total de un Rebote)",
        "🍊 Problema 4: Serie Cuadrática (Pirámide de Base Cuadrada)"
    ])

    with tab_s1:
        st.info(
            "**Problema 1 (Serie Lineal):** Un teatro municipal tiene **$n = 20\\text{ filas}$** de asientos. "
            "La primera fila tiene **$a_1 = 18\\text{ asientos}$**, la segunda tiene **$22\\text{ asientos}$**, "
            "la tercera tiene **$26\\text{ asientos}$**, y así sucesivamente aumentando de a $4$ asientos por cada nueva fila.\n\n"
            "1. Expresa el número total de asientos del teatro usando notación sumatoria ($\\sum$).\n"
            "2. ¿Cuál es la **capacidad total de personas sentadas ($S_{20}$)** que caben en todo el teatro?"
        )
        if st.button("Revelar solución paso a paso (Serie 1)", key="btn_ser1"):
            st.success("**Solución estructurada:**")
            st.markdown("**1. Término general y notación sumatoria:** Es una sucesión lineal con $a_1 = 18$ y $d = 4$, por lo que $a_k = 18 + (k-1)4 = 4k + 14$:")
            st.latex(r"S_{20} = \sum_{k=1}^{20} (4k + 14)")
            st.markdown("**2. Calculamos los asientos de la última fila ($a_{20}$):**")
            st.latex(r"a_{20} = 4(20) + 14 = 80 + 14 = 94 \text{ asientos en la fila 20}")
            st.markdown("**3. Aplicamos la fórmula de la Serie Lineal (Gauss):**")
            st.latex(r"S_{20} = \frac{n(a_1 + a_{20})}{2} = \frac{20(18 + 94)}{2} = 10 \cdot (112) = 1\,120 \text{ asientos en total}")

    with tab_s2:
        st.info(
            "**Problema 2 (Serie Geométrica Finita):** Para comprar un instrumento musical, Mateo decide hacer un reto de ahorro "
            "durante **$n = 10\\text{ meses}$**. En el mes $1$ guarda en su alcancía **$a_1 = \\$5\\,000\\text{ pesos}$**, "
            "y cada mes siguiente se compromete a guardar exactamente **el doble ($r = 2$)** de lo que guardó en el mes anterior "
            "($\\$10\\,000$ en el mes 2, $\\$20\\,000$ en el mes 3, etc.).\n\n"
            "1. ¿Cuánto dinero habrá depositado en el mes $10$ únicamente ($a_{10}$)?\n"
            "2. ¿Cuál es el **dinero total acumulado ($S_{10}$)** dentro de la alcancía al finalizar los $10$ meses?"
        )
        if st.button("Revelar solución paso a paso (Serie 2)", key="btn_ser2"):
            st.success("**Solución estructurada:**")
            st.markdown("**1. Cuota del décimo mes ($a_{10}$):** Con $a_1 = 5\\,000$ y $r = 2$:")
            st.latex(r"a_{10} = 5\,000 \cdot 2^{10-1} = 5\,000 \cdot 2^9 = 5\,000 \cdot 512 = \$2\,560\,000 \text{ pesos}")
            st.markdown("**2. Suma total acumulada en los 10 meses ($S_{10}$):** Planteamos la serie geométrica finita:")
            st.latex(r"S_{10} = \sum_{k=1}^{10} 5\,000 \cdot 2^{k-1} = a_1 \cdot \frac{r^{10} - 1}{r - 1}")
            st.latex(r"S_{10} = 5\,000 \cdot \frac{2^{10} - 1}{2 - 1} = 5\,000 \cdot \frac{1\,024 - 1}{1} = 5\,000 \cdot 1\,023 = \$5\,115\,000 \text{ pesos en total}")

    with tab_s3:
        st.info(
            "**Problema 3 (Serie Geométrica Infinita):** Un péndulo en el laboratorio recorre un arco de **$a_1 = 40\\text{ cm}$** "
            "en su primera oscilación. Por la fricción con el aire, en cada oscilación siguiente recorre el **$80\\%$ ($r = 0.8$)** "
            "de la distancia del movimiento anterior ($32\\text{ cm}$, $25.6\\text{ cm}$, $\\dots$) hasta que finalmente se detiene por completo.\n\n"
            "• ¿Cuál es la **distancia total acumulada ($S_{\\infty}$)** que habrá recorrido la punta del péndulo desde que se soltó hasta quedar en reposo?"
        )
        if st.button("Revelar solución paso a paso (Serie 3)", key="btn_ser3"):
            st.success("**Solución estructurada:**")
            st.markdown(
                "Como la razón $r = 0.8$ cumple que $|r| < 1$, la suma de las infinitas oscilaciones converge a un valor finito. "
                "Usamos la fórmula de la **Serie Geométrica Infinita**:"
            )
            st.latex(r"S_{\infty} = \sum_{k=1}^{\infty} 40 \cdot (0.8)^{k-1} = \frac{a_1}{1 - r}")
            st.latex(r"S_{\infty} = \frac{40}{1 - 0.8} = \frac{40}{0.2} = 200 \text{ cm (2 metros en total)}")

    with tab_s4:
        st.info(
            "**Problema 4 (Serie Cuadrática):** En una plaza de mercado de Boyacá, un comerciante apila naranjas formando una "
            "**pirámide de base cuadrada** de **$n = 8\\text{ niveles de altura}$** (contando desde la punta hacia abajo). "
            "En el nivel $k = 1$ (la punta superior) hay $1^2 = 1\\text{ naranja}$; en el nivel $k = 2$ hay un cuadrado de $2^2 = 4\\text{ naranjas}$; "
            "en el nivel $k = 3$ hay $3^2 = 9\\text{ naranjas}$; y en el nivel $k$ hay $a_k = k^2\\text{ naranjas}$.\n\n"
            "1. Escribe la sumatoria que representa el total de naranjas en los $8$ niveles.\n"
            "2. Calcula el **número total de naranjas ($S_8$)** que conforman toda la pirámide usando la fórmula notable de los cuadrados."
        )
        if st.button("Revelar solución paso a paso (Serie 4)", key="btn_ser4"):
            st.success("**Solución estructurada:**")
            st.markdown("**1. Planteamiento en notación sumatoria:**")
            st.latex(r"S_8 = \sum_{k=1}^{8} k^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2")
            st.markdown("**2. Aplicamos la fórmula de la suma notable cuadrática con $n = 8$:**")
            st.latex(r"\sum_{k=1}^{n} k^2 = \frac{n(n + 1)(2n + 1)}{6}")
            st.latex(r"S_8 = \frac{8 \cdot (8 + 1) \cdot (2(8) + 1)}{6} = \frac{8 \cdot 9 \cdot 17}{6}")
            st.latex(r"S_8 = \frac{1\,224}{6} = 204 \text{ naranjas en total}")