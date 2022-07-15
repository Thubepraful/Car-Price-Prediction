# Car-Price-Prediction
Web application of Machine learning Model for predicting price of cars depending on various aspects of a car.

Preview of file : https://drive.google.com/file/d/1oq5ZB-vqW15en89Dl-TWKp9gE-iqPPfX/view?usp=sharing

Summery :
- Firstly we have imported all the necessary libraries and the file itself.
- Then it was found that some of the features has peculiar datatypes indicating null values in the form of string anomalies.
- So instead of dropping the record we replaced them with mean values as there were less no. records in the dataset.
- Then for the target column we rectified the outliars and removed them to make the data normalized.
- Next step was to convert the arbitary datatypes to numbers via encoding.
- Then we handled skewness of number datatype features to make the dataset normally distributed & found out that most of the features are co-related, so we reduced skewness of one column
- After that it was all left about getting started with building the model building.
- We splitted the data into independent & dependent features then into training set & testing set of it.
- Then we cross checked the the distribution & relationship of data which was linear.
- So we imported linear regression model, trianed it with data, found out the accuracy.
- Then we dumped the file into string rep file by pickling to export the model & it's data fitting objects.
