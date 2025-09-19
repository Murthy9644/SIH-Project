// Animations

// Global variables
let tid = ""
let detailsData = {}

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
                
                <button onclick="handleChangeScreen('loginScreen', 'detailsScreen')" id = "login-btn">Login</button>
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
            <button id = cancelBtn>Cancel</button>
            <button id = generateBtn onclick = "handleDetails2QR()">Generate QR & Travel ID</button>
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

                <div id="qr-code-image">

                </div>

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
        case "loginScreen":
                let body = document.getElementById("body")
                body.style.background = "linear-gradient(to bottom right, rgb(25, 169, 226), rgb(25, 72, 226), rgb(25, 169, 226))"
                body.style.backgroundColor = "transparent"
                body.innerHTML = loginScreenHTML
                break

            case "detailsScreen":
                let body2 = document.getElementById("body")
                body2.style.background = "none"
                body2.style.backgroundColor = "rgba(157, 157, 201, 0.2)"
                body2.innerHTML = detailsScreenHTML
                break

            case "qrScreen":
                let body3 = document.getElementById("body")
                body3.innerHTML = qrScreenHTML
                document.getElementById("qr-code-image").innerHTML = `<img src="./assets/qr_codes/${tid}.png" alt="QR Code">`
                document.getElementById("number").innerText = tid
                document.getElementById("tourist-details").children[1].children[1].innerText = detailsData["fullname"]
                document.getElementById("tourist-details").children[2].children[1].innerText = detailsData["phoneNo"]
                document.getElementById("tourist-details").children[3].children[1].innerText = detailsData["destination"]
                document.getElementById("tourist-details").children[4].children[1].innerText = `${detailsData["duration"][0]} to ${detailsData["duration"][1]}`
                document.getElementById("body").style.backgroundColor = "rgba(157, 157, 201, 0.2)"
                document.getElementById("body").style.background = "none"
                break
        }
}

// Checks if all required credentials are filled before changing the page
async function loginCredCheck(page){

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

    if (dataTransferStatus == "success") changePage("qrScreen", true)

    document.getElementById("generateBtn").innerText = "Generate QR & Travel ID"
    document.getElementById("generateBtn").style.color = "white"
    document.getElementById("generateBtn").style.cursor = "pointer"
    document.getElementById("generateBtn").disabled = false
}