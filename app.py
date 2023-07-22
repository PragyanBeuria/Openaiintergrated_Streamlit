import streamlit as st
import requests
import random
import openai
import os
from PIL import Image
import toml
#api_key=st.secrets['']
#os.environ['openai.api_key'] = ""

# Load the API key from the TOML file
#st.write("Secret Key", st.secrets["openai.api_key"])
# And the root-level secrets are also accessible as environment variables:
#st.write("Has environment variables been set:",os.environ["openai.api_key"] == st.secrets["openai.pi_key"])

# Get the API key from the secrets object
api_key = st.secrets["openai.api_key"]
# Print the API key to the Streamlit app
st.write(api_key)

# Background Image
background_image_url = "https://source.unsplash.com/1600x900/?indian-food"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url('{background_image_url}') no-repeat center center;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

def generate_recipe(ingredients, servings, cuisine_type,scale_ingredients):
    # Generate a random recipe URL using OpenAI API
    prompt = f"Generate a {cuisine_type} recipe with ingredients: {ingredients}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        n=1,
        stop=None,
    )
    recipe_url = response.choices[0].text.strip()

    # Generate recipe using OpenAI API
    prompt = f"Recipe Name: {cuisine_type}\nCooking Time: XX minutes\nIngredients: {ingredients}\nNumber of Servings: {servings}\n\nCooking Procedure:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        n=1,
        stop=None,
    )
    recipe = response.choices[0].text.strip()

    return recipe, recipe_url

# Streamlit app
st.title("Recipe Generator")

# Fetch a random Indian food image
image_url = "https://source.unsplash.com/1600x900/?indian-food"
response = requests.get(image_url, stream=True)

# Check if the image is successfully fetched
if response.status_code == 200:
    # Open the image using PIL library
    image = Image.open(response.raw)
    
    # Display the image in Streamlit
    st.image(image, caption="Random Indian Food", use_column_width=True)

# Recipe input fields
ingredients = st.text_area("Recipe")
servings = st.number_input("Number of Servings", min_value=1, step=1)
cuisine_type = st.selectbox("Cuisine Type", ["Indian", "Chinese", "Mexican", "Italian","American"])
scale_ingredients = st.checkbox("Scale ingredients?")
# Generate recipe
if st.button("Generate Recipe"):
    if ingredients.strip() == "":
        st.error("Please enter the Recipe.")
    else:
        recipe, recipe_url = generate_recipe(ingredients, servings, cuisine_type,scale_ingredients)
        st.subheader(f"{cuisine_type} Recipe")
        st.write(recipe)

        # Display additional information
        st.sidebar.subheader("Recipe Details")
        st.sidebar.markdown(f"**Ingredients:**\n{ingredients}")
        st.sidebar.markdown(f"**Cuisine Type:** {cuisine_type}")
        st.sidebar.markdown(f"**Servings:** {servings}")





