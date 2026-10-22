# Taiwan Earthquake Tracker 🌋

This project automatically crawls and visualizes Taiwan earthquake reports (including both "Significant Felt Earthquakes" and "Local Felt Earthquakes") from the **Central Weather Administration (CWA) Open Data Platform**. It structures the raw data into a clean, unified JSON payload, updates the project readme table, and serves a premium glassmorphism Single Page Application (SPA) web dashboard for easy browsing.

The tracker is designed for automated data version control using **GitHub and PythonAnywhere scheduled tasks**. By committing data updates directly to `data/earthquake.json`, your GitHub commit history serves as a long-term historical database.

---

## 📂 Project Directory Structure

*   `earthquake_tracker.py` - Core Python CLI (handles fetching, parsing, sorting, updating README, and hosts local HTTP server).
*   `cwa_crawler_pa.py` - Lightweight headless Python crawler designed for periodic runs on **PythonAnywhere**.
*   `config.json` - Shared configurations (containing API Key, dataset IDs, and local server port settings).
*   `index.html` - Web dashboard main SPA structure.
*   `style.css` - Glassmorphism stylesheet featuring a premium dark theme and responsive layout.
*   `app.js` - Dashboard application logic (JSON parsing, live filtering, and rendering shaking intensities).
*   `run_tracker.bat` - Windows launcher script providing a quick interactive console menu.
*   `run_pa_test.bat` - Windows launcher to test the PythonAnywhere crawler locally.
*   `git_sync.sh` - Linux Shell automation script to crawl and push updates to GitHub.
*   `data/` - Created data directory:
    *   `earthquake.json` - Unified data package containing the latest 50 earthquake records.

---

## 📊 Live Earthquake Report

<!-- EARTHQUAKE_START -->

**⏰ Last Updated (Taipei Time)**: `2026-10-23 04:35:18`

### 🚨 Latest Earthquake Report
- **Report ID**: S20261021145120
- **Origin Time**: `2026-10-21T14:51:20+08:00`
- **Magnitude**: `3.9`
- **Focal Depth**: `8.2 km`
- **Epicenter**: 臺東縣政府西南方  12.7  公里 (位於臺東縣近海)
- **Max Intensity**: **2級**
- **Report Content**: 10/21-14:51臺東縣近海發生規模3.9有感地震，最大震度臺東縣太麻里2級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202610/2026102114512039_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20261021145120 | 2026-10-21T14:51:20+08:00 | 臺東縣政府西南方  12.7  公里 | 3.9 | 8.2 | **2級** | Local |
| S20261021040319 | 2026-10-21T04:03:19+08:00 | 花蓮縣政府東北東方  9.9  公里 | 3.4 | 18.2 | **2級** | Local |
| S20261017111319 | 2026-10-17T11:13:19+08:00 | 宜蘭縣政府南方  23.9  公里 | 4.6 | 67.1 | **2級** | Local |
| S20261016074032 | 2026-10-16T07:40:32+08:00 | 花蓮縣政府南南西方  17.4  公里 | 3.5 | 18.7 | **2級** | Local |
| 115069 | 2026-10-13T17:30:10+08:00 | 花蓮縣政府南南西方  50.8  公里 | 4.3 | 33.8 | **3級** | Significant |
| S20261012171645 | 2026-10-12T17:16:45+08:00 | 宜蘭縣政府東南東方  26.4  公里 | 4.4 | 61.1 | **2級** | Local |
| S20261012053004 | 2026-10-12T05:30:04+08:00 | 花蓮縣政府南方  50.4  公里 | 3.7 | 31.6 | **2級** | Local |
| 115068 | 2026-10-06T16:41:08+08:00 | 高雄市政府南南西方  42.4  公里 | 4.5 | 34.1 | **3級** | Significant |
| S20261005052610 | 2026-10-05T05:26:10+08:00 | 花蓮縣政府東北東方  .8  公里 | 3.5 | 24.7 | **2級** | Local |
| 115067 | 2026-09-30T13:00:24+08:00 | 花蓮縣政府東方  136.0  公里 | 5.9 | 13.3 | **2級** | Significant |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 37 | 74 | 111 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 34 | 48 | 82 |
| 2026 | 南投縣 | 33 | 34 | 67 |
| 2026 | 宜蘭縣 | 22 | 30 | 52 |
| 2026 | 臺中市 | 30 | 20 | 50 |
| 2026 | 彰化縣 | 33 | 15 | 48 |
| 2026 | 雲林縣 | 30 | 14 | 44 |
| 2026 | 臺東縣 | 25 | 18 | 43 |
| 2026 | 嘉義縣 | 27 | 15 | 42 |
| 2026 | 臺南市 | 21 | 10 | 31 |
| 2026 | 新北市 | 15 | 14 | 29 |
| 2026 | 新竹縣 | 17 | 11 | 28 |
| 2026 | 嘉義市 | 21 | 6 | 27 |
| 2026 | 苗栗縣 | 18 | 8 | 26 |
| 2026 | 桃園市 | 16 | 9 | 25 |
| 2026 | 高雄市 | 15 | 8 | 23 |
| 2026 | 臺北市 | 12 | 8 | 20 |
| 2026 | 屏東縣 | 12 | 5 | 17 |
| 2026 | 新竹市 | 9 | 2 | 11 |
| 2026 | 基隆市 | 6 | 0 | 6 |
| 2026 | 澎湖縣 | 3 | 0 | 3 |

<!-- STATS_END -->

---

## 🛠️ Getting Started & Configurations

### 1. Obtain CWA Open Data API Key
Data is retrieved from the Taiwan Central Weather Administration. A free API key is required:
1.  Sign up on the [CWA Meteorological Data Open Platform](https://opendata.cwa.gov.tw/).
2.  Go to **Member Area -> API Key** and copy your personal Authorization code.

### 2. Configure config.json
Edit or create `config.json` in the root folder, pasting your API key:
```json
{
    "cwa_api_key": "YOUR_CWA_API_KEY_HERE",
    "output_dir": "data",
    "datasets": [
        "E-A0015-001",
        "E-A0016-001"
    ],
    "server_port": 8800
}
```

### 3. Running Locally

#### 💡 Windows (Recommended):
Double-click **`run_tracker.bat`** to open the interactive selection menu:
*   **[1] Fetch Earthquake Data**: Pulls latest data from CWA.
*   **[2] Launch Dashboard**: Starts the local server and automatically opens your browser.
*   **[3] Fetch and Launch**: Performs both actions sequentially.

#### 💻 Command Line (CLI):
*   **Fetch latest earthquake data**:
    ```bash
    python earthquake_tracker.py --fetch
    ```
*   **Launch local HTTP dashboard server** (starts on port `8800` by default; automatically searches for the next open port if occupied):
    ```bash
    python earthquake_tracker.py --serve
    ```
*   **Start server on custom port**:
    ```bash
    python earthquake_tracker.py --serve --port 9000
    ```

---

## 📄 License
This codebase is open source under the MIT License. Meteorological and seismological data is owned by the Central Weather Administration of Taiwan and licensed under the Open Government Data License, version 1.0.
