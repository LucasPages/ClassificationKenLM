import kenlm
import pandas as pd
import pickle
import sys
import argparse

"""Fichier utilisé pour la classification des blogs par des modèles de langues"""


parser = argparse.ArgumentParser()
parser.add_argument("--n", help="Order of the ngram model")

args = parser.parse_args()


def get_max_index(p0, p1, p2):
    if p0 >= p1:
        if p0 >= p2:
            return 0
        else:
            return 2
    else:
        if p1 >= p2:
            return 1
        else:
            return 2


model0 = kenlm.Model(args.n + "gram_0.binary")
model1 = kenlm.Model(args.n + "gram_1.binary")
model2 = kenlm.Model(args.n + "gram_2.binary")

df = pd.read_csv(sys.stdin, names=['blog', 'class'])

blogs = df['blog'].tolist()
results = []


for line in blogs:
    score0 = model0.score(line)
    score1 = model1.score(line)
    score2 = model2.score(line)

    max_index = get_max_index(score0, score1, score2)
    results.append(max_index)

with open("../out/" + args.n + "grams.out", "wb+") as f:
    pickle.dump(results, f)

