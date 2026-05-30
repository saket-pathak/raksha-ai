import { Routes, Route, useNavigate } from 'react-router-dom';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import ReportIssue from './pages/ReportIssue';
import RiskAlert from './pages/RiskAlert';
import SOSPage from './pages/SOSPage';
import LegalInfo from './pages/LegalInfo';
import LoginPage from './pages/LoginPage';
import AdminPage from './pages/AdminPage';
import CheckStatus from './pages/CheckStatus';
import { LanguageProvider } from './context/LanguageContext';

export default function App() {
  return (
    <LanguageProvider>
      <style>{`
        body { margin: 0; padding: 0; background-color: #060810; }
        *, *::before, *::after { box-sizing: border-box; }
      `}</style>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/report-issue" element={<ReportIssue />} />
        <Route path="/risk-alert" element={<RiskAlert />} />
        <Route path="/sos" element={<SOSPage />} />
        <Route path="/legal-info" element={<LegalInfo />} />
        <Route path="/status" element={<CheckStatus />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="*" element={<Home />} />
      </Routes>
    </LanguageProvider>
  );
}
