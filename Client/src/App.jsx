import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useLocation,
  Outlet,
  Navigate
} from "react-router-dom";

import Navbar from "./components/Navbar/Navbar.jsx";
import Footer from "./components/Footer/Footer.jsx";
import Sidebar from "./components/Sidebar/Sidebar";

import Report from "./pages/Report.jsx";
import GreenActions from "./pages/GreenActions.jsx";
import Dashboard from "./pages/Dashboard.jsx";
import About from "./pages/About.jsx";
import LandingPage from "./pages/LandingPage.jsx";
import Signup from "./pages/Signup.jsx";
import Login from "./pages/Login.jsx";
import MyReportspage from "./pages/MyReportspage.jsx";
import Profile from "./pages/Profile.jsx";
import Contact from "./pages/Contact.jsx";


const DashboardLayout = () => (
  <div style={{ display: "flex", minHeight: "100vh" }}>
    <Sidebar />
    <div style={{ flex: 1, padding: "20px" }}>
      <Outlet />
    </div>
  </div>
);

const AppContent = () => {
  const location = useLocation();
  const isAuthenticated = !!localStorage.getItem("token");

 
  const showFooterPages = ["/", "/about", "/contact", "/green-actions"];
  const shouldShowFooter = showFooterPages.includes(location.pathname);

 
  const hideNavbarPages = ["/dashboard", "/report", "/my-reports", "/profile"];
  const shouldShowNavbar = !hideNavbarPages.includes(location.pathname);

  return (
    <div className="app-container">
      {shouldShowNavbar && <Navbar />}

      <main className="main-content">
        <Routes>

        
          <Route path="/" element={<LandingPage />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/join" element={<Signup />} />
          <Route path="/login" element={<Login />} />

          
          <Route
            path="/green-actions"
            element={isAuthenticated ? <GreenActions /> : <Navigate to="/login" />}
          />

    
          <Route element={<DashboardLayout />}>
            <Route
              path="/dashboard"
              element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />}
            />
            <Route
              path="/report"
              element={isAuthenticated ? <Report /> : <Navigate to="/login" />}
            />
            <Route
              path="/my-reports"
              element={isAuthenticated ? <MyReportspage /> : <Navigate to="/login" />}
            />
            <Route
              path="/profile"
              element={isAuthenticated ? <Profile /> : <Navigate to="/login" />}
            />
          </Route>

        </Routes>
      </main>

      {shouldShowFooter && <Footer />}
    </div>
  );
};

const App = () => (
  <Router>
    <AppContent />
  </Router>
);

export default App;