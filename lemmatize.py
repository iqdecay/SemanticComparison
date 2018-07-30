from treetaggerwrapper import TreeTagger


def define_tagger(lang="fr", tag_dir="C:\TreeTagger"):
    return TreeTagger(TAGLANG=lang, TAGDIR=tag_dir)


def lemmatize_text(text, tagger):
    """Return the cleaned text (in the form of a string) in lemmatized and tokenized form"""
    text_tokenized_lemmatized = []
    lines = tagger.tag_text(text)
    lemma = ''
    for line in lines:
        _, _, lemma = line.split('\t')
    text_tokenized_lemmatized.append(lemma)
    return text_tokenized_lemmatized
