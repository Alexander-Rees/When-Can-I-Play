"use client"
import "./report.css"
import Link from 'next/link'
import { useState } from "react";

export default function Report() {
    const [report, setReport] = useState("");
    const [reportList, setReportList] = useState<Array<string>>([])

    console.log(reportList)

    const handleUpdateList = () => {
        setReportList(arr => [...arr, report]);
        setReport("")
    }

    return (
        <div>

            {/* Sidebar */}
            <div className="w-64 bg-red-500 text-white p-4 fixed h-full"> {/* Make sidebar fixed and full height */}
                {/* Sidebar content */}
            </div>


            <div className="ml-64 p-4"> {/* Main content with left margin */}
                {/* Header with back button */}
                <div className="flex justify-between items-center mb-4">
                    <Link href="/" passHref>
                        <button className="bg-black text-white rounded-full px-4 py-2">Home</button>
                    </Link>
                    <h1 className="text-xl font-bold">User Reports Page</h1>
                </div>

                <p id="enter-report">Enter a Report:</p>
                <form onSubmit={(e) => {
                    e.preventDefault()
                    handleUpdateList()
                }}>
                    <input type="text" id="user-input" placeholder="report..." value={report} onChange={(e) => {
                        setReport(e.target.value)
                    }} />
                    <button type="submit" id="report-btn">Submit</button>

                    <h3 id="you-entered">You entered:</h3>

                </form>
                <h4 id="table">
                    <output id="reported-output">{reportList.map((reportItem, index) => (
                        <p key={index}>{reportItem}<hr /></p> // Added a key for each item
                    ))}</output> </h4>
            </div>
        </div>

    );

}

// git push origin reportPage
