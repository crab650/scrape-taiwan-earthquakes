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

**⏰ Last Updated (Taipei Time)**: `2026-09-20 16:35:14`

### 🚨 Latest Earthquake Report
- **Report ID**: S20260920160536
- **Origin Time**: `2026-09-20T16:05:36+08:00`
- **Magnitude**: `3.6`
- **Focal Depth**: `8.3 km`
- **Epicenter**: 臺南市政府東北東方  42.1  公里 (位於臺南市楠西區)
- **Max Intensity**: **2級**
- **Report Content**: 09/20-16:05臺南市楠西區發生規模3.6有感地震，最大震度臺南市楠西2級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202609/2026092016053636_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20260920160536 | 2026-09-20T16:05:36+08:00 | 臺南市政府東北東方  42.1  公里 | 3.6 | 8.3 | **2級** | Local |
| S20260920160529 | 2026-09-20T16:05:29+08:00 | 臺南市政府東北東方  44.2  公里 | 3.8 | 7.0 | **4級** | Local |
| S20260919041407 | 2026-09-19T04:14:07+08:00 | 花蓮縣政府南方  3.2  公里 | 3.7 | 24.3 | **2級** | Local |
| S20260917174519 | 2026-09-17T17:45:19+08:00 | 花蓮縣政府南南東方  65.1  公里 | 4.3 | 15.9 | **2級** | Local |
| S20260916000039 | 2026-09-16T00:00:39+08:00 | 臺東縣政府南南東方  74.6  公里 | 3.8 | 23.8 | **3級** | Local |
| S20260914171804 | 2026-09-14T17:18:04+08:00 | 高雄市政府北北西方  19.5  公里 | 3.1 | 27.9 | **1級** | Local |
| 115063 | 2026-09-14T06:44:41+08:00 | 臺東縣政府東南東方  43.0  公里 | 4.9 | 10.1 | **4級** | Significant |
| 115062 | 2026-09-14T03:21:35+08:00 | 花蓮縣政府南南西方  54.9  公里 | 4.7 | 17.6 | **4級** | Significant |
| 115061 | 2026-09-11T19:24:56+08:00 | 花蓮縣政府南方  67.9  公里 | 4.5 | 24.6 | **4級** | Significant |
| S20260911030233 | 2026-09-11T03:02:33+08:00 | 花蓮縣政府東北方  14.3  公里 | 3.7 | 41.4 | **1級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 31 | 60 | 91 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 29 | 38 | 67 |
| 2026 | 南投縣 | 28 | 26 | 54 |
| 2026 | 宜蘭縣 | 18 | 25 | 43 |
| 2026 | 臺中市 | 25 | 16 | 41 |
| 2026 | 彰化縣 | 27 | 12 | 39 |
| 2026 | 雲林縣 | 25 | 13 | 38 |
| 2026 | 臺東縣 | 20 | 15 | 35 |
| 2026 | 嘉義縣 | 21 | 14 | 35 |
| 2026 | 臺南市 | 17 | 9 | 26 |
| 2026 | 新北市 | 14 | 12 | 26 |
| 2026 | 新竹縣 | 15 | 7 | 22 |
| 2026 | 嘉義市 | 17 | 5 | 22 |
| 2026 | 桃園市 | 14 | 7 | 21 |
| 2026 | 苗栗縣 | 15 | 5 | 20 |
| 2026 | 高雄市 | 11 | 7 | 18 |
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
