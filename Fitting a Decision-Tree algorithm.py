    #Fitting Decision Tree classifier to the training set  
    From sklearn.tree import DecisionTreeClassifier  
    classifier= DecisionTreeClassifier(criterion='entropy', random_state=0)  
    classifier.fit(x_train, y_train)  
