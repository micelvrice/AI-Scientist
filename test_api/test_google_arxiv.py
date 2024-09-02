import arxiv
from scholarly import scholarly
def get_citation_count(title, authors):
    title = 'Longlora: Efficient fine-tuning of long-context large language models'
    search_query = scholarly.search_pubs(title)
    paper = next(search_query)
    print(paper)
    
    # Verify if it's the correct paper (comparing first author)
    if authors and paper['bib']['author'][0].lower() in authors[0].name.lower():
        return paper['num_citations']

# Construct the default API client.
client = arxiv.Client()

# Search for the 10 most recent articles matching the keyword "quantum."
search = arxiv.Search(
  query = "quantum",
  max_results = 1,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

results = client.results(search)

for result in client.results(search):
    citation_count = get_citation_count(result.title, result.authors)
    print(citation_count)
    exit()
    arxiv_id = result.entry_id.split('/')[-1]
    citation_count = get_citation_count(arxiv_id)
    print(citation_count)
