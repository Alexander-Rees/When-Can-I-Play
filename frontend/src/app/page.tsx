"use client"

import axios from 'axios';
import Image from 'next/image'
import Link from 'next/link'
import { useEffect, useState } from 'react';

export default function Home() {
  // Mock data
  const mockData = {
    "use client": [
      { name: 'Carter 2B', timeTill: '4:30pm', distance: '0.7 mi' },
      { name: 'Roxbury 2S', timeTill: '3:30pm', distance: '0.9 mi' },
      // ... other mock location data
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
          {data['use client'].map((location, index) => (
            <div key={index} className="bg-gray-100 p-4 rounded-lg">
              <h2 className="text-lg font-semibold">{location.name}</h2>
              <p>Time Till: {location.timeTill}</p>
              <p>Distance: {location.distance}</p>
            </div>
          ))}
        </div>

        {/* Footer or other content */}
      </div>
    </div>
  );

}

