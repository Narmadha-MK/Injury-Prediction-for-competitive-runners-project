# Injury-Prediction-for-competitive-runners-project
## INJURY PREDICTION FOR COMPETITIVE RUNNERS
### INTRODUCTION

Running is a widely popular sport worldwide, with millions of individuals engaging in various activities such as jogging, running, or trail running. In the United States alone, approximately 60 million people participated in these activities in 2017. However, a concerning statistic reveals that about half of these runners experience injuries annually. Managing these injuries can be challenging and time-consuming, prompting runners to adopt preventive measures such as using rollers, receiving massages, and seeking guidance from professional coaches. Unfortunately, these resources may not be accessible to everyone, making injury prevention a significant concern for many runners.

To address this concern, experts and data scientists are turning to machine learning to predict and prevent injuries in competitive runners. By leveraging advanced algorithms and extensive datasets, machine learning models have the potential to revolutionize injury prevention strategies, ultimately improving the overall well-being of athletes.

### BENEFITS OF INJURY PREDICTION IN MACHINE LEARNING
Machine learning can analyze extensive datasets, including injury records, training patterns, biometrics, and environmental factors, to uncover hidden patterns and correlations, aiding in more informed decision-making by coaches and athletes. These models can continuously learn from new data, improving their accuracy and effectiveness over time and adapting to changing injury risk factors as an athlete's career progresses. Real-time injury risk assessments are provided by machine learning, allowing for immediate adjustments to training loads and practices, reducing the chances of injuries during intense training or competitions. summarize this

### ABOUT THE DATASET
The dataset comprises a comprehensive training log from a renowned Dutch high-level running team spanning seven years (2012-2019). It includes middle and long-distance runners competing in races between 800 meters and the marathon. This choice is justified by their comparable endurance-based training regimes. Notably, the team's head coach remained consistent throughout the data collection period. There are records from 74 runners in the dataset, with 27 women and 47 men. On average, the athletes had been part of the team for about 3.7 years. The majority of runners competed at the national level, while some participated in international competitions. The study strictly adhered to the Declaration of Helsinki guidelines and received approval from the ethics committee of the second author's institution.

### OBJECTIVE
The objective of an injury prediction project is to develop machine learning models that can accurately forecast the likelihood of competitive runners experiencing injuries. By analyzing various factors such as training patterns, biometrics, and environmental conditions, these models aim to provide early identification of injury risks, personalized risk assessments for individual runners, and actionable insights to prevent injuries and optimize performance. Ultimately, the goal is to enhance the long-term health and performance of athletes by minimizing injury occurrence and severity.

### FRAMEWORK
This model was used for predicting the injury based on various factors. The model has undergone through data preprocessing and modelling using various models like SVC,Bagging etc,. The data has been split into 75-25 train-test for validation purpose and separated test data was used to test the model..

### READING DATA
This dataset has been downloaded from kaggle.The first step is reading the data(pd.read_csv)

### DATA PREPROCESSING
In data preprocessing,we have checked the null values and dropped some columns for reducing high dimensional and making the data efficient to use for further proceedings.Using the count plot() we found that the non-injured cases is having a heavy skew and in order to prevent overfitting in our predictive models, we have balanced the dataset using sampling techniques. This ensures that both the injured and non-injured cases are equally represented in the training data.

### MODELS USED
I have used K-NN,SVM (oversampling and undersampling),Bagging(with undersampling and oversampling) for predicting the inury..

### EVALUATION METRICS
This model was evaluated with metrics accuracy().

### RESULT
The model's accuracy was influenced mainly by the sampling method used. The oversampling approach performed better in classifying non-injured data points, while the undersampling method excelled in accurately identifying the injured data points.

To balance the data set, we applied various strategies like sampling, oversampling, and undersampling. Afterward, we evaluated the different balanced datasets using multiple binary classifiers, including KNN, SVM, Bagging. The best performance was achieved using SVM(Oversampling) with an impressive accuracy.

### DEMO VIDEO
