# DAS732: Data Visualization — Assignment 2 (A2)
**International Institute of Information Technology, Bangalore (IIITB)**  
*Term 1 (2026–27)*

---

## 👥 Team & Contributions

| Team Member | SciVis Task | InfoVis Task |
| :--- | :--- | :--- |
| **Sahasra** | **Contour Mapping**: Marching Squares / contour fill, global vs. local scaling, level count variations, scalar field animations | **Horizon & Ridgeline Plots**: Time-series horizon plots (bands, normalization) and group-wise ridgeline distributions |
| **Dayanithaa** | **Color Mapping**: Continuous, discrete, and logarithmic colormaps; sequential vs. diverging palettes; global vs. local extremes | **Browser Visualizations (D3.js)**: Parallel Coordinates with edge bundling & Zoomable Treemap visualizations |
| **Ashwini B Takalikar** | **Quiver Plots**: Wind vector field (`vs`, `th`), grid sampling strategies (stride vs. coarsen), vector magnitude scaling, temporal animations | **Node-Link Diagrams**: Network construction (k-NN), comparison of 3 graph layouts (Spring, Kamada-Kawai, Tutte) and UI interactions |

---

## 🌐 Interactive Web Visualizations (Live Demos)

The interactive JavaScript / D3 browser visualizations are deployed on GitHub Pages:

1. **Parallel Coordinates Plot with Edge Bundling**:  
   🔗 **[https://dayanithaa.github.io/DataVis-ParallelCoord/](https://dayanithaa.github.io/DataVis-ParallelCoord/)**  
   *Features: Interactive axis reordering, multi-axis brushing/filtering, B-spline edge bundling tension control, and dataset switching (Road Infrastructure vs. Weather attributes).*

2. **Zoomable Treemap Visualizations**:  
   🔗 **[https://dayanithaa.github.io/TreeMaps/](https://dayanithaa.github.io/TreeMaps/)**  
   *Features: Hierarchical zoom-in/zoom-out interactions, breadcrumb navigation, dynamic dataset remodeling (`State → City`, `State → Severity`, `Day/Night → Severity`), and tooltip statistics.*

---

## 📂 Repository Directory Structure

```text
datavisualization2/
├── .gitignore                          # Excludes large raw data files (*.nc, *.zip, checkpoints)
├── README.md                           # Assignment implementation guide and documentation
│
├── Colourmaps/                         # SciVis Task 1: Color Mapping
│   ├── dvasn2-colour-mapping.ipynb     # Implementation notebook for colormap experiments
│   └── *.png                           # Output plots (global/local, discrete/continuous, anomalies)
│
├── Contourplots/                       # SciVis Task 2: Contour Mapping
│   ├── contourplots_fixed2.ipynb       # Marching Squares & contour fill implementation
│   ├── figures/                        # High-resolution comparison figures
│   ├── final_contours/                 # Contour maps across time instances
│   ├── seasonal_*/                     # Seasonal variations (tmax, tmin, rmax, dtr, vpd)
│   ├── tmmx_global_scale.gif           # Temporal animation using global scale
│   └── tmmx_local_scale.gif            # Temporal animation using local scale
│
├── Quiver plots/                       # SciVis Task 3: Quiver Plots
│   ├── quiverplot.ipynb                # Quiver plot generation and sampling comparison
│   ├── Wind_biweekly_mean.png          # Biweekly wind vector field
│   └── wind.gif                        # Temporal quiver field animation
│
├── Node-link Diagrams/                 # InfoVis Task 1: Network Visualizations
│   ├── Buildgraph.ipynb                # k-NN network construction from US Accidents data
│   ├── graphLayout.ipynb               # Graph layout algorithms & analysis
│   └── accidents_network_*.png         # Layout comparisons (Spring, Kamada-Kawai, Tutte) & UI captures
│
├── Parallel_coordinates/               # InfoVis Task 2a: Parallel Coordinates
│   ├── index.html                      # Standalone interactive D3 web visualization
│   ├── parallel_coordinates.html       # D3 markup and interaction logic
│   ├── build.py                        # Bundles CSV data directly into standalone HTML
│   ├── road_parallel.csv               # Sampled road infrastructure dataset (10,000 samples)
│   ├── weather_parallel.csv            # Normalized weather dataset (15,000 samples)
│   ├── parallel-coordinates.ipynb      # Data preprocessing notebook
│   └── *.png                           # Screenshots of bundling & axis ordering experiments
│
├── TreeMaps/                           # InfoVis Task 2b: Zoomable Treemaps
│   ├── index.html                      # Interactive D3 zoomable treemap web application
│   ├── accidents_state_city.json       # Remodel 1: Hierarchy by State -> City
│   ├── accidents_state_severity.json   # Remodel 2: Hierarchy by State -> Severity
│   ├── accidents_day_night_severity.json # Remodel 3: Hierarchy by Day/Night -> Severity
│   ├── treemaps.ipynb                  # Data transformation and tree remodel notebook
│   └── *.png                           # High-resolution screenshots of treemap states & zooms
│
└── Horizon and Ridge plots/            # InfoVis Task 3: Horizon & Ridgeline Plots
    ├── horizonandridgefinal (1).ipynb  # Implementation notebook for horizon and ridge plots
    └── horizon and ridgeplots/         # Output visualizations across bands, baselines & distributions
```

---

## 📊 Datasets

### 1. SciVis: gridMET Meteorological Dataset
- **Source**: [https://www.climatologylab.org/gridmet.html](https://www.climatologylab.org/gridmet.html)
- **Time Slice**: July 1, 2021 – September 30, 2021 (Contiguous 3-month summer quarter).
- **Variables**:
  - `tmmx` (Daily Maximum Temperature, K)
  - `tmmn` (Daily Minimum Temperature, K)
  - `vs` (Wind Speed at 10 m, m/s)
  - `th` (Wind Direction at 10 m, degrees clockwise from north)
  - `srad` (Surface Downwelling Solar Radiation, W/m²)
  - `pr` (Precipitation Amount, mm)
  - `rmax` / `rmin` (Maximum / Minimum Relative Humidity, %)
- *Note*: NetCDF data files (`*.nc`) exceed GitHub's file size limits (>100 MB) and are excluded from the repository via `.gitignore`. Download the 2021 NetCDF files from gridMET and place them in `Contourplots/data/` or reference local paths to run from scratch.

### 2. InfoVis: US Accidents Dataset (2016–2023)
- **Source**: Kaggle US Accidents Dataset (Moosavi et al.).
- **Attributes Used**: `Severity`, `State`, `City`, `Start_Lat`, `Start_Lng`, `Civil_Twilight`, `Temperature(F)`, `Visibility(mi)`, `Precipitation(in)`, `Wind_Speed(mph)`, `Humidity(%)`, `Bump`, `Crossing`, `Junction`, `Traffic_Signal`.
- The sampled and preprocessed data files (`road_parallel.csv`, `weather_parallel.csv`, and JSON hierarchies) are included directly in the repository for immediate execution.

---

## 🔬 Implementation Highlights

### SciVis Tasks
1. **Color Mapping (`Colourmaps/`)**:
   - Experimentation with continuous, discrete, and logarithmic scales across different colormaps (`coolwarm`, `plasma`, `viridis`, `magma`).
   - Comparison of global vs. local min/max parametric mappings to study seasonal temperature variations and anomalous precipitation events.
2. **Contour Mapping (`Contourplots/`)**:
   - Utilizes Marching Squares / contour fill algorithms (`plt.contour` and `plt.contourf`).
   - Evaluated 5, 10, 15, and 20 iso-levels, quantile vs. equal-width intervals, and spatial Gaussian smoothing.
   - Generated temporal animation GIFs (`tmmx_global_scale.gif`, `tmmx_local_scale.gif`) over 10 sampled time steps.
3. **Quiver Plots (`Quiver plots/`)**:
   - Computes Cartesian wind vector components: $u = -vs \cdot \sin(th)$, $v = -vs \cdot \cos(th)$.
   - Compares spatial subsampling techniques (striding vs. area coarsening) and magnitude-proportional arrows.

### InfoVis Tasks
1. **Node-Link Network Diagrams (`Node-link Diagrams/`)**:
   - Built a spatial adjacency graph using k-Nearest Neighbors ($k=4$) on accident coordinates.
   - Compared 3 layout algorithms: Spring (Fruchterman-Reingold force-directed), Kamada-Kawai (path-distance spring), and Tutte (barycentric convex layout).
2. **Browser Visualizations (`Parallel_coordinates/` & `TreeMaps/`)**:
   - **Parallel Coordinates**: Implemented in D3.js with cubic B-spline curves, interactive edge bundling tension control, axis reordering via drag-and-drop, and multi-axis range brushing.
   - **Zoomable Treemaps**: Hierarchical tree transformation with squarified and slice-and-dice layouts, color-coded by accident severity, with smooth click-to-zoom transitions.
3. **Horizon and Ridgeline Plots (`Horizon and Ridge plots/`)**:
   - **Horizon Plots**: 2, 4, and 6 band variations; evaluated raw counts, relative index, and detrended anomaly baselines.
   - **Ridgeline Plots**: Kernel Density Estimation with varying bandwidths ($h = 0.2, 0.4, 0.8$), analyzing accident density across time of day, seasons, and visibility thresholds.

---

## 🚀 How to Run

### 1. Python Notebooks
Ensure you have Python 3.9+ installed with the following packages:
```bash
pip install numpy pandas matplotlib seaborn xarray netcdf4 networkx scikit-learn scipy pillow
```
Launch Jupyter Notebook or Jupyter Lab:
```bash
jupyter lab
```
Navigate to any subfolder (`Colourmaps/`, `Contourplots/`, `Node-link Diagrams/`, `Horizon and Ridge plots/`, etc.) and execute the cells.

### 2. Interactive Web Visualizations (Local)
You can directly open the deployed links above, or view them locally:
- **Parallel Coordinates**:
  ```bash
  cd Parallel_coordinates
  python -m http.server 8000
  ```
  Open `http://localhost:8000/index.html` (or `parallel_coordinates.html`).
- **TreeMaps**:
  ```bash
  cd TreeMaps
  python -m http.server 8000
  ```
  Open `http://localhost:8000/index.html`.
