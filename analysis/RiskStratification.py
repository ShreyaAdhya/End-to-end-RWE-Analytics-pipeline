from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=4, random_state=42)
tree.fit(X_train, y_train)

preds_tree = tree.predict(X_test)
print(classification_report(y_test, preds_tree))
