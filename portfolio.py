import streamlit as st
from PIL import Image

def unity_func():
    st.markdown("These games were produced to serve as an example for 7 classes with high school students from the technology class. All videos and games below were produced by me.")
    st.markdown("They learned how to make games in Unity, program in C#, create a vector art character with InkScape, and animate with DragonBones")
    st.success("[GitHub](https://github.com/FabioLofredo/Small-games-in-Unity-for-Teaching-2022)")
    st.write('compilation of 10 games in Unity:')
    st.video('https://youtu.be/e4NozORcyOE')
    st.write('Vector art character with InkScape:')
    st.video('https://youtu.be/fyCAIKxhtxo')
    st.write('Animation with DragonBones:')
    st.video('https://youtu.be/HW85GSgfJTQ')
    st.write('Animation with Unity:')
    st.video('https://youtu.be/2E4LlLDfx4Y')
    st.write('Sound Effects:')
    st.video('https://youtu.be/DjiULL6zqpY')
    st.write('Music:')
    st.video('https://youtu.be/AidI1NtttTA')
    st.write('Dialog:')
    st.video('https://youtu.be/raC8U0Q7LE0')
    st.write('Board Game:')
    st.video('https://youtu.be/WOk4YUOig2Y')

def arduino_func():
    st.markdown("This project is still ongoing")
    st.markdown("this project was made for 3 classes with high school students from physics class")
    st.success("[GitHub](https://github.com/FabioLofredo/Arduino-Projects-2023)")
    st.write('Project 1: Light Sensor (sinal + graph): ')
    st.write('It was made on Python with pyfirmata, a light sensor colect the light intensity and plots on a graph.')
    st.video('https://youtu.be/jDDUAnyqsSo')
    st.write('Project 2: Distance Sensor:')
    st.write('A distance sensor turns the LEDs on and off based on distance')
    st.video('https://youtu.be/WQMvbVNAx7c')

def titanic_func():
    st.markdown("The data was taken from kaggle on Titanic - Machine Learning from Disaster")
    st.markdown("The analysis was done in 5 parts")
    st.markdown("1.Statistical Tests. A statistical analysis of the data was made by obtaining the p-value and his conclusions, calculating values for obtain information and answering some questions.")
    st.markdown("2.Cleaning for Machine Learning. the data were cleaned, and transformed into numbers, the data was exported for the step number 3.")
    st.markdown("3.Machine Learning, Regression for Age. The following Machine Learning were used to calculate the age, the best algorithm exported the data: Random Forest Regression (best results) Decision Tree Regression Support Vector Regression (SVR) Multiple Linear Regression Polynomial Regression")
    st.markdown("4.Machine Learning, Classification for Survived (Prediction). The following Machine Learning were used to calculate the survived, the best algorithm exported the data: Logistic Regression (probabilistic approach) (best results) Extreme Tree Classification Decision Tree Classification Random Forest Classification KNN")
    st.markdown("5.Machine Learning, Unsupervised. K-means was used to make analysis.")
    st.success("[GitHub](https://github.com/FabioLofredo/Data-Science-Titanic-Project-2023)")

def ml_from_zero_func():
    st.markdown("Three Machine Learning Algorithms were built from the ground up: Decision Tree Classifier, Decision Tree Regressor, and Random Forest Classifier. All of them were made without using Sklearn.")
    st.success("[GitHub](https://github.com/FabioLofredo/Data-Science-ML-Without-Sklearn-2023)")
    st.video('https://youtu.be/zCkC2Dh4KKM')

def pts_func():
    st.markdown("This game was made by Fábio Lofredo Cesar in 2014, in the vacations for fun. It was made using the programming language Monkey X.")
    st.success("[GitHub](https://github.com/FabioLofredo/Protect-the-Spaceship-2014)")
    st.video('https://youtu.be/8qkj7s9h2GE')

def per_func():
    st.markdown("The teacher himself creates the images with the questions and answers. The program takes the image file and randomly generates the order of questions to be listed below for the user.")
    st.success("[GitHub](https://github.com/FabioLofredo/Educative-Game-in-Unity-Perguntas-e-Respostas-2023)")
    st.video('https://youtu.be/yIPI3T5ITgA')

def truco_func():
    st.markdown("Truco - This game was created by Fábio Lofredo Cesar in 2007 in the University as student using C++")
    st.success("[GitHub](https://github.com/FabioLofredo/Truco-2007)")

if 'mode' not in st.session_state:
    st.session_state.mode = 'Home'

with st.sidebar:
    mode = "Home"
    if st.button('Home'):
        st.session_state.mode = "Home"
    if st.button('Projects'):
        st.session_state.mode = "Projects"
    if st.button('Contact'):
        st.session_state.mode = "Contact"

if st.session_state.mode == "Home":
    st.title("Home")
    st.image(Image.open('foto.PNG'))
    st.header("Hi, I am Fábio Lofredo Cesar...")
    st.markdown("I have degree in physics on Unicamp (University of Campinas), I am currently doing Bachelor in Data Science on Univesp (Virtual University of the State of São Paulo) and making projects in the Research Group GEIA (Artificial Intelligence Study Group)")
    st.markdown("I also have experience and interests in Python, C#, Unity, Game Developer, Education, Arduino, Machine Learning and Neural Networks.")
    st.success("[GitHub](https://github.com/FabioLofredo?tab=repositories)")

elif st.session_state.mode == "Projects":
    st.title("Projects")
    project_selection = st.selectbox("Select a project:",('Select here','Unity (Teaching)','Arduino (Teaching)','Data Analisys and Machine Learning(Titanic)',
    'Machine Learning Algorithms from zero', 'Protect the Spaceship (Game)', 'Perguntas e Respostas (Tool for teacher)','Truco (Game)'))
    if project_selection == 'Unity (Teaching)':
        unity_func()
    elif project_selection == 'Arduino (Teaching)':
        arduino_func()
    elif project_selection == 'Data Analisys and Machine Learning(Titanic)':
        titanic_func()
    elif project_selection == 'Machine Learning Algorithms from zero':
        ml_from_zero_func()
    elif project_selection == 'Protect the Spaceship (Game)':
        pts_func()
    elif project_selection == 'Perguntas e Respostas (Tool for teacher)':
        per_func()
    elif project_selection == 'Truco (Game)':
        truco_func()    
elif st.session_state.mode == "Contact":
    st.title("Contact")
    st.success("[Linkedin](https://www.linkedin.com/in/f%C3%A1bio-lofredo-cesar-050613262/?locale=en_US)")



