# Ticker Announcement Filter

## Overview

This Streamlit application allows users to filter announcements related to stock tickers. The primary functionalities include:

- **Filtering by Ticker**: Select a ticker from a predefined list to view announcements related to that ticker.
- **Filtering by 'Trading Halt'**: Click a button to filter announcements containing the text "trading halt" in the header.
- **Search Functionality**: (Commented out) Search for specific text in the announcement headers.

## Features

- **Ticker Selection**: Choose a ticker from the sidebar to filter the data.
- **Trading Halt Filter**: Click the button to display announcements that include "trading halt" in the header.
- **Search Functionality**: (Currently commented out) Allows searching for specific keywords in the headers.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Pandas

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Place your dataset file (`test_data.csv`) in the `data` directory.

2. Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```


3. Open the application in your web browser (usually at `http://localhost:8501`).

### Data Format

The application expects a CSV file (`test_data.csv`) with the following columns:

- `header`: The announcement header text.
- `issuer_code`: The code of the issuer.
- `issuer_full_name`: The full name of the issuer.

## Code Explanation

- **Page Configuration**: Sets up the page title, icon, and layout.
- **Data Caching**: Uses `@st.cache_resource` to cache the data retrieval process and reduce loading times.
- **Sidebar Filters**: Provides options to filter by ticker and a button to apply the "trading halt" filter.
- **Data Filtering**:
  - **By Ticker**: Displays announcements related to the selected ticker.
  - **By 'Trading Halt'**: Filters and displays announcements containing "trading halt" in the header.

## Future Enhancements

- **Search Functionality**: The commented-out code for text search can be enabled to allow users to search for specific keywords in the announcement headers.

## Author

**Ejelonu Benedict O.**


