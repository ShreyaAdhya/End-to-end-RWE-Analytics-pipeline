from sklearn.cluster import KMeans

df_model = df[features]
df_scaled = scaler.fit_transform(df_model)

kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(df_scaled)

print(df.groupby("cluster")[features].mean())
