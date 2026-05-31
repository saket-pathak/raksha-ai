# 💻 Raksha AI - Frontend Application

This is the React Single Page Application (SPA) frontend for **Raksha AI**, scaffolded using **Vite**. It provides citizens with a premium, responsive, dark-mode dashboard to report road hazards, review route risk indices, configure preferences, and trigger instant SOS rescues in multiple languages.

---

## 🎨 Technology Stack

- **Framework**: [React 18](https://react.dev/)
- **Build Tool**: [Vite](https://vitejs.dev/)
- **Routing**: [React Router DOM v6](https://reactrouter.com/)
- **Mapping**: [Leaflet](https://leafletjs.com/) for interactive maps
- **Localization**: [i18next](https://www.i18next.com/) & [react-i18next](https://react.i18next.com/)
- **Styling**: Modern, responsive Custom CSS with premium dark-mode gradients and micro-animations.

---

## 🌐 Multilingual Setup (i18n)

The application supports real-time translation and locale formatting for English, Hindi, Tamil, Telugu, Kannada, and Malayalam.

### Localization Structure
```
frontend/src/
├── i18n/
│   ├── config.js               # Initializer for i18next
│   └── locales/                # JSON dictionaries for each language
│       ├── en/translation.json
│       ├── hi/translation.json
│       ├── ta/translation.json
│       ├── te/translation.json
│       ├── kn/translation.json
│       └── ml/translation.json
├── context/
│   └── LanguageContext.jsx     # Handles language states across views
└── hooks/
    └── useLocalization.js      # Utility hook for date/currency formatting
```

### Key Utilities
- **`useTranslation`**: Standard hook from `react-i18next` for translation interpolation (e.g., `t('key')`).
- **`useLocalization`**: Returns the active locale, and formatting utilities such as `formatDate(date)`, `formatNumber(number)`, and standard currency signs (₹).

---

## 📁 Pages Tree

- **Home (`/`)**: Main landing page with safety mission and core actions.
- **Dashboard (`/dashboard`)**: Tactical command center showing active incident stats, heatmaps, recent reports, and live alert streams via SSE.
- **Report Issue (`/report-issue`)**: Form to upload photos, input coordinates (or select on Leaflet map), and trigger AI validation.
- **Risk Alert (`/risk-alert`)**: Interactive tool to evaluate coordinates or profile entire travel routes for hazard scores.
- **SOS Page (`/sos`)**: Emergency distress center with custom note setup and instant location logging.
- **Status Checker (`/status`)**: Form to track details of reported road issues.
- **Login (`/login`)**: Secure login page for user and administrative privileges.
- **Admin Panel (`/admin`)**: Operations center to manage, verify, and resolve reported road issues.

---

## ⚙️ Environment Variables

Create a `.env` file in the `frontend/` directory to configure the application during development:

```env
# Backend API Base URL
VITE_APP_API_BASE_URL=http://127.0.0.1:5000

# Firebase configurations (optional)
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your_project_id
```

---

## 🚀 Scripts & Command Reference

From the `frontend/` directory:

### Install dependencies
```bash
npm install
```

### Start development server
Runs a local development server on Port 3000 (configured in `vite.config.js`):
```bash
npm run dev
```

### Build for production
Compiles optimized assets to the `dist/` directory:
```bash
npm run build
```

### Preview production build
Launches a server to view the built production package:
```bash
npm run preview
```
