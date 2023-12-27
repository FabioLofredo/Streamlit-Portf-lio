import streamlit as st
from PIL import Image

def titanic_func():
    st.markdown("The data for this analysis was obtained from Kaggle's 'Titanic - Machine Learning from Disaster' competition (https://www.kaggle.com/competitions/titanic).")
    st.markdown("The analysis was conducted in five parts:")
    st.markdown("1.Statistical Tests: A statistical analysis of the data involved obtaining p-values and drawing conclusions. Calculations were performed to gather information and address specific questions.")
    st.markdown("2.Cleaning for Machine Learning: The data underwent cleaning and transformation into numerical format. The processed data was then exported for the subsequent step.")
    st.markdown("3.Machine Learning for Age Regression: Various machine learning algorithms, including Random Forest Regression (yielding the best results), Decision Tree Regression, Support Vector Regression (SVR), Multiple Linear Regression, and Polynomial Regression, were employed to predict ages.")
    st.markdown("4.Machine Learning for Survival Prediction (Classification): Several machine learning algorithms, such as Logistic Regression (using a probabilistic approach and achieving the best results), Extreme Tree Classification, Decision Tree Classification, Random Forest Classification, and K-Nearest Neighbors (KNN), were utilized to predict survival outcomes.")
    st.markdown("5.Machine Learning Unsupervised Analysis: K-means clustering was employed for an unsupervised analysis.")
    st.success("[GitHub](https://github.com/FabioLofredo/Data-Science-Titanic-Project-2023)")

def ml_from_zero_func():
    st.markdown("I developed three distinct Machine Learning Algorithms—Decision Tree Classifier, Decision Tree Regressor, and Random Forest Classifier—from scratch, without relying on the Sklearn library.")
    st.success("[GitHub](https://github.com/FabioLofredo/Data-Science-ML-Without-Sklearn-2023)")
    st.video('https://youtu.be/zCkC2Dh4KKM')

def cnn_func():
    st.markdown("Investigation into Convolutional Neural Networks (CNN)")
    st.markdown("The '.xlsx' file is a Google Sheet that can also be opened in Excel, detailing CNN step by step on sheets.")
    st.markdown("The three '.pdf' files, all created by me, consist of a tutorial that offers theoretical insights and explanations about CNNs for educational purposes, presentation slides, and a '.pdf' version of the CNN sheet.")
    st.success("[GitHub](https://github.com/FabioLofredo/CNN-Convolutional-Neural-Network)")
    st.video('https://youtu.be/RmKWPcaoYlk')

def tl_func():
    st.markdown("Transfer Learning")
    st.markdown("Project 'Chest X-Ray Images' from kaggle. The transfer learning uses Resnet_v2 and Inception_v3.")
    st.markdown("https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/")    
    st.success("[GitHub](https://github.com/FabioLofredo/Data-Science-Transfer-Learning)")
    
def sheets_func():
    st.markdown("Google sheets and Excel files")
    st.markdown("'CNN - Convolutional Neural Network.xlsx' is an example of a CNN.")
    st.markdown("'Rede Neural Perceptron.xlsx' is a file containing a perceptron neural network.")
    st.markdown("'Tabela para digitar notas v1.4.xlsx' is a sheet for the teacher to enter the students' grades.")
    st.markdown("'Univesp atividades.xlsx' is a tool for students to calculate their grades.")
    st.success("[GitHub](https://github.com/FabioLofredo/Planilhas-Google-Sheet-Excel-)")

def unity_func():
    st.markdown("I created these games as examples for seven high school technology classes. All the videos and games below were produced by me.")
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
    st.markdown("This project was created for three high school physics classes. The examples below demonstrate what was presented to them")
    st.success("[GitHub](https://github.com/FabioLofredo/Arduino-Projects-2023)")
    st.write('Project 1: Light Sensor (sinal + graph): ')
    st.write('It was made on Python with pyfirmata, a light sensor colect the light intensity and plots on a graph.')
    st.video('https://youtu.be/jDDUAnyqsSo')
    st.write('Project 2: Distance Sensor:')
    st.write('A distance sensor turns the LEDs on and off based on distance')
    st.video('https://youtu.be/WQMvbVNAx7c')

def pts_func():
    st.markdown("I created this game for fun during my 2014 vacation using the programming language Monkey X.")
    st.success("[GitHub](https://github.com/FabioLofredo/Protect-the-Spaceship-2014)")
    st.video('https://youtu.be/8qkj7s9h2GE')

def per_func():
    st.markdown("The teacher himself creates the images with the questions and answers. The program takes the image file and randomly generates the order of questions for the user.")
    st.success("[GitHub](https://github.com/FabioLofredo/Educative-Game-in-Unity-Perguntas-e-Respostas-2023)")
    st.video('https://youtu.be/yIPI3T5ITgA')

def truco_func():
    st.markdown("Truco - This game was created by me in 2007 in the University as student using C++")
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
    projects = ['Select here',
                'Data Analisys and Machine Learning - Titanic',
                'Machine Learning Algorithms from zero',
                'CNN - Convolutional Neural Network',
                'Transfer Learning - X-ray Project',
                'Sheets for Excel or Google Sheets',
                'Unity (Teaching)',
                'Arduino (Teaching)',
                'Protect the Spaceship (Game)',
                'Perguntas e Respostas (Tool for teacher)',
                'Truco (Game)']
    project_selection = st.selectbox("Select a project:",projects)
    if project_selection == projects[0]:
        st.write('')
    elif project_selection == projects[1]:
        titanic_func()
    elif project_selection == projects[2]:
        ml_from_zero_func()
    elif project_selection == projects[3]:
        cnn_func()
    elif project_selection == projects[4]:
        tl_func()
    elif project_selection == projects[5]:
        sheets_func()
    elif project_selection == projects[6]:
        unity_func()
    elif project_selection == projects[7]:
        arduino_func()
    elif project_selection == projects[8]:
        pts_func()
    elif project_selection == projects[9]:
        per_func()
    elif project_selection == projects[10]:
        truco_func()    
elif st.session_state.mode == "Contact":
    st.title("Contact")
    st.success("[Linkedin](https://www.linkedin.com/in/f%C3%A1bio-lofredo-cesar-050613262/?locale=en_US)")



