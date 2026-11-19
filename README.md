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

**⏰ Last Updated (Taipei Time)**: `2026-11-19 15:35:13`

### 🚨 Latest Earthquake Report
- **Report ID**: S20261118102752
- **Origin Time**: `2026-11-18T10:27:52+08:00`
- **Magnitude**: `3.5`
- **Focal Depth**: `12.6 km`
- **Epicenter**: 臺南市政府東北方  38.2  公里 (位於臺南市東山區)
- **Max Intensity**: **2級**
- **Report Content**: 11/18-10:27臺南市東山區發生規模3.5有感地震，最大震度臺南市白河、嘉義縣義竹2級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202611/2026111810275235_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20261118102752 | 2026-11-18T10:27:52+08:00 | 臺南市政府東北方  38.2  公里 | 3.5 | 12.6 | **2級** | Local |
| S20261117222850 | 2026-11-17T22:28:50+08:00 | 臺東縣政府北北東方  81.7  公里 | 3.8 | 34.0 | **2級** | Local |
| S20261117164605 | 2026-11-17T16:46:05+08:00 | 臺東縣政府北北東方  81.8  公里 | 4.0 | 33.7 | **3級** | Local |
| S20261116123924 | 2026-11-16T12:39:24+08:00 | 臺南市政府西北西方  5.6  公里 | 3.2 | 13.1 | **2級** | Local |
| 115080 | 2026-11-16T07:47:07+08:00 | 臺南市政府西北西方  5.9  公里 | 4.0 | 14.0 | **3級** | Significant |
| S20261115180341 | 2026-11-15T18:03:41+08:00 | 花蓮縣政府南南西方  67.5  公里 | 3.5 | 12.3 | **2級** | Local |
| S20261113095555 | 2026-11-13T09:55:55+08:00 | 花蓮縣政府西北西方  11.4  公里 | 3.8 | 14.6 | **3級** | Local |
| S20261113025437 | 2026-11-13T02:54:37+08:00 | 花蓮縣政府北北西方  6.5  公里 | 3.1 | 6.5 | **2級** | Local |
| S20261111191510 | 2026-11-11T19:15:10+08:00 | 雲林縣政府東南東方  23.2  公里 | 3.4 | 11.8 | **3級** | Local |
| S20261111171357 | 2026-11-11T17:13:57+08:00 | 宜蘭縣政府南南西方  24.9  公里 | 3.7 | 45.0 | **1級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 48 | 95 | 143 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 42 | 63 | 105 |
| 2026 | 南投縣 | 41 | 42 | 83 |
| 2026 | 宜蘭縣 | 28 | 36 | 64 |
| 2026 | 臺中市 | 37 | 23 | 60 |
| 2026 | 臺東縣 | 29 | 28 | 57 |
| 2026 | 彰化縣 | 36 | 18 | 54 |
| 2026 | 雲林縣 | 36 | 16 | 52 |
| 2026 | 嘉義縣 | 34 | 17 | 51 |
| 2026 | 臺南市 | 27 | 13 | 40 |
| 2026 | 新北市 | 18 | 16 | 34 |
| 2026 | 嘉義市 | 26 | 7 | 33 |
| 2026 | 新竹縣 | 20 | 12 | 32 |
| 2026 | 高雄市 | 20 | 8 | 28 |
| 2026 | 苗栗縣 | 20 | 8 | 28 |
| 2026 | 桃園市 | 18 | 10 | 28 |
| 2026 | 臺北市 | 14 | 8 | 22 |
| 2026 | 屏東縣 | 15 | 5 | 20 |
| 2026 | 新竹市 | 10 | 2 | 12 |
| 2026 | 基隆市 | 7 | 0 | 7 |
| 2026 | 澎湖縣 | 4 | 0 | 4 |

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
