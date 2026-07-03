// Taiwan Earthquake Tracker - Dashboard Logic

document.addEventListener('DOMContentLoaded', () => {
    // API data endpoint
    const DATA_URL = 'data/earthquake.json';
    
    // Application State
    let earthquakes = [];
    let filteredEarthquakes = [];
    let selectedId = null;
    
    // Filters State
    let searchQuery = '';
    let magFilter = 'all';
    let typeFilter = 'all';

    // DOM Elements
    const searchInput = document.getElementById('search-input');
    const magFilterContainer = document.getElementById('magnitude-filter');
    const typeFilterContainer = document.getElementById('type-filter');
    
    const listContainer = document.getElementById('earthquake-list');
    const listCountBadge = document.getElementById('list-count');
    
    const selectPrompt = document.getElementById('select-prompt');
    const detailContent = document.getElementById('detail-content');
    
    // Statistics Elements
    const statTotal = document.getElementById('stat-total');
    const statSig = document.getElementById('stat-sig');
    const statMaxMag = document.getElementById('stat-max-mag');
    const statMinDepth = document.getElementById('stat-min-depth');
    const updateTimeEl = document.getElementById('update-time');

    // Detail Panel Elements
    const detType = document.getElementById('det-type');
    const detId = document.getElementById('det-id');
    const detLocation = document.getElementById('det-location');
    const detTime = document.getElementById('det-time');
    const detMagnitude = document.getElementById('det-magnitude');
    const detDepth = document.getElementById('det-depth');
    const detMaxIntensity = document.getElementById('det-max-intensity');
    const detReportContent = document.getElementById('det-report-content');
    const detIntensities = document.getElementById('det-intensities');
    const detImage = document.getElementById('det-image');
    const detWebLink = document.getElementById('det-web-link');

    // Initialize application
    init();

    async function init() {
        setupEventListeners();
        await fetchEarthquakeData();
    }

    // Set up sidebar filter change and card click events
    function setupEventListeners() {
        // Search Input filter
        searchInput.addEventListener('input', (e) => {
            searchQuery = e.target.value.trim().toLowerCase();
            applyFilters();
        });

        // Magnitude filter buttons
        magFilterContainer.addEventListener('click', (e) => {
            if (e.target.classList.contains('filter-btn')) {
                // Update active state
                magFilterContainer.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
                e.target.classList.add('active');
                
                magFilter = e.target.dataset.mag;
                applyFilters();
            }
        });

        // Type filter buttons
        typeFilterContainer.addEventListener('click', (e) => {
            if (e.target.classList.contains('filter-btn')) {
                // Update active state
                typeFilterContainer.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
                e.target.classList.add('active');
                
                typeFilter = e.target.dataset.type;
                applyFilters();
            }
        });
    }

    // Fetch simplified JSON data from the server
    async function fetchEarthquakeData() {
        try {
            showLoading(true);
            const response = await fetch(DATA_URL);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            earthquakes = await response.json();
            filteredEarthquakes = [...earthquakes];
            
            showLoading(false);
            calculateStats();
            renderList();
            
            // Auto-select the first (latest) earthquake
            if (earthquakes.length > 0) {
                selectEarthquake(earthquakes[0].id);
            }
            
        } catch (error) {
            console.error('Failed to load earthquake data:', error);
            showError();
        }
    }

    // Calculate metadata/statistics from the loaded dataset
    function calculateStats() {
        if (!earthquakes.length) return;
        
        statTotal.textContent = earthquakes.length;
        
        const sigCount = earthquakes.filter(eq => eq.type === '顯著有感').length;
        statSig.textContent = sigCount;
        
        const magnitudes = earthquakes.map(eq => parseFloat(eq.magnitude) || 0);
        const maxMag = Math.max(...magnitudes);
        statMaxMag.textContent = maxMag.toFixed(1);
        
        const depths = earthquakes.map(eq => parseFloat(eq.depth) || 9999);
        const minDepth = Math.min(...depths);
        statMinDepth.textContent = minDepth === 9999 ? '-' : `${minDepth} km`;
        
        // Show current client fetch time as update time, or first earthquake's time
        const now = new Date();
        updateTimeEl.textContent = now.toLocaleTimeString('zh-TW', { hour12: false });
    }

    // Filter earthquakes based on active filters
    function applyFilters() {
        filteredEarthquakes = earthquakes.filter(eq => {
            // 1. Search Query filter (matches location or report content)
            const matchesSearch = eq.epicenter.location.toLowerCase().includes(searchQuery) || 
                                  eq.report_content.toLowerCase().includes(searchQuery) ||
                                  eq.id.includes(searchQuery);
                                  
            // 2. Magnitude filter
            let matchesMag = true;
            const mag = parseFloat(eq.magnitude) || 0;
            if (magFilter === '5') {
                matchesMag = mag >= 5.0;
            } else if (magFilter === '4') {
                matchesMag = mag >= 4.0 && mag < 5.0;
            } else if (magFilter === '3') {
                matchesMag = mag < 4.0;
            }
            
            // 3. Type filter
            const matchesType = typeFilter === 'all' || eq.type === typeFilter;
            
            return matchesSearch && matchesMag && matchesType;
        });
        
        renderList();
        
        // If the selected earthquake is no longer in the filtered list, hide the detail panel
        if (selectedId && !filteredEarthquakes.some(eq => eq.id === selectedId)) {
            clearSelection();
        }
    }

    // Render list of cards on the left panel
    function renderList() {
        listContainer.innerHTML = '';
        listCountBadge.textContent = `顯示 ${filteredEarthquakes.length} 筆`;
        
        if (filteredEarthquakes.length === 0) {
            listContainer.innerHTML = `
                <div class="error-state">
                    <i class="fa-solid fa-magnifying-glass-minus"></i>
                    <p>沒有符合篩選條件的地震紀錄</p>
                </div>
            `;
            return;
        }
        
        filteredEarthquakes.forEach(eq => {
            const card = document.createElement('div');
            card.className = `earthquake-card ${eq.id === selectedId ? 'selected' : ''}`;
            card.dataset.id = eq.id;
            
            // Determine severity class for magnitude badge
            const mag = parseFloat(eq.magnitude) || 0;
            let severityClass = 'mag-low';
            if (mag >= 5.5) {
                severityClass = 'mag-high';
            } else if (mag >= 4.0) {
                severityClass = 'mag-med';
            }
            
            // Format short time: "07-03 13:00"
            const shortTime = eq.origin_time ? eq.origin_time.substring(5, 16) : '未知時間';
            
            // Clean location text for display in card list
            let displayLocation = eq.epicenter.location;
            if (displayLocation.includes(' (位於')) {
                displayLocation = displayLocation.split(' (位於')[0];
            }
            
            const tagClass = eq.type === '顯著有感' ? 'tag-sig' : 'tag-small';
            
            card.innerHTML = `
                <div class="magnitude-badge ${severityClass}">${mag.toFixed(1)}</div>
                <div class="card-info">
                    <div class="card-title-row">
                        <span class="card-location">${displayLocation}</span>
                        <span class="tag ${tagClass}">${eq.type}</span>
                    </div>
                    <div class="card-meta-row">
                        <span class="card-time"><i class="fa-regular fa-clock"></i> ${shortTime}</span>
                        <div class="card-tags">
                            <span class="tag tag-intensity">深 ${eq.depth}km</span>
                            <span class="tag tag-intensity">震度 ${eq.max_intensity}</span>
                        </div>
                    </div>
                </div>
            `;
            
            card.addEventListener('click', () => selectEarthquake(eq.id));
            listContainer.appendChild(card);
        });
    }

    // Highlight a selected card and show its details in the right panel
    function selectEarthquake(id) {
        selectedId = id;
        
        // Highlight active card
        const cards = listContainer.querySelectorAll('.earthquake-card');
        cards.forEach(card => {
            if (card.dataset.id === id) {
                card.classList.add('selected');
            } else {
                card.classList.remove('selected');
            }
        });
        
        // Show detail panel
        const eq = earthquakes.find(item => item.id === id);
        if (!eq) return;
        
        selectPrompt.classList.add('hidden');
        detailContent.classList.remove('hidden');
        
        // Populate text content
        detType.textContent = `${eq.type}地震報告`;
        detType.className = `badge-type ${eq.type === '顯著有感' ? 'tag-sig' : 'tag-small'}`;
        detId.textContent = `報告編號：${eq.id}`;
        detLocation.textContent = eq.epicenter.location;
        detTime.textContent = `${eq.origin_time} (台北時間)`;
        
        detMagnitude.textContent = parseFloat(eq.magnitude).toFixed(1) || '0.0';
        detDepth.textContent = eq.depth || '-';
        detMaxIntensity.textContent = eq.max_intensity || '無';
        
        detReportContent.textContent = eq.report_content || '無報告內容說明。';
        
        // Handle image loading with error fallback
        if (eq.report_image) {
            detImage.src = eq.report_image;
            detImage.style.display = 'block';
        } else {
            detImage.src = 'https://placehold.co/600x400?text=No+Earthquake+Image';
        }
        
        // Web Link Setup
        if (eq.web_link) {
            detWebLink.href = eq.web_link;
            detWebLink.style.display = 'inline-flex';
        } else {
            detWebLink.style.display = 'none';
        }
        
        // Render shaking area intensity badges
        renderIntensities(eq.shaking_areas);
    }

    // Render intensity cards in the detail block
    function renderIntensities(areas) {
        detIntensities.innerHTML = '';
        
        if (!areas || areas.length === 0) {
            detIntensities.innerHTML = '<p class="text-secondary">無感地區或未提供震度資料。</p>';
            return;
        }
        
        areas.forEach(area => {
            const card = document.createElement('div');
            card.className = 'intensity-area-card';
            
            // Map Intensity level to specific class name: int-4, int-5弱 etc.
            const rawIntensity = area.intensity;
            const intClass = `int-${rawIntensity}`;
            
            card.innerHTML = `
                <span class="intensity-area-name">${area.area_name}</span>
                <span class="intensity-badge ${intClass}">${rawIntensity}</span>
            `;
            detIntensities.appendChild(card);
        });
    }

    // Clear selection and return to prompt view
    function clearSelection() {
        selectedId = null;
        selectPrompt.classList.remove('hidden');
        detailContent.classList.add('hidden');
    }

    // UI Helpers: Show Loading/Error States
    function showLoading(isLoading) {
        if (isLoading) {
            listContainer.innerHTML = `
                <div class="loading-state">
                    <i class="fa-solid fa-circle-notch fa-spin"></i>
                    <p>載入地震報告中...</p>
                </div>
            `;
        }
    }

    function showError() {
        listContainer.innerHTML = `
            <div class="error-state">
                <i class="fa-solid fa-triangle-exclamation"></i>
                <p>資料載入失敗！請確認 CWA API 金鑰是否配置正確，且已在本機抓取最新資料。</p>
                <button class="filter-btn" onclick="location.reload()" style="margin-top: 10px;">重新整理</button>
            </div>
        `;
    }
});
