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

**⏰ Last Updated (Taipei Time)**: `2026-10-07 20:35:15`

### 🚨 Latest Earthquake Report
- **Report ID**: 115068
- **Origin Time**: `2026-10-06T16:41:08+08:00`
- **Magnitude**: `4.5`
- **Focal Depth**: `34.1 km`
- **Epicenter**: 高雄市政府南南西方  42.4  公里 (位於臺灣西南部海域)
- **Max Intensity**: **3級**
- **Report Content**: 10/06-16:41臺灣西南部海域發生規模4.5有感地震，最大震度高雄市3級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202610/2026100616410845068_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 115068 | 2026-10-06T16:41:08+08:00 | 高雄市政府南南西方  42.4  公里 | 4.5 | 34.1 | **3級** | Significant |
| S20261005052610 | 2026-10-05T05:26:10+08:00 | 花蓮縣政府東北東方  .8  公里 | 3.5 | 24.7 | **2級** | Local |
| 115067 | 2026-09-30T13:00:24+08:00 | 花蓮縣政府東方  136.0  公里 | 5.9 | 13.3 | **2級** | Significant |
| S20260929165938 | 2026-09-29T16:59:38+08:00 | 花蓮縣政府南南西方  69.6  公里 | 3.5 | 12.3 | **2級** | Local |
| 115066 | 2026-09-29T02:20:45+08:00 | 花蓮縣政府東南方  33.3  公里 | 5.0 | 16.3 | **3級** | Significant |
| 115065 | 2026-09-27T15:33:02+08:00 | 花蓮縣政府南方  31.8  公里 | 4.4 | 36.9 | **2級** | Significant |
| S20260927141627 | 2026-09-27T14:16:27+08:00 | 宜蘭縣政府南南東方  41.4  公里 | 3.5 | 11.8 | **3級** | Local |
| S20260926115906 | 2026-09-26T11:59:06+08:00 | 苗栗縣政府南方  24.7  公里 | 3.7 | 24.3 | **2級** | Local |
| S20260925010123 | 2026-09-25T01:01:23+08:00 | 新竹市政府南南西方  7.6  公里 | 2.6 | 5.7 | **1級** | Local |
| S20260924055705 | 2026-09-24T05:57:05+08:00 | 嘉義市政府北方  2.1  公里 | 3.4 | 7.3 | **3級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 36 | 68 | 104 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 33 | 43 | 76 |
| 2026 | 南投縣 | 32 | 30 | 62 |
| 2026 | 宜蘭縣 | 21 | 27 | 48 |
| 2026 | 臺中市 | 29 | 17 | 46 |
| 2026 | 彰化縣 | 32 | 14 | 46 |
| 2026 | 雲林縣 | 29 | 14 | 43 |
| 2026 | 嘉義縣 | 26 | 15 | 41 |
| 2026 | 臺東縣 | 24 | 16 | 40 |
| 2026 | 臺南市 | 21 | 10 | 31 |
| 2026 | 新北市 | 15 | 12 | 27 |
| 2026 | 新竹縣 | 17 | 9 | 26 |
| 2026 | 嘉義市 | 20 | 6 | 26 |
| 2026 | 苗栗縣 | 17 | 7 | 24 |
| 2026 | 桃園市 | 16 | 7 | 23 |
| 2026 | 高雄市 | 14 | 8 | 22 |
| 2026 | 臺北市 | 12 | 6 | 18 |
| 2026 | 屏東縣 | 12 | 4 | 16 |
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
