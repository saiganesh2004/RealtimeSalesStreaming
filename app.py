import streamlit as st
import pandas as pd
import redis
import time
from datetime import datetime
import timeit

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Live Sales Dashboard",
    layout="wide",
    page_icon="📊"
)

# --------------------------------------------------
# REDIS CONNECTION
# --------------------------------------------------
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# --------------------------------------------------
# TITLE (STATIC)
# --------------------------------------------------
st.title("📊 Live Sales Dashboard")
st.caption("Auto-updating using while loop • Redis Streams")

# --------------------------------------------------
# PLACEHOLDER (VERY IMPORTANT)
# --------------------------------------------------
ui = st.empty()

# --------------------------------------------------
# READ DATA FROM REDIS STREAM
# --------------------------------------------------
def read_redis_data():
    entries = r.xrange("sales_stream", "-", "+")
    rows = []

    for _, fields in entries:
        try:
            rows.append({
                "timestamp": pd.to_datetime(fields["time"]),
                "sales": int(fields["amount"])
            })
        except Exception:
            continue

    if not rows:
        return pd.DataFrame(columns=["timestamp", "sales"])

    df = pd.DataFrame(rows)
    df["hour"] = df["timestamp"].dt.hour
    return df

# --------------------------------------------------
# WHILE LOOP (AUTO UPDATE + DISPLAY)
# --------------------------------------------------
while True:
    stime=timeit.default_timer()
    df = read_redis_data()
    print(" Time taken to proces ",timeit.default_timer()-stime)
    with ui.container():
        st.subheader(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")

        if df.empty:
            st.warning("Waiting for data from Redis...")
        else:
            # ---------------- KPIs ----------------
            total_sales = df["sales"].sum()
            avg_sales = df["sales"].mean()

            c1, c2 = st.columns(2)
            c1.metric("💰 Total Sales", f"₹ {int(total_sales):,}")
            c2.metric("📊 Average Sale", f"₹ {int(avg_sales):,}")

            st.divider()

            # ---------------- CHART ----------------
            hourly_sales = (
                df.groupby("hour", as_index=False)["sales"]
                .sum()
                .sort_values("hour")
            )

            st.subheader("⏰ Hourly Sales")
            st.line_chart(hourly_sales.set_index("hour"))

            # ---------------- TABLE ----------------
            st.subheader("📋 Latest Sales Records")
            st.dataframe(df.tail(10), use_container_width=True)

    time.sleep(0.1)  # refresh every 2 seconds
