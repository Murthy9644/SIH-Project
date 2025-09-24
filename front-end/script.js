// Animations

// Global variables
let tid = ""
let detailsData = {}
let serverIP = ""

<<<<<<< HEAD
let serverFindingHTML = `
    <div id="body-child">
        <div id="animation"></div>

        <div id="animation2"></div>
=======
// HTML structure for Server finding page
let serverFindingHTML = `
    <div id="body-child">
        <div id="animation">
            <div id="animation2"></div>
        </div>
>>>>>>> 72871a44a6e2e1638e54fd1e4aefe3dcbfda5b99

        <h4>Finding the server</h4>
    </div>
`

<<<<<<< HEAD
// HTML structure for server not found
let serverNotFoundHTML = `
    <div id="body-child2">
=======
// HTML structure for Server not found page
let serverNotFoundHTML = `
    <div id="body-child">
>>>>>>> 72871a44a6e2e1638e54fd1e4aefe3dcbfda5b99
        <div id="uh-oh">
            <div id="eye1"></div>

            <div id="eye2"></div>

            <div id="mouth"></div>

            <div id="tear"></div>
        </div>

        <h4>Server Not Found</h4>

        <button id="closeExe">Exit</button>
    </div>
`

// HTML structure for login screen
let loginScreenHTML = `
    <div id="alertBox"></div>

    <div id="login-screen">
        <div id = "login-screen-child">
            <div id="reg-btn"><button>Register</button></div>
            
            <div id="login-header">
                <div id="login-header-shield">
                    <i class="fa-solid fa-shield"></i>
                </div>
                
                <div id="login-header-text">
                    <h2 id="login-h2">Tourist Safety System</h2>
                    <p id="login-p1">Authorized Personnel Access Only</p>
                </div>
            </div>
            
            <div id="login-container">
                <div id="login-container-header">
                    <h3>Authority Login</h3>
                    <p>Enter your authorized credentials to access the system</p>
                </div>
                
                <div id="loginId">
                    <h5>Authorized ID Number</h5>
                    <div id = "login-input-container">
                        <input id = "login-id-input" type="text" name = "id" placeholder="Enter your ID">
                        <div></div>
                    </div>
                </div>
                
                <div id="loginPswd">
                    <h5>Password</h5>
                    <div id = "login-input-container">
                        <input id = "login-pswd-input" type="password" name = "password" placeholder="Enter your password">
                        <div></div>
                    </div>
                </div>
                
                <div id="captcha">
                    <div id="text"><h3>demo text</h3></div>
                    <div id = "login-input-container">
                        <input type="text" name = "captcha" placeholder="Enter the captcha">
                        <div></div>
                    </div>
                </div>
                
                <button id = "login-btn">Login</button>
            </div>
        </div>
    </div>
`

let loginBtn = document.getElementById("login-btn")
if (loginBtn){
    loginBtn.addEventListener("click", () => {
        handleChangeScreen("loginScreen", "homeScreen")
    })
}

// HTML structure for home screen
let homeScreenHTML = `
    <div id="homeScreen">
        <div id="header">
            <div id="title-block">
                <div id="logo"></div>
                
                <div id="titles">
                    <h4 id="title">Trip Pilot</h4>
                    
                    <p id="subtitle">Your Travel Companion</p>
                </div>
            </div>

            <div id="profile">
                <div id="profile-btn"><i class="fa-solid fa-user"></i></div>
            </div>
        </div>

        <div id="home-body">
            <div id="tools-block">
                <div id="tools-text" class = "tool">
                    <p>Create new Registration:</p>

                    <p>Central resolver for Help Desk issues:</p>

                    <p>Remove Tourist [Cancel tour]:</p>
                </div>

                <div id="tools-btn" class = "tool">
                    <button id="new-reg-btn" class = "tool-btn"><i class="fa-solid fa-user-plus"></i> New Registration</button>

                    <button id="control-desk-btn" class = "tool-btn"><i class="fa-solid fa-inbox"></i> Control Desk</button>

                    <button id="remove-tourist-btn" class = "tool-btn"><i class="fa-solid fa-trash"></i> Remove Tourist</button>
                </div>
            </div>

            <div id="touristwise-details">
                
            </div>
        </div>
    </div>
`

// HTML structure for details screen
let detailsScreenHTML = `
    <div id="alertBox"></div>

    <div id="details-screen">
        <div id="details-header">
            <button id="details-back-btn" onclick = "changePage('loginScreen', true)">
                <i class="fa-solid fa-arrow-left"></i>
                <p>Back to Login</p>
            </button>
    
            <div id="details-header-text">
                <h2>Tourist Registration</h2>
                <p>Enter tourist details for safety monitoring</p>
            </div>
        </div>
    
        <div id="details-form-container">
            <div id="details-personal-information">
                <div id="details-PI-header">
                    <div>
                        <i class="fa-regular fa-user"></i>
                        <h3>Personal Information</h3>
                    </div>
    
                    <p>Basic details as per official documentations</p>
                </div>
    
                <div id="details-name">
                    <h5>Full Name *</h5>
                    <input type="text" name = "fullname" placeholder="Enter full name">
                </div>
    
                <div id="details-phoneNum">
                    <h5>Phone Number *</h5>
                    <input type="tel" name = "phoneNo" placeholder="+1234567890">
                </div>
    
                <div id="details-dob">
                    <h5>Date of Birth *</h5>
                    <input type="date" name = dob>
                </div>
    
                <div id="nation">
                    <h5>Nationality</h5>
                    <input type="text" placeholder="Enter nationality" name = "nation">
                </div>
            </div>
    
            <div id="details-travel-information">
                <div id="details-TI-header">
                    <div>
                        <i class="fa-solid fa-location-dot"></i>
                        <h3>Travel Information</h3>
                    </div>
    
                    <p>Trip details and emergency contacts</p>
                </div>
    
                <div id="details-destination">
                    <h5>Destination</h5>
                    <input type="text" placeholder="Enter travel destination" name = "destination">
                </div>
    
                <div id="details-trip-duration">
                    <h5>Trip Duration *</h5>
                    <h6>From</h6>
                    <input type="date" name = "trip-from-date">
                    <h6>To</h6>
                    <input type="date" name = "trip-to-date">
                </div>
    
                <div id="details-trip-reason">
                    <h5>Trip Reason *</h5>
                    <input type="text" placeholder="Enter the trip reason" name = "tripReason">
                </div>
    
                <div id="details-emergency-contact">
                    <h5>Emergency Contact</h5>
                    <input type="tel" placeholder="Emergency contact number" name = emergencyPhn>
                </div>
            </div>
        </div>
    
        <div id="details-foot-buttons">
            <button id = "cancelBtn">Cancel</button>
            <button id = "generateBtn">Generate QR & Travel ID</button>
        </div>
    </div>
`

let qrScreenHTML = `
        <div id="qrScreen">
        <div id="qr-header">
            <div id="qr-header-text">
                <h2>Tourist Registration Complete</h2>

                <p>QR Code & Travel ID generated successfully</p>
            </div>

            <div id="qr-header-btns">
                <button id = "back-btn"><i class="fa-solid fa-arrow-left" style="font-size: 10px; position: relative; top: -1px;"></i> Back to Form</button>
                <button id = "New-reg-btn">New Registration</button>
            </div>
        </div>

        <div id="qr-details-container">
            <div id="qr-code-container">
                <div id="qr-code-header">
                    <h3><i class="fa-solid fa-qrcode" style="color: rgb(94, 94, 252);"></i> Generated QR Code</h3>

                    <p>Scan this QR code to access the mobile application</p>
                </div>

                <div id="qr-code-image"></div>

                <div id="qr-bottom-text">
                    <p>This QR code contains encrypted tourist data</p>
                    <p>for sceure access to the mobile application</p>
                </div>
            </div>

            <div id="qr-tid-details-container">
                <div id="tid-header">
                    <h3><i class="fa-regular fa-square-check" style="color: rgb(4, 219, 4); font-size: 20px;"></i> Travel ID Generated</h3>
                    
                    <p>Unique identifier for this tourist registration</p>
                </div>

                <div id="tid-number">
                    <h5>Travel ID</h5>

                    <div id="number-container">
                        <div id="number"></div>

                        <button id="copy-btn"><i class="fa-solid fa-clone"></i></button>
                    </div>
                </div>

                <div id="tourist-details">
                    <h5>Tourist Information</h5>

                    <div>
                        <p id="field-name">Name:</p>
                        <p id="value"></p>
                    </div>

                    <div>
                        <p id="field-name">Phone:</p>
                        <p id="value"></p>
                    </div>

                    <div>
                        <p id="field-name">Destination:</p>
                        <p id="value"></p>
                    </div>

                    <div>
                        <p id="field-name">Duration:</p>
                        <p id="value"></p>
                    </div>

                    <div>
                        <p id="field-name">Registration:</p>
                        <p id="value"></p>
                    </div>
                </div>
            </div>
        </div>

        <div id="bottom-btns">
            <button id="download"><i class="fa-solid fa-download"></i> Download PDF</button>

            <button id="print"><i class="fa-solid fa-print"></i> Print</button>
        </div>
    </div>
`

<<<<<<< HEAD
let serverIPStatus = null
let touristDetails = null

window.addEventListener("pywebviewready", async () => {
    // document.getElementById("body").innerHTML = serverFindingHTML
    // serverIPStatus = await window.pywebview.api.startFindingServer()

    // if (serverIPStatus == "success"){
    //     changePage("loginScreen", true)
    // }
    // else{
    //     changePage("serverNotFound", true)

    //     return
    // }

    try {
        let touristsNdetails = await window.pywebview.api.asyncUtils.getTouristsNdetails();
        window.pywebview.api.widutils.printer(touristsNdetails)

        if (touristsNdetails == "null"){
            window.pywebview.api.widutils.printer("Nulled")
            touristDetails = null;
        }

        else touristDetails = JSON.parse(touristsNdetails);
    } catch (err) {
        window.pywebview.api.widutils.printer(err)
        touristDetails = null;
    }
});
=======
// Starting protocol

let startingProtocolStatus;
(async () => {
    startingProtocolStatus = await startingProtocol()
})()

>>>>>>> 72871a44a6e2e1638e54fd1e4aefe3dcbfda5b99

// Handles Screen change based on credential check
async function handleChangeScreen(currentpage, nextpage){
    
    let credCheckStatus = await loginCredCheck(currentpage)
    
    if (credCheckStatus){
        changePage(nextpage, true)
    }
}

// Handles closing the alert box
function closeDiv(){
    document.getElementById("alertBox").innerHTML = ``
}

// Changes the page based on the given page name
function changePage(page, credCheckStatus = true){

    if (! credCheckStatus) return
    
    switch (page){
        case "serverNotFound":
            let body_ = document.getElementById("body")
            body_.innerHTML = serverNotFoundHTML

            let closeExe = document.getElementById("closeExe")
            if (closeExe){
                closeExe.addEventListener("click", () => {
                    window.close()
                })
            }
            break

        case "loginScreen":
            let body = document.getElementById("body")
            body.style.background = "linear-gradient(to bottom right, rgb(25, 169, 226), rgb(25, 72, 226), rgb(25, 169, 226))"
            body.style.backgroundColor = "transparent"
            body.innerHTML = loginScreenHTML
            let loginBtn = document.getElementById("login-btn")

            if (loginBtn){
                loginBtn.addEventListener("click", () => {
                handleChangeScreen("loginScreen", "homeScreen")
                })
            }

            return

        case "homeScreen":
            let body1 = document.getElementById("body")
            body1.innerHTML = homeScreenHTML
            let newRegBtn = document.getElementById("new-reg-btn")

            if (newRegBtn){
                window.pywebview.api.widutils.printer("new reg btn activated")

                newRegBtn.addEventListener("click", () => {
                    window.pywebview.api.widutils.printer("new reg btn activated2")
                    changePage("detailsScreen", true)
                })
            }

            let controlDeskBtn = document.getElementById("control-desk-btn")
            if (controlDeskBtn){
                controlDeskBtn.addEventListener("click", () => {
                    // alert("Control Desk feature coming soon!")
                })
            }

            let removeTouristBtn = document.getElementById("remove-tourist-btn")
            if (removeTouristBtn){
                removeTouristBtn.addEventListener("click", () => {
                    // alert("Remove Tourist feature coming soon!")
                })
            }

            if (touristDetails == null) {
                window.pywebview.api.widutils.printer("entered if in hscreen")
                document.getElementById("touristwise-details").innerHTML = `<p style="color: white; text-align: center; margin-top: 20px;">No tourist data available.</p>`;
            }

            else {for (key in touristDetails){

                let touristDiv = document.createElement("div")
                touristDiv.id = "a-tourist"
                touristDiv.innerHTML = `
                <div id="a-tourist">
                    <div id="name-tid">
                        <h5 id="tourist-name">${touristDetails[key]["fullname"]}</h5>

                        <p id="tourist-id">TID: ${key}</p>
                    </div>
                        
                    <div id="date">
                        <p id="from-date">From: ${touristDetails[key]["duration"][0]}</p>
                            
                        <p id="to-date">To: ${touristDetails[key]["duration"][1]}</p>
                    </div>

                    <button id="go-to-details">Details</button>
                    <button id="notifi-btn"><i class="fa-solid fa-bell"></i></button>
                </div>
                `

                document.getElementById("touristwise-details").appendChild(touristDiv)
            }}

            break

        case "detailsScreen":
            let body2 = document.getElementById("body")
            body2.style.background = "none"
            body2.style.backgroundColor = "rgba(157, 157, 201, 0.2)"
            body2.innerHTML = detailsScreenHTML

            document.getElementById("cancelBtn").addEventListener("click", () => {
                changePage("homeScreen", true)
            })

            document.getElementById("details-back-btn").addEventListener("click", () => {
                changePage("loginScreen", true)
            })

            document.getElementById("generateBtn").addEventListener("click", () => {
                handleDetails2QR()
            })

            break

        case "qrScreen":
            let body3 = document.getElementById("body")
            body3.innerHTML = qrScreenHTML

            document.getElementById("back-btn").addEventListener("click", () => {
                changePage("detailsScreen", true)
            })

            document.getElementById("New-reg-btn").addEventListener("click", () => {
                changePage("detailsScreen", true)
            })


            document.getElementById("number").innerText = tid
            document.getElementById("tourist-details").children[1].children[1].innerText = detailsData["fullname"]
            document.getElementById("tourist-details").children[2].children[1].innerText = detailsData["phoneNo"]
            document.getElementById("tourist-details").children[3].children[1].innerText = detailsData["destination"]
            document.getElementById("tourist-details").children[4].children[1].innerText = `${detailsData["duration"][0]} to ${detailsData["duration"][1]}`
            document.getElementById("body").style.background = "none"
            document.getElementById("body").style.backgroundColor = "rgba(157, 157, 201, 0.2)"
            document.getElementById("qr-code-image").style.backgroundImage = `url(${serverIP}/getQr/${tid}.png)`
            break
    }
}

// Checks if all required credentials are filled before changing the page
async function loginCredCheck(page){
    serverIP = await window.pywebview.api.widutils.getServerIP()

    switch (page){
        case "loginScreen":
            let id = document.querySelector("input[name='id']")
            let pswd = document.querySelector("input[name='password']")
            let captcha = document.querySelector('input[name = "captcha"]')
            
            let loginData = {
                id: id ? id.value : '',
                pswd: pswd ? pswd.value : '',
                captcha: captcha ? captcha.value : ''
            }

            let response = await window.pywebview.api.widutils.credCheck(loginData, page)
            
            if (! response){
                document.getElementById("alertBox").innerHTML = `
                <div id="alert">
                    <p>Fill all the required credentials before submitting.</p>
                    <button onclick="closeDiv()">OK</button>
                </div>
                `

                return false
            }

            let loginInfo = await window.pywebview.api.dataTransfer.getLoginInfo(loginData["id"])

            if ((! loginInfo[0]) || (loginInfo[1] != loginData["pswd"])){
                document.getElementById("alertBox").innerHTML = `
                <div id="alert">
                    <p>Incorrect Login Credentials</p>
                    <button onclick="closeDiv()">OK</button>
                </div>
                `

                return false
            }

            break

            case "detailsScreen":
            let fullname = document.querySelector('input[name = "fullname"]')
            let phoneNo = document.querySelector('input[name = "phoneNo"]')
            let dob = document.querySelector('input[name = "dob"]')
            let tripFromDate = document.querySelector('input[name = "trip-from-date"]')
            let tripToDate = document.querySelector('input[name = "trip-to-date"]')
            let tripReason = document.querySelector('input[name = "tripReason"]')

            let detailsData = {
                fullname: fullname ? fullname.value : '',
                phoneNo: phoneNo ? phoneNo.value : '',
                dob: dob ? dob.value : '',
                tripFromDate: tripFromDate ? tripFromDate.value : '',
                tripToDate: tripToDate ? tripToDate.value : '',
                tripReason: tripReason ? tripReason.value : '',
            }

            let response2 = await window.pywebview.api.widutils.credCheck(detailsData, page)
            
            if (! response2){
                document.getElementById("alertBox").innerHTML = `
                <div id="alert">
                    <p>Fill all the required credentials before submitting.</p>
                    <button onclick="closeDiv()">OK</button>
                </div>
                `

                return false
            }

            break
            
            default:
            break
        }

        return true
    }
//Handles Details to QR code generation
async function handleDetails2QR(){
    let credCheckStatus = await loginCredCheck("detailsScreen")
        
    if (! credCheckStatus) return
    
    document.getElementById("generateBtn").innerText = "Generating QR..."
    document.getElementById("generateBtn").style.color = "rgba(220, 220, 220, 0.7)"
    document.getElementById("generateBtn").style.cursor = "not-allowed"
    document.getElementById("generateBtn").disabled = true

    let tidNo = Date.now()
    
    detailsData = {
        fullname: document.querySelector('input[name = "fullname"]').value,
        phoneNo: document.querySelector('input[name = "phoneNo"]').value,
        dob: document.querySelector('input[name = "dob"]').value,
        nationality: document.querySelector('input[name = "nation"]').value,
        destination: document.querySelector('input[name = "destination"]').value,
        duration: [document.querySelector('input[name = "trip-from-date"]').value, document.querySelector('input[name = "trip-to-date"]').value],
        tripReason: document.querySelector('input[name = "tripReason"]').value,
        emergencyContact: document.querySelector('input[name = "emergencyPhn"]').value
    }

    tid = `${detailsData["fullname"][0]}-${tidNo}`
    let dataTransferStatus = await window.pywebview.api.dataTransfer.sendData(detailsData, tid)

    if (dataTransferStatus[0] == "success" && dataTransferStatus[1] == "success"){
        changePage("qrScreen", true)
    }

    document.getElementById("generateBtn").innerText = "Generate QR & Travel ID"
    document.getElementById("generateBtn").style.color = "white"
    document.getElementById("generateBtn").style.cursor = "pointer"
    document.getElementById("generateBtn").disabled = false
}

function startingProtocol(){}