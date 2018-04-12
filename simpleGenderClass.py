from sklearn import tree

x = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [165,65,40], [190,90,47], [175,64,39],
	[175,64,39], [177,70,40], [159,55,37], [171,75,42]]

y = ['male', 'female', 'female', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[200,90,44]])

print (prediction)