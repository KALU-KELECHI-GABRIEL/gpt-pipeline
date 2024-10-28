# import requests
# import csv
# import json

# def search_crossref(query):
#     base_url = "https://api.crossref.org/works"
#     params = {
#         "query.bibliographic": query,
#         "filter": "from-pub-date:2014-01-01,until-pub-date:2024-12-31",
#         "rows": 1000,  # Adjust the number of results as needed
#         "cursor": "*"  # Use '*' to get all results
#     }
#     publications = []
#     while True:
#         response = requests.get(base_url, params=params)
#         data = response.json()
#         if "message" not in data or "items" not in data["message"]:
#             break
#         for item in data["message"]["items"]:
#             publications.append(item)
#         if "next-cursor" not in data:
#             break
#         params["cursor"] = data["next-cursor"]
#     return publications

# def export_to_json(publications):
#     with open("publications.json", "w") as json_file:
#         json.dump(publications, json_file, indent=4)

# def export_to_csv(publications):
#     keys = ["type", "created", "author", "title", "container-title", "ISBN", "DOI", "URL", "abstract", "published-print", "published-online", "page", "collection-title", "publisher", "subject"]
#     with open("publications.csv", "w", newline='', encoding='utf-8') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=keys)
#         writer.writeheader()
#         for item in publications:
#             writer.writerow(item)

# def main():
#     ieee_security_query = "IEEE Symposium on Security and Privacy"
#     ieee_info_forensics_query = "IEEE Transactions on Information Forensics and Security"
#     machine_learning_query = "machine learning"
    
#     security_publications = search_crossref(ieee_security_query)
#     info_forensics_publications = search_crossref(ieee_info_forensics_query)
    
#     machine_learning_publications = []
#     for query, publications in [(ieee_security_query, security_publications),
#                                (ieee_info_forensics_query, info_forensics_publications)]:
#         for item in publications:
#             title = item.get("title", [])
#             keywords = item.get("keywords", [])
#             if any(machine_learning_query in t.lower() for t in title) or \
#                any(machine_learning_query in k.lower() for k in keywords):
#                 machine_learning_publications.append(item)
    
#     print("Exporting publications related to machine learning in specified IEEE conferences to JSON and CSV...")
    
#     export_to_json(machine_learning_publications)
#     # export_to_csv(machine_learning_publications)
    
#     print("Export completed!")

# if __name__ == "__main__":
#     main()


import requests
import json
import csv

def search_crossref(query):
    base_url = "https://api.crossref.org/works"
    params = {
        "query.bibliographic": query,
        "filter": "from-pub-date:2014-01-01,until-pub-date:2024-12-31",
        "rows": 1000,  # Adjust the number of results as needed
        "cursor": "*"  # Use '*' to get all results
    }
    publications = []
    while True:
        response = requests.get(base_url, params=params)
        data = response.json()
        if "message" not in data or "items" not in data["message"]:
            break
        for item in data["message"]["items"]:
            publications.append(item)
        if "next-cursor" not in data:
            break
        params["cursor"] = data["next-cursor"]
    return publications
def export_to_json(publications):
    with open("publications.json", "w") as json_file:
        json.dump(publications, json_file, indent=4)

def export_to_csv(publications):
    keys = ["type", "created", "author", "title", "container-title", "ISBN", "DOI", "URL", "abstract", "published-print", "published-online", "page", "collection-title", "publisher", "subject"]
    with open("publications.csv", "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        for item in publications:
            writer.writerow(item)
def main():
    ieee_security_query = "IEEE Symposium on Security and Privacy"
    ieee_info_forensics_query = "IEEE Transactions on Information Forensics and Security"
    machine_learning_query = "machine learning"
    
    security_publications = search_crossref(ieee_security_query)
    info_forensics_publications = search_crossref(ieee_info_forensics_query)
    
    machine_learning_publications = []
    for query, publications in [(ieee_security_query, security_publications),
                               (ieee_info_forensics_query, info_forensics_publications)]:
        for item in publications:
            title = item.get("title", [])
            keywords = item.get("keywords", [])
            if any(machine_learning_query in t.lower() for t in title) or \
               any(machine_learning_query in k.lower() for k in keywords):
                machine_learning_publications.append(item)
    
    print("Publications related to machine learning in specified IEEE conferences:")
    for item in machine_learning_publications:
        item_type = item.get("type")
        publication_year = item.get("created", {}).get("date-parts", [[None]])[0][0]
        authors = [author.get("given", "") + " " + author.get("family", "") for author in item.get("author", [])]
        title = item.get("title", [""])[0]
        publication_title = item.get("container-title", [""])[0]
        isbn = item.get("ISBN", [])
        doi = item.get("DOI", "")
        url = item.get("URL", "")
        abstract = item.get("abstract", "")
        date = item.get("published-print", item.get("published-online", ""))
        date_added = item.get("created", {}).get("date-time", "")
        pages = item.get("page", "")
        series = item.get("collection-title", "")
        publisher = item.get("publisher", "")
        manual_tags = item.get("subject", [])
        
        print("\nItem Type:", item_type)
        print("Publication Year:", publication_year)
        print("Author(s):", ", ".join(authors))
        print("Title:", title)
        print("Publication Title:", publication_title)
        print("ISBN:", ", ".join(isbn))
        print("DOI:", doi)
        print("URL:", url)
        print("Abstract:", abstract)
        print("Date:", date)
        print("Date Added:", date_added)
        print("Pages:", pages)
        print("Series:", series)
        print("Publisher:", publisher)
        print("Manual Tags:", ", ".join(manual_tags))
        
       
    export_to_json(machine_learning_publications)
    # export_to_csv(machine_learning_publications)

if __name__ == "__main__":
    main()
