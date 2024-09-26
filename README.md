Here is the updated `README` with the example `teams.json` data added:

---

# Fortnite Player Tracker (RallyCry Integration) - README

## Overview

This Python script tracks Fortnite player and team data by pulling information from RallyCry team pages and the Fortnite API. The script retrieves team member details such as Epic Games and Discord handles, Fortnite account levels, and links to Fortnite Tracker profiles for easier player management and monitoring.

### Features

- **RallyCry Integration**: Extracts team and player information from RallyCry's API, including team details, competition names, and team leaders.
- **Fortnite API**: Retrieves Fortnite player account information, including account levels.
- **Fortnite Tracker Links**: Provides direct links to each player's Fortnite Tracker profile for further statistics.
- **Error Handling**: Comprehensive error reporting for issues like invalid usernames, incorrect API keys, or HTTP errors.

## Prerequisites

Ensure you have the following set up:

- **Python 3.x**
- **Requests library**: Install it using pip:
  ```bash
  pip install requests
  ```

You will also need valid API keys for both RallyCry and Fortnite APIs.

### Required Files

1. **`teams.json`**: Contains a list of RallyCry teams and their respective details.
2. **`urls.py`**: Defines URL patterns for RallyCry and Fortnite API endpoints.
3. **`Headers.py`**: Contains headers, including API keys, for making authenticated requests.

## File Descriptions

### `teams.json`

This file includes the data structure for teams. The script reads this file to fetch team information from RallyCry.

#### Example Input:

```json
{
  "content": [
    {
      "id": 12345,
      "competition": {
        "id": 101,
        "name": "Fortnite Squad Championship 2024",
        "stateOrdinal": 2,
        "dateTouched": "2024-09-15T12:00:00Z",
        "ordinal": 1,
        "dateCreated": "2024-07-10T14:22:00Z"
      },
      "representing": {
        "id": 5678,
        "name": "University of Gamers",
        "image": "https://example.com/images/uog-logo.png"
      },
      "alternateName": "UoG Squad Champs",
      "joinRestriction": "NORMAL",
      "leader": {
        "id": 2020,
        "name": "UoGProGamer",
        "image": "https://example.com/images/leader-avatar.png"
      },
      "lookingForMore": false,
      "membersCount": 5
    },
    {
      "id": 67890,
      "competition": {
        "id": 202,
        "name": "Fortnite Duo Finals 2024",
        "stateOrdinal": 3,
        "dateTouched": "2024-10-01T16:30:00Z",
        "ordinal": 2,
        "dateCreated": "2024-08-01T09:00:00Z"
      },
      "representing": {
        "id": 7890,
        "name": "Gaming Academy",
        "image": "https://example.com/images/ga-logo.png"
      },
      "alternateName": "GA Duo Finals",
      "joinRestriction": "INVITE_ONLY",
      "leader": {
        "id": 3030,
        "name": "GAElitePlayer",
        "image": "https://example.com/images/elite-avatar.png"
      },
      "lookingForMore": true,
      "membersCount": 2
    }
  ],
  "totalElements": 2,
  "size": 2
}
```

In this structure:

- **Team 1**:

  - `id`: 12345
  - `competition`: "Fortnite Squad Championship 2024"
  - `representing`: University of Gamers
  - `leader`: UoGProGamer
  - `membersCount`: 5

- **Team 2**:
  - `id`: 67890
  - `competition`: "Fortnite Duo Finals 2024"
  - `representing`: Gaming Academy
  - `leader`: GAElitePlayer
  - `membersCount`: 2 (looking for more players)

### `urls.py`

This file contains the URL patterns for querying RallyCry and Fortnite APIs.

```python
RallycryAccountContacts = "https://rallycry.api/teams/{}/contacts"
TeamPage = "https://rallycry.api/teams/{}"
```

### `Headers.py`

This file stores the HTTP headers, including the API keys, required for authenticating requests to RallyCry and Fortnite APIs.

```python
RallycryHeaders = {
    'accept': '*/*',
    'accept-language': 'en',
    'authorization': '',  # Insert your RallyCry API key here
    'cache-vary': 'uid-1NBtE3BBb9VWqg5rVhMbFJkDq5B2',
    'origin': '',
    'priority': 'u=1, i',
    'referer': '',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
}

FortniteApiIOHeaders = {
    'Authorization': ''  # Insert your Fortnite API key here
}
```

## How to Use

1. **API Keys**: Insert your RallyCry API key in the `RallycryHeaders` section and your Fortnite API key in the `FortniteApiIOHeaders` section of `Headers.py`.

2. **Update teams.json**: Add the appropriate team IDs and details into the `teams.json` file. Each team should have an ID, competition details, and team members.

3. **Run the Script**:

   - Open a terminal or command prompt.
   - Navigate to the script directory and run:
     ```bash
     python main.py
     ```

4. **Output**: The script will pull data for each team from RallyCry and display details such as:
   - Epic Games handles.
   - Fortnite account levels.
   - Links to Fortnite Tracker profiles for further stats.

### Example Output:

```
UoG Squad Champs:
    Epic Games: UoGProGamer
    level: 45
    https://fortnitetracker.com/profile/all/UoGProGamer
    Discord: UoGProGamer#1234
```

## Error Handling

The script handles various HTTP errors and provides descriptive error messages:

- **400**: Bad Request – Incorrectly formatted request.
- **401**: Unauthorized – Invalid or missing API keys.
- **403**: Forbidden – Insufficient permissions to access the resource.
- **404**: Not Found – Team or player data was not found.

If an error occurs, the script will print an appropriate message and, in some cases, exit the execution.

## Customization

- **Adding Teams**: To track more teams, add them to the `teams.json` file.
- **Modifying URLs**: Update the URLs in `urls.py` if RallyCry or Fortnite API endpoints change.

## License

This script is for personal and non-commercial use. Please ensure you comply with the terms and conditions of the RallyCry and Fortnite APIs.

---

The `README` now includes the updated `teams.json` example with the necessary explanation for users to customize their own data.
