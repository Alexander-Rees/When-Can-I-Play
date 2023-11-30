// Calendar.js
import React from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import './Calendar.css'; // Import your custom CSS file

const EmptyCalendar = () => {
  return (
    <div>
      <h1 id="page-title">When Can I Play</h1>
      <h1 >id="heatmap-label" Activity Heatmap</h1>
      <Calendar />
    </div>
  );
};

export default EmptyCalendar;