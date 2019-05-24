#!/usr/bin/env python

import re
import os
from time import gmtime, strftime
from datetime import datetime, timedelta
import unicodedata
import operator

import sentimentLists

def computeSentiment(A_list, search_words):
    a_counter = {}

    for word in A_list:
        upper = word.upper()
        if upper in a_counter:
            a_counter[upper] += 1
        else:
            a_counter[upper] = 1

    sentimentScore = 0

    for search_word in search_words:
        if search_word in a_counter:
            sentimentScore += a_counter[search_word]

    return sentimentScore

def findSentimentAppearance(stories_list, combinedSentiment):

    containerArray = []
    for story in stories_list:
        a_counter = {}

        for word in story:
            upper = word.upper()
            if upper in a_counter:
                a_counter[upper] += 1
            else:
                a_counter[upper] = 1

        normalizedScoreArray = []
        for search_words in combinedSentiment:
            totalCounter = {}

            for word in search_words:
                if word in a_counter:
                    totalCounter[word] = a_counter[word]

            totalWords = 0
            for key in a_counter:
                totalWords += a_counter[key]

            listWords = 0
            for key in totalCounter:
                listWords += totalCounter[key]

            try:
                normalizedCount = (listWords/totalWords) * 100
            except:
                normalizedCount = 0
            normalizedScoreArray.append(normalizedCount)

        containerArray.append(normalizedScoreArray)
    for subset in containerArray:
        print('normalized score,'+str(subset[0])+ ',' +str(subset[1]) + ',' + str(subset[2])
            + ',' + str(subset[3]) + ',' + str(subset[4]) + ',' + str(subset[5])
            + ',' + str(subset[6]) + ',' + str(subset[7]) + ',' + str(subset[8])
            + ',' + str(subset[9]))


def ComputeJaccardSimilarity(words_A, words_B):

    '''
    Compute Jaccard similarity between document A and
    document B.

    Parameters
    ----------
    words_A : set
        Words in document A.
    words_B : set
        Words in document B

    Returns
    -------
    jaccard_score : float
        Jaccard similarity between document
        A and document B.

    '''

    # Count number of words in both A and B
    words_intersect = len(words_A.intersection(words_B))

    # Count number of words in A or B
    words_union = len(words_A.union(words_B))

    # Compute Jaccard similarity score
    jaccard_score = words_intersect / words_union

    return jaccard_score

translationA1 = open("./stories/BarbersBurton.txt", "r", encoding="utf8")
translationA2 = open("./stories/MerchantGenieBurton.txt", "r", encoding="utf8")
translationA3 = open("./stories/PorterBurton.txt", "r", encoding="utf8")
translationA4 = open("./stories/TailorsBurton.txt", "r", encoding="utf8")
translationA5 = open("./stories/ThreeApplesBurton.txt", "r", encoding="utf8")
translationB1 = open("./stories/BarbersLane.txt", "r", encoding="utf8")
translationB2 = open("./stories/MerchantGenieLane.txt", "r", encoding="utf8")
translationB3 = open("./stories/PorterLane.txt", "r", encoding="utf8")
translationB4 = open("./stories/TailorsLane.txt", "r", encoding="utf8")
translationB5 = open("./stories/ThreeApplesLane.txt", "r", encoding="utf8")
translationC1 = open("./stories/BarbersPane.txt", "r", encoding="utf8")
translationC2 = open("./stories/MerchantGeniePane.txt", "r", encoding="utf8")
translationC3 = open("./stories/PorterPane.txt", "r", encoding="utf8")
translationC4 = open("./stories/TailorsPane.txt", "r", encoding="utf8")
translationC5 = open("./stories/ThreeApplesPane.txt", "r", encoding="utf8")


A1_list = re.findall(r"[\w']+", translationA1.read())
B1_list = re.findall(r"[\w']+", translationB1.read())
C1_list = re.findall(r"[\w']+", translationC1.read())
A2_list = re.findall(r"[\w']+", translationA2.read())
B2_list = re.findall(r"[\w']+", translationB2.read())
C2_list = re.findall(r"[\w']+", translationC2.read())
A3_list = re.findall(r"[\w']+", translationA3.read())
B3_list = re.findall(r"[\w']+", translationB3.read())
C3_list = re.findall(r"[\w']+", translationC3.read())
A4_list = re.findall(r"[\w']+", translationA4.read())
B4_list = re.findall(r"[\w']+", translationB4.read())
C4_list = re.findall(r"[\w']+", translationC4.read())
A5_list = re.findall(r"[\w']+", translationA5.read())
B5_list = re.findall(r"[\w']+", translationB5.read())
C5_list = re.findall(r"[\w']+", translationC5.read())

words_A1 = set(A1_list)
words_B1 = set(B1_list)
words_C1 = set(C1_list)
words_A2 = set(A2_list)
words_B2 = set(B2_list)
words_C2 = set(C2_list)
words_A3 = set(A3_list)
words_B3 = set(B3_list)
words_C3 = set(C3_list)
words_A4 = set(A4_list)
words_B4 = set(B4_list)
words_C4 = set(C4_list)
words_A5 = set(A5_list)
words_B5 = set(B5_list)
words_C5 = set(C5_list)


jaccard = 0
jaccard = ComputeJaccardSimilarity(words_A1, words_B1)
print('A1-B1,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_B1, words_C1)
print('B1-C1,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A1, words_C1)
print('A1-C1,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A2, words_B2)
print('A2-B2,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_B2, words_C2)
print('B2-C2,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A2, words_C2)
print('A2-C2,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A3, words_B3)
print('B3-C3,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_B3, words_C3)
print('B3-C3,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A3, words_C3)
print('A3-C3,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A4, words_B4)
print('A4-B4,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_B4, words_C4)
print('B4-C4,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A4, words_C4)
print('A4-C4,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A5, words_B5)
print('A5-B5,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_B5, words_C5)
print('B5-C5,'+str(jaccard))
jaccard = ComputeJaccardSimilarity(words_A5, words_C5)
print('A5-C5,'+str(jaccard))




importedSentiment = sentimentLists.sentimentList
convertedImportedSentiment = []

for list in importedSentiment:
    tempList = []

    for word in list:
        tempList.append(word)
        tempList.append(word+'S')
        tempList.append(word+'ES')
        tempList.append(word+'D')
        tempList.append(word+'ED')
        tempList.append(word+'LY')
        tempList.append(word+'ING')
        tempList.append(word+word[-1]+'ED')
        tempList.append(word+word[-1]+'ING')

    convertedImportedSentiment.append(tempList)

stories_list = [A1_list, B1_list, C1_list, A2_list, B2_list,
 C2_list, A3_list, B3_list, C3_list, A4_list, B4_list, C4_list,
 A5_list, B5_list, C5_list]

finalScores = []

for story in stories_list:
    sentimentArray = []
    for sentiment in importedSentiment:
        score = computeSentiment(story, sentiment)
        sentimentArray.append(score)
    finalScores.append(sentimentArray)

totalCounter = findSentimentAppearance(stories_list, importedSentiment)
# print(finalScores)
# print(len(finalScores))
for subset in finalScores:
    print('score,'+str(subset[0])+ ',' +str(subset[1]) + ',' + str(subset[2])
        + ',' + str(subset[3]) + ',' + str(subset[4]) + ',' + str(subset[5])
        + ',' + str(subset[6]) + ',' + str(subset[7]) + ',' + str(subset[8])
        + ',' + str(subset[9]))
