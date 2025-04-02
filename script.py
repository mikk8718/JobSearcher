import requests
import pandas as pd
import argparse
from bs4 import BeautifulSoup

if __name__ == "__main__":
    title, url, distance, description = ([] for i in range(4))

    # get radius
    parser = argparse.ArgumentParser(description="radius")
    parser.add_argument("radius", type=int)
    args = parser.parse_args()

    page = 1
    total_jobs = 0
    while True:
        base_url = "https://www.jobindex.dk/jobsoegning/it?address=Vesterbro+117%2C+9000+Aalborg&radius={}&page={}".format(args.radius,page)
        response = requests.get(base_url)
        
        if response.status_code != 200:
            print(f"Oops, got {response.status_code}. Check the URL or network!")
            exit()
        
        soup = BeautifulSoup(response.text, "html.parser")
        job_listings = soup.find_all("div", class_=("PaidJob-inner", "jix_robotjob-inner"))
        total_jobs += len(job_listings)
        if len(job_listings) < 1: 
            print("no more listings \n found {} jobs".format(total_jobs))
            if input("save to a csv? [y/n]") == "y":
                jobs = pd.DataFrame({
                    "title": title,
                    "description": description,
                    "url" : url,
                    "distance": distance
                })

                df_sorted = jobs.sort_values(by="distance", ascending=True)
                df_sorted.to_csv("informationTeknologiJobs", index=False)
            exit()
        

        for i in job_listings:
            h4_tag = i.find("h4")
            if h4_tag:  
                a_tag = h4_tag.find("a")  
                if a_tag:  
                    job_url = a_tag["href"]
                    job_title = a_tag.text.strip()

            span_tag = i.find("span", class_="job-distance")
            job_distance = span_tag.text.strip().replace(" km", "") if span_tag else "N/A"

            paragraphs = [p.get_text(strip=True) for p in i.find_all("p")]
            description_ = "\n".join(paragraphs)

            print(f"Job Title: {job_title}")

            title.append(job_title)
            description.append(description_)
            url.append(job_url)
            distance.append(job_distance)
       
        page += 1
