"use client"

import axios from 'axios';
import Image from 'next/image'
import Link from 'next/link'
import { useEffect, useState } from 'react';

export default function Home() {
  // Mock data
  const mockData = {
    "use client": [
      { name: 'Carter 2B', event: 'Soccer Practice', group: 'Youth Team', timeTill: '4:30pm' },
      { name: 'Carter 2B', event: 'Lacrosse Practice', group: 'High School Girls', timeTill: '3:30pm' },
      { name: 'Carter 2A', event: 'Community Soccer Match', group: 'Open', timeTill: '2:15pm' },
      { name: 'Carter 1B', event: 'Soccer Practice', group: 'Youth Team', timeTill: '5:00pm' },
      { name: 'Carter 1B', event: 'Adult Fitness Class', group: 'Adults', timeTill: '1:00pm' },
      { name: 'Carter 1A', event: 'Ultimate Frisbee', group: 'College Students', timeTill: '2:00pm' },
      { name: 'Carter 2B', event: 'Flag Football Game', group: 'Community League', timeTill: '3:00pm' },
      { name: 'Carter 2A', event: 'Soccer Tournament', group: 'Youth League', timeTill: '4:00pm' },
      { name: 'Carter 1B', event: 'Lacrosse Scrimmage', group: 'High School Boys', timeTill: '5:30pm' },
      { name: 'Carter 1A', event: 'Flag Football', group: 'Open', timeTill: '6:00pm' },
      { name: 'Carter 2B', event: 'Kickball Fun Game', group: 'Families', timeTill: '6:30pm' },
      { name: 'Carter 2A', event: 'Evening Jogging Group', group: 'Adults', timeTill: '7:00pm' },
    ]
  };



  const [data, setData] = useState(mockData); // Set default state to mock data
  const [count, setCount] = useState(0);

  useEffect(() => {
    // Now we just set the data without fetching from an API
    setData(mockData);
    setCount(count + 1);
    console.log(mockData);
  }, []);

  return (
    <div className="flex h-screen bg-white"> {/* Make the entire background white and extend the full height of the screen */}
      {/* Sidebar */}
      <div className="w-64 bg-red-500 text-white p-4 fixed h-full"> {/* Make sidebar fixed and full height */}
        {/* Sidebar content */}
      </div>

      {/* Main content */}
      <div className="flex-1 p-4 ml-64"> {/* Add left margin to make room for the sidebar */}
        {/* Header */}
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-xl font-bold">Home</h1>
          <div>
            {/* Header buttons */}
            <Link href="/report" className="bg-black text-white rounded-full px-4 py-2 mr-2">
              Report Field Activity
            </Link>

            <Link href="/when-can-I" className="bg-black text-white rounded-full px-4 py-2 inline-block">
              When Can I Play?
            </Link>
          </div>
        </div>

        {/* Cards */}
        <div className="grid grid-cols-3 gap-4">
          {/* Each card for locations */}
          {data['use client'].map((event, index) => (
            <div key={index} className="bg-gray-100 p-4 rounded-lg">
              <h2 className="text-lg font-semibold">{event.name}</h2>
              <p className="text-sm text-gray-500">{event.group}</p>
              <p className="text-md">{event.event}</p>
              <p>Starts at: {event.timeTill}</p>
            </div>
          ))}
        </div>

        {/* Recent User Reports - Positioned at the bottom */}
        <div className="fixed bottom-0 left-64 right-0 bg-white p-4 border-t-2 border-gray-200">
          <p className="text-gray-600">Recent User Reports: "Cold day here at Carter, bouta run some spikeball!!!" - Joe 15min ago</p> {/* Placeholder for actual data */}
        </div>
      </div>
    </div>
  );


}

