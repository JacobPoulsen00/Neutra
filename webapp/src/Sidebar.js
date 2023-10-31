import React from 'react';
import './Sidebar.css'; // Assuming you have a CSS file for styling

const Sidebar = () => {
    return (
        <div className="sidebar">
            <div className="profile-pic">
                <img src="/default-profile-pic.png" alt="Profile" />
            </div>
            <div className="navigation">
                <ul>
                    <li><i className="icon-cloud"></i> Analyze</li>
                    <li><i className="icon-shared"></i> History</li>
                    <li><i className="icon-settings"></i> Settings</li>
                    <li><i className="icon-logout"></i> Log out</li>
                </ul>
            </div>
        </div>
    );
}

export default Sidebar;
