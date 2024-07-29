import requests


def get_image_link(query):
    # Define your Unsplash access key
    access_key = "ZuydbUNPgA7uzxQd-NxRUptEoWAQymo4Tz0VmX9ZiLA"

    # Define the base URL for the Unsplash API
    base_url = "https://api.unsplash.com/"

    # Endpoint for searching photos
    endpoint = "search/photos"

    # Parameters for the API request
    params = {"query": query, "client_id": access_key}

    try:
        # Send GET request to the API
        response = requests.get(f"{base_url}{endpoint}", params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Extract image link from the response
        image_link = response.json()["results"][0]["urls"]["regular"]
        print(image_link)
        return image_link
    except Exception as e:
        print("An error occurred:", e)
        return None


# Get user input
# search_query = input("Enter a search query: ")

# # Get the image link
# image_link = get_image_link(search_query)

# if image_link:
#     print("Image link:", image_link)
# else:
#     print("Failed to fetch image link.")
