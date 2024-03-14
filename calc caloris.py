import streamlit as st

# Add a title
st.title("Nutritional Requirements Calculator")

# Step 1: Define the necessary variables
gender = st.selectbox("Select your gender", ["Male", "Female"])
weight = st.number_input("Enter your weight in kg", min_value=0.00, max_value=400.00, step=1.00)
height = st.number_input("Enter your height in cm", min_value=0.00, max_value=250.00, step=1.00)
age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)
activity_level = st.selectbox("Select your activity level", ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"])
dietary_restrictions = st.selectbox("Select your dietary restrictions (if any)", ["None", "Vegan", "Gluten-free"])
sport_type = st.selectbox("Select your sport type", ["Endurance", "Power", "Mixed"])
goal = st.selectbox("Select your goal", ["Weight loss", "Muscle gain", "Maintaining muscle mass"])

# Add a button to calculate the nutritional requirements
if st.button("Calculate"):
    # Step 2: Calculate the nutritional requirements
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    if activity_level == "Sedentary":
        tdee = bmr * 1.2
        protein_ratio = 1.3 * weight
        carb_ratio = 2 * weight
        fat_ratio = (tdee * 0.25) / 9
    elif activity_level == "Lightly active":
        tdee = bmr * 1.375
        protein_ratio = 1.7 * weight
        carb_ratio = 2.5 * weight
        fat_ratio = (tdee * 0.25) / 9
    elif activity_level == "Moderately active":
        tdee = bmr * 1.55
        protein_ratio = 2 * weight
        carb_ratio = 3 * weight
        fat_ratio = (tdee * 0.25) / 9
    elif activity_level == "Very active":
        tdee = bmr * 1.725
        protein_ratio = 2.1 * weight
        carb_ratio = 3.5 * weight
        fat_ratio = (tdee * 0.25) / 9
    else:
        tdee = bmr * 1.9
        protein_ratio = 2.3 * weight
        carb_ratio = 4 * weight
        fat_ratio = (tdee * 0.25) / 9

    # Adjust macronutrient ratios based on the goal
    if goal == "Weight loss":
        protein_ratio += 5
        carb_ratio -= 10
    elif goal == "Muscle gain":
        protein_ratio += 30
        carb_ratio += 60

    # Step 4: Calculate the macronutrient amounts
    protein_amount = protein_ratio
    carb_amount = carb_ratio
    fat_amount = fat_ratio

    # Step 5: Display the results
    st.write(f"Your Total Daily Energy Expenditure (TDEE) is: {tdee} calories per day.")
    st.write("Your recommended macronutrient amounts are:")
    st.write(f"- Protein: {protein_amount:.1f} grams.")
    st.write(f"- Carbohydrates: {carb_amount:.1f} grams.")
    st.write(f"- Fats: {fat_amount:.1f} grams.")

    # Step 6: Suggest meal ideas based on dietary restrictions
    if "vegan" in dietary_restrictions.lower():
        st.write("Here are some vegan meal ideas:")
        st.write("- Tofu stir-fry with mixed vegetables and brown rice")
        st.write("- Lentil soup with whole grain bread")
        st.write("- Quinoa salad with chickpeas, cucumber, tomatoes, and avocado")
        st.write("- Black bean and corn tacos with salsa and guacamole")
        st.write("- Vegan chili with kidney beans, tomatoes, and quinoa")
    elif "gluten-free" in dietary_restrictions.lower():
        st.write("Here are some gluten-free meal ideas:")
        st.write("- Grilled chicken with roasted vegetables and quinoa")
        st.write("- Baked salmon with sweet potato and steamed broccoli")
        st.write("- Beef stir-fry with mixed vegetables and brown rice")
        st.write("- Egg and vegetable scramble with gluten-free toast")
        st.write("- Turkey and avocado lettuce wraps with a side of fruit")
    else:
        st.write("Here are some meal ideas:")
        st.write("- Grilled chicken with mixed vegetables and brown rice")
        st.write("- Baked salmon with quinoa and steamed broccoli")
        st.write("- Beef stir-fry with mixed vegetables and noodles")
        st.write("- Scrambled eggs with toast and fruit")
        st.write("- Tuna salad sandwich with a side of chips")
