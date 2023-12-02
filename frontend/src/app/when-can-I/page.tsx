"use client"
import React from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import './Calendar.css';
import Link from 'next/link'; // Import Link from Next.js

const EmptyCalendar = () => {
  const eventSchedule = [
    { date: new Date(2023, 11, 1), time: '10:00 AM', name: 'NU Fair' },
    { date: new Date(2023, 11, 5), time: '2:30 PM', name: 'BPS Game' },
    { date: new Date(2023, 11, 10), time: '2:30 PM', name: 'Lax practice' }
  ];

  return (
    <div className="page-background">
      {/* Header with Home button */}
      <div className="flex justify-between items-center mb-4">
        <Link href="/" passHref>
          <button className="bg-black text-white rounded-full px-4 py-2">Home</button>
        </Link>
        <h1 id="heatmap-label">Carter Fields Events</h1>
      </div>

      <h1 id="page-title">When Can I Play</h1>

      <Calendar
        tileContent={({ date, view }) => {
          if (view === 'month') {
            const day = date.getDate();
            const eventsForDay = eventSchedule.filter(
              (event) => event.date.getDate() === day
            );

            if (eventsForDay.length > 0) {
              return (
                <div className="event-indicator">
                  {eventsForDay.map((event, index) => (
                    <div key={index} className="event">
                      <div>{event.time}</div>
                      <div>{event.name}</div>
                    </div>
                  ))}
                </div>
              );
            }
          }

          return null;
        }}
      />
    </div>
  );
};

export default EmptyCalendar;
