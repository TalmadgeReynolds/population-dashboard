import streamlit as st
import openai

# Streamlit UI
st.title("Brigid V2 Streamlit Dashboard")
st.write("Explore connections between politicians, corporations, and global entities.")

# Sidebar for input
st.sidebar.title("Input Settings")
user_input = st.sidebar.text_area("Enter your query", placeholder="e.g., 'TechCorp political lobbying' or 'Senator Jane Smith's market ties'")

# Button to get the response
if st.sidebar.button("Submit"):
    if user_input.strip():
        st.write("**Query:**", user_input)
        
        # Make the query to Brigid V2
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Brigid V2, specializing in uncovering connections between politicians, corporations, and global entities. Provide detailed, multidimensional insights."},
                {"role": "user", "content": user_input}
            ]
        )
        
        # Display the response
        response_content = response.choices[0].message['content']
        st.write("**Response:**")
        st.write(response_content)
    else:
        st.sidebar.warning("Please enter a query.")

# Instructions
st.sidebar.info("""
**Instructions**:
- Type your query in the text area.
- Click "Submit" to get insights from Brigid V2.
""")
