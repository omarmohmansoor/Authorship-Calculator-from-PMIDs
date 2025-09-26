from Bio import Entrez
from collections import Counter

# Set your email

Entrez.email = ""

# List of PMIDs separate them by commas
pmids = [
    
]

def check_AuthorSurname_author_positions(pmids):
    AuthorSurname_pmids = []
    for pmid in pmids:
        handle = Entrez.efetch(db="pubmed", id=str(pmid), rettype="medline", retmode="text")
        record = handle.read()
        handle.close()
        authors = [line for line in record.split('\n') if line.startswith("AU  -")]
        for position, author_line in enumerate(authors[:500], start=1):
            if "AuthorSurname" in author_line:
                AuthorSurname_pmids.append((pmid, position))
                break
    return AuthorSurname_pmids

AuthorSurname_author_positions = check_AuthorSurname_author_positions(pmids)

position_counts = Counter(position for pmid, position in AuthorSurname_author_positions)
for position, count in sorted(position_counts.items()):
    print(f"Position {position}: {count} time(s)")

for pmid, position in AuthorSurname_author_positions:
    print(f"PMID: {pmid}, AuthorSurname is author number: {position}")  