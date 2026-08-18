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

**⏰ Last Updated (Taipei Time)**: `2026-08-18 14:35:14`

### 🚨 Latest Earthquake Report
- **Report ID**: S20260818072621
- **Origin Time**: `2026-08-18T07:26:21+08:00`
- **Magnitude**: `4.0`
- **Focal Depth**: `39.9 km`
- **Epicenter**: 臺東縣政府東北方  71.4  公里 (位於臺灣東部海域)
- **Max Intensity**: **2級**
- **Report Content**: 08/18-07:26臺灣東部海域發生規模4.0有感地震，最大震度臺東縣長濱2級。

![Earthquake Report Map](https://scweb.cwa.gov.tw/webdata/OLDEQ/202608/2026081807262140_H.png)


### 🗺️ Recent 10 Earthquake Records
| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S20260818072621 | 2026-08-18T07:26:21+08:00 | 臺東縣政府東北方  71.4  公里 | 4.0 | 39.9 | **2級** | Local |
| 115055 | 2026-08-15T19:30:16+08:00 | 宜蘭縣政府東南東方  52.8  公里 | 5.2 | 66.6 | **3級** | Significant |
| 115054 | 2026-08-13T03:54:22+08:00 | 屏東縣政府南南東方  91.7  公里 | 4.4 | 40.2 | **3級** | Significant |
| S20260812202051 | 2026-08-12T20:20:51+08:00 | 臺東縣政府南南西方  37.3  公里 | 4.0 | 20.8 | **2級** | Local |
| S20260811015653 | 2026-08-11T01:56:53+08:00 | 臺東縣政府東北方  70.8  公里 | 4.0 | 42.3 | **2級** | Local |
| S20260810213446 | 2026-08-10T21:34:46+08:00 | 花蓮縣政府東北方  42.2  公里 | 3.5 | 33.1 | **2級** | Local |
| S20260809011012 | 2026-08-09T01:10:12+08:00 | 南投縣政府東北東方  33.1  公里 | 3.8 | 16.7 | **2級** | Local |
| S20260805042532 | 2026-08-05T04:25:32+08:00 | 臺東縣政府東北方  61.8  公里 | 3.9 | 35.5 | **2級** | Local |
| S20260803170650 | 2026-08-03T17:06:50+08:00 | 臺南市政府東北東方  35.9  公里 | 3.3 | 8.9 | **2級** | Local |
| S20260803161738 | 2026-08-03T16:17:38+08:00 | 臺南市政府東北東方  36.4  公里 | 3.6 | 9.2 | **2級** | Local |

<!-- EARTHQUAKE_END -->

---

## 📈 Yearly Statistics

<!-- STATS_START -->

### 📈 Yearly General Statistics
| Year | Significant | Local Area | Total |
| :--- | :--- | :--- | :--- |
| 2026 | 23 | 38 | 61 |

### 🏢 Yearly Felt Earthquakes by County (Intensity >= 1)
| Year | County | Significant | Local Area | Total Felt |
| :--- | :--- | :--- | :--- | :--- |
| 2026 | 花蓮縣 | 21 | 26 | 47 |
| 2026 | 南投縣 | 21 | 18 | 39 |
| 2026 | 宜蘭縣 | 14 | 19 | 33 |
| 2026 | 臺中市 | 19 | 12 | 31 |
| 2026 | 彰化縣 | 20 | 10 | 30 |
| 2026 | 雲林縣 | 18 | 9 | 27 |
| 2026 | 嘉義縣 | 14 | 9 | 23 |
| 2026 | 臺東縣 | 13 | 7 | 20 |
| 2026 | 新北市 | 12 | 8 | 20 |
| 2026 | 新竹縣 | 13 | 5 | 18 |
| 2026 | 桃園市 | 12 | 5 | 17 |
| 2026 | 臺南市 | 11 | 5 | 16 |
| 2026 | 嘉義市 | 11 | 4 | 15 |
| 2026 | 臺北市 | 9 | 5 | 14 |
| 2026 | 苗栗縣 | 10 | 3 | 13 |
| 2026 | 新竹市 | 6 | 2 | 8 |
| 2026 | 屏東縣 | 6 | 2 | 8 |
| 2026 | 高雄市 | 6 | 1 | 7 |
| 2026 | 基隆市 | 5 | 0 | 5 |
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
