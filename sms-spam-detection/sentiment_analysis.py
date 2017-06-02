from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB


with open("smsspamcollection/SMSSpamCollection","r") as text_file:
    lines = text_file.read().split("\n")

    lines= [line.split("\t",1) for line in lines if (line.split("\t")[0]<> '')]
    training_documents = [line[1] for line in lines]

    training_labels = [line[0] for line in lines]

    count_vectorizer = CountVectorizer(binary='true')
training_documents = count_vectorizer.fit_transform(training_documents)

classfier= BernoulliNB().fit(training_documents,training_labels)

print classfier.predict(count_vectorizer.transform(["You have won ?1,000 cash or a ?2,000 prize! To claim, call09050000327"]))

