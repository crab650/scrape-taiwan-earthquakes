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

**⏰ Last Updated (Taipei Time)**: `2026-08-27 00:35:15`

### 🚨 Latest Earthquake Report
- **Report ID**: S20260826050935
- **Origin Time**: `2026-08-26T05:09:35+08:00`
- **Magnitude**: `3.8`
- **Focal Depth**: `24.4 km`
- **Epicenter**: 南投縣政府東南東方  9.8  公里 (位於南投縣中寮鄉)
- **Max Intensity**: **2級**
- **Report Content**: 08/26-05:09南投縣中寮鄉發生規模3.8有感地震，最大震度南投縣南投市、彰化縣員林、彰化縣彰化市、雲林縣四湖2級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202608/2026082605093538_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20260826050935 | 2026-08-26T05:09:35+08:00 | 南投縣政府東南東方  9.8  公里 | 3.8 | 24.4 | **2級** | Local |
| S20260825152207 | 2026-08-25T15:22:07+08:00 | 臺東縣政府東南東方  45.4  公里 | 4.2 | 13.1 | **2級** | Local |
| S20260825150230 | 2026-08-25T15:02:30+08:00 | 臺東縣政府東南東方  44.7  公里 | 4.3 | 30.7 | **2級** | Local |
| 115057 | 2026-08-25T15:00:11+08:00 | 臺東縣政府東南東方  48.0  公里 | 5.8 | 13.1 | **4級** | Significant |
| 115056 | 2026-08-22T11:40:15+08:00 | 宜蘭縣政府東南方  41.7  公里 | 5.1 | 27.8 | **3級** | Significant |
| S20260820033208 | 2026-08-20T03:32:08+08:00 | 花蓮縣政府東北東方  36.1  公里 | 4.2 | 24.7 | **1級** | Local |
| S20260819210855 | 2026-08-19T21:08:55+08:00 | 花蓮縣政府東北東方  34.3  公里 | 4.1 | 39.1 | **2級** | Local |
| S20260819065100 | 2026-08-19T06:51:00+08:00 | 花蓮縣政府南南西方  10.3  公里 | 3.1 | 9.7 | **2級** | Local |
| S20260819001018 | 2026-08-19T00:10:18+08:00 | 宜蘭縣政府南方  43.2  公里 | 3.6 | 6.3 | **3級** | Local |
| S20260818072621 | 2026-08-18T07:26:21+08:00 | 臺東縣政府東北方  71.4  公里 | 4.0 | 39.9 | **2級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 25 | 45 | 70 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 23 | 30 | 53 |
| 2026 | 南投縣 | 23 | 22 | 45 |
| 2026 | 宜蘭縣 | 16 | 22 | 38 |
| 2026 | 臺中市 | 21 | 14 | 35 |
| 2026 | 彰化縣 | 22 | 11 | 33 |
| 2026 | 雲林縣 | 20 | 10 | 30 |
| 2026 | 嘉義縣 | 16 | 10 | 26 |
| 2026 | 新北市 | 14 | 10 | 24 |
| 2026 | 臺東縣 | 14 | 9 | 23 |
| 2026 | 新竹縣 | 15 | 5 | 20 |
| 2026 | 桃園市 | 14 | 5 | 19 |
| 2026 | 臺南市 | 12 | 5 | 17 |
| 2026 | 嘉義市 | 13 | 4 | 17 |
| 2026 | 臺北市 | 11 | 5 | 16 |
| 2026 | 苗栗縣 | 12 | 3 | 15 |
| 2026 | 新竹市 | 8 | 2 | 10 |
| 2026 | 屏東縣 | 7 | 2 | 9 |
| 2026 | 高雄市 | 7 | 1 | 8 |
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
