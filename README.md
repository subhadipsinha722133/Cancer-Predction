# Cancer Prediction Web Application 🎗️🔬


A machine learning-based web application for predicting cancer risk based on various health and lifestyle factors. 

![Cancer Prediction App](https://img.shields.io/badge/Health-Tech-brightgreen) ![Machine Learning](https://img.shields.io/badge/ML-Powered-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

## Live Demo 📺
🔗[Demo Link](https://cancer-predction-uavkqxcjbgepf9mrxappzfc.streamlit.app/)

## Overview 💡

This project implements a Decision Tree classifier 🌳 to predict cancer risk using patient data including age, BMI, lifestyle factors, and genetic history. The application features an interactive web interface built with Streamlit that allows users to input patient information and receive immediate predictions.

## Features ✨

- **🎛️ Interactive Web Interface**: User-friendly input forms with sliders and radio buttons
- **🤖 Machine Learning Model**: Decision Tree classifier with optimized parameters
- **⚡ Real-time Predictions**: Instant cancer risk assessment
- **📊 Data Visualization**: Charts displaying dataset characteristics and feature importance
- **📱 Responsive Design**: Adapts to different screen sizes
- **🎯 User-Friendly**: Simple and intuitive interface with emoji enhancements

## Dataset 📋

The application uses a dataset with the following features:
- 👨‍👩‍👧‍👦 Age: Patient age
- ⚖️ BMI: Body Mass Index
- 🚬 Smoking: Yes/No indicator
- 🧬 GeneticRisk: Yes/No indicator
- 🏃‍♂️ PhysicalActivity: Activity level measurement
- 🍷 AlcoholIntake: Consumption level
- 🏥 CancerHistory: Family history of cancer (Yes/No)

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/subhadipsinha722133/Cancer-Predction.git
cd Cancer-Predction
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage 🚀

1. Ensure the dataset file `The_Cancer_data_1500_V2.csv` is in the project directory
2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. Open your web browser and navigate to the local URL provided (typically http://localhost:8501)

4. Use the sidebar controls to input patient information:
   - Adjust sliders for Age, BMI, Physical Activity, and Alcohol Intake
   - Select Yes/No options for Smoking, Genetic Risk, and Cancer History

5. View the prediction results and data visualizations on the main panel

## Model Details 🤖

- **Algorithm**: Decision Tree Classifier 🌳
- **Parameters**: max_depth=44, criterion="log_loss"
- **Preprocessing**: StandardScaler for feature normalization
- **Validation**: 80/20 train-test split with random_state=42
- **Performance**: Accuracy metrics displayed in console

## Project Structure 📁

```
Cancer-Predction/
├── app.py                 # Main application file
├── The_Cancer_data_1500_V2.csv  # Dataset
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation

```

## Dependencies 📦

- pandas==2.3.1
- scikit-learn==1.7.1
- streamlit==1.48.1
- matplotlib==3.10.5
- numpy==2.3.2
- altair==5.5.0

See requirements.txt for a complete list of dependencies.

## Contributing 👥

We welcome contributions to improve this application! 🙌

1. Fork the repository 🍴
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request ⭐

Please ensure:
- Code follows PEP 8 guidelines 📝
- Tests are added for new features 🧪
- Documentation is updated accordingly 📚

## Limitations ⚠️

- ❗ This is a demonstration application and should not be used for actual medical diagnosis
- 📊 Model performance depends on the quality and representativeness of the training data
- 🏥 Clinical validation would be required before real-world use
- 🔒 Not intended for production use without proper medical oversight

## Future Enhancements 🔮

- 🗃️ Integration with additional data sources
- 📝 Model explainability features
- 🔐 User authentication and data persistence
- 📤 Export functionality for results
- 🌐 Multi-language support
- 📲 Mobile app version
- ☁️ Cloud deployment options

## License 📄

This project is for educational purposes. Please ensure proper licensing before deployment in production environments.

## Support 💬

For questions or issues regarding this application, please open an issue in the project repository or contact the maintainers.

---

**⭐ Don't forget to star the repository if you find this project useful!**

**🔔 Check back often for updates and new features!**

---

*Made with ❤️ for the healthcare and tech community*
