# Shopify CRO Auditor

An AI-powered Shopify **Conversion Rate Optimization (CRO) Auditor** that automatically analyzes Shopify storefronts, extracts UX and merchandising signals, audits product pages, captures visual evidence, and generates actionable CRO recommendations with downloadable PDF reports.

The application combines **Playwright**, **FastAPI**, and **React** to automate the manual CRO auditing process typically performed by e-commerce consultants.

---

## ✨ Features

### Homepage Analysis

- Hero Section Detection
- Hero CTA Detection
- Hero Subheading Extraction
- Search Availability Detection
- Account, Wishlist & Cart Detection
- Announcement Bar Detection
- Footer Detection
- Newsletter Detection
- Featured Collection Extraction
- Homepage Trust Signal Detection

### Product Page Analysis

- Product Title
- Price Detection
- Discount Detection
- Rating Detection
- Review Count
- Product Images
- Add To Cart Detection
- Sticky Add To Cart Detection
- Shipping Information
- Returns Information
- Size Guide Detection
- Breadcrumb Detection
- Variant Detection
- Trust Badge Detection

### CRO Intelligence

- Overall CRO Score
- Rule-based Recommendation Engine
- Experiment Suggestions
- Impact / Confidence / Effort Scoring
- Evidence-backed Recommendations

### Reporting

- Screenshot Capture
- Homepage Screenshot
- Product Page Screenshots
- Downloadable PDF Report

---

# 🏗 Architecture

```
                 Shopify Store
                        │
                        ▼
              Playwright Browser
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Homepage Extractor              Product Discovery
                                        │
                                        ▼
                               PDP Extractor
                                        │
                                        ▼
                         Recommendation Engine
                                        │
                                        ▼
                              PDF Report Generator
                                        │
                                        ▼
                             React Dashboard
```

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Playwright
- Pydantic
- BeautifulSoup
- ReportLab
- Python 3.11

## Frontend

- React
- TypeScript
- Vite
- TailwindCSS
- Framer Motion
- Axios
- Lucide Icons

## Development Tools

- VS Code
- Git
- npm
- uvicorn

---

# 📂 Project Structure

```
ShopifyCRO/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── crawler/
│   │   ├── extractors/
│   │   ├── models/
│   │   ├── services/
│   │   └── utils/
│   ├── screenshots/
│   ├── requirements.txt
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── dashboard/
│   │   ├── hero/
│   │   ├── hooks/
│   │   ├── layout/
│   │   ├── pages/
│   │   ├── services/
│   │   └── types/
│   └── package.json
│
└── README.md
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone <repository-url>

cd ShopifyCRO
```

## Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright Browser

```bash
playwright install chromium
```

Run Backend

```bash
uvicorn main:app
```

Backend runs at

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# 📊 How It Works

1. Enter any Shopify Store URL.
2. Playwright launches a Chromium browser.
3. Homepage is analyzed.
4. Product pages are automatically discovered.
5. Multiple product pages are crawled.
6. CRO evidence is extracted.
7. Recommendation Engine evaluates multiple CRO heuristics.
8. Screenshots are captured.
9. PDF report is generated.
10. Dashboard visualizes the audit.

---

# 🧠 Recommendation Engine

The recommendation engine evaluates multiple CRO heuristics across homepage and product pages.

Current evaluation rules include:

- Search Availability
- Announcement Bar
- Featured Collections
- Homepage Trust Signals
- Newsletter
- Footer
- Add To Cart
- Sticky Add To Cart
- Product Reviews
- Product Images
- Product Variants
- Shipping Information
- Returns Information
- Size Guide
- Trust Badges

Each recommendation includes:

- Evidence
- Impact Score
- Confidence Score
- Implementation Effort
- Suggested Experiment
- Primary Success Metric

---

# 📄 PDF Report

Each analysis automatically generates a downloadable PDF containing:

- Overall CRO Score
- Homepage Summary
- Product Summary
- CRO Recommendations
- Evidence
- Suggested Experiments

---

# 📸 Screenshot Evidence

Every analysis creates a unique analysis directory containing:

```
screenshots/

└── analysis-id/
    ├── homepage.png
    ├── product_1.png
    ├── product_2.png
    ├── ...
    ├── product_10.png
    └── report.pdf
```

This allows every audit to preserve its visual evidence independently.

---

# ⚡ Future Improvements

- AI-powered recommendations using Large Language Models
- Competitor Benchmarking
- Category-wise Product Sampling
- Google Analytics Integration
- Heatmap Integration
- Shopify App Deployment
- Multi-page Homepage Analysis
- Collection Page Analysis
- Checkout Flow Analysis
- Accessibility Audit
- SEO Audit
- Performance Audit
- Mobile-specific CRO Analysis

---

# 📌 Design Decisions

- Playwright is used instead of HTTP scraping to support JavaScript-rendered Shopify storefronts.
- Product discovery uses representative sampling to balance audit quality with execution time.
- Rule-based recommendations ensure deterministic and explainable outputs.
- Each audit stores screenshots in a unique analysis directory to preserve evidence.
- PDF reports provide portable audit summaries suitable for sharing with stakeholders.

---

# ⚠ Current Limitations

- Optimized primarily for Shopify storefronts.
- Recommendation engine is rule-based rather than AI-driven.
- Product sampling is limited for faster execution.
- Checkout flow is intentionally excluded.
- Dynamic content may vary across highly customized themes.

---

# 👨‍💻 Author

**Piyush Arora**

B.Tech Information Technology  
IIIT Una

GitHub: https://github.com/Piyusharora04

LinkedIn: https://linkedin.com/in/piyush-arora-363a59265

---

# 📜 License

This project is developed as part of a Software Engineering assignment and is intended for educational and demonstration purposes.

MIT License.

