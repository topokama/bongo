import input_reader
import concept_extraction
import text_preparations
import argparse
import pdb

parser = argparse.ArgumentParser(description='Builds an ontology from text(s)')
parser.add_argument(dest='files', metavar='file', nargs='+',
                   help='text files name (or names)')

args = parser.parse_args()
# print(files)
texts = []
for file in args.files:
    texts.append(input_reader.readFile('texts/' + file))
textsData = text_preparations.PrepareTexts(texts)
contepts = concept_extraction.GetConcepts(textsData)

q=1


