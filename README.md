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

**⏰ Last Updated (Taipei Time)**: `2026-09-25 06:35:14`

### 🚨 Latest Earthquake Report
- **Report ID**: S20260925010123
- **Origin Time**: `2026-09-25T01:01:23+08:00`
- **Magnitude**: `2.6`
- **Focal Depth**: `5.7 km`
- **Epicenter**: 新竹市政府南南西方  7.6  公里 (位於新竹市香山區)
- **Max Intensity**: **1級**
- **Report Content**: 09/25-01:01新竹市香山區發生規模2.6有感地震，最大震度苗栗縣竹南、新竹縣竹東1級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202609/2026092501012326_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20260925010123 | 2026-09-25T01:01:23+08:00 | 新竹市政府南南西方  7.6  公里 | 2.6 | 5.7 | **1級** | Local |
| S20260924055705 | 2026-09-24T05:57:05+08:00 | 嘉義市政府北方  2.1  公里 | 3.4 | 7.3 | **3級** | Local |
| S20260924015512 | 2026-09-24T01:55:12+08:00 | 花蓮縣政府西南西方  17.5  公里 | 3.3 | 18.6 | **2級** | Local |
| S20260923152035 | 2026-09-23T15:20:35+08:00 | 花蓮縣政府北北東方  14.6  公里 | 3.3 | 7.2 | **2級** | Local |
| 115064 | 2026-09-22T05:16:13+08:00 | 臺南市政府東北東方  43.9  公里 | 4.2 | 7.5 | **4級** | Significant |
| S20260920160536 | 2026-09-20T16:05:36+08:00 | 臺南市政府東北東方  42.1  公里 | 3.6 | 8.3 | **2級** | Local |
| S20260920160529 | 2026-09-20T16:05:29+08:00 | 臺南市政府東北東方  44.2  公里 | 3.8 | 7.0 | **4級** | Local |
| S20260919041407 | 2026-09-19T04:14:07+08:00 | 花蓮縣政府南方  3.2  公里 | 3.7 | 24.3 | **2級** | Local |
| S20260917174519 | 2026-09-17T17:45:19+08:00 | 花蓮縣政府南南東方  65.1  公里 | 4.3 | 15.9 | **2級** | Local |
| S20260916000039 | 2026-09-16T00:00:39+08:00 | 臺東縣政府南南東方  74.6  公里 | 3.8 | 23.8 | **3級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 32 | 64 | 96 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 30 | 40 | 70 |
| 2026 | 南投縣 | 29 | 28 | 57 |
| 2026 | 宜蘭縣 | 18 | 25 | 43 |
| 2026 | 臺中市 | 25 | 16 | 41 |
| 2026 | 彰化縣 | 28 | 13 | 41 |
| 2026 | 雲林縣 | 26 | 14 | 40 |
| 2026 | 嘉義縣 | 22 | 15 | 37 |
| 2026 | 臺東縣 | 21 | 15 | 36 |
| 2026 | 臺南市 | 18 | 10 | 28 |
| 2026 | 新北市 | 14 | 12 | 26 |
| 2026 | 嘉義市 | 18 | 6 | 24 |
| 2026 | 新竹縣 | 15 | 8 | 23 |
| 2026 | 苗栗縣 | 15 | 6 | 21 |
| 2026 | 桃園市 | 14 | 7 | 21 |
| 2026 | 高雄市 | 12 | 7 | 19 |
| 2026 | 臺北市 | 11 | 6 | 17 |
| 2026 | 屏東縣 | 10 | 4 | 14 |
| 2026 | 新竹市 | 8 | 2 | 10 |
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
