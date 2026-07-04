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

**⏰ Last Updated (Taipei Time)**: `2026-07-05 02:35:15`

### 🚨 Latest Earthquake Report
- **Report ID**: S20260702224430
- **Origin Time**: `2026-07-02T22:44:30+08:00`
- **Magnitude**: `5.3`
- **Focal Depth**: `113.8 km`
- **Epicenter**: 宜蘭縣政府東方  80.9  公里 (位於臺灣東部海域)
- **Max Intensity**: **2級**
- **Report Content**: 07/02-22:44臺灣東部海域發生規模5.3有感地震，最大震度宜蘭縣宜蘭市、花蓮縣和平、桃園市三光、新竹縣關西、臺中市德基、臺東縣成功2級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202607/2026070222443053_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20260702224430 | 2026-07-02T22:44:30+08:00 | 宜蘭縣政府東方  80.9  公里 | 5.3 | 113.8 | **2級** | Local |
| S20260702114525 | 2026-07-02T11:45:25+08:00 | 花蓮縣政府西南方  19.3  公里 | 3.5 | 14.1 | **2級** | Local |
| S20260702090144 | 2026-07-02T09:01:44+08:00 | 屏東縣政府南南東方  101.7  公里 | 4.0 | 22.1 | **2級** | Local |
| 115048 | 2026-07-02T07:06:06+08:00 | 花蓮縣政府南南西方  41.0  公里 | 4.0 | 5.0 | **4級** | Significant |
| S20260702003154 | 2026-07-02T00:31:54+08:00 | 宜蘭縣政府東南東方  30.8  公里 | 4.3 | 56.0 | **2級** | Local |
| S20260630051502 | 2026-06-30T05:15:02+08:00 | 宜蘭縣政府東北東方  36.4  公里 | 5.0 | 94.1 | **2級** | Local |
| S20260629092057 | 2026-06-29T09:20:57+08:00 | 花蓮縣政府西北方  18.1  公里 | 3.6 | 22.4 | **2級** | Local |
| S20260625053042 | 2026-06-25T05:30:42+08:00 | 嘉義縣政府東南東方  15.2  公里 | 3.1 | 7.0 | **2級** | Local |
| S20260621103730 | 2026-06-21T10:37:30+08:00 | 嘉義市政府西方  2.0  公里 | 3.5 | 11.5 | **3級** | Local |
| S20260619193311 | 2026-06-19T19:33:11+08:00 | 宜蘭縣政府南南東方  37.4  公里 | 3.5 | 9.9 | **3級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 16 | 16 | 32 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 16 | 11 | 27 |
| 2026 | 南投縣 | 15 | 9 | 24 |
| 2026 | 臺中市 | 14 | 7 | 21 |
| 2026 | 宜蘭縣 | 11 | 9 | 20 |
| 2026 | 彰化縣 | 13 | 5 | 18 |
| 2026 | 雲林縣 | 12 | 5 | 17 |
| 2026 | 桃園市 | 10 | 4 | 14 |
| 2026 | 新竹縣 | 10 | 4 | 14 |
| 2026 | 新北市 | 10 | 4 | 14 |
| 2026 | 嘉義縣 | 9 | 3 | 12 |
| 2026 | 臺北市 | 7 | 4 | 11 |
| 2026 | 苗栗縣 | 7 | 2 | 9 |
| 2026 | 臺東縣 | 8 | 1 | 9 |
| 2026 | 臺南市 | 6 | 2 | 8 |
| 2026 | 嘉義市 | 6 | 2 | 8 |
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
