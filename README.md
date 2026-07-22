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

**⏰ Last Updated (Taipei Time)**: `2026-07-23 04:35:14`

### 🚨 Latest Earthquake Report
- **Report ID**: S20260722230855
- **Origin Time**: `2026-07-22T23:08:55+08:00`
- **Magnitude**: `3.4`
- **Focal Depth**: `17.0 km`
- **Epicenter**: 花蓮縣政府西南西方  15.1  公里 (位於花蓮縣秀林鄉)
- **Max Intensity**: **2級**
- **Report Content**: 07/22-23:08花蓮縣秀林鄉發生規模3.4有感地震，最大震度花蓮縣銅門、花蓮縣花蓮市2級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202607/2026072223085534_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20260722230855 | 2026-07-22T23:08:55+08:00 | 花蓮縣政府西南西方  15.1  公里 | 3.4 | 17.0 | **2級** | Local |
| S20260722200455 | 2026-07-22T20:04:55+08:00 | 花蓮縣政府東南方  11.2  公里 | 3.5 | 25.8 | **2級** | Local |
| S20260722033121 | 2026-07-22T03:31:21+08:00 | 花蓮縣政府西南方  25.2  公里 | 3.8 | 15.4 | **3級** | Local |
| S20260720011107 | 2026-07-20T01:11:07+08:00 | 花蓮縣政府西北西方  12.5  公里 | 3.4 | 20.1 | **2級** | Local |
| S20260718040914 | 2026-07-18T04:09:14+08:00 | 花蓮縣政府南南東方  15.2  公里 | 4.1 | 23.8 | **2級** | Local |
| 115050 | 2026-07-15T22:44:30+08:00 | 嘉義縣政府東北東方  38.5  公里 | 4.0 | 5.2 | **4級** | Significant |
| S20260709092901 | 2026-07-09T09:29:01+08:00 | 宜蘭縣政府東北方  28.7  公里 | 3.6 | 5.9 | **2級** | Local |
| 115049 | 2026-07-08T23:47:21+08:00 | 花蓮縣政府西南西方  21.5  公里 | 4.3 | 20.5 | **4級** | Significant |
| S20260707124711 | 2026-07-07T12:47:11+08:00 | 宜蘭縣政府南方  38.3  公里 | 3.8 | 12.4 | **3級** | Local |
| S20260706031135 | 2026-07-06T03:11:35+08:00 | 宜蘭縣政府東北東方  51.2  公里 | 4.9 | 122.3 | **2級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 18 | 24 | 42 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 17 | 18 | 35 |
| 2026 | 南投縣 | 17 | 14 | 31 |
| 2026 | 宜蘭縣 | 12 | 16 | 28 |
| 2026 | 臺中市 | 15 | 10 | 25 |
| 2026 | 彰化縣 | 15 | 6 | 21 |
| 2026 | 雲林縣 | 13 | 5 | 18 |
| 2026 | 新北市 | 10 | 7 | 17 |
| 2026 | 新竹縣 | 11 | 5 | 16 |
| 2026 | 桃園市 | 10 | 5 | 15 |
| 2026 | 嘉義縣 | 10 | 3 | 13 |
| 2026 | 臺北市 | 7 | 5 | 12 |
| 2026 | 苗栗縣 | 7 | 3 | 10 |
| 2026 | 臺東縣 | 8 | 2 | 10 |
| 2026 | 臺南市 | 7 | 2 | 9 |
| 2026 | 嘉義市 | 7 | 2 | 9 |
| 2026 | 新竹市 | 5 | 2 | 7 |
| 2026 | 高雄市 | 4 | 0 | 4 |
| 2026 | 屏東縣 | 3 | 1 | 4 |
| 2026 | 基隆市 | 3 | 0 | 3 |
| 2026 | 澎湖縣 | 1 | 0 | 1 |

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
