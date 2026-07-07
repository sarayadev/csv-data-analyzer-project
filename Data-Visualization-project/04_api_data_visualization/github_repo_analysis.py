import requests
import plotly.express as px
import plotly.io as pio
import logging
import time


pio.renderers.default = "browser"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


GITHUB_API_URL = "https://api.github.com/search/repositories?q=language:python&sort=stars"


def fetch_repositories(retries=3, timeout=10):
    """
    Fetch repository data from GitHub API with error handling and retry logic.
    """

    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Request attempt {attempt}")

            response = requests.get(GITHUB_API_URL, timeout=timeout)
            response.raise_for_status()

            data = response.json()

            if "items" not in data:
                raise ValueError("Invalid API response structure: missing 'items'")

            return data["items"]

        except requests.exceptions.Timeout:
            logging.warning("Request timed out.")

        except requests.exceptions.ConnectionError:
            logging.warning("Connection error occurred.")

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error: {http_err}")
            break

        except ValueError as val_err:
            logging.error(f"Data format error: {val_err}")
            break

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            break

        time.sleep(2)  # wait before retrying

    return []


def process_data(repositories):
    """
    Extract relevant fields from API response safely.
    """

    if not repositories:
        return [], []

    names = []
    stars = []

    for repo in repositories[:10]:
        names.append(repo.get("name", "Unknown"))
        stars.append(repo.get("stargazers_count", 0))

    return names, stars


def visualize_data(names, stars):
    """
    Create bar chart visualization using Plotly.
    """

    if not names or not stars:
        logging.warning("No data available for visualization.")
        return

    fig = px.bar(
        x=names,
        y=stars,
        title="Most Starred Python Repositories on GitHub",
        labels={"x": "Repository Name", "y": "Star Count"}
    )

    fig.show()


def main():
    repositories = fetch_repositories()
    names, stars = process_data(repositories)
    visualize_data(names, stars)

if __name__ == "__main__":
    main()