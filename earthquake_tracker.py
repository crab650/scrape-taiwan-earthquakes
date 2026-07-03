#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Taiwan Earthquake Tracker - Core Script
Fetches earthquake reports from the Taiwan Central Weather Administration (CWA) Open Data Platform,
saves it in simplified JSON format, updates README.md, and hosts a dashboard to visualize it.
"""

import os
import ssl
import json
import argparse
import datetime
import urllib.request
import urllib.error
import http.server
import socketserver
import webbrowser
from pathlib import Path

# Get the directory where this script is located
SCRIPT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

# Constants
DEFAULT_CONFIG_FILE = "config.json"
DATASET_SIGNIFICANT = "E-A0015-001"  # 顯著有感地震報告
DATASET_SMALL = "E-A0016-001"        # 小區域有感地震報告
API_URL_TEMPLATE = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/{dataset_id}"

DEFAULT_CONFIG = {
    "cwa_api_key": "YOUR_CWA_API_KEY_HERE",
    "output_dir": "data",
    "datasets": [DATASET_SIGNIFICANT, DATASET_SMALL],
    "server_port": 8800
}

def setup_config():
    """Create default config file if it does not exist."""
    if not os.path.exists(DEFAULT_CONFIG_FILE):
        print(f"[*] Creating default configuration file: {DEFAULT_CONFIG_FILE}")
        with open(DEFAULT_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4, ensure_ascii=False)
        print("[!] Please edit 'config.json' and fill in your Central Weather Administration API key (cwa_api_key).")
        print("[!] You can obtain a free API key at: https://opendata.cwa.gov.tw/")
        return DEFAULT_CONFIG
    
    try:
        with open(DEFAULT_CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error reading config file: {e}")
        return DEFAULT_CONFIG

def get_api_key(config):
    """Retrieve API key from config or environment variable."""
    api_key = os.environ.get("CWA_API_KEY")
    if api_key:
        return api_key
    
    config_key = config.get("cwa_api_key")
    if config_key and config_key != "YOUR_CWA_API_KEY_HERE":
        return config_key
        
    return None

def fetch_data(dataset_id, api_key):
    """Fetch JSON data from CWA Open Data API."""
    url = API_URL_TEMPLATE.format(dataset_id=dataset_id)
    query_url = f"{url}?Authorization={api_key}&format=JSON"
    
    print(f"[*] Fetching dataset '{dataset_id}' from CWA Open Data Platform...")
    
    req = urllib.request.Request(
        query_url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) EarthquakeTracker/1.0'}
    )
    
    try:
        # Avoid SSL cert verification issues on PythonAnywhere
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
    """Map intensity string (e.g. '4強', '5弱', '3級') to a numeric value for sorting/finding max."""
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
    """Calculate the maximum intensity from shaking areas list."""
    if not shaking_areas:
        return "無"
    max_area = max(shaking_areas, key=lambda a: get_intensity_rank(a["intensity"]), default=None)
    return max_area["intensity"] if max_area else "無"

def parse_earthquakes(raw_data, dataset_type):
    """Parses CWA Earthquake JSON into a clean, simplified list format."""
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
        
        # Parse shaking areas
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
                
        # Sort shaking areas by intensity level descending
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

def update_readme(earthquakes, data_dir):
    """Update README.md with the latest earthquake information."""
    readme_path = SCRIPT_DIR / "README.md"
    if not readme_path.exists():
        print("[!] README.md not found. Skipping README update.")
        return
        
    tz_taiwan = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(tz_taiwan)
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Generate Markdown content
    md_content = []
    md_content.append(f"**⏰ Last Updated (Taipei Time)**: `{formatted_time}`\n")
    
    if earthquakes:
        # Show detailed card of the most recent earthquake
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
        
        # Generate Table of Recent Earthquakes
        md_content.append("### 🗺️ Recent 10 Earthquake Records")
        md_content.append("| Report ID | Origin Time | Epicenter Location | Mag | Depth (km) | Max Intensity | Type |")
        md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        
        for eq in earthquakes[:10]:
            # Clean location string to be shorter for table if needed
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

def save_earthquake_json(earthquakes, output_dir):
    """Save earthquake data list to earthquake.json file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / "earthquake.json"
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(earthquakes, f, indent=2, ensure_ascii=False)
        print(f"[+] Earthquake JSON updated: {file_path} (Total: {len(earthquakes)} records)")
        return file_path
    except Exception as e:
        print(f"[!] Failed to save earthquake JSON: {e}")
        return None

def run_fetch_pipeline(config):
    """Main pipeline to fetch, parse, sort and save earthquake data."""
    api_key = get_api_key(config)
    if not api_key:
        print("[!] CWA API Key is missing. Please configure it in config.json or set the CWA_API_KEY environment variable.")
        return False
        
    output_dir = SCRIPT_DIR / config.get("output_dir", "data")
    
    all_earthquakes = []
    
    # 1. Fetch and parse Significant Earthquakes
    sig_raw = fetch_data(DATASET_SIGNIFICANT, api_key)
    if sig_raw:
        sig_list = parse_earthquakes(sig_raw, DATASET_SIGNIFICANT)
        all_earthquakes.extend(sig_list)
        print(f"[+] Loaded {len(sig_list)} significant earthquakes.")
    else:
        print("[!] Warning: Failed to fetch significant earthquakes dataset.")
        
    # 2. Fetch and parse Small-scale Earthquakes
    small_raw = fetch_data(DATASET_SMALL, api_key)
    if small_raw:
        small_list = parse_earthquakes(small_raw, DATASET_SMALL)
        all_earthquakes.extend(small_list)
        print(f"[+] Loaded {len(small_list)} small-scale earthquakes.")
    else:
        print("[!] Warning: Failed to fetch small-scale earthquakes dataset.")
        
    if not all_earthquakes:
        print("[!] Error: No earthquake data could be retrieved. Aborting update.")
        return False
        
    # 3. Sort all earthquakes by OriginTime descending
    all_earthquakes.sort(key=lambda x: x["origin_time"], reverse=True)
    
    # Keep the latest 50 records to prevent file size from blowing up
    latest_records = all_earthquakes[:50]
    
    # 4. Save JSON file
    save_earthquake_json(latest_records, output_dir)
    
    # 5. Update README.md
    update_readme(latest_records, output_dir)
    
    print("[+] Earthquake data pipeline completed successfully!")
    return True

def serve_dashboard(port, output_dir):
    """Start a local web server to display the earthquake dashboard."""
    class DashboardHTTPHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()
            
    socketserver.TCPServer.allow_reuse_address = True
    
    current_port = port
    max_attempts = 20
    httpd = None
    
    for attempt in range(max_attempts):
        try:
            httpd = socketserver.TCPServer(("", current_port), DashboardHTTPHandler)
            break
        except OSError as e:
            if "already in use" in str(e) or getattr(e, 'errno', None) in (98, 10048):
                print(f"[!] Port {current_port} is already in use. Trying port {current_port + 1}...")
                current_port += 1
            else:
                print(f"[!] Socket error: {e}")
                return
                
    if not httpd:
        print(f"[!] Failed to find an open port after {max_attempts} attempts.")
        return
        
    try:
        with httpd:
            print(f"[+] Dashboard is live!")
            print(f"[*] Opening browser to http://localhost:{current_port}/index.html ...")
            webbrowser.open(f"http://localhost:{current_port}/index.html")
            print("[*] Press Ctrl+C to stop the server.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")
    except Exception as e:
        print(f"[!] Failed to run dashboard server: {e}")

def main():
    parser = argparse.ArgumentParser(description="Taiwan Earthquake Tracker CLI")
    parser.add_argument("--fetch", action="store_true", help="Fetch latest earthquake data from CWA API")
    parser.add_argument("--serve", action="store_true", help="Start the dashboard local web server")
    parser.add_argument("--port", type=int, default=None, help="Dashboard port (default from config or 8800)")
    parser.add_argument("--setup", action="store_true", help="Initialize or fix config.json")
    
    args = parser.parse_args()
    
    # Initialize configuration
    config = setup_config()
    
    if args.setup:
        print("[+] Setup complete. Please configure config.json before running.")
        return
        
    action_taken = False
    
    if args.fetch:
        action_taken = True
        run_fetch_pipeline(config)
        
    if args.serve:
        action_taken = True
        port = args.port or config.get("server_port", 8800)
        output_dir = config.get("output_dir", "data")
        serve_dashboard(port, output_dir)
        
    if not action_taken:
        # Default behavior: run fetch, then exit.
        print("[*] No action specified. Running earthquake data fetch pipeline...")
        success = run_fetch_pipeline(config)
        if success:
            print("\n[*] Tip: Run 'python earthquake_tracker.py --serve' to view the visual dashboard!")
            print("[*] Tip: Edit config.json to supply your CWA Open Data API key.")

if __name__ == "__main__":
    main()
