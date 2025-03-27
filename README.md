-> To install dependencies:
1. {pip install poetry} - installs the poetry dependency.
2. {poetry new pubmed_proj} - creating new folder
3. {poetry add requests} -  installs the requests package for making API calls.


-> Project Explanation:
1. I had developed two python files("pubmed_api.py and main.py")

2. In "pubmed_api.py" file, 
    PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
there will be two PubMed API's available. And I had set how the output should be displayed in csv file.

3. In "main.py" file, the above two API will be called by the "fetch_pubmed_ids() and fetch_paper_details()" present in main() method and the output format mentioned in "pubmed_api.py" file, that data will be saved in csv file format.

4. The command {python main.py "cancer treatment" -f results.csv} should written in terminal to execute the project. It explains,
    python main.py -	Runs the Python script named main.py.
    "cancer treatment" -	The search query passed as an argument (in this case, looking for papers related to "cancer treatment").
    -f results.csv -	Saves the fetched results into a file named results.csv.

5. After that command, the following command {python main.py "biotech companies" -d} should written in terminal to execute the project. It explains,
    python main.py -	Runs the Python script named main.py.
    "biotech companies" -	The search query passed as an argument (fetches research papers related to "biotech companies").
    -d -	Enables debug mode to print detailed logs for troubleshooting.


