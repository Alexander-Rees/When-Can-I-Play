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
    <div>
      <h1 className='font-bold'>When Can I Play?</h1>
      <Link href={'/spaces'}>go to spaces</Link>
    </div>
  )
}
