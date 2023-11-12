"use client"

import axios from 'axios';
import Image from 'next/image'
import Link from 'next/link'
import { useEffect, useState } from 'react';

export default function Home() {
  const [data, setData] = useState("");
  const [count, setCount] = useState(0)

  const getData = async () => {
    const resp = await axios.get('https://api.sampleapis.com/coffee/hot');
    const json = await resp.data;
    setData(json);
    setCount(count + 1)
    console.log(json)
  }

  useEffect(() => {
    getData();
  }, []);

  return (
    <div className="flex">
      {/* Sidebar */}
      <div className="w-64 bg-red-500 text-white p-4"> {/* Adjust width and padding as needed */}
        {/* Sidebar content */}
      </div>

      {/* Main content */}
      <div className="flex-1 p-4">
        {/* Header */}
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-xl font-bold">Home</h1>
          <div>
            {/* Header buttons */}
            <button className="bg-black text-white rounded-full px-4 py-2 mr-2">Report Field Activity</button>
            <Link href="/spaces" passHref>
              <a className="bg-black text-white rounded-full px-4 py-2 inline-block">
                When Can I Play?
              </a>
            </Link>
          </div>
        </div>

        {/* Cards */}
        <div className="grid grid-cols-3 gap-4">
          {/* Each card */}
          <div className="bg-gray-100 p-4 rounded-lg">
            <h2 className="text-lg font-semibold">Closest Open Locations:</h2>
            {/* Locations list */}
          </div>
          {/* Repeat for other cards */}
        </div>

        {/* Footer or other content */}
      </div>
    </div>
  );
}
