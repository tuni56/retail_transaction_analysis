import streamlit as st
import pandas as pd
import plotly.express as px

# 📌 Configurar el layout de la app
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

# 📊 Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv("Online Retail.csv", encoding="ISO-8859-1")

df = load_data()

# 📌 Mostrar información general
st.title("📊 Análisis de Ventas con Apriori 🚀")
st.write(f"📦 Total de transacciones: {df.shape[0]}")
st.write(f"🛍️ Total de productos: {df['Description'].nunique()}")

# 📈 Gráfico de los 10 productos más vendidos
st.subheader("🔝 Top 10 Productos Más Vendidos")
top_products = df["Description"].value_counts().head(10)
fig = px.bar(top_products, x=top_products.index, y=top_products.values, 
             title="Top 10 Productos Más Vendidos", labels={"x": "Producto", "y": "Cantidad Vendida"})
st.plotly_chart(fig)

# 🔮 Recomendaciones Personalizadas
st.subheader("🎯 Recomendaciones Basadas en Compras")
producto_seleccionado = st.selectbox("Selecciona un Producto", df["Description"].unique())

# Simulación de recomendaciones
recomendaciones = df[df["Description"] == producto_seleccionado]["StockCode"].value_counts().head(3).index
productos_recomendados = df[df["StockCode"].isin(recomendaciones)]["Description"].unique()

st.write("🔹 Basado en las compras de otros usuarios, podrías estar interesado en:")
st.write(", ".join(str(producto) for producto in productos_recomendados))

