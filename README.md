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

**⏰ Last Updated (Taipei Time)**: `2026-09-05 02:35:15`

### 🚨 Latest Earthquake Report
- **Report ID**: 115059
- **Origin Time**: `2026-09-04T17:11:00+08:00`
- **Magnitude**: `4.5`
- **Focal Depth**: `13.7 km`
- **Epicenter**: 臺東縣政府東南東方  44.9  公里 (位於臺灣東南部海域)
- **Max Intensity**: **4級**
- **Report Content**: 09/04-17:11臺灣東南部海域發生規模4.5有感地震，最大震度臺東縣綠島4級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202609/2026090417110045059_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 115059 | 2026-09-04T17:11:00+08:00 | 臺東縣政府東南東方  44.9  公里 | 4.5 | 13.7 | **4級** | Significant |
| S20260903173005 | 2026-09-03T17:30:05+08:00 | 臺東縣政府東南東方  14.4  公里 | 4.5 | 17.8 | **3級** | Local |
| S20260903164522 | 2026-09-03T16:45:22+08:00 | 臺東縣政府東南東方  13.9  公里 | 4.4 | 20.0 | **3級** | Local |
| S20260830194845 | 2026-08-30T19:48:45+08:00 | 臺南市政府東北東方  43.4  公里 | 3.4 | 12.7 | **3級** | Local |
| S20260828181157 | 2026-08-28T18:11:57+08:00 | 臺東縣政府東北東方  43.4  公里 | 3.8 | 22.3 | **3級** | Local |
| S20260828102056 | 2026-08-28T10:20:56+08:00 | 高雄市政府南方  66.3  公里 | 4.4 | 50.7 | **2級** | Local |
| 115058 | 2026-08-27T05:47:20+08:00 | 臺東縣政府東北東方  21.3  公里 | 5.2 | 35.0 | **3級** | Significant |
| S20260826050935 | 2026-08-26T05:09:35+08:00 | 南投縣政府東南東方  9.8  公里 | 3.8 | 24.4 | **2級** | Local |
| S20260825152207 | 2026-08-25T15:22:07+08:00 | 臺東縣政府東南東方  45.4  公里 | 4.2 | 13.1 | **2級** | Local |
| S20260825150230 | 2026-08-25T15:02:30+08:00 | 臺東縣政府東南東方  44.7  公里 | 4.3 | 30.7 | **2級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 27 | 50 | 77 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 25 | 33 | 58 |
| 2026 | 南投縣 | 24 | 22 | 46 |
| 2026 | 宜蘭縣 | 17 | 22 | 39 |
| 2026 | 臺中市 | 22 | 14 | 36 |
| 2026 | 彰化縣 | 23 | 11 | 34 |
| 2026 | 雲林縣 | 21 | 11 | 32 |
| 2026 | 臺東縣 | 16 | 12 | 28 |
| 2026 | 嘉義縣 | 17 | 11 | 28 |
| 2026 | 新北市 | 14 | 10 | 24 |
| 2026 | 新竹縣 | 15 | 5 | 20 |
| 2026 | 臺南市 | 13 | 6 | 19 |
| 2026 | 桃園市 | 14 | 5 | 19 |
| 2026 | 嘉義市 | 14 | 4 | 18 |
| 2026 | 苗栗縣 | 13 | 3 | 16 |
| 2026 | 臺北市 | 11 | 5 | 16 |
| 2026 | 高雄市 | 8 | 5 | 13 |
| 2026 | 屏東縣 | 8 | 3 | 11 |
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
