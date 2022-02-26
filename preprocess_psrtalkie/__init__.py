from preprocess_kgptalkie import utils 
__version__ = '0.0.1'

def _get_wordcounts(x):
	return utils._get_wordcounts(x)
def _get_charcounts(x):
	return utils._get_charcounts(x)
def _get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)
def _get_hashtag_counts(x):
	return utils._get_hashtag_counts(x)
def _get_mentions_counts(x):
	return utils._get_mentions_counts(x)
def _get_digit_counts(x):
	return utils._get_digit_counts(x):
def _get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)
def get_const_exp(x):
	return utils._get_cont_exp(x)
def get_emails(x):
	return utils._remove_emails(x)
def remove_urls(x):
	return utils._remove_rt(x)
def remove_rt(x):
	return utils._remove_special_chars(x)
def _remove_html_tags(x):
	return utils._remove_html_tags(x)
def remove_accented_chars(x):
	return utils._remove_accented_chars(x)
def _remove_stopwords(x):
	return utils._remove_stopwords(x)

def make_base(x):
	return utils._make_base(x)
def _remove_common_words(x,n=20):
	return utils._remove_common_words(x,n=20)
def remove_rarewords(x,n=20):
	return utils._remove_rarewords(x,n=20)
def _spelling_correction(x):
	return utils._spelling(x,n=20)


