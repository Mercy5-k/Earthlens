import React from "react";
import { useNavigate } from "react-router-dom";
import "./Sidebar.css";


const Sidebar = () => {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <aside className="sidebar">
      <div className="sidebar-logo">
        <img src="/logo.png" alt="App Logo" className="logo-img" /> 
        <p className="brand-name">EARTH<br />LENS</p>
      </div>

      <button onClick={() => navigate("/dashboard")} className="sidebar-btn">Dashboard</button>
      <button onClick={() => navigate("/report")} className="sidebar-btn">Report</button>
      <button onClick={() => navigate("/my-reports")} className="sidebar-btn">My Reports</button>
      <button onClick={() => navigate("/green-actions")} className="sidebar-btn">Green Action</button>
      <button onClick={() => navigate("/profile")} className="sidebar-btn">Profile</button>

      <button onClick={logout} className="sign-out-btn">Sign out</button>
    </aside>
  );
};

export default Sidebar;
