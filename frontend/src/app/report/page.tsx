"use client"
import "./report.css"

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
    
        
        <div>
        <h1 id="page-title">User Reports Page</h1>
        <p id="enter-report">Enter a Report:</p>
        <form onSubmit={(e) => {
            e.preventDefault()
            handleUpdateList}
        }>
        <input type="string" id="user-input" placeholder="report..." value={report} onChange={(e) => {
            setReport(e.target.value)
        }}/>
        <button id="report-btn" onClick={handleUpdateList}>Submit</button>
        
        <h3 id="you-entered">You entered:</h3>

        </form>
        <h4 id="table">
         <output id="reported-output">{reportList.map((reportItem) => (
            <p>{reportItem}<hr /></p>
        ))}</output> </h4>
        </div>
    </div>

    ); 

}


// git push origin reportPage 