#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Taiwan Earthquake Tracker - PythonAnywhere Dedicated Crawler
Fetches earthquake reports from the CWA API, parses, sorts, saves to data/earthquake.json,
and updates README.md. Designed to be run periodically via cron/scheduled tasks.
"""

import os
import ssl
import json
import datetime
import urllib.request
import urllib.error
from pathlib import Path

SCRIPT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = SCRIPT_DIR / "config.json"
DATASET_SIGNIFICANT = "E-A0015-001"  # 顯著有感地震報告
DATASET_SMALL = "E-A0016-001"        # 小區域有感地震報告
API_URL_TEMPLATE = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/{dataset_id}"

def get_config():
    if not CONFIG_PATH.exists():
        default_config = {
            "cwa_api_key": "YOUR_CWA_API_KEY_HERE",
            "output_dir": "data",
            "datasets": [DATASET_SIGNIFICANT, DATASET_SMALL],
            "server_port": 8800
        }
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4, ensure_ascii=False)
        print(f"[!] config.json not found. Created template at: {CONFIG_PATH}")
        return None

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error reading config.json: {e}")
        return None

def fetch_data(dataset_id, api_key):
    url = API_URL_TEMPLATE.format(dataset_id=dataset_id)
    query_url = f"{url}?Authorization={api_key}&format=JSON"
    
    print(f"[*] Fetching dataset '{dataset_id}' from CWA Open Data Platform...")
    
    req = urllib.request.Request(
        query_url, 
        headers={'User-Agent': 'PythonAnywhereEarthquakeClient/1.0'}
    )
    
    try:
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(req, timeout=30, context=context) as response:
            if response.status == 200:
                raw_data = response.read().decode('utf-8')
                return json.loads(raw_data)
            print(f"[!] API request failed with status code: {response.status}")
            return None
    except urllib.error.HTTPError as e:
        print(f"[!] HTTP Error {e.code}: {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"[!] Connection Error: {e.reason}")
        return None
    except Exception as e:
        print(f"[!] Unexpected error during fetch: {e}")
        return None

def get_intensity_rank(intensity_str):
    if not intensity_str:
        return 0
    val = intensity_str.replace("級", "")
    rank_map = {
        "0": 0, "1": 1, "2": 2, "3": 3,
        "4弱": 4.1, "4強": 4.2, "4": 4,
        "5弱": 5.1, "5強": 5.2, "5": 5,
        "6弱": 6.1, "6強": 6.2, "6": 6,
        "7": 7
    }
    return rank_map.get(val, 0)

def get_max_intensity(shaking_areas):
    if not shaking_areas:
        return "無"
    max_area = max(shaking_areas, key=lambda a: get_intensity_rank(a["intensity"]), default=None)
    return max_area["intensity"] if max_area else "無"

def parse_earthquakes(raw_data, dataset_type):
    if not raw_data or not raw_data.get("success") == "true":
        return []
        
    records = raw_data.get("records", {})
    earthquakes_list = records.get("Earthquake", [])
    parsed_list = []
    
    for eq in earthquakes_list:
        info = eq.get("EarthquakeInfo", {})
        origin_time = info.get("OriginTime", "")
        eq_no = eq.get("EarthquakeNo")
        
        # If EarthquakeNo is empty, generic, or it's a small-scale report, generate a unique ID
        if not eq_no or str(eq_no).endswith("000") or dataset_type == DATASET_SMALL:
            digits = "".join([c for c in origin_time if c.isdigit()])
            eq_no = f"S{digits[:14]}"
            
        epicenter = info.get("Epicenter", {})
        magnitude = info.get("EarthquakeMagnitude", {})
        
        intensity_data = eq.get("Intensity", {})
        shaking_areas = []
        areas = intensity_data.get("ShakingArea", [])
        
        if isinstance(areas, dict):
            areas = [areas]
            
        for area in areas:
            area_name = area.get("CountyName") or area.get("AreaName") or area.get("AreaDesc") or ""
            area_intensity = area.get("AreaIntensity", "")
            area_desc = area.get("AreaDesc", "")
            
            if area_name and area_intensity:
                shaking_areas.append({
                    "area_name": area_name,
                    "intensity": area_intensity,
                    "area_desc": area_desc
                })
                
        shaking_areas.sort(key=lambda a: get_intensity_rank(a["intensity"]), reverse=True)
        max_intensity = get_max_intensity(shaking_areas)
        
        parsed_list.append({
            "id": str(eq_no),
            "type": "顯著有感" if dataset_type == DATASET_SIGNIFICANT else "小區域",
            "report_content": eq.get("ReportContent", ""),
            "report_image": eq.get("ReportImageURI", ""),
            "web_link": eq.get("Web", ""),
            "origin_time": origin_time,
            "depth": info.get("FocalDepth"),
            "magnitude": magnitude.get("MagnitudeValue"),
            "epicenter": {
                "location": epicenter.get("Location", ""),
                "latitude": epicenter.get("EpicenterLatitude"),
                "longitude": epicenter.get("EpicenterLongitude")
            },
            "shaking_areas": shaking_areas,
            "max_intensity": max_intensity
        })
        
    return parsed_list

def update_readme(earthquakes):
    readme_path = SCRIPT_DIR / "README.md"
    if not readme_path.exists():
        print("[!] README.md not found. Skipping README update.")
        return
        
    tz_taiwan = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_taiwan)
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    md_content = []
    md_content.append(f"**⏰ Last Updated (Taipei Time)**: `{formatted_time}`\n")
    
    if earthquakes:
        latest = earthquakes[0]
        md_content.append("### 🚨 Latest Earthquake Report")
        md_content.append(f"- **Report ID**: {latest['id']}")
        md_content.append(f"- **Origin Time**: `{latest['origin_time']}`")
        md_content.append(f"- **Magnitude**: `{latest['magnitude']}`")
        md_content.append(f"- **Focal Depth**: `{latest['depth']} km`")
        md_content.append(f"- **Epicenter**: {latest['epicenter']['location']}")
        md_content.append(f"- **Max Intensity**: **{latest['max_intensity']}**")
        if latest['report_content']:
            md_content.append(f"- **Report Content**: {latest['report_content']}")
        if latest['report_image']:
            md_content.append(f"\n![Earthquake Report Map]({latest['report_image']})")
        md_content.append("\n")
        
        md_content.append("### 🗺️ Recent 10 Earthquake Records")
        md_content.append("| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |")
        md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        
        for eq in earthquakes[:10]:
            loc = eq['epicenter']['location']
            if " (位於" in loc:
                loc = loc.split(" (位於")[0]
            
            # Map type to English
            eq_type = "Significant" if eq['type'] == "顯著有感" else "Local"
            
            md_content.append(
                f"| {eq['id']} | {eq['origin_time']} | {loc} | {eq['magnitude']} | {eq['depth']} | **{eq['max_intensity']}** | {eq_type} |"
            )
    else:
        md_content.append("*No earthquake records available.*")
        
    md_block = "\n".join(md_content)
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_text = f.read()
            
        start_marker = "<!-- EARTHQUAKE_START -->"
        end_marker = "<!-- EARTHQUAKE_END -->"
        
        if start_marker in readme_text and end_marker in readme_text:
            parts = readme_text.split(start_marker)
            before = parts[0]
            after = parts[1].split(end_marker)[1]
            
            new_readme = f"{before}{start_marker}\n\n{md_block}\n\n{end_marker}{after}"
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_readme)
            print("[+] README.md has been automatically updated with the latest earthquake info.")
        else:
            print("[!] Warning: EARTHQUAKE markers not found in README.md. Skipping README update.")
    except Exception as e:
        print(f"[!] Failed to update README.md: {e}")

def main():
    tz_taiwan = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_taiwan)
    print(f"[*] Starting CWA earthquake data fetch at {now.isoformat()} (Taiwan Time)...")
    
    config = get_config()
    if not config:
        print("[!] Execution aborted due to config error.")
        return
        
    api_key = config.get("cwa_api_key")
    if not api_key or api_key == "YOUR_CWA_API_KEY_HERE":
        print("[!] Error: CWA API Key is not configured in config.json.")
        return
        
    output_dir_name = config.get("output_dir", "data")
    data_dir = SCRIPT_DIR / output_dir_name
    
    all_earthquakes = []
    
    sig_raw = fetch_data(DATASET_SIGNIFICANT, api_key)
    if sig_raw:
        sig_list = parse_earthquakes(sig_raw, DATASET_SIGNIFICANT)
        all_earthquakes.extend(sig_list)
        
    small_raw = fetch_data(DATASET_SMALL, api_key)
    if small_raw:
        small_list = parse_earthquakes(small_raw, DATASET_SMALL)
        all_earthquakes.extend(small_list)
        
    if not all_earthquakes:
        print("[!] No data fetched.")
        return
        
    all_earthquakes.sort(key=lambda x: x["origin_time"], reverse=True)
    latest_records = all_earthquakes[:50]
    
    data_dir.mkdir(parents=True, exist_ok=True)
    file_path = data_dir / "earthquake.json"
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(latest_records, f, indent=2, ensure_ascii=False)
        print(f"[+] Earthquake JSON updated: {file_path}")
        
        update_readme(latest_records)
        print("[+] CWA earthquake tracker task executed successfully!")
    except Exception as e:
        print(f"[!] Error parsing or saving data: {e}")

if __name__ == "__main__":
    main()