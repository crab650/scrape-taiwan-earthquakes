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

**⏰ Last Updated (Taipei Time)**: `2026-11-10 13:35:20`

### 🚨 Latest Earthquake Report
- **Report ID**: 115079
- **Origin Time**: `2026-11-09T12:21:57+08:00`
- **Magnitude**: `4.2`
- **Focal Depth**: `11.0 km`
- **Epicenter**: 雲林縣政府東南東方  23.2  公里 (位於雲林縣古坑鄉)
- **Max Intensity**: **4級**
- **Report Content**: 11/09-12:21雲林縣古坑鄉發生規模4.2有感地震，最大震度嘉義縣番路4級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202611/2026110912215742079_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 115079 | 2026-11-09T12:21:57+08:00 | 雲林縣政府東南東方  23.2  公里 | 4.2 | 11.0 | **4級** | Significant |
| S20261108050710 | 2026-11-08T05:07:10+08:00 | 花蓮縣政府南方  48.3  公里 | 3.7 | 30.6 | **2級** | Local |
| S20261106235545 | 2026-11-06T23:55:45+08:00 | 高雄市政府西北方  37.2  公里 | 2.7 | 7.9 | **1級** | Local |
| 115078 | 2026-11-06T12:01:13+08:00 | 花蓮縣政府北北東方  2.4  公里 | 4.0 | 23.0 | **3級** | Significant |
| 115077 | 2026-11-06T08:37:41+08:00 | 臺東縣政府西南方  12.9  公里 | 4.4 | 7.9 | **3級** | Significant |
| S20261104074202 | 2026-11-04T07:42:02+08:00 | 花蓮縣政府南方  61.5  公里 | 4.0 | 34.6 | **2級** | Local |
| S20261104013122 | 2026-11-04T01:31:22+08:00 | 宜蘭縣政府南南東方  32.8  公里 | 3.4 | 15.0 | **3級** | Local |
| 115076 | 2026-11-03T23:22:05+08:00 | 宜蘭縣政府南南東方  33.5  公里 | 4.5 | 15.2 | **4級** | Significant |
| S20261103141156 | 2026-11-03T14:11:56+08:00 | 臺東縣政府北北東方  52.5  公里 | 3.7 | 15.3 | **2級** | Local |
| S20261102102309 | 2026-11-02T10:23:09+08:00 | 宜蘭縣政府東南方  56.6  公里 | 4.8 | 60.4 | **2級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 47 | 84 | 131 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 42 | 57 | 99 |
| 2026 | 南投縣 | 41 | 37 | 78 |
| 2026 | 宜蘭縣 | 28 | 34 | 62 |
| 2026 | 臺中市 | 37 | 22 | 59 |
| 2026 | 臺東縣 | 29 | 24 | 53 |
| 2026 | 彰化縣 | 36 | 16 | 52 |
| 2026 | 雲林縣 | 36 | 14 | 50 |
| 2026 | 嘉義縣 | 33 | 15 | 48 |
| 2026 | 臺南市 | 26 | 11 | 37 |
| 2026 | 新北市 | 18 | 15 | 33 |
| 2026 | 嘉義市 | 26 | 6 | 32 |
| 2026 | 新竹縣 | 20 | 11 | 31 |
| 2026 | 苗栗縣 | 20 | 8 | 28 |
| 2026 | 桃園市 | 18 | 10 | 28 |
| 2026 | 高雄市 | 19 | 8 | 27 |
| 2026 | 臺北市 | 14 | 8 | 22 |
| 2026 | 屏東縣 | 14 | 5 | 19 |
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
