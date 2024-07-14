
def download_data(url, staging_dir):
    #os.makedirs(staging_dir, exist_ok=True)
    
    file_name = url.split('/')[-1]
    file_path = os.path.join(staging_dir, file_name)

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded data from {url} to {file_path}")
        return file_path
    else:
        print(f"Failed to download data from {url}")
        return None

def download_all_data(urls, staging_dir):
    for url in urls:
        download_data(url, staging_dir)
