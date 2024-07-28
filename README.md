# Django News Bot

This project is a Python-based bot that fetches the latest news articles from Nepal and posts them to Facebook every 3 hours using GitHub Actions. It leverages the NewsData API for retrieving news articles and the Facebook Graph API for posting updates.

## Features

- Fetches the latest news articles from Nepal.
- Posts news updates to Facebook every 3 hours.
- Automated scheduling using GitHub Actions.
- Easy setup and deployment with GitHub.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a GitHub account.
- You have an API key from [NewsData.io](https://newsdata.io/).
- You have a Facebook access token from the [Facebook Graph API](https://developers.facebook.com/docs/graph-api).

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/django-news-bot.git
    cd django-news-bot
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Add your API keys to GitHub Secrets**:

    - Go to your GitHub repository.
    - Navigate to `Settings` > `Secrets and variables` > `Actions`.
    - Add the following secrets:
        - `NEWS_API_KEY` with your NewsData API key.
        - `FACEBOOK_ACCESS_TOKEN` with your Facebook access token.

## Usage

1. **GitHub Actions Workflow**:

    The GitHub Actions workflow is defined in `.github/workflows/schedule.yml`. It is set to run every 3 hours and post the latest news to Facebook.

    ```yaml
    name: Post News to Facebook

    on:
      schedule:
        - cron: '0 */3 * * *' # This runs every 3 hours
      workflow_dispatch:

    jobs:
      post_news:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout repository
          uses: actions/checkout@v2

        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.x'

        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt

        - name: Run script
          env:
            NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
            FACEBOOK_ACCESS_TOKEN: ${{ secrets.FACEBOOK_ACCESS_TOKEN }}
          run: |
            python logo.py
    ```

2. **Run Locally** (optional):

    You can also run the script locally for testing purposes:

    ```bash
    python logo.py
    ```

## Contributing

If you have suggestions for improving this project, please open an issue or fork the repository and submit a pull request. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [NewsData.io](https://newsdata.io/) for the news API.
- [Facebook Graph API](https://developers.facebook.com/docs/graph-api) for enabling automated posts.
- [GitHub Actions](https://github.com/features/actions) for providing continuous integration and automation.

