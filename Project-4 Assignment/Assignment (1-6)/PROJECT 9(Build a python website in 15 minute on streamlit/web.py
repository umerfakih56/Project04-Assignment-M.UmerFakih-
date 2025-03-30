import streamlit as st
import pandas as pd
import random
import datetime

# Page Configuration
st.set_page_config(page_title="Student Data Generator", layout="wide")

# Sidebar Section
st.sidebar.header("Settings")
num_students = st.sidebar.slider("Select Number of Students", min_value=5, max_value=50, value=15)

st.title("📄 Student CSV File Generator")

# Names List
names = ["Ali", "Alisha", "Ahmed", "Fatima", "Usman", "Umar", "Zainab", "Hania", 
         "Saim", "Hamzah", "Naila", "Sawaira", "Tarib", "Mikail", "Zara"]

# Generating Student Data
students = []
for i in range(1, num_students + 1):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

# Convert to DataFrame
df = pd.DataFrame(students)

# Display Data
st.subheader("📊 Generated Student Data")
st.dataframe(df, use_container_width=True)

# Convert DataFrame to CSV
csv_file = df.to_csv(index=False).encode('utf-8')
file_name = f"students_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Download Button
st.download_button("⬇️ Download CSV File", csv_file, file_name, "text/csv")

# Success Message
st.success(f"{num_students} Students Record Generated Successfully!")
