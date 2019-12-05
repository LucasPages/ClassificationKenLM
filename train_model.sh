#! /bin/bash

if [ $# != 2 ]
then
	echo "Usage : ./train_model n corpus"
	exit 1
fi

n=$1
corpus=$2

kenlm/build/bin/lmplz -o $n < ../plain_corpus_$corpus.txt > arpa/$n"gram"_$corpus.arpa
kenlm/build/bin/build_binary arpa/$n"gram"_$corpus.arpa $n"gram"_$corpus.binary
rm arpa/*
