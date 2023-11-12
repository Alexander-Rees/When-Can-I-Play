"use client"

import { useState } from "react";

export default function Report() {
    const [report, setReport] = useState("");
    const [reportList, setReportList] = useState<Array<string>>([])


    // const reportButton = document.getElementById("reportBtn") as HTMLInputElement
    // const printedReport = document.getElementById("reportedOutput") as HTMLInputElement


    // function displayReport(): void {
    //     const initInput = input.toString(); 
    //     printedReport.textContent = initInput; 
    // }

    // reportButton.addEventListener("click", displayReport); 
    console.log(reportList)

    const handleUpdateList = () => {
        setReportList(arr => [...arr, report]);
        setReport("")
    }

    return (
        <div>
        <h1>User Reports Page</h1>
        <p>Enter Your Own Report:</p>
        <form onSubmit={(e) => {
            e.preventDefault()
            handleUpdateList}
        }>
        <input type="string" id="userInput" placeholder="report..." value={report} onChange={(e) => {
            setReport(e.target.value)
        }}/>
        <button id="reportBtn" onClick={handleUpdateList}>Enter</button>
        </form>
        <h3>You entered: <output id="reportedOutut">{reportList.map((reportItem) => (
            <p>{reportItem}</p>
        ))}</output></h3>
        </div>

    ); 
}
