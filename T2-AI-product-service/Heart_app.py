import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('train_new_mod.sav', 'rb') as model_file:
    model = pickle.load(model_file)

# Define function to make predictions
def predict_heart_disease(features):
    # Reshape the input features into the format expected by the model
    input_features = np.array(features).reshape(1, -1)
    # Make prediction
    prediction = model.predict(input_features)
    return prediction

# Define the web app
def main():
    st.title("Heart Health Predictor")
    
    # Add image
    # Add image with custom height and width using CSS styling
    image = 'https://pics.craiyon.com/2023-07-05/64c0ff3658c44869b4ad53dfed590f72.webp'  # Replace 'your_image.png' with the path to your image file
    custom_height = 300  # Adjust as needed
    custom_width = 500  # Adjust as needed
    st.image(image, width=custom_width, caption='Your Image', use_column_width=False)
    

    
    # Add sidebar for user input
    st.sidebar.header("User Input")
    
    # Collect user input using sidebar sliders and radio buttons
    age_category = st.sidebar.selectbox("Age Category", ["18 to 24", "25 to 29", "30 to 34",
                                                          "35 to 39", "40 to 44", "45 to 49",
                                                          "50 to 54", "55 to 59", "60 to 64",
                                                          "65 to 69", "70 to 74", "75 to 79",
                                                          "80 or older"])
    age_categories = {
        "18 to 24": 1,
        "25 to 29": 2,
        "30 to 34": 3,
        "35 to 39": 4,
        "40 to 44": 5,
        "45 to 49": 6,
        "50 to 54": 7,
        "55 to 59": 8,
        "60 to 64": 9,
        "65 to 69": 10,
        "70 to 74": 11,
        "75 to 79": 12,
        "80 or older": 13
    }
    age = age_categories[age_category]
    high_bp = st.sidebar.radio("High Blood Pressure", ["No", "Yes"])
    high_bp = 1 if high_bp == "Yes" else 0
    high_chol = st.sidebar.radio("High Cholesterol", ["No", "Yes"])
    high_chol = 1 if high_chol == "Yes" else 0
    chol_check = st.sidebar.radio("Cholesterol Check ( Past 5 years)", ["No", "Yes"])
    chol_check = 1 if chol_check == "Yes" else 0
    bmi = st.sidebar.slider("BMI = weight (kg) / (height (m))^2")
    smoker = st.sidebar.radio("Smoker ( atleast 100 cigarettes )", ["No", "Yes"])
    smoker = 1 if smoker == "Yes" else 0
    stroke = st.sidebar.radio("Stroke", ["No", "Yes"])
    stroke = 1 if stroke == "Yes" else 0
    diabetes = st.sidebar.radio("Diabetes", ["No", "Yes"])
    diabetes = 1 if diabetes == "Yes" else 0
    phys_activity = st.sidebar.radio("phys_activity", ["No", "Yes"])
    phys_activity = 1 if phys_activity == "Yes" else 0
    fruits = st.sidebar.radio("Fruits", ["No", "Yes"])
    fruits = 1 if fruits == "Yes" else 0
    veggies = st.sidebar.radio("Veggies", ["No", "Yes"])
    veggies = 1 if veggies == "Yes" else 0
    
    heavy_alcohol = st.sidebar.radio("Heavy Alcohol Consumption (more than 14 drinks per week)", ["No", "Yes"])
    heavy_alcohol = 1 if heavy_alcohol == "Yes" else 0
    gen_health = st.sidebar.slider("General Health (1. excellent, 2. very good, 3. good, 4. fair, 5. poor)", 1, 5, help="Indicates the person's response to how well their general health is")

    ment_health = st.sidebar.slider("Mental Health", 0,30)
    phys_health = st.sidebar.slider("Physical Health", 0, 30)
    diff_walk = st.sidebar.radio("difficulty walking", ["No", "Yes"])
    diff_walk = 1 if diff_walk == "Yes" else 0
    
    sex = st.sidebar.radio("Sex", ["Female", "Male"])
    sex = 1 if sex == "Male" else 0
    
    # Collect the user input into a list
    user_input = [high_bp, high_chol, chol_check, bmi, smoker, stroke, diabetes,
                  phys_activity, fruits, veggies, heavy_alcohol,
                  gen_health, ment_health, phys_health, diff_walk,
                  sex, age]
    
    # Add a button to trigger the prediction
    if st.sidebar.button("Result"):
        # Predict the heart disease based on the user input
        prediction = predict_heart_disease(user_input)
        
        # Display the prediction result
        st.write("")
        st.write("## Result")
        if prediction[0] == 1:
            st.write("The model predicts that the person is likely to have heart disease.")
        else:
            st.write("The model predicts that the person is not likely to have heart disease.")
        
        # Feedback form
        st.header("Feedback Form")
        name = st.text_input("Name", "")
        email = st.text_input("Email", "")
        feedback = st.text_area("Feedback Message", "")
        satisfaction_rating = st.slider("Satisfaction Rating", 1, 5)
        improvement_suggestions = st.text_area("Improvement Suggestions", "")
        if st.button("Submit Feedback"):
            # Process feedback submission (you can add your code to handle feedback submission here)
            st.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()
