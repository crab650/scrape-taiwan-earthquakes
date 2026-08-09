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

**⏰ Last Updated (Taipei Time)**: `2026-08-09 19:35:16`

### 🚨 Latest Earthquake Report
- **Report ID**: S20260809011012
- **Origin Time**: `2026-08-09T01:10:12+08:00`
- **Magnitude**: `3.8`
- **Focal Depth**: `16.7 km`
- **Epicenter**: 南投縣政府東北東方  33.1  公里 (位於南投縣仁愛鄉)
- **Max Intensity**: **2級**
- **Report Content**: 08/09-01:10南投縣仁愛鄉發生規模3.8有感地震，最大震度南投縣埔里2級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202608/2026080901101238_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20260809011012 | 2026-08-09T01:10:12+08:00 | 南投縣政府東北東方  33.1  公里 | 3.8 | 16.7 | **2級** | Local |
| S20260805042532 | 2026-08-05T04:25:32+08:00 | 臺東縣政府東北方  61.8  公里 | 3.9 | 35.5 | **2級** | Local |
| S20260803170650 | 2026-08-03T17:06:50+08:00 | 臺南市政府東北東方  35.9  公里 | 3.3 | 8.9 | **2級** | Local |
| S20260803161738 | 2026-08-03T16:17:38+08:00 | 臺南市政府東北東方  36.4  公里 | 3.6 | 9.2 | **2級** | Local |
| 115053 | 2026-07-31T00:58:36+08:00 | 臺東縣政府北北東方  44.1  公里 | 4.7 | 20.2 | **4級** | Significant |
| S20260730081016 | 2026-07-30T08:10:16+08:00 | 花蓮縣政府南方  21.2  公里 | 3.8 | 22.2 | **2級** | Local |
| 115052 | 2026-07-27T10:14:49+08:00 | 臺南市政府東北東方  36.7  公里 | 4.8 | 9.6 | **4級** | Significant |
| 115051 | 2026-07-26T20:36:17+08:00 | 新北市政府東南東方  35.8  公里 | 5.6 | 95.7 | **3級** | Significant |
| S20260725020453 | 2026-07-25T02:04:53+08:00 | 宜蘭縣政府南南東方  43.0  公里 | 4.0 | 19.6 | **3級** | Local |
| S20260725015216 | 2026-07-25T01:52:16+08:00 | 宜蘭縣政府南南東方  43.1  公里 | 3.7 | 18.9 | **3級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 21 | 34 | 55 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 20 | 23 | 43 |
| 2026 | 南投縣 | 20 | 17 | 37 |
| 2026 | 宜蘭縣 | 13 | 18 | 31 |
| 2026 | 臺中市 | 18 | 12 | 30 |
| 2026 | 彰化縣 | 18 | 9 | 27 |
| 2026 | 雲林縣 | 16 | 8 | 24 |
| 2026 | 嘉義縣 | 13 | 8 | 21 |
| 2026 | 新北市 | 11 | 8 | 19 |
| 2026 | 新竹縣 | 12 | 5 | 17 |
| 2026 | 桃園市 | 11 | 5 | 16 |
| 2026 | 臺東縣 | 11 | 4 | 15 |
| 2026 | 臺南市 | 10 | 5 | 15 |
| 2026 | 嘉義市 | 10 | 4 | 14 |
| 2026 | 臺北市 | 8 | 5 | 13 |
| 2026 | 苗栗縣 | 9 | 3 | 12 |
| 2026 | 新竹市 | 6 | 2 | 8 |
| 2026 | 高雄市 | 6 | 1 | 7 |
| 2026 | 屏東縣 | 5 | 1 | 6 |
| 2026 | 基隆市 | 4 | 0 | 4 |
| 2026 | 澎湖縣 | 2 | 0 | 2 |

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
